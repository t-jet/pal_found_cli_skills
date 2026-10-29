"""The pinned VersionId example must verify the requested UUID."""

import runpy
from pathlib import Path

import pytest


EXAMPLE = (
    Path(__file__).parents[1]
    / ".agents/skills/pal-found-dev/examples/rest/085/v2/functions/VersionId/invoke_get.py"
)


def test_version_id_example_accepts_matching_identifiers():
    runpy.run_path(str(EXAMPLE))["verify"]()


def test_version_id_example_rejects_wrong_uuid_with_matching_semantic_version():
    example = runpy.run_path(str(EXAMPLE))
    semantic_version = example["SUCCESS"]["version"]
    example["SUCCESS"]["versionId"] = "00000000-0000-0000-0000-000000000002"
    assert example["SUCCESS"]["version"] == semantic_version

    with pytest.raises(AssertionError, match="Returned version ID differs from request"):
        example["verify"]()
