"""Deliberate broken fixtures prove structural failures are detected."""

from copy import deepcopy
from pathlib import Path

import pytest

from test_offline_topic_acceptance import (
    COMPONENTS, fixture_revision_matches, local_graph, local_link,
    markdown_anchors, operation_inventory_matches, topic_contract,
)


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
