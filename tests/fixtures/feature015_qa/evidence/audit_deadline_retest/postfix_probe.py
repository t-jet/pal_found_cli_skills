"""Check corrected Audit budget decisions on the post-fix skill snapshot."""

import hashlib
import json
import runpy
import socket
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[6]
SNAPSHOT = ROOT / ".ept/tmp/feature015_audit_postfix_skill_20261011"
SCRIPT = SNAPSHOT / "examples/rest/073/v2/audit/LogFile/list_pagination.py"
OUTPUT = Path(__file__).with_name("postfix_output.json")
enumerate_files = runpy.run_path(str(SCRIPT))["enumerate_files"]
calls = []


def deny(*_args, **_kwargs):
    raise AssertionError("PUBLIC_NETWORK_DENIED")


def page(*_args, **kwargs):
    calls.append(kwargs["request_timeout"])
    return SimpleNamespace(data=[SimpleNamespace(id="log-1")], next_page_token=None)


client = SimpleNamespace(audit=SimpleNamespace(Organization=SimpleNamespace(
    LogFile=SimpleNamespace(list=page)
)))
with patch.object(socket, "getaddrinfo", deny), patch.object(socket.socket, "connect", deny):
    try:
        socket.getaddrinfo("www.palantir.com", 443)
    except AssertionError as error:
        assert str(error) == "PUBLIC_NETWORK_DENIED"
    else:
        raise AssertionError("Network-denial probe failed")
    short_ticks = iter([0, 0])
    short = enumerate_files(client, max_pages=5, seconds=0.01,
                            clock=lambda: next(short_ticks))
    assert short == ([], False, "time_budget", None) and calls == []
    overrun_ticks = iter([0, 0, 1.2])
    overrun = enumerate_files(client, max_pages=5, seconds=1.01,
                              clock=lambda: next(overrun_ticks))
    assert overrun == (["log-1"], False, "time_budget", None) and calls == [1]

payload = {
    "executed_utc": datetime.now(timezone.utc).isoformat(),
    "snapshot_tree_sha256": "790d67ad9a291e4810ad97dfdc3ad2d6c8a62fe1237b2f34a47b615dcf6adb4f",
    "source_path": "examples/rest/073/v2/audit/LogFile/list_pagination.py",
    "source_sha256": hashlib.sha256(SCRIPT.read_bytes()).hexdigest(),
    "mode": "synthetic clock and page with cooperative DNS/socket denial",
    "cases": [
        {"id": "subsecond", "seconds": 0.01, "expected": [[], False, "time_budget", None],
         "actual": list(short), "request_count": 0, "status": "PASS"},
        {"id": "response_overrun", "seconds": 1.01,
         "expected": [["log-1"], False, "time_budget", None],
         "actual": list(overrun), "request_count": 1, "request_timeout": 1, "status": "PASS"},
    ],
    "live_tenant_tested": False,
    "hard_wall_time_preemption_claimed": False,
}
OUTPUT.write_bytes((json.dumps(payload, indent=2) + "\n").encode())
print(json.dumps({"cases": 2, "passed": 2, "source_sha256": payload["source_sha256"]}))
