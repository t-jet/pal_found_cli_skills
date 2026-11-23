"""Regress the published T01/T02 navigation and environment contracts.

Expected destinations follow the approved topic ownership and journey map.
These checks execute local navigation, not a simulated reader's reasoning or
live Foundry work. Independent semantic journeys remain separate QA work.
"""

from pathlib import Path
import re
import runpy

import pytest

from test_offline_topic_acceptance import local_link, markdown_prose


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / ".agents/skills/pal-found-dev"
ENTRY = SKILL / "SKILL.md"
PATHS = SKILL / "references/development-paths.md"
NETWORK = runpy.run_path(str(ROOT / "tests/fixtures/offline/topic-acceptance/runner.py"))
LINK = re.compile(r"\[([^]]+)\]\(([^)]+)\)")

# Route selectors identify published table rows. Expected paths and terminal
# contracts come from SA-DES-014's ownership/journey map, not generated ledgers.
ROUTES = [
    ("J01", "Write Python, SQL", "references/pipelines.md", ("repositories.md",)),
    ("J02", "Write Python, SQL", "references/pipelines.md", ("transactions.md",)),
    ("J03", "SQL syntax, declared datasets", "references/pipelines/sql.md", ()),
    ("J04", "Ontology types, object sets", "references/ontology-compute.md", ("modeling.md",)),
    ("J05", "Ontology types, object sets", "references/ontology-compute.md", ("actions.md", "functions.md")),
    ("J06", "Run a custom container", "references/ontology-compute.md", ("lifecycle.md", "execution.md", "integration.md")),
    ("J07", "Build a custom web or Python app", "references/applications-branching-security.md", ("osdk.md", "react.md")),
    ("J08", "Embed a React component", "references/applications-branching-security.md", ("lifecycle.md", "integration.md")),
    ("J09", "OSDK/React, Workshop widgets", "references/applications-branching-security.md", ("contexts.md",)),
    ("J10", "Schedules, lineage, observability", "references/operations.md", ("lineage.md",)),
    ("J11", "Integrate an external client", "references/rest-api.md", ("catalog.md",)),
    ("J12", "Integrate an external client", "references/rest-api.md", ("client-behavior.md",)),
    ("J13", "Navigate projects/folders", "references/rest-api.md", ("catalog.md",)),
    ("J14", "Develop an AIP integration", "references/rest-api.md", ("catalog.md",)),
]


def table_rows(text):
    """Read actual Markdown cells; ignore separator rows and fenced code."""
    return [
        [cell.strip() for cell in line.strip().strip("|").split("|")]
        for line in markdown_prose(text).splitlines()
        if line.startswith("|") and not re.fullmatch(r"[| :\-]+", line)
    ]


def route_destination(entry_text, selector, expected):
    """Resolve one published route within its owner, including its anchor."""
    rows = [row for row in table_rows(entry_text) if row[0].startswith(selector)]
    assert len(rows) == 1, f"Missing or ambiguous route: {selector}"
    links = LINK.findall(rows[0][1])
    assert len(links) == 1, f"Expected one local route for {selector}"
    target = local_link(ENTRY, links[0][1], SKILL)
    assert target == (SKILL / expected).resolve(), f"Wrong capability route: {selector}"
    return target


def linked_destinations(page):
    """Resolve the finite direct links on a selected overview."""
    return {
        target
        for _, link in LINK.findall(markdown_prose(page.read_text(encoding="utf-8")))
        if (target := local_link(page, link, SKILL)) is not None
    }


@pytest.mark.parametrize("journey,selector,expected,leaves", ROUTES, ids=[row[0] for row in ROUTES])
def test_journey_entry_routes_reach_owned_guides(journey, selector, expected, leaves):
    with NETWORK["denied_public_network"]():
        target = route_destination(ENTRY.read_text(encoding="utf-8"), selector, expected)
        destinations = linked_destinations(target)
    for name in leaves:
        assert any(path.name == name for path in destinations), (journey, name)


def test_governance_and_aip_routes_keep_distinct_namespace_contracts():
    """Both use REST; their supported resources are not interchangeable."""
    with NETWORK["denied_public_network"]():
        catalog = SKILL / "references/rest/catalog.md"
        services = linked_destinations(catalog)
        for service, resource in (("filesystem", "Folder/get.md"), ("aip_agents", "Agent/get.md")):
            index = SKILL / f"references/rest/v2/{service}/index.md"
            assert index.resolve() in services
            contract = SKILL / f"references/rest/contracts/v2/{service}/{resource}"
            assert contract.resolve() in linked_destinations(index)


