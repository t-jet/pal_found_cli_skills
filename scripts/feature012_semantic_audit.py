"""Build a reproducible source locator register for FEATURE-012 QA."""

import ast
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SKILL_ROOT = ROOT / "pal_found_cli_skills/.agents/skills"
SDK_ROOT = ROOT / ".ept/docs/customer_input/foundry-platform-python/foundry_sdk/v2"
TOOL_ROOT = ROOT / "pal_found_cli_tool/src/pal_found_cli"
TEST = ROOT / "pal_found_cli_skills/tests/test_offline_skill_gate.py"
OUTPUT = ROOT / "pal_found_cli_skills/maintainer/feature012-independent-semantic-audit.json"
REVIEW_DIR = ROOT / "pal_found_cli_skills/maintainer/feature012-semantic-reviews"


def revision(path: Path) -> str:
    return subprocess.run(
        ["git", "-C", str(path), "rev-parse", "HEAD"],
        check=True, capture_output=True, text=True,
    ).stdout.strip()


def load_reviews(register: dict[str, set[str]]) -> dict[tuple[str, str], dict[str, str]]:
    """Load signed decisions from namespace files without modifying them."""
    reviews = {}
    for path in sorted(REVIEW_DIR.glob("*.json")):
        skill = path.stem
        if skill not in register:
            raise ValueError(f"Unknown review namespace: {path}")
        document = json.loads(path.read_text(encoding="utf-8"))
        if document.get("schema_version") != 1 or not isinstance(document.get("reviews"), dict):
            raise ValueError(f"Invalid review file structure: {path}")
        for operation, review in document["reviews"].items():
            key = operation.replace(".", " ", 1)
            if key not in register[skill]:
                raise ValueError(f"Unknown reviewed operation: {skill} {operation}")
            if not isinstance(review, dict) or review.get("decision") not in {"pass", "fail"}:
                raise ValueError(f"Invalid review decision: {skill} {operation}")
            required = ("reviewer", "reviewed_on", "record_sha256", "cli_sha256",
                        "sdk_sha256", "note")
            if any(not isinstance(review.get(field), str) or not review[field].strip()
                   for field in required):
                raise ValueError(f"Incomplete review: {skill} {operation}")
            if review["decision"] == "fail" and not review.get("defect_ticket"):
                raise ValueError(f"Failed review needs defect_ticket: {skill} {operation}")
            reviews[(skill, operation)] = review
    return reviews

tree = ast.parse(TEST.read_text(encoding="utf-8"))
register = next(ast.literal_eval(node.value) for node in tree.body
                if isinstance(node, ast.Assign) and any(
                    isinstance(target, ast.Name) and target.id == "FROZEN_OPERATIONS"
                    for target in node.targets))
manual_reviews = load_reviews(register)

rows = []
for skill, operations in sorted(register.items()):
    namespace = skill.removeprefix("pal-found-").replace("-", "_")
    cli = TOOL_ROOT / namespace / "scripts" / f"pal_found_{namespace}_cli.py"
    sdk_dir = SDK_ROOT / namespace
    records = {}
    for path in sorted((SKILL_ROOT / skill).rglob("*.md")):
        content = path.read_text(encoding="utf-8")
        matches = list(re.finditer(r"^### ([a-z][a-z0-9_]*\.[a-z][a-z0-9_]*)\s*$", content, re.M))
        for i, match in enumerate(matches):
            key = match.group(1).replace(".", " ", 1)
            body = content[match.end():matches[i + 1].start() if i + 1 < len(matches) else len(content)]
            records.setdefault(key, []).append((path, content[:match.start()].count("\n") + 1, body))
    for key in sorted(operations):
        resource, operation = key.split(" ", 1)
        found = records.get(key, [])
        sdk = sdk_dir / f"{resource}.py"
        sdk_method_lines = []
        sdk_returns = []
        if sdk.exists():
            sdk_tree = ast.parse(sdk.read_text(encoding="utf-8"))
            sdk_methods = [node for node in ast.walk(sdk_tree)
                           if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
                           and node.name == operation]
            sdk_method_lines = [node.lineno for node in sdk_methods]
            sdk_returns = [ast.unparse(node.returns) if node.returns else None for node in sdk_methods]
        record_path, record_line, body = found[0] if found else (None, None, "")
        checks = {
            "unique_record": len(found) == 1,
            "example": bool(re.search(r"\bExample\s*:", body, re.I)),
            "sdk_method": bool(sdk_method_lines),
            "cli_source": cli.exists(),
        }
        record_hash = hashlib.sha256(body.encode("utf-8")).hexdigest() if record_path else None
        cli_hash = hashlib.sha256(cli.read_bytes()).hexdigest() if cli.exists() else None
        sdk_hash = hashlib.sha256(sdk.read_bytes()).hexdigest() if sdk_method_lines else None
        manual = manual_reviews.get((skill, key.replace(" ", ".", 1)))
        if manual and (record_hash, cli_hash, sdk_hash) != (
            manual["record_sha256"], manual["cli_sha256"], manual["sdk_sha256"]
        ):
            raise ValueError(f"Stale review source hashes: {skill} {key}")
        decision = manual["decision"] if manual else "pending_semantic_review"
        rows.append({
            "skill": skill, "operation": key,
            "record": f"{record_path.relative_to(ROOT).as_posix()}:{record_line}" if record_path else None,
            "record_sha256": record_hash,
            "cli_source": cli.relative_to(ROOT).as_posix() if cli.exists() else None,
            "cli_sha256": cli_hash,
            "sdk_source": f"{sdk.relative_to(ROOT).as_posix()}:{sdk_method_lines[0]}" if sdk_method_lines else None,
            "sdk_sha256": sdk_hash,
            "sdk_return": sdk_returns[0] if sdk_returns else None,
            "checks": checks,
            "qa_decision": decision,
            "finding": manual["note"] if manual else None,
            "reviewer": manual["reviewer"] if manual else None,
            "reviewed_on": manual["reviewed_on"] if manual else None,
            "defect_ticket": manual.get("defect_ticket") if manual else None,
        })

summary = {
    "total": len(rows),
    "by_namespace": {skill: len(ops) for skill, ops in sorted(register.items())},
    "checks_passed": {check: sum(row["checks"][check] for row in rows)
                      for check in rows[0]["checks"]},
    "semantic_pass": sum(row["qa_decision"] == "pass" for row in rows),
    "semantic_fail": sum(row["qa_decision"] == "fail" for row in rows),
    "semantic_pending": sum(row["qa_decision"] == "pending_semantic_review" for row in rows),
}
if summary["total"] != 351 or any(count != 351 for count in summary["checks_passed"].values()):
    raise SystemExit(f"Frozen operation trace is incomplete: {summary}")
OUTPUT.write_text(json.dumps({"scope": "FEATURE-012 frozen CLI operations",
                              "source_revisions": {
                                  "sdk": revision(SDK_ROOT.parents[1]),
                                  "skills": revision(SKILL_ROOT.parents[1]),
                                  "cli": revision(TOOL_ROOT.parents[1]),
                              },
                              "method": "Mechanical source-locator checks only; semantic decisions require manual source comparison.",
                              "summary": summary, "rows": rows}, indent=2) + "\n", encoding="utf-8")
print(json.dumps(summary, indent=2))
