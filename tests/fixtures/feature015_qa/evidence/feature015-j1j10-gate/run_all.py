"""Capture isolated local fixture and public-network denial evidence."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import foundry_sdk
from importlib.metadata import version


BASE = Path(__file__).resolve().parent
SKILL = BASE / "pal-found-dev"
MANIFEST = BASE / "manifest.json"
NODE = "node"


def captured(label: str, command: list[str], cwd: Path) -> dict:
    result = subprocess.run(command, cwd=cwd, capture_output=True, text=True, timeout=90)
    return {
        "label": label,
        "command": command,
        "cwd": str(cwd),
        "exit_code": result.returncode,
        "stdout": result.stdout.strip(),
        "stderr": result.stderr.strip(),
    }


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    changed = [
        row["path"]
        for row in manifest["files"]
        if hashlib.sha256((SKILL / row["path"]).read_bytes()).hexdigest() != row["sha256"]
    ]
    assert not changed, f"Skill snapshot changed: {changed[:3]}"
    manifest_digest = hashlib.sha256(
        json.dumps(manifest, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    results = [captured("python_j1_j6_j9_j10", [sys.executable, "-B", str(BASE / "run_python_gate.py")], BASE)]
    results.append(captured("node_denial_probe", [NODE, "--require", str(BASE / "deny_public.cjs"), str(BASE / "probe_node.cjs")], BASE))
    for relative in (
        "examples/ontology/query_fixture.mjs",
        "examples/applications/fixture_run.mjs",
        "examples/applications/timeout_unit_fixture.mjs",
        "examples/widgets/fixture_run.mjs",
    ):
        results.append(captured(relative, [NODE, "--require", str(BASE / "deny_public.cjs"), relative], SKILL))
    evidence = {
        "skill_root": str(SKILL),
        "skill_file_count": manifest["file_count"],
        "manifest_sha256": manifest_digest,
        "sdk_version": foundry_sdk.__version__,
        "sdk_distribution_version": version("foundry-platform-sdk"),
        "network_boundary": "Python socket/DNS and Node DNS/TCP/IP/fetch/UDP/subprocess/worker patched; no loopback exception",
        "results": results,
    }
    (BASE / "gate_results.json").write_text(json.dumps(evidence, indent=2), encoding="utf-8")
    for row in results:
        print(f"{row['label']}: exit {row['exit_code']}")
    if any(row["exit_code"] != 0 for row in results):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
