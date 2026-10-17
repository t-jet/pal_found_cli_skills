"""Mutations proving the independent oracle rejects meaningful contract gaps."""

import ast
from copy import deepcopy
import hashlib
from pathlib import Path

import pytest

from test_offline_rest_acceptance import (
    assert_reader_field_meaning_matches,
    assert_signature_contract,
    no_public_network_probe,
    reader_symbol_definitions,
    rest_input_bundle_sha256,
    reconcile_symbol_definitions,
    source_symbol_closure,
    verify_domain_acceptance,
    verify_reader_definitions,
)


def test_visible_markdown_link_preserves_field_meaning():
    source = "An RID identifying an Agent created in [AIP Chatbot Studio](https://palantir.com/docs/foundry/chatbot-studio/overview/)."
    reader = "An RID identifying an Agent created in AIP Chatbot Studio."
    assert_reader_field_meaning_matches(source, reader, "AgentNotFoundParameters", "agentRid")
    with pytest.raises(AssertionError, match="field meaning omitted or changed"):
        assert_reader_field_meaning_matches(
            source, "An RID identifying an Agent deleted in AIP Chatbot Studio.",
            "AgentNotFoundParameters", "agentRid",
        )


def test_local_note_cannot_change_source_meaning_or_drop_example_url():
    symbol = "foundry_sdk.v2.connectivity.models.SmbConnectionConfiguration"
    source = "Must be a valid SMB share name. https://learn.microsoft.com/en-us/openspecs/example"
    reader = "Must be a valid SMB share name. Confirm the share name on the SMB server."
    assert_reader_field_meaning_matches(source, reader, symbol, "share")
    with pytest.raises(AssertionError, match="field meaning omitted or changed"):
        assert_reader_field_meaning_matches(
            source, "Any string is a valid SMB share name. Confirm the share name on the SMB server.",
            symbol, "share",
        )
    example = "An example URL is https://example.snowflakecomputing.com."
    with pytest.raises(AssertionError, match="field meaning omitted or changed"):
        assert_reader_field_meaning_matches(example, "An example URL is", "example", "account_identifier")


def test_exact_source_fence_remains_required_after_prose_localization():
    source = "class Error:\n    field: str\n    \"\"\"See [local guide](https://example.invalid).\"\"\""
    changed = "class Error:\n    field: str\n    \"\"\"See local guide.\"\"\""
    oracle = {"symbols": {"foundry_sdk.v2.filesystem.errors.Error": {"definition": source}}}
    with pytest.raises(AssertionError, match="mismatch"):
        verify_reader_definitions(oracle, {"foundry_sdk.v2.filesystem.errors.Error": ast.dump(ast.parse(changed), include_attributes=False)})


def test_equal_count_symbol_substitution_is_rejected():
    with pytest.raises(AssertionError, match="Unresolved symbol closure"):
        reconcile_symbol_definitions({"A": "definition"}, {"B": "definition"})


@pytest.mark.parametrize("changed", [
    "Alias = Annotated[str, Field(pattern='.*')]",
    "Alias = Annotated[str, Field(discriminator='other')]",
    "class Model:\n    field: str = None",
])
def test_changed_constraints_discriminators_or_default_are_rejected(changed):
    expected = {"Alias": {"definition": "Alias = Annotated[str, Field(pattern='[0-9]+')]"}}
    with pytest.raises(AssertionError, match="mismatch"):
        verify_reader_definitions({"symbols": expected}, {"Alias": ast.dump(ast.parse(changed), include_attributes=False)})


def test_missing_error_dataclass_decorator_is_rejected(tmp_path: Path):
    (tmp_path / "Error.md").write_text("# foundry_sdk.v2.filesystem.errors.Error\n\n```python\nclass Error:\n    name: str\n```\n")
    expected = {"foundry_sdk.v2.filesystem.errors.Error": {"definition": "@dataclass\nclass Error:\n    name: str"}}
    with pytest.raises(AssertionError, match="mismatch"):
        verify_reader_definitions({"symbols": expected}, reader_symbol_definitions(tmp_path))


