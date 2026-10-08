"""Structural offline gates; semantic approval remains independent QA evidence."""

import hashlib
import json
from pathlib import Path
import re
import unicodedata
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / ".agents" / "skills"
REGISTER = ROOT / "tests" / "fixtures" / "offline" / "topic-register.json"
COMPONENTS = {
    "concept", "prerequisites", "procedure", "example", "validation",
    "recovery", "access_boundary",
}
PUBLIC_SCHEMES = {"http", "https", "mailto"}
LINK = re.compile(r"!?(?:\[[^\]\n]*\])\(([^\n]*?)\)")
HEADING = re.compile(r"^ {0,3}#{1,6}\s+(.+?)(?:\s+#+)?\s*$", re.M)


def markdown_prose(text: str) -> str:
    """Exclude literal code before looking for navigation links."""
    lines, fence = [], None
    for line in text.splitlines():
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            if fence is None:
                fence = marker.group(1)
            elif marker.group(1)[0] == fence[0] and len(marker.group(1)) >= len(fence):
                fence = None
            lines.append("")
        else:
            lines.append(line if fence is None else "")
    return re.sub(r"(`+).*?\1", "", "\n".join(lines))


def markdown_anchors(text: str) -> set[str]:
    """Resolve ordinary GitHub headings, including repeated-heading suffixes."""
    counts: dict[str, int] = {}
    anchors = set(re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)["\']', text))
    fenced = False
    for line in text.splitlines():
        if line.lstrip().startswith(("```", "~~~")):
            fenced = not fenced
            continue
        match = HEADING.fullmatch(line) if not fenced else None
        if not match:
            continue
        title = re.sub(r"<[^>]+>", "", match.group(1)).lower()
        slug = "".join(
            char for char in title
            if char in " -_" or unicodedata.category(char)[0] in {"L", "N"}
        ).replace(" ", "-")
        occurrence = counts.get(slug, 0)
        counts[slug] = occurrence + 1
        anchors.add(slug if occurrence == 0 else f"{slug}-{occurrence}")
    return anchors


def local_link(page: Path, target: str, owner: Path) -> Path | None:
    """Check a file/anchor reference without resolving public attribution."""
    target = target.strip().strip("<>")
    if not target:
        raise AssertionError(f"{page}: empty link")
    parsed = urlsplit(target)
    if parsed.scheme in PUBLIC_SCHEMES:
        return None
    assert not parsed.scheme and not parsed.netloc, f"{page}: unknown link scheme {target}"
    candidate = (page.parent / unquote(parsed.path)).resolve() if parsed.path else page.resolve()
    assert candidate.is_relative_to(owner.resolve()), f"{page}: link escapes owning folder: {target}"
    assert candidate.is_file(), f"{page}: missing local asset: {target}"
    if parsed.fragment:
        assert candidate.suffix == ".md", f"{page}: anchor on non-Markdown asset: {target}"
        assert unquote(parsed.fragment) in markdown_anchors(candidate.read_text(encoding="utf-8")), (
            f"{page}: missing anchor: {target}"
        )
    return candidate


def local_graph(owner: Path) -> set[Path]:
    pending = [owner / "SKILL.md"]
    visited: set[Path] = set()
    while pending:
        page = pending.pop().resolve()
        if page in visited:
            continue
        visited.add(page)
        if page.suffix != ".md":
            continue
        text = page.read_text(encoding="utf-8")
        assert len(text.splitlines()) <= 300, f"{page}: leaf exceeds 300 lines"
        for match in LINK.finditer(markdown_prose(text)):
            target = local_link(page, match.group(1), owner)
            if target is not None and target not in visited:
                pending.append(target)
    return visited


def topic_contract(owner: Path, register: dict) -> None:
    topics = register["topics"]
    assert {row["id"] for row in topics} == {f"T{n:02}" for n in range(1, 38)}, (
        "Topic identities must be exactly T01 through T37"
    )
    assert len(topics) == 37, "Duplicate topic owner"
    graph = local_graph(owner)
    for row in topics:
        assert set(row["components"]) == COMPONENTS, f"{row['id']}: missing topic component"
        for name, destination in {"root": row["root"], **row["components"]}.items():
            page = local_link(owner / "SKILL.md", destination, owner)
            assert page in graph, f"{row['id']}/{name}: destination unreachable from entry"
        assert row["access_boundary_review"] == "independent QA required", (
            "Structural reachability cannot approve local/enrollment/admin semantics"
        )


def fixture_revision_matches(expected: dict, actual: dict) -> None:
    """Changed shared/REST content invalidates previously accepted evidence."""
    assert expected["candidate_sha"] == actual["candidate_sha"], "Stale accepted REST revision"
    assert expected["required_file_hashes"] == actual["required_file_hashes"], (
        "Changed accepted REST/shared facts require affected checks again"
    )


def operation_inventory_matches(actual: list[str], baseline: dict) -> None:
    assert len(actual) == len(set(actual)) == baseline["operation_count"], (
        "Changed or duplicate CLI operation inventory"
    )
    digest = hashlib.sha256(("\n".join(sorted(actual)) + "\n").encode()).hexdigest()
    assert digest == baseline["operation_sha256"], "Changed CLI operation identity"


def test_all_topics_reachable_inside_standalone_development_skill() -> None:
    topic_contract(SKILLS / "pal-found-dev", json.loads(REGISTER.read_text(encoding="utf-8")))


def test_every_skill_local_graph_stays_inside_owning_folder() -> None:
    for skill in sorted(SKILLS.glob("*/SKILL.md")):
        local_graph(skill.parent)


def test_skill_identities_match_reviewed_baseline() -> None:
    baseline = json.loads(REGISTER.read_text(encoding="utf-8"))["baseline"]
    actual = sorted(path.parent.name for path in SKILLS.glob("*/SKILL.md"))
    assert actual == baseline["skill_identities"]


def test_cli_operation_inventory_matches_reviewed_baseline() -> None:
    from test_offline_skill_gate import FROZEN_OPERATIONS

    baseline = json.loads(REGISTER.read_text(encoding="utf-8"))["baseline"]
    actual = [
        f"{skill}:{operation}"
        for skill, operations in FROZEN_OPERATIONS.items()
        for operation in operations
    ]
    operation_inventory_matches(actual, baseline)
