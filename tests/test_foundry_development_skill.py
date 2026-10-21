"""User-facing and copied-folder gates for the Foundry development skill."""

import ast
from pathlib import Path
import re
import runpy
import shutil
from types import SimpleNamespace


ROOT = Path(__file__).parent.parent
SKILLS = ROOT / ".agents" / "skills"
DEV = SKILLS / "pal-found-dev"
PARTS = {
    "pipelines.md",
    "ontology-compute.md",
    "applications-branching-security.md",
    "rest-api.md",
    "operations.md",
}


def _markdown_files(root: Path) -> list[Path]:
    return sorted(root.rglob("*.md"))


def _local_links(page: Path) -> list[str]:
    text = page.read_text(encoding="utf-8")
    return [
        target.split("#", 1)[0]
        for target in re.findall(r"\]\(([^)]+)\)", text)
        if not target.startswith(("https://", "http://", "mailto:", "#"))
    ]


def test_development_skill_has_all_local_parts_and_official_sources() -> None:
    assert (DEV / "SKILL.md").is_file()
    assert PARTS <= {p.name for p in (DEV / "references").glob("*.md")}
    for page in _markdown_files(DEV):
        text = page.read_text(encoding="utf-8")
        assert "utm_source=" not in text, page
    # Topic reachability, exact anchors and owning-folder boundaries are
    # validated by the offline topic register. Attribution is optional.


def test_copied_development_skill_has_only_self_contained_links(tmp_path: Path) -> None:
    copied = tmp_path / "pal-found-dev"
    shutil.copytree(DEV, copied)
    for page in _markdown_files(copied):
        for link in _local_links(page):
            target = (page.parent / link).resolve()
            assert target.is_relative_to(copied.resolve()) and target.is_file(), (
                f"{page.relative_to(copied)}: broken or external local link {link}"
            )


def test_distributed_skills_omit_project_internals_and_copy_directions() -> None:
    forbidden = (
        re.compile(r"\.ept[/\\]", re.I),
        re.compile(r"\bADR[- ]?\d+\b", re.I),
        re.compile(r"\b(?:BA|SA)-(?:ANA|DES)-\d+\b", re.I),
        re.compile(r"\b(?:FEATURE|DEV-STORY|CODEREVIEW)-\d+\b", re.I),
        re.compile(r"foundry-platform-python|docs[/\\]customer_input|docs[/\\]deliverables", re.I),
        re.compile(r"(?<![a-z0-9])docs[/\\]v[12][/\\]", re.I),
        re.compile(r"development-skill-coverage|architecture decision record", re.I),
        re.compile(r"copy (?:the entire |this |the )?(?:skill )?folder", re.I),
    )
    for page in _markdown_files(SKILLS):
        text = page.read_text(encoding="utf-8")
        # An official SDK source citation is provenance, not an internal
        # checkout dependency. Check the surrounding reader prose separately.
        text = re.sub(r"https?://[^\s)<>]+", "", text)
        for pattern in forbidden:
            assert not pattern.search(text), f"{page}: forbidden {pattern.pattern}"


def test_rest_guide_routes_to_local_contract_and_bounded_paging() -> None:
    """Keep REST guidance navigable after examples moved into local parts."""
    guide = (DEV / "references" / "rest-api.md").read_text(encoding="utf-8")
    behavior = (DEV / "references" / "rest" / "client-behavior.md").read_text(
        encoding="utf-8"
    )
    contract = DEV / "references/rest/contracts/v2/filesystem/Folder/get.md"
    assert "rest/catalog.md" in guide
    assert "rest/client-behavior.md#bounded-pagination" in guide
    assert "rest/contracts/v2/filesystem/Folder/get.md" in guide
    assert contract.is_file()
    for item in ("FoundryClient", "UserTokenAuth", "request_timeout=30"):
        assert item in guide
    for item in ("nextPageToken", "repeated", "empty", "page"):
        assert item in behavior
    # Error status handling lives with the operation-specific error models;
    # the common guide explains the recovery decision and its local route.
    assert "Errors and cleanup" in behavior
    assert "identity or permission" in behavior
    assert "PalantirRPCException" in behavior
    # The entry-point example is an indented Python block; it must parse.
    snippet = guide.split("    from foundry_sdk import", 1)[1].split("\n\nRead ", 1)[0]
    ast.parse("from foundry_sdk import" + snippet.replace("\n    ", "\n"))


def test_local_paging_helper_handles_empty_page_and_repeated_cursor() -> None:
    helper = runpy.run_path(str(DEV / "examples/rest/common/bounded_pages.py"))
    fetch_pages = helper["fetch_pages"]
    network = runpy.run_path(str(ROOT / "tests/fixtures/offline/topic-acceptance/runner.py"))
    calls, closed = [], []
    pages = [([], "next"), ([{"id": 2}], None)]

    def fetch_page(*, page_token):
        calls.append(page_token)
        data, cursor = pages[len(calls) - 1]
        return SimpleNamespace(
            decode=lambda: SimpleNamespace(data=data, next_page_token=cursor),
            close=lambda: closed.append(page_token),
        )

    with network["denied_public_network"]():
        result = fetch_pages(fetch_page, max_pages=3, max_items=2)
    assert result.complete and result.items == [{"id": 2}]
    assert calls == [None, "next"] and closed == [None, "next"]

    calls.clear()
    closed.clear()
    pages = [([], "same"), ([], "same")]
    with network["denied_public_network"]():
        result = fetch_pages(fetch_page, max_pages=3, max_items=2)
    assert not result.complete and result.reason == "repeated-token"
    assert calls == [None, "same"] and closed == [None, "same"]
