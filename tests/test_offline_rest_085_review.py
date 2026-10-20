"""Bind the independent Functions review to the exact SDK and local assets."""

import hashlib
import importlib.metadata
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / ".agents/skills/pal-found-dev"
REVIEWER = "/root/feature015_rest_review_audit"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_independent_review_085_tracks_current_source_and_assets():
    evidence = load(ROOT / "maintainer/rest-domain-independent-review-085.json")
    register = load(ROOT / "maintainer/rest-domain-authoring-register.json")
    oracle = load(ROOT / "tests/fixtures/offline/rest-acceptance/source-oracle.json")

    rows = {row["id"]: row for row in register["operations"] if row["story"] == "DEV-STORY-085"}
    operations = evidence["operations"]
    ids = [operation["id"] for operation in operations]
    assert len(ids) == len(set(ids)) == len(rows) == 11
    assert set(ids) == set(rows)
    assert evidence["story"] == "DEV-STORY-085"
    assert evidence["reviewer_agent"] == REVIEWER
    formal = load(ROOT / "maintainer/rest-domain-formal-qa-085.json")
    assert evidence["independent_qa_agent"] is None
    assert evidence["formal_qa_status"] == "pending"
    assert evidence["formal_qa_tasks_observed_2026_10_16"] == {
        "TESTCASE-082": "Open",
        "TESTEXEC-082": "Open",
    }
    assert evidence["source_sdk"] == "foundry-platform-sdk==1.101.0"
    assert importlib.metadata.version("foundry-platform-sdk") == oracle["sdk_release"] == "1.101.0"
    assert evidence["source_commit"] == oracle["source_commit"]

    for operation in operations:
        identity = operation["id"]
        row = rows[identity]
        source = oracle["operations"][identity]
        assert operation["story"] == "DEV-STORY-085"
        assert operation["verdict"] == operation["diagnostic_fixture_result"] == "PASS"
        assert operation["reviewer_agent"] == REVIEWER
        assert operation["independent_qa_agent"] is None
        assert row["independent_reviewer"] == row["reviewer_agent"] == REVIEWER
        assert row["independent_qa_agent"] == formal["reviewer_agent"]
        assert row["author_agent"] != REVIEWER
        assert row["semantic_review_status"] == "accepted"
        assert row["independent_qa_status"] == "accepted"
        assert row["fixture_status"] == "passed"

        assert operation["source_sdk"] == row["source_sdk"] == "1.101.0"
        assert operation["source_commit"] == row["source_commit"] == oracle["source_commit"]
        assert operation["stage"] == source["documentation"]["stage"]
        assert repr(operation["http_method"]) == source["wire"]["method"]
        assert repr(operation["resource_path"]) == source["wire"]["resource_path"]
        assert operation["declared_errors"] == source["wire"]["throwable_errors"]
        assert operation["source_module"] == source["module"]
        assert operation["source_sha256"] == row["source_sha256"] == source["source_sha256"]
        source_spec = importlib.util.find_spec(operation["source_module"])
        assert source_spec is not None and source_spec.origin is not None
        assert digest(Path(source_spec.origin)) == operation["source_sha256"]

        for asset in ("behavior", "example", "contract", "helper"):
            path = operation[asset]
            asset_hash = operation[f"{asset}_sha256"]
            if path is None:
                assert asset == "helper" and asset_hash is None
                continue
            assert digest(SKILL / path) == asset_hash
            if asset in ("behavior", "example"):
                assert path == row[asset]
                assert asset_hash == row[f"{asset}_sha256"]


