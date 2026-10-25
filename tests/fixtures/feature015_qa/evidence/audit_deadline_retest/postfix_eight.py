"""Record all eight corrected Audit pagination fixture paths with exact outputs."""

import hashlib
import json
import runpy
import socket
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[6]
SNAPSHOT = ROOT / ".ept/tmp/feature015_audit_postfix_skill_20261011"
SCRIPT = SNAPSHOT / "examples/rest/073/v2/audit/LogFile/list_pagination.py"
OUTPUT = Path(__file__).with_name("postfix_eight_output.json")
namespace = runpy.run_path(str(SCRIPT))
scenario = namespace["scenario"]
pages = [
    {"data": [{"id": "log-1"}], "nextPageToken": "A"},
    {"data": [], "nextPageToken": "B"},
    {"data": [{"id": "log-2"}]},
]
cases = []


def deny(*_args, **_kwargs):
    raise AssertionError("PUBLIC_NETWORK_DENIED")


def record(case_id, expected, actual):
    assert actual == expected, (case_id, actual, expected)
    cases.append({"case": case_id, "expected": expected, "actual": actual, "status": "PASS"})


with patch.object(socket, "getaddrinfo", deny), patch.object(socket.socket, "connect", deny), \
     patch.object(socket.socket, "connect_ex", deny), patch.object(socket, "create_connection", deny):
    try:
        socket.getaddrinfo("www.palantir.com", 443)
    except AssertionError as error:
        assert str(error) == "PUBLIC_NETWORK_DENIED"
    else:
        raise AssertionError("Network-denial probe failed")
    record("complete_through_empty_page", [None, "A", "B"],
           scenario(pages, 5, (["log-1", "log-2"], True, None, None)))
    record("page_budget", [None, "A"],
           scenario(pages[:2], 2, (["log-1"], False, "page_budget", "B")))
    record("item_budget", [None],
           scenario([{"data": [{"id": "log-1"}, {"id": "log-2"}], "nextPageToken": "A"}],
                    5, (["log-1"], False, "item_budget", None), max_items=1))
    record("repeated_token", [None, "A"],
           scenario([pages[0], {"data": [], "nextPageToken": "A"}],
                    5, (["log-1"], False, "repeated_token", "A")))
    expired_ticks = iter([0, 31])
    record("expired_before_request", [],
           scenario([], 5, ([], False, "time_budget", None),
                    clock=lambda: next(expired_ticks)))
    short_ticks = iter([0, 0])
    record("subsecond_no_request", [],
           scenario([], 5, ([], False, "time_budget", None), seconds=0.01,
                    clock=lambda: next(short_ticks)))
    overrun_ticks = iter([0, 0, 1.2])
    record("response_overrun_partial", [None],
           scenario([{"data": [{"id": "log-1"}]}], 5,
                    (["log-1"], False, "time_budget", None), seconds=1.01,
                    clock=lambda: next(overrun_ticks)))
    namespace["missing_start_date"]()
    record("missing_start_date_named_error", "MissingStartDate", "MissingStartDate")

payload = {
    "executed_utc": datetime.now(timezone.utc).isoformat(),
    "snapshot_tree_sha256": "790d67ad9a291e4810ad97dfdc3ad2d6c8a62fe1237b2f34a47b615dcf6adb4f",
    "source_path": "examples/rest/073/v2/audit/LogFile/list_pagination.py",
    "source_sha256": hashlib.sha256(SCRIPT.read_bytes()).hexdigest(),
    "mode": "SDK 1.101.0 MockTransport, synthetic clock, cooperative public DNS/socket denial",
    "cases": cases,
    "live_tenant_tested": False,
}
OUTPUT.write_bytes((json.dumps(payload, indent=2) + "\n").encode())
print(json.dumps({"cases": len(cases), "passed": len(cases),
                  "source_sha256": payload["source_sha256"]}))
