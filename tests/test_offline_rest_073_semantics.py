"""REST-073 examples must verify identities, absolute paths, and deployed versions."""

import runpy
from pathlib import Path

import pytest


BASE = Path(__file__).parents[1] / ".agents/skills/pal-found-dev/examples/rest/073/v2"
EXAMPLES = (
    "filesystem/Folder/get_batch.py",
    "filesystem/Resource/get_batch.py",
    "filesystem/Resource/get_by_path.py",
    "filesystem/Resource/get_by_path_batch.py",
    "third_party_applications/Website/deploy.py",
)


@pytest.mark.parametrize("relative_path", EXAMPLES)
def test_rest073_semantic_examples_pass(relative_path):
    runpy.run_path(str(BASE / relative_path))["verify"]()


@pytest.mark.parametrize("resource", ("Folder", "Resource"))
@pytest.mark.parametrize("fault", ("missing", "wrong_rid"))
def test_batch_examples_reject_missing_or_mismatched_requested_identity(resource, fault):
    example = runpy.run_path(str(BASE / f"filesystem/{resource}/get_batch.py"))
    data = example["SUCCESS"]["data"]
    if fault == "missing":
        data.clear()
        message = "Requested RID missing from batch response"
    else:
        next(iter(data.values()))["rid"] = "ri.synthetic.main.resource.00000000-0000-0000-0000-000000000099"
        message = "Returned RID differs from request"

    with pytest.raises(AssertionError, match=message):
        example["verify"]()


@pytest.mark.parametrize("operation", ("get_by_path", "get_by_path_batch"))
def test_path_examples_use_full_paths_and_reject_different_resource_path(operation):
    example = runpy.run_path(str(BASE / f"filesystem/Resource/{operation}.py"))
    if operation == "get_by_path":
        requested = example["EXPECTED_QUERY"]["path"]
        returned = example["SUCCESS"]
        message = "Returned path differs from request"
    else:
        requested = example["EXPECTED_BODY"][0]["path"]
        returned = example["SUCCESS"]["data"][0]
        message = "Returned paths differ from request"
    assert requested.startswith("/")
    assert requested.split("/")[1:] == ["synthetic-space", "synthetic-project", "synthetic-value"]
    returned["path"] = "/synthetic-space/synthetic-project/other-resource"

    with pytest.raises(AssertionError, match=message):
        example["verify"]()


@pytest.mark.parametrize("fault", ("missing", "wrong_version"))
def test_website_deploy_example_rejects_missing_or_wrong_deployed_version(fault):
    example = runpy.run_path(str(BASE / "third_party_applications/Website/deploy.py"))
    if fault == "missing":
        example["SUCCESS"].pop("deployedVersion")
    else:
        example["SUCCESS"]["deployedVersion"] = "other-version"

    with pytest.raises(AssertionError, match="Deployed version differs from request"):
        example["verify"]()
