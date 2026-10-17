"""Structural offline gates; semantic approval remains independent QA evidence."""

import hashlib
import json
from pathlib import Path
import re
import runpy
import unicodedata
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / ".agents" / "skills"
REGISTER = ROOT / "tests" / "fixtures" / "offline" / "topic-register.json"
URL_AUDIT = ROOT / "maintainer" / "offline-knowledge-audit.json"
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


def skill_identities_match(actual: list[str], baseline: dict) -> None:
    assert sorted(actual) == baseline["skill_identities"], "Changed 20-skill identity set"


def url_audit_complete(audit: dict, expected_skills: set[str] | None = None,
                       skill_root: Path | None = None) -> None:
    """Require a reviewed, nonblocking decision for each public URL context."""
    current = audit["current_url_audit"]
    rows = current["occurrences"]
    if expected_skills is not None:
        assert set(current["skill_counts"]) == expected_skills, "Incomplete 20-skill URL audit"
        assert {row["skill"] for row in rows} == expected_skills, "Missing skill URL review"
    assert rows, "Missing 20-skill URL audit"
    blocking = []
    for row in rows:
        assert row["skill"] and row["path"] and row["url"], "Incomplete URL context"
        assert row.get("qa_reviewer") and row.get("qa_reason"), (
            f"{row['path']}:{row['line']}: URL context lacks review"
        )
        assert row.get("qa_disposition") and row["qa_disposition"] != "unreviewed", (
            f"{row['path']}:{row['line']}: URL context lacks a disposition"
        )
        if row.get("acceptance_blocking") is not False:
            blocking.append(f"{row['path']}:{row['line']}")
    assert not blocking, (
        f"{len(blocking)} essential public-reading contexts unresolved; "
        f"first: {', '.join(blocking[:3])}"
    )
    if skill_root is not None:
        for row in rows:
            page = (skill_root / row["path"]).resolve()
            assert page.is_relative_to(skill_root.resolve()) and page.is_file(), (
                f"{row['path']}: stale URL audit path"
            )
            lines = page.read_text(encoding="utf-8").splitlines()
            assert 0 < row["line"] <= len(lines) and row["url"] in lines[row["line"] - 1], (
                f"{row['path']}:{row['line']}: stale URL audit context"
            )


def test_all_topics_reachable_inside_standalone_development_skill() -> None:
    topic_contract(SKILLS / "pal-found-dev", json.loads(REGISTER.read_text(encoding="utf-8")))


def test_staged_development_skill_keeps_complete_local_topic_graph() -> None:
    runner = runpy.run_path(str(ROOT / "tests/fixtures/offline/topic-acceptance/runner.py"))
    staged = runner["stage_skill"](SKILLS / "pal-found-dev", ROOT.parent / ".ept/tmp")
    topic_contract(staged, json.loads(REGISTER.read_text(encoding="utf-8")))
    assert staged.parent.parent == (ROOT.parent / ".ept/tmp").resolve()
    assert sorted(path.name for path in staged.parent.iterdir()) == ["pal-found-dev"]


def test_every_skill_local_graph_stays_inside_owning_folder() -> None:
    for skill in sorted(SKILLS.glob("*/SKILL.md")):
        local_graph(skill.parent)


def test_skill_identities_match_reviewed_baseline() -> None:
    baseline = json.loads(REGISTER.read_text(encoding="utf-8"))["baseline"]
    actual = sorted(path.parent.name for path in SKILLS.glob("*/SKILL.md"))
    skill_identities_match(actual, baseline)


def test_offline_knowledge_audit_tracks_current_local_pages() -> None:
    audit = json.loads(URL_AUDIT.read_text(encoding="utf-8"))
    listed = audit["files"]
    listed_paths = [row["path"].replace("\\", "/") for row in listed]
    actual_paths = {
        page.relative_to(SKILLS).as_posix()
        for page in SKILLS.glob("pal-found*/**/*.md")
        if page.relative_to(SKILLS).parts[:3] != ("pal-found-dev", "references", "rest")
    }
    assert len(listed_paths) == len(set(listed_paths)), "Duplicate audit page"
    assert set(listed_paths) == actual_paths, "Offline knowledge audit page inventory drift"
    assert audit["scope"]["markdown_files"] == len(actual_paths), "Stale audit page count"
    assert {path.split("/")[0] for path in actual_paths} == {
        page.parent.name for page in SKILLS.glob("*/SKILL.md")
    }, "Missing skill in audit page inventory"
    for row, relative in zip(listed, listed_paths):
        page = SKILLS / relative
        assert hashlib.sha256(page.read_bytes()).hexdigest() == row["sha256"], (
            f"{relative}: stale offline audit hash"
        )
        assert len(page.read_text(encoding="utf-8").splitlines()) == row["lines"], (
            f"{relative}: stale offline audit line count"
        )
        assert row["owner"] and row["review_status"] and row["disposition"], (
            f"{relative}: incomplete audit ownership or review state"
        )


def test_cli_operation_inventory_matches_reviewed_baseline() -> None:
    baseline = json.loads(REGISTER.read_text(encoding="utf-8"))["baseline"]
    actual = []
    for page in SKILLS.glob("pal-found-*/**/*.md"):
        if page.parent.name == "pal-found-dev" or "pal-found-dev" in page.parts:
            continue
        for resource, operation in re.findall(
            r"^### ([a-z][a-z0-9_]+)\.([a-z][a-z0-9_]+)$",
            page.read_text(encoding="utf-8"), re.M,
        ):
            actual.append(f"{page.relative_to(SKILLS).parts[0]}:{resource} {operation}")
    operation_inventory_matches(actual, baseline)


def test_reader_case_plan_covers_all_topics_journeys_and_rest_namespaces() -> None:
    fixtures = ROOT / "tests/fixtures/feature015_qa"
    plan = json.loads((fixtures / "reader_coverage.json").read_text(encoding="utf-8"))
    prompts = json.loads((fixtures / "reader_prompts.json").read_text(encoding="utf-8"))
    topics = json.loads(REGISTER.read_text(encoding="utf-8"))["topics"]
    journey_ids = {f"J{number}" for number in range(1, 15)}
    topic_ids = {row["id"] for row in topics}
    assert set(plan["journey_topic_map"]) == journey_ids
    assert {row["id"] for row in prompts["cases"]} == journey_ids - {"J9", "J10"}
    assert set().union(*(set(ids) for ids in plan["journey_topic_map"].values())) == topic_ids
    assert len(plan["rubric_dimensions"]) == len(set(plan["rubric_dimensions"])) == 6
    namespace_cases = json.loads(
        (fixtures / plan["rest_namespace_cases"]).resolve().read_text(encoding="utf-8")
    )["cases"]
    assert len(namespace_cases) == len({case["id"] for case in namespace_cases}) == 20


def test_all_public_url_contexts_have_nonblocking_local_disposition() -> None:
    baseline = json.loads(REGISTER.read_text(encoding="utf-8"))["baseline"]
    url_audit_complete(
        json.loads(URL_AUDIT.read_text(encoding="utf-8")),
        set(baseline["skill_identities"]),
        SKILLS,
    )
