"""Deliberate broken fixtures prove structural failures are detected."""

from copy import deepcopy
import hashlib
import importlib.util
import os
from pathlib import Path
import socket
import subprocess

import httpx
import pytest

from test_offline_topic_acceptance import (
    COMPONENTS, fixture_revision_matches, local_graph, local_link,
    markdown_anchors, operation_inventory_matches, skill_identities_match, topic_contract,
    url_audit_complete,
)


RUNNER = Path(__file__).parent / "fixtures/offline/topic-acceptance/runner.py"
SPEC = importlib.util.spec_from_file_location("topic_acceptance_runner", RUNNER)
assert SPEC is not None and SPEC.loader is not None
runner = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(runner)


def make_skill(root: Path) -> Path:
    owner = root / "skill"
    owner.mkdir()
    (owner / "SKILL.md").write_text("# Entry\n\n[Topic](topic.md#topic)\n", encoding="utf-8")
    (owner / "topic.md").write_text("# Topic\n\n[Entry](SKILL.md)\n", encoding="utf-8")
    return owner


def test_literal_code_is_not_treated_as_navigation(tmp_path):
    owner = make_skill(tmp_path)
    page = owner / "topic.md"
    page.write_text("# Topic\n\nLiteral punctuation `[]()` and `[missing](missing.md)`.\n\n```python\nvalue = '[also](absent.md)'\n```\n\n[Entry](SKILL.md)\n")
    assert local_graph(owner) == {(owner / "SKILL.md").resolve(), page.resolve()}


def valid_register() -> dict:
    return {"topics": [
        {"id": f"T{n:02}", "root": "topic.md#topic",
         "components": dict.fromkeys(COMPONENTS, "topic.md#topic"),
         "access_boundary_review": "independent QA required"}
        for n in range(1, 38)
    ]}


@pytest.mark.parametrize("target", ["../outside.md", "absent.csv", "topic.md#absent"])
def test_missing_asset_anchor_or_folder_escape_fails(tmp_path, target) -> None:
    owner = make_skill(tmp_path)
    (tmp_path / "outside.md").write_text("# Outside", encoding="utf-8")
    with pytest.raises(AssertionError):
        local_link(owner / "SKILL.md", target, owner)


def test_optional_public_attribution_needs_no_network(tmp_path) -> None:
    owner = make_skill(tmp_path)
    assert local_link(owner / "SKILL.md", "https://www.palantir.com/docs/foundry/", owner) is None


def test_markdown_anchors_ignore_code_and_handle_repeated_headings() -> None:
    assert markdown_anchors("# Topic\n## Prerequisites\n\n```python\n# Ignore\n```\n## Prerequisites") == {
        "topic", "prerequisites", "prerequisites-1",
    }


def test_overlong_linked_leaf_fails(tmp_path) -> None:
    owner = make_skill(tmp_path)
    (owner / "topic.md").write_text("# Topic\n" + "\n" * 300, encoding="utf-8")
    with pytest.raises(AssertionError, match="300"):
        local_graph(owner)


def test_register_requires_every_topic_and_access_boundary(tmp_path) -> None:
    owner = make_skill(tmp_path)
    register = valid_register()
    topic_contract(owner, register)
    incomplete = deepcopy(register)
    incomplete["topics"].pop()
    with pytest.raises(AssertionError, match="identities"):
        topic_contract(owner, incomplete)
    incomplete = deepcopy(register)
    del incomplete["topics"][0]["components"]["access_boundary"]
    with pytest.raises(AssertionError, match="component"):
        topic_contract(owner, incomplete)


def test_unreachable_topic_cannot_pass_due_to_file_presence(tmp_path) -> None:
    owner = make_skill(tmp_path)
    (owner / "other.md").write_text("# Topic", encoding="utf-8")
    register = valid_register()
    register["topics"][0]["root"] = "other.md#topic"
    with pytest.raises(AssertionError, match="unreachable"):
        topic_contract(owner, register)


def test_stale_revision_or_shared_file_change_requires_retest() -> None:
    accepted = {"candidate_sha": "accepted", "required_file_hashes": {"model.md": "old"}}
    fixture_revision_matches(accepted, deepcopy(accepted))
    for changed in [
        {"candidate_sha": "other", "required_file_hashes": {"model.md": "old"}},
        {"candidate_sha": "accepted", "required_file_hashes": {"model.md": "new"}},
    ]:
        with pytest.raises(AssertionError):
            fixture_revision_matches(accepted, changed)


def test_operation_substitution_cannot_pass_an_equal_count() -> None:
    import hashlib
    baseline = {"operation_count": 2, "operation_sha256": hashlib.sha256(b"a\nb\n").hexdigest()}
    operation_inventory_matches(["b", "a"], baseline)
    with pytest.raises(AssertionError, match="identity"):
        operation_inventory_matches(["a", "c"], baseline)


