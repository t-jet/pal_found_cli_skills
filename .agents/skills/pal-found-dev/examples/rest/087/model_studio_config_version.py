"""SDK1.101 integer-path regression and faithful bounded direct REST read.

This public HTTP alternative retains SDK response and named-error types. It
does not patch the SDK, alter its frozen version or retry a failed mutation.
"""

import json
import sys
from pathlib import Path
from urllib.parse import quote

import httpx
from pydantic import TypeAdapter
from foundry_sdk import PalantirRPCException
from foundry_sdk.v2.models.models import ModelStudioConfigVersion, ModelStudioRid
from foundry_sdk.v2.models.errors import ModelStudioConfigVersionNotFound, ModelStudioNotFound
from foundry_sdk.v2.models.model_studio_config_version import ModelStudioConfigVersionClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "common"))
from mock_transport import mock_resource

STUDIO = "ri.synthetic.main.resource.00000000-0000-0000-0000-000000000001"
TRAINER = "ri.synthetic.main.resource.00000000-0000-0000-0000-000000000002"


def get_config_version(http, *, hostname, token, studio_rid, version, preview=None,
                       timeout=30, max_bytes=1_000_000, max_chunks=1000):
    """Read one saved configuration through its frozen public REST contract.

    Supply an authorized bare hostname/token and actual studio/version. The
    caller owns the HTTP client's lifecycle. Limits are application budgets.
    """
    studio_rid = TypeAdapter(ModelStudioRid).validate_python(studio_rid)
    if type(version) is not int:
        raise TypeError("version must be an integer")
    if preview is not None and type(preview) is not bool:
        raise TypeError("preview must be a boolean or None")
    if timeout <= 0 or max_bytes <= 0 or max_chunks <= 0:
        raise ValueError("timeout and response budgets must be positive")
    url = (f"https://{hostname}/api/v2/models/modelStudios/{quote(studio_rid, safe='')}"
           f"/configVersions/{quote(str(version), safe='')}")
    params = {} if preview is None else {"preview": "true" if preview else "false"}
    with http.stream("GET", url, params=params,
                     headers={"Authorization": f"Bearer {token}", "Accept": "application/json"},
                     timeout=timeout) as response:
        chunks, size = [], 0
        for count, chunk in enumerate(response.iter_bytes(), 1):
            size += len(chunk)
            if size > max_bytes or count > max_chunks:
                raise RuntimeError("Configuration response budget exhausted")
            chunks.append(chunk)
        body = b"".join(chunks)
        if response.is_success:
            return ModelStudioConfigVersion.model_validate_json(body)
        try:
            error = json.loads(body)
        except (ValueError, UnicodeDecodeError):
            response.raise_for_status()
            raise
        if (not isinstance(error, dict)
                or not all(isinstance(error.get(key), str) for key in
                           ("errorName", "errorCode", "errorInstanceId"))
                or not isinstance(error.get("parameters"), dict)):
            response.raise_for_status()
        named = {"ModelStudioConfigVersionNotFound": ModelStudioConfigVersionNotFound,
                 "ModelStudioNotFound": ModelStudioNotFound}.get(error["errorName"])
        if named is not None:
            parameters = TypeAdapter(named.__annotations__["parameters"]).validate_python(error["parameters"])
            raise named(name=error["errorName"], parameters=parameters,
                        error_instance_id=error["errorInstanceId"])
        raise PalantirRPCException(error)


def payload():
    return {"name": "Governance trainer configuration", "version": 1,
            "trainerId": TRAINER, "trainer": {"trainerId": TRAINER, "version": "1.0"},
            "workerConfig": {"inputs": {}, "outputs": {}},
            "resources": {"memory": "1Gi", "cpu": "1"},
            "createdBy": "00000000-0000-0000-0000-000000000003",
            "createdTime": "2026-10-07T00:00:00Z"}


def verify():
    touched = []
    def unexpected_transport(request):
        touched.append(request)
        raise AssertionError("Native SDK integer path should fail before HTTP")
    with mock_resource(ModelStudioConfigVersionClient, unexpected_transport) as sdk:
        try:
            sdk.get(STUDIO, 1, preview=True, request_timeout=30)
        except Exception as error:
            assert "quote_from_bytes() expected bytes" in str(error)
        else:
            raise AssertionError("Frozen SDK regression unexpectedly disappeared")
    assert not touched

    def success(request):
        assert request.method == "GET"
        assert request.url.path == f"/api/v2/models/modelStudios/{STUDIO}/configVersions/1"
        assert request.url.params["preview"] == "true"
        assert request.headers["Accept"] == "application/json"
        assert request.headers["Authorization"] == "Bearer offline-fixture-token"
        return httpx.Response(200, json=payload())
    options = {"hostname": "offline.example.invalid", "token": "offline-fixture-token",
               "studio_rid": STUDIO, "version": 1, "preview": True}
    with httpx.Client(transport=httpx.MockTransport(success)) as http:
        result = get_config_version(http, **options)
        assert result.version == 1 and result.trainer.trainer_id == TRAINER
        try:
            get_config_version(http, **options, max_bytes=10)
        except RuntimeError as error:
            assert str(error) == "Configuration response budget exhausted"
        else:
            raise AssertionError("Expected response budget failure")

    for name, parameters, kind in [
        ("ModelStudioConfigVersionNotFound", {"studioRid": STUDIO, "configVersion": 1}, ModelStudioConfigVersionNotFound),
        ("ModelStudioNotFound", {"studioRid": STUDIO}, ModelStudioNotFound),
        ("UnclassifiedServiceFailure", {}, PalantirRPCException),
    ]:
        def missing(request):
            return httpx.Response(404, json={"errorName": name, "errorCode": "NOT_FOUND",
                "errorInstanceId": "00000000-0000-0000-0000-000000000004", "parameters": parameters})
        with httpx.Client(transport=httpx.MockTransport(missing)) as http:
            try:
                get_config_version(http, **options)
            except kind as error:
                assert error.name == name and error.parameters == parameters
            else:
                raise AssertionError(f"Missing {name} handling")


if __name__ == "__main__":
    verify()
    print("Native SDK integer-path regression and bounded direct REST/model/error fixtures passed")