def test_compound_forward_union_resolves_both_variants():
    files = {
        "foundry_sdk/_core/config.py": b"class Config: pass",
        "foundry_sdk/v2/filesystem/models.py": b"""
from typing import Annotated, Union
from pydantic import Field
class VariantA: pass
class VariantB: pass
Request = Annotated[Union['VariantA', 'VariantB'], Field(discriminator='type')]
""",
        "foundry_sdk/v2/filesystem/folder.py": b"""
from foundry_sdk.v2.filesystem.models import Request
class FolderClient:
    def create(self, body: Request) -> Request:
        return core.RequestInfo(body=body, response_type=Request)
""",
    }
    closure, _ = source_symbol_closure(files)
    assert closure["foundry_sdk.v2.filesystem.models.Request"]["dependencies"] == [
        "foundry_sdk.v2.filesystem.models.VariantA",
        "foundry_sdk.v2.filesystem.models.VariantB",
    ]


def test_optional_annotation_does_not_make_required_argument_omittable():
    def required(value: str | None) -> str:
        return str(value)
    expected = {"signature": "value: str | None = None", "return": "str", "coroutine_definition": False}
    with pytest.raises(AssertionError, match="default/requiredness"):
        assert_signature_contract("fixture", required, expected, {})


def test_direct_async_iterator_is_not_assumed_coroutine():
    def direct() -> str:
        return "iterator stand-in"
    expected = {"signature": "", "return": "str", "coroutine_definition": True}
    with pytest.raises(AssertionError):
        assert_signature_contract("fixture", direct, expected, {})


def test_public_network_probe_is_really_denied():
    no_public_network_probe()


@pytest.mark.parametrize("mutation,message", [
    ("missing", "Incomplete behavioral"),
    ("selfreview", "self-review"),
    ("pending", "semantic review pending"),
    ("stale_sha", "Stale domain"),
    ("changed_example", "changed accepted example"),
])
def test_behavioral_acceptance_requires_complete_independent_current_evidence(tmp_path, mutation, message):
    (tmp_path / "behavior.md").write_text("Reviewed procedure")
    (tmp_path / "example.py").write_text("print('fixture')")
    sha = "a" * 40
    row = {
        "id": "v2.filesystem.Folder.get", "source_sdk": "1.101.0",
        "source_commit": "168d51910570b6966afa2320333ab36f6a3f7ccf",
        "author": "content-author", "independent_reviewer": "another-reviewer",
        "author_agent": "author-agent", "reviewer_agent": "review-agent", "independent_qa_agent": "qa-agent",
        "semantic_review_status": "accepted", "independent_qa_status": "accepted",
        "fixture_status": "passed", "source_sha256": "source-hash", "doc_sha256": "doc-hash",
        "fixture_entrypoint": "verify", "behavior": "behavior.md", "example": "example.py",
        "behavior_sha256": hashlib.sha256((tmp_path / "behavior.md").read_bytes()).hexdigest(),
        "example_sha256": hashlib.sha256((tmp_path / "example.py").read_bytes()).hexdigest(),
    }
    oracle = {"operations": {row["id"]: {"source_sha256": "source-hash", "documentation": {"doc_sha256": "doc-hash"}}}}
    register = {"candidate_sha": sha, "input_bundle_sha256": rest_input_bundle_sha256(tmp_path), "operations": [deepcopy(row)]}
    verify_domain_acceptance(oracle, register, tmp_path, sha)
    if mutation == "missing":
        register["operations"] = []
    elif mutation == "selfreview":
        register["operations"][0]["independent_reviewer"] = row["author"]
    elif mutation == "pending":
        register["operations"][0]["semantic_review_status"] = "pending"
    elif mutation == "stale_sha":
        register["candidate_sha"] = "b" * 40
    else:
        (tmp_path / "example.py").write_text("Changed after QA")
    with pytest.raises(AssertionError, match=message):
        verify_domain_acceptance(oracle, register, tmp_path, sha)