def test_candidate_hash_check_rejects_changed_content_and_revision(tmp_path) -> None:
    owner = make_skill(tmp_path)
    content = (owner / "topic.md").read_bytes()
    accepted = {"candidate_sha": "reviewed", "required_file_hashes": {
        "topic.md": hashlib.sha256(content).hexdigest(),
    }}
    runner.verify_accepted_candidate(owner, accepted, "reviewed")
    with pytest.raises(AssertionError, match="Stale"):
        runner.verify_accepted_candidate(owner, accepted, "changed")
    (owner / "topic.md").write_text("# New topic\n", encoding="utf-8")
    with pytest.raises(AssertionError, match="Changed accepted"):
        runner.verify_accepted_candidate(owner, accepted, "reviewed")
    with pytest.raises(AssertionError, match="external candidate"):
        runner.file_hashes(owner, ["../outside.md"])


def test_offline_fixture_denies_dns_tcp_and_subprocess() -> None:
    with runner.denied_public_network():
        with pytest.raises(AssertionError, match="network denied"):
            socket.getaddrinfo("example.com", 443)
        with pytest.raises(AssertionError, match="network denied"):
            socket.socket().connect(("127.0.0.1", 80))
        with pytest.raises(AssertionError, match="network denied"):
            subprocess.Popen(["python", "-V"])
        with pytest.raises(AssertionError, match="network denied"):
            os.system("echo should-not-run")
        with httpx.Client() as client:
            with pytest.raises(AssertionError, match="network denied"):
                client.get("https://example.com/")
        with httpx.Client(transport=httpx.MockTransport(
            lambda _request: httpx.Response(200, json={"fixture": True})
        )) as client:
            assert client.get("https://example.com/").json() == {"fixture": True}


def test_required_public_reading_disposition_blocks_acceptance() -> None:
    row = {"skill": "pal-found-dev", "path": "SKILL.md", "line": 3,
           "url": "https://example.com/required", "qa_reviewer": "qa-engineer",
           "qa_reason": "The only instructions are on the public page.",
           "qa_disposition": "model_or_contract_localization_review",
           "acceptance_blocking": True}
    audit = {"current_url_audit": {"occurrences": [row],
                                   "skill_counts": {"pal-found-dev": 1}}}
    with pytest.raises(AssertionError, match="essential public-reading contexts unresolved"):
        url_audit_complete(audit)
    row["qa_disposition"] = "optional_provenance_local_page"
    row["acceptance_blocking"] = False
    url_audit_complete(audit, {"pal-found-dev"})


def test_missing_skill_and_audit_entry_are_detected() -> None:
    baseline = {"skill_identities": ["pal-found", "pal-found-dev"]}
    skill_identities_match(["pal-found-dev", "pal-found"], baseline)
    with pytest.raises(AssertionError, match="20-skill identity"):
        skill_identities_match(["pal-found-dev"], baseline)
    audit = {"current_url_audit": {"skill_counts": {"pal-found-dev": 1},
                                   "occurrences": [{"skill": "pal-found-dev"}]}}
    with pytest.raises(AssertionError, match="20-skill URL audit"):
        url_audit_complete(audit, set(baseline["skill_identities"]))


def test_stale_public_url_context_requires_audit_refresh(tmp_path) -> None:
    page = tmp_path / "pal-found-dev" / "SKILL.md"
    page.parent.mkdir()
    page.write_text("# Skill\nOptional source: https://example.com/overview\n", encoding="utf-8")
    row = {"skill": "pal-found-dev", "path": "pal-found-dev/SKILL.md", "line": 2,
           "url": "https://example.com/overview", "qa_reviewer": "qa-engineer",
           "qa_reason": "Local concept supplied", "qa_disposition": "optional_provenance_local_page",
           "acceptance_blocking": False}
    audit = {"current_url_audit": {"skill_counts": {"pal-found-dev": 1},
                                   "occurrences": [row]}}
    url_audit_complete(audit, {"pal-found-dev"}, tmp_path)
    page.write_text("# Skill\nLocal concept only\n", encoding="utf-8")
    with pytest.raises(AssertionError, match="stale URL audit context"):
        url_audit_complete(audit, {"pal-found-dev"}, tmp_path)


def test_staging_accepts_only_development_skill_under_parent_tmp(tmp_path) -> None:
    owner = tmp_path / "pal-found-dev"
    owner.mkdir()
    (owner / "SKILL.md").write_text("# Offline topic\n", encoding="utf-8")
    with pytest.raises(AssertionError, match="parent"):
        runner.stage_skill(owner, tmp_path)
    approved_tmp = Path(__file__).resolve().parents[2] / ".ept" / "tmp"
    staged = runner.stage_skill(owner, approved_tmp)
    assert staged.is_relative_to(approved_tmp)
    assert sorted(path.name for path in staged.iterdir()) == ["SKILL.md"]
