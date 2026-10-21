"""Capture guarded J7/J8 fixture output from the frozen reader snapshot."""

import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[6]
HERE = Path(__file__).resolve().parent
SNAPSHOT = ROOT / ".ept/tmp/feature015_j7j8_addendum_resume_skill"
MANIFEST = HERE / "snapshot_manifest.txt"
GUARD = HERE.parent / "feature015-j1j10-gate/deny_public.cjs"
EXPECTED_MANIFEST = "5cbf2fc67b3bc706262884b40942caf7a345738edb965dfc0a979e3d785b56b8"


def execute(name, script, cwd):
    command = ["node", "--require", str(GUARD), str(script)]
    result = subprocess.run(command, cwd=cwd, text=True, capture_output=True, timeout=30)
    displayed = []
    for value in command:
        path = Path(value)
        displayed.append(path.relative_to(ROOT).as_posix() if path.is_absolute() else value)
    return {
        "case": name,
        "command": displayed,
        "exit_code": result.returncode,
        "stdout": result.stdout.strip(),
        "stderr": result.stderr.strip(),
    }


def main():
    manifest_hash = hashlib.sha256(MANIFEST.read_bytes()).hexdigest()
    assert manifest_hash == EXPECTED_MANIFEST, "reader snapshot manifest changed"
    entries = [line.rsplit(" ", 1) for line in MANIFEST.read_text(encoding="utf-8").splitlines()]
    assert len(entries) == 4379, "reader snapshot file count changed"
    for relative, expected_hash in entries:
        actual_hash = hashlib.sha256((SNAPSHOT / relative).read_bytes()).hexdigest()
        assert actual_hash == expected_hash, f"reader snapshot changed: {relative}"
    rows = [
        execute("J7 local UI states", "examples/applications/fixture_run.mjs", SNAPSHOT),
        execute("J7 timeout and recovery", "examples/applications/timeout_unit_fixture.mjs", SNAPSHOT),
        execute("J8 widget event and selection", "examples/widgets/fixture_run.mjs", SNAPSHOT),
        execute("J7/J8 independent addendum", HERE / "reader_resume.mjs", HERE),
    ]
    assert all(row["exit_code"] == 0 for row in rows), rows
    assert "No React hook, OAuth grant, Action or website deployment executed" in rows[0]["stdout"]
    assert "selectedRelease" in rows[3]["stdout"]
    evidence = {
        "executed_utc": datetime.now(timezone.utc).isoformat(),
        "snapshot_manifest_sha256": manifest_hash,
        "snapshot_files_verified": len(entries),
        "mode": "synthetic Node fixtures with cooperative public network and child-process denial",
        "live_tenant_tested": False,
        "runs": rows,
    }
    (HERE / "formal_run_output.json").write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"runs": len(rows), "passed": len(rows), "snapshot": manifest_hash}))


if __name__ == "__main__":
    main()
