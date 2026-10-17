"""Reproduce the pre-fix Audit time-budget failure without network access."""

import hashlib
import json
import runpy
import socket
from datetime import datetime, timezone
from pathlib import Path
from time import monotonic, sleep
from types import SimpleNamespace
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[6]
SNAPSHOT = ROOT / ".ept/tmp/feature015_final_reader_skill_20261011"
SCRIPT = SNAPSHOT / "examples/rest/073/v2/audit/LogFile/list_pagination.py"
OUTPUT = Path(__file__).with_name("failure.json")
SOURCE_SHA = hashlib.sha256(SCRIPT.read_bytes()).hexdigest()
enumerate_files = runpy.run_path(str(SCRIPT))["enumerate_files"]
timeouts = []


def deny(*_args, **_kwargs):
    raise AssertionError("PUBLIC_NETWORK_DENIED")


def page(*_args, **kwargs):
    timeouts.append(kwargs["request_timeout"])
    sleep(0.12)
    return SimpleNamespace(data=[], next_page_token=None)


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
    started = monotonic()
    result = enumerate_files(client, max_pages=1, seconds=0.01)
    elapsed = monotonic() - started

failure = elapsed > 0.01 and timeouts == [1] and result == ([], True, None, None)
payload = {
    "executed_utc": datetime.now(timezone.utc).isoformat(),
    "snapshot_tree_sha256": "6949469c7055ba3396bdf8f7570ab696f2122298536962f7be7e646a11a00eb7",
    "source_path": "examples/rest/073/v2/audit/LogFile/list_pagination.py",
    "source_sha256": SOURCE_SHA,
    "mode": "synthetic in-process fake page with cooperative DNS/socket denial",
    "budget_seconds": 0.01,
    "fake_page_delay_seconds": 0.12,
    "elapsed_seconds": round(elapsed, 3),
    "request_timeout_seconds": timeouts,
    "expected": "Do not claim completion after the stated wall-time budget ends",
    "actual": {"file_ids": result[0], "complete": result[1], "reason": result[2], "cursor": result[3]},
    "status": "FAIL" if failure else "PASS",
    "live_tenant_tested": False,
}
OUTPUT.write_bytes((json.dumps(payload, indent=2) + "\n").encode())
print(json.dumps({key: payload[key] for key in ("budget_seconds", "elapsed_seconds", "request_timeout_seconds", "actual", "status")}))
if failure:
    raise SystemExit(1)
