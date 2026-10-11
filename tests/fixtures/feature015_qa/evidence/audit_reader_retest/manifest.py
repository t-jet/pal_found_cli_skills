"""Bind the Audit reader evidence to its isolated skill snapshot."""

import hashlib
import json
from importlib.metadata import version
from pathlib import Path


WORKSPACE = Path(__file__).resolve().parents[6]
SNAPSHOT = WORKSPACE / ".ept/tmp/feature015_audit_reader_retest/pal-found-dev"
EVIDENCE = Path(__file__).resolve().parent


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    files = sorted(path for path in SNAPSHOT.rglob("*") if path.is_file())
    aggregate = hashlib.sha256()
    for path in files:
        aggregate.update(path.relative_to(SNAPSHOT).as_posix().encode("utf-8"))
        aggregate.update(b"\0")
        aggregate.update(bytes.fromhex(digest(path)))
    prior = WORKSPACE / "pal_found_cli_skills/tests/fixtures/feature015_qa/evidence/feature015_namespace_reader"
    historical = sorted(path for path in prior.rglob("*") if path.is_file()) if prior.exists() else []
    result = {
        "sdk_distribution": "foundry-platform-sdk",
        "sdk_version": version("foundry-platform-sdk"),
        "snapshot_path": str(SNAPSHOT.relative_to(WORKSPACE)).replace("\\", "/"),
        "snapshot_files": len(files),
        "snapshot_sha256": aggregate.hexdigest(),
        "selected_skill_files": {
            name: digest(SNAPSHOT / name)
            for name in (
                "SKILL.md",
                "references/rest/v2/audit/LogFile.md",
                "references/rest/contracts/v2/audit/LogFile/list.md",
                "examples/rest/073/v2/audit/LogFile/list_pagination.py",
            )
        },
        "reader_sha256": digest(EVIDENCE / "reader.py"),
        "answer_sha256": digest(EVIDENCE / "answer.json"),
        "output_sha256": digest(EVIDENCE / "output.json"),
        "historical_failed_artifacts": [
            {"path": str(path.relative_to(WORKSPACE)).replace("\\", "/"), "sha256": digest(path)}
            for path in historical if "audit" in path.name.lower() or "score" in path.name.lower()
        ],
        "boundary": "Cooperative process DNS and socket denial; synthetic MockTransport; no live tenant call.",
    }
    (EVIDENCE / "manifest.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"snapshot_files": len(files), "snapshot_sha256": aggregate.hexdigest(), "historical_artifacts": len(result["historical_failed_artifacts"])}))


if __name__ == "__main__":
    main()