ENVIRONMENTS = [
    ("Local fixture authoring/testing", False, ("Source", "runtime", "bindings")),
    ("Local preview against Foundry", True, ("tooling", "credentials")),
    ("Foundry-hosted workspace", True, ("Code Workspaces", "resource access", "runtime")),
    ("Live SDK/application operation", True, ("SDK", "host/client", "identity")),
]


def environment_contract(text, name, enrollment_required, artifacts):
    """Return a concrete prepared-artifact/access row, not an execution result."""
    rows = [row for row in table_rows(text) if row[0] == name]
    assert len(rows) == 1, f"Missing environment: {name}"
    _, prepared, boundary = rows[0]
    for artifact in artifacts:
        assert artifact.lower() in prepared.lower(), (name, artifact)
    if enrollment_required:
        if name == "Local preview against Foundry":
            assert all(term in boundary for term in (
                "Administrator-enabled", "download permissions on every input", "local memory",
            )), f"Live step incorrectly described as disconnected: {name}"
            assert "deployment need authorized enrollment access" in " ".join(text.split())
        else:
            assert "needs" in boundary.lower() and "enrollment" in boundary.lower(), (
                f"Live step incorrectly described as disconnected: {name}"
            )
    else:
        assert "without public or enrollment access" in boundary
        assert "fixture behavior" in boundary
    return prepared, boundary


@pytest.mark.parametrize("name,enrollment_required,artifacts", ENVIRONMENTS)
def test_prepared_environments_preserve_connectivity_boundary(name, enrollment_required, artifacts):
    with NETWORK["denied_public_network"]():
        prepared, boundary = environment_contract(
            PATHS.read_text(encoding="utf-8"), name, enrollment_required, artifacts
        )
    assert prepared and boundary


def test_t01_worked_example_keeps_four_different_outcomes():
    """A fixture plan cannot conflate a dataset build, edit, or API effect."""
    rows = table_rows(PATHS.read_text(encoding="utf-8"))
    for task, tool, evidence in (
        ("Join orders/customers", "Python Code Repository", ("expectation", "release", "output build")),
        ("Display an Order", "OSDK React", ("bindings", "OAuth", "validation", "verified edit")),
        ("Discover project/folder", "REST SDK Filesystem", ("traversal", "request", "effect check")),
        ("Add agent assistance", "REST AIP", ("version", "execution result", "finite")),
    ):
        matches = [row for row in rows if row[0].startswith(task)]
        assert len(matches) == 1, task
        assert tool in matches[0][1]
        for requirement in evidence:
            assert requirement in matches[0][2], (task, requirement)


@pytest.mark.parametrize("mutation", ("wrong-guide", "missing-guide", "folder-escape"))
def test_actual_entry_route_mutations_are_rejected(mutation):
    entry = ENTRY.read_text(encoding="utf-8")
    bad = {
        "wrong-guide": "references/pipelines.md",
        "missing-guide": "references/missing-production-guide.md",
        "folder-escape": "../../outside-skill.md",
    }[mutation]
    changed = entry.replace("references/operations.md", bad)
    assert changed != entry
    with NETWORK["denied_public_network"](), pytest.raises(AssertionError):
        route_destination(changed, "Schedules, lineage, observability", "references/operations.md")


def test_live_preview_cannot_be_reclassified_as_disconnected():
    text = PATHS.read_text(encoding="utf-8")
    rows = table_rows(text)
    preview = next(row for row in rows if row[0] == "Local preview against Foundry")
    changed = text.replace(preview[2], "Can run without public or enrollment access; fixture behavior only.")
    assert changed != text
    with pytest.raises(AssertionError, match="incorrectly described as disconnected"):
        environment_contract(changed, "Local preview against Foundry", True, ("tooling", "credentials"))


def test_missing_prepared_runtime_cannot_pass_environment_contract():
    text = PATHS.read_text(encoding="utf-8")
    changed = text.replace("matching runtime/dependencies", "unspecified dependencies")
    assert changed != text
    with pytest.raises(AssertionError):
        environment_contract(changed, "Local fixture authoring/testing", False, ("runtime",))
