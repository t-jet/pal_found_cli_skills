"""Check FEATURE-015 acceptance records against current, local release assets.

Run explicitly before release: ``python scripts/verify_feature015_release.py``.
Development tests may pass while independent review is still in progress.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
import re
import subprocess


ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / ".agents" / "skills"
DEV = SKILLS / "pal-found-dev"
HEX40 = re.compile(r"[0-9a-f]{40}\Z")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def input_bundle_digest(owner: Path) -> str:
    paths = [owner / "references/rest-api.md"]
    for directory in ("references/rest", "examples/rest", "assets/rest"):
        paths.extend(path for path in (owner / directory).rglob("*")
                     if path.is_file() and "__pycache__" not in path.parts)
    entries = [f"{path.relative_to(owner).as_posix()}:{digest(path)}"
               for path in sorted(set(paths)) if path.is_file()]
    return hashlib.sha256(("\n".join(entries) + "\n").encode()).hexdigest()


class Report:
    def __init__(self) -> None:
        self.counts: Counter[str] = Counter()
        self.examples: dict[str, list[str]] = defaultdict(list)

    def fail(self, gate: str, item: str) -> None:
        self.counts[gate] += 1
        if len(self.examples[gate]) < 3:
            self.examples[gate].append(item)

    def checked_file(self, gate: str, owner: Path, relative: str,
                     expected: str | None) -> None:
        path = (owner / relative).resolve()
        if not path.is_relative_to(owner.resolve()) or not path.is_file():
            self.fail(gate, f"missing/escaped {relative}")
        elif not expected or digest(path) != expected:
            self.fail(gate, f"stale hash {relative}")

    def print(self) -> None:
        if not self.counts:
            print("FEATURE-015 release gate: PASS")
            return
        print("FEATURE-015 release gate: BLOCKED")
        for gate, count in sorted(self.counts.items()):
            print(f"  {gate}: {count}")
            for item in self.examples[gate]:
                print(f"    {item}")


def load(root: Path, name: str, report: Report) -> dict:
    path = root / "maintainer" / f"{name}.json"
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        report.fail("missing_or_invalid_ledgers", f"{path}: {exc}")
        return {}


def unique_rows(rows: list[dict], label: str, report: Report) -> dict[str, dict]:
    result: dict[str, dict] = {}
    for row in rows:
        identity = row.get("id")
        if not identity or identity in result:
            report.fail("inventory_gaps", f"{label}: missing/duplicate id {identity}")
        else:
            result[identity] = row
    return result


def check_operations(root: Path, contract: dict, domain: dict,
                     oracle: dict, report: Report, candidate_sha: str) -> None:
    if (contract.get("sdk_release"), contract.get("source_commit")) != (
        oracle.get("sdk_release"), oracle.get("source_commit")):
        report.fail("operation_source_gaps", "contract and frozen source revisions differ")
    expected = unique_rows(contract.get("operations", []), "contract", report)
    authored = unique_rows(domain.get("operations", []), "domain", report)
    frozen = oracle.get("operations", {})
    for identity in expected.keys() ^ authored.keys():
        report.fail("operation_inventory_gaps", identity)
    for identity in expected.keys() ^ frozen.keys():
        report.fail("operation_source_gaps", identity)
    if contract.get("operation_count") != len(expected) or len(expected) != 425:
        report.fail("operation_inventory_gaps", f"expected 425, found {len(expected)}")
    stored_sha = domain.get("candidate_sha")
    if not stored_sha or not HEX40.fullmatch(stored_sha) or stored_sha != candidate_sha:
        report.fail("candidate_sha", f"domain candidate {stored_sha!r} != {candidate_sha}")
    stored_bundle = domain.get("input_bundle_sha256")
    current_bundle = input_bundle_digest(root / ".agents/skills/pal-found-dev")
    if not stored_bundle or stored_bundle != current_bundle:
        report.fail("input_bundle_sha256", f"domain {stored_bundle!r} != current {current_bundle}")
    for identity, row in authored.items():
        if row.get("semantic_review_status") != "accepted":
            report.fail("operation_semantic_pending", identity)
        if row.get("independent_qa_status") != "accepted":
            report.fail("operation_qa_pending", identity)
        if row.get("fixture_status") != "passed":
            report.fail("operation_fixture_pending", identity)
        if not row.get("independent_reviewer") or row.get("independent_reviewer") == row.get("author") or not row.get("reviewer_agent") or row.get("reviewer_agent") == row.get("author_agent"):
            report.fail("operation_review_provenance", identity)
        if not row.get("independent_qa_agent") or row.get("independent_qa_agent") == row.get("author_agent"):
            report.fail("operation_qa_provenance", identity)
        source = frozen.get(identity, {})
        if (row.get("source_sdk"), row.get("source_commit")) != (
            oracle.get("sdk_release"), oracle.get("source_commit")):
            report.fail("operation_source_gaps", f"{identity}: source revision differs")
        if row.get("source_sha256") != source.get("source_sha256") or row.get("doc_sha256") != source.get("documentation", {}).get("doc_sha256"):
            report.fail("operation_source_hashes", identity)
        for kind in ("behavior", "example"):
            relative = row.get(kind)
            if not relative:
                report.fail("operation_asset_hashes", f"{identity}: missing {kind}")
            else:
                report.checked_file("operation_asset_hashes", root / ".agents/skills/pal-found-dev",
                                    relative, row.get(f"{kind}_sha256"))
        if not row.get("fixture_entrypoint"):
            report.fail("operation_fixture_pending", f"{identity}: no entrypoint")


def check_models(root: Path, model: dict, matrix: dict,
                 review: dict, report: Report) -> None:
    if (model.get("sdk_release") != "1.101.0"
        or matrix.get("sdk_release") != model.get("sdk_release")
        or not model.get("source_commit")
        or matrix.get("source_commit") != model.get("source_commit")
        or review.get("source_commit") != model.get("source_commit")):
        report.fail("model_source_revision", "register, matrix and independent review disagree")
    registered = unique_rows(model.get("symbols", []), "model register", report)
    mapped = unique_rows(matrix.get("symbols", []), "model matrix", report)
    reviewed = unique_rows(review.get("symbols", []), "model review", report)
    for identity in registered.keys() ^ mapped.keys() | mapped.keys() ^ reviewed.keys():
        report.fail("model_inventory_gaps", identity)
    if (len(mapped) != 3251 or model.get("candidate_symbol_count") != len(registered)
        or matrix.get("symbol_count") != len(mapped)
        or review.get("counts", {}).get("symbols") != len(reviewed)):
        report.fail("model_inventory_gaps", f"expected 3251, found {len(mapped)}")
    for name, document in (("rest-model-register", model), ("rest-model-semantic-matrix", matrix)):
        field = "register_sha256" if name.endswith("register") else "matrix_sha256"
        if review.get(field) != digest(root / "maintainer" / f"{name}.json"):
            report.fail("model_review_ledger_hashes", f"{field} stale")
    for identity, row in mapped.items():
        reg, rev = registered.get(identity, {}), reviewed.get(identity, {})
        if row.get("source_fidelity_review") != "PASS":
            report.fail("model_matrix_source_pending", identity)
        if rev.get("source_fidelity_review") != "PASS":
            report.fail("model_independent_source_unaccepted", identity)
        if row.get("local_meaning_review") != "PASS":
            report.fail("model_matrix_meaning_pending", identity)
        if rev.get("local_meaning_review") != "PASS" or not rev.get("semantic_review_evidence") or rev.get("issues"):
            report.fail("model_independent_meaning_pending", identity)
        if reg.get("semantic_review_status") != "accepted":
            report.fail("model_register_pending", identity)
        if (reg.get("source_sha256") != row.get("source_file_sha256") or
            reg.get("definition_sha256") != row.get("source_definition_sha256") or
            rev.get("reviewed_source_definition_sha256") != row.get("source_definition_sha256") or
            rev.get("reviewed_reader_prose_sha256") != row.get("reader_prose_sha256")):
            report.fail("model_source_hashes", identity)
        pages, hashes = row.get("local_pages", []), row.get("local_page_sha256", [])
        if not pages or len(pages) != len(hashes) or hashes != rev.get("reviewed_local_page_sha256"):
            report.fail("model_page_hashes", identity)
        for relative, expected in zip(pages, hashes):
            report.checked_file("model_page_hashes", root / ".agents/skills/pal-found-dev", relative, expected)


def check_topics(root: Path, ledger: dict, report: Report) -> None:
    topics = ledger.get("topics", [])
    reviewer = ledger.get("independent_reviewer")
    if not reviewer or reviewer == ledger.get("author"):
        report.fail("topic_review_provenance", "missing independent reviewer")
    identities = [row.get("topic") for row in topics]
    if len(topics) != 36 or len(set(identities)) != 36:
        report.fail("topic_inventory_gaps", f"expected 36 distinct topics, found {len(topics)}")
    for row in topics:
        identity = row.get("topic", "unknown")
        if not row.get("authored") or not row.get("registered_path"):
            report.fail("topic_inventory_gaps", identity)
            continue
        if row.get("acceptance") != "accepted":
            report.fail("topic_review_pending", identity)
        if not row.get("review_evidence"):
            report.fail("topic_review_provenance", f"{identity}: missing review evidence")
        report.checked_file("topic_asset_hashes", root / ".agents/skills/pal-found-dev",
                            row["registered_path"], row.get("sha256"))
        path = root / ".agents/skills/pal-found-dev" / row["registered_path"]
        if path.is_file() and row.get("registered_heading"):
            headings = [line.lstrip("# ").strip() for line in path.read_text(encoding="utf-8").splitlines()
                        if line.startswith("#")]
            if row["registered_heading"] not in headings:
                report.fail("topic_inventory_gaps", f"{identity}: missing heading {row['registered_heading']}")
    if ledger.get("status") != "accepted":
        report.fail("topic_review_pending", "ledger status")


def check_skills(root: Path, audit: dict, report: Report) -> None:
    if not audit.get("independent_reviewer"):
        report.fail("skill_review_provenance", "missing independent reviewer")
    folders = {path.name for path in (root / ".agents/skills").iterdir() if path.is_dir() and path.name.startswith("pal-found")}
    if len(folders) != 20 or audit.get("scope", {}).get("skills") != 20:
        report.fail("skill_inventory_gaps", f"expected 20, found {len(folders)}")
    for folder in folders:
        if not (root / ".agents/skills" / folder / "SKILL.md").is_file():
            report.fail("skill_inventory_gaps", f"{folder}: missing SKILL.md")
    audited = set()
    for row in audit.get("files", []):
        relative = row.get("path")
        if not relative:
            report.fail("skill_inventory_gaps", "missing file path")
            continue
        normalized = relative.replace("\\", "/")
        audited.add(normalized)
        report.checked_file("skill_asset_hashes", root / ".agents/skills",
                            normalized, row.get("sha256"))
        if row.get("review_status") != "accepted":
            report.fail("skill_review_pending", relative)
        if not row.get("review_evidence"):
            report.fail("skill_review_provenance", f"{relative}: missing review evidence")
    if len(audit.get("files", [])) != audit.get("scope", {}).get("markdown_files"):
        report.fail("skill_inventory_gaps", "audited markdown count differs from declared count")
    for folder in sorted(folders - {"pal-found-dev"}):
        for path in (root / ".agents/skills" / folder).rglob("*.md"):
            relative = path.relative_to(root / ".agents/skills").as_posix()
            if relative not in audited:
                report.fail("skill_inventory_gaps", f"unreviewed file {relative}")
    if audit.get("status") != "accepted":
        report.fail("skill_review_pending", "audit status")


def check_candidate_anchor(root: Path, candidate_sha: str, report: Report) -> None:
    """Allow review-ledger commits after a frozen content commit."""
    if not HEX40.fullmatch(candidate_sha):
        report.fail("candidate_sha", f"invalid candidate {candidate_sha!r}")
        return
    exists = subprocess.run(["git", "-C", str(root), "cat-file", "-e",
                             f"{candidate_sha}^{{commit}}"], capture_output=True)
    if exists.returncode:
        report.fail("candidate_sha", f"candidate {candidate_sha} is not a local commit")
        return
    ancestor = subprocess.run(["git", "-C", str(root), "merge-base", "--is-ancestor",
                              candidate_sha, "HEAD"], capture_output=True)
    if ancestor.returncode:
        report.fail("candidate_sha", f"candidate {candidate_sha} is not an ancestor of HEAD")
        return
    frozen_paths = (".agents/skills", "tests/fixtures/feature015_qa",
                    "tests/fixtures/offline/rest-acceptance",
                    "tests/fixtures/offline/topic-acceptance",
                    "maintainer/rest-contract-register.json")
    changed = subprocess.run(["git", "-C", str(root), "diff", "--quiet", candidate_sha,
                              "--", *frozen_paths], capture_output=True)
    if changed.returncode:
        report.fail("candidate_sha", "frozen skill, source or QA inputs changed since candidate commit")


def verify(root: Path = ROOT, candidate_sha: str | None = None) -> Report:
    report = Report()
    contract = load(root, "rest-contract-register", report)
    domain = load(root, "rest-domain-authoring-register", report)
    frozen_sha = candidate_sha or domain.get("candidate_sha")
    if frozen_sha:
        check_candidate_anchor(root, frozen_sha, report)
    model = load(root, "rest-model-register", report)
    matrix = load(root, "rest-model-semantic-matrix", report)
    review = load(root, "rest-model-independent-review", report)
    topics = load(root, "development-author-source-evidence", report)
    skills = load(root, "offline-knowledge-audit", report)
    oracle_path = root / "tests/fixtures/offline/rest-acceptance/source-oracle.json"
    try:
        oracle = json.loads(oracle_path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        report.fail("missing_or_invalid_ledgers", f"{oracle_path}: {exc}")
        oracle = {}
    check_operations(root, contract, domain, oracle, report, frozen_sha or "")
    check_models(root, model, matrix, review, report)
    check_topics(root, topics, report)
    check_skills(root, skills, report)
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidate-sha", help="Frozen candidate commit reviewed by independent QA")
    args = parser.parse_args()
    report = verify(candidate_sha=args.candidate_sha)
    report.print()
    return bool(report.counts)


if __name__ == "__main__":
    raise SystemExit(main())
