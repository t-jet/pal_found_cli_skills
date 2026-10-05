"""User-facing and copied-folder gates for the Foundry development skill."""

import ast
from pathlib import Path
import re
import shutil


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
    assert {p.name for p in (DEV / "references").glob("*.md")} == PARTS
    for page in _markdown_files(DEV):
        text = page.read_text(encoding="utf-8")
        assert "https://www.palantir.com/docs/foundry/" in text, page
        assert "utm_source=" not in text, page
        if page.name != "SKILL.md":
            assert "../SKILL.md" in text, f"{page}: missing entry-point link"


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
        re.compile(r"development-skill-coverage|architecture decision record", re.I),
        re.compile(r"copy (?:the entire |this |the )?(?:skill )?folder", re.I),
    )
    for page in _markdown_files(SKILLS):
        text = page.read_text(encoding="utf-8")
        for pattern in forbidden:
            assert not pattern.search(text), f"{page}: forbidden {pattern.pattern}"


def test_rest_guide_contains_read_only_contract_and_limits() -> None:
    text = (DEV / "references" / "rest-api.md").read_text(encoding="utf-8")
    required = (
        "GET /api/v2/datasets/{datasetRid}",
        "FoundryClient",
        "UserTokenAuth",
        "nextPageToken",
        "pageToken",
        "timeout",
        "401",
        "403",
        "429",
        "https://www.palantir.com/docs/foundry/api/v2/general/overview/sdks",
    )
    for item in required:
        assert item in text, f"REST guide missing {item}"
    assert "https://www.palantir.com/docs/foundry/api/general/overview/sdk" not in text
    snippets = re.findall(r"```python\n(.*?)\n```", text, re.S)
    assert snippets, "REST guide must include executable Python examples"
    for snippet in snippets:
        ast.parse(snippet)
