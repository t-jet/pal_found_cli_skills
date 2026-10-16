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
        assert row["independent_qa_agent"] is None
        assert row["author_agent"] != REVIEWER
        assert row["semantic_review_status"] == "accepted"
        assert row["independent_qa_status"] == "pending"
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