def test_formal_085_acceptance_binds_execution_log_source_and_closed_workflow():
    """Reject stale evidence, missing cases, altered logs and premature acceptance."""
    evidence = load(ROOT / "maintainer/rest-domain-formal-qa-085.json")
    acceptance = load(ROOT / "maintainer/rest-domain-formal-qa-085-acceptance.json")
    oracle = load(ROOT / "tests/fixtures/offline/rest-acceptance/source-oracle.json")
    register = load(ROOT / "maintainer/rest-domain-authoring-register.json")
    rows = {
        row["id"]: row for row in register["operations"]
        if row["story"] == "DEV-STORY-085"
    }
    assert acceptance["formal_qa_status"] == "accepted"
    qa_agent = acceptance["independent_qa_agent"]
    assert qa_agent == evidence["reviewer_agent"]
    assert evidence["verdict"] == "PASS"
    assert evidence["story"] == acceptance["story"] == "DEV-STORY-085"
    assert evidence["testcase"] == "TESTCASE-082"
    assert evidence["testexec"] == "TESTEXEC-082"
    assert evidence["candidate_commit"] == acceptance["execution_candidate_commit"]
    assert evidence["source_sdk"] == oracle["sdk_release"] == "1.101.0"
    assert evidence["source_commit"] == oracle["source_commit"]
    assert evidence["tenant_verification"] is False
    assert evidence["public_network"] == "denied sockets plus verified denial probe"
    assert evidence["started_at"] <= evidence["finished_at"] <= acceptance["observed_at_utc"]

    for relative, expected in acceptance["artifacts"].items():
        path = (ROOT / relative).resolve()
        assert path.is_relative_to(ROOT.resolve())
        assert digest(path) == expected
    for ticket in ("TESTCASE-082", "TESTEXEC-082"):
        closure = acceptance["closure"][ticket]
        text = (ROOT / closure["evidence"]).read_text(encoding="utf-8")
        assert closure["status"] == "Closed"
        assert digest(ROOT / closure["evidence"]) == closure["sha256"]
        assert f"ticket_id: {ticket}\ncurrent_status: Closed\n" in text
        assert "parent         : DEV-STORY-085" in text

    harness = ROOT / "maintainer/evidence/rest085_formal_execute.py"
    assert digest(harness) == evidence["harness_sha256"]
    harness_text = harness.read_text(encoding="utf-8")
    assert "patch('socket.socket.connect',denied)" in harness_text
    assert "patch('socket.create_connection',denied)" in harness_text
    assert "patch('socket.getaddrinfo',denied)" in harness_text
    assert "else:raise AssertionError('socket trap inactive')" in harness_text
    log_text = (ROOT / "maintainer/evidence/rest085_formal_execute.log").read_text(
        encoding="utf-8"
    )
    logged_checks = [
        json.loads(line) for line in log_text.splitlines() if line.startswith("{")
    ]
    assert logged_checks == evidence["checks"]
    assert "PASS: 91 independent checks; 11/11 formal cases" in log_text
    assert len(logged_checks) == acceptance["checks"] == 91
    assert all(check["result"] == "PASS" for check in logged_checks)
    pairs = {(check["case_id"], check["check"]) for check in logged_checks}
    assert len(pairs) == 91
    common = {
        "selectors_success", "http_401", "http_403", "timeout",
        "missing_required", "malformed", "reader_example",
    }
    extra = {
        "F085-02": {"poll_None", "poll_280"},
        "F085-03": {"worked_example"},
        "F085-04": {"completed", "worked_example"},
        "F085-06": {"omitted_version"},
        "F085-07": {"batch_0", "batch_1", "batch_100", "batch_101"},
        "F085-08": {"finite_sse", "async_sse"},
        "F085-09": {"finite_sse", "async_sse"},
    }
    operations = evidence["operations"]
    assert len(operations) == acceptance["operations"] == len(rows) == 11
    assert {operation["id"] for operation in operations} == set(rows)
    assert {operation["formal_case"] for operation in operations} == {
        f"F085-{index:02}" for index in range(1, 12)
    }
    for index, operation in enumerate(operations, 1):
        identity = operation["id"]
        row = rows[identity]
        source = oracle["operations"][identity]
        case = operation["formal_case"]
        assert case == f"F085-{index:02}"
        assert {name for case_id, name in pairs if case_id == case} == (
            common | extra.get(case, set())
        )
        assert operation["testcase"] == "TESTCASE-082"
        assert operation["testexec"] == "TESTEXEC-082"
        assert operation["verdict"] == "PASS"
        assert operation["independent_qa_agent"] == row["independent_qa_agent"] == qa_agent
        assert qa_agent not in (row["author_agent"], row["reviewer_agent"])
        assert row["independent_qa_status"] == "accepted"
        assert row["semantic_review_status"] == "accepted"
        assert operation["source_module"] == source["module"]
        assert operation["source_sha256"] == row["source_sha256"] == source["source_sha256"]
        source_spec = importlib.util.find_spec(operation["source_module"])
        assert source_spec is not None and source_spec.origin is not None
        assert digest(Path(source_spec.origin)) == operation["source_sha256"]
        assert repr(operation["http_method"]) == source["wire"]["method"]
        assert repr(operation["resource_path"]) == source["wire"]["resource_path"]
        assert operation["declared_errors"] == source["wire"]["throwable_errors"]
        resource, method = identity.split(".")[-2:]
        assert operation["reader_example"] == (
            f"examples/rest/085/v2/functions/{resource}/invoke_{method}.py"
        )
        for asset in ("behavior", "example", "contract", "helper", "reader_example"):
            if operation.get(asset):
                assert digest(SKILL / operation[asset]) == operation[f"{asset}_sha256"]
        for asset in ("behavior", "example"):
            assert operation[asset] == row[asset]
            assert operation[f"{asset}_sha256"] == row[f"{asset}_sha256"]
