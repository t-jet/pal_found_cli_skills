"""Execute source-blind namespace examples with public sockets denied."""

from __future__ import annotations

import contextlib
import io
import json
import runpy
import socket
import traceback
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SKILL = ROOT / "pal_found_cli_skills/.agents/skills/pal-found-dev"
OUT = Path(__file__).resolve().parent

CASES = {
    "v1.datasets": "074/v1/datasets/Dataset/get.py",
    "v1.ontologies": "077/v1/ontologies/Attachment/get.py",
    "v2.admin": "071/v2/admin/Group/get.py",
    "v2.aip_agents": "087/v2/aip_agents/AgentVersion/get.py",
    "v2.audit": "073/v2/audit/LogFile/list.py",
    "v2.checkpoints": "075/v2/checkpoints/Record/get.py",
    "v2.connectivity": "089/v2/connectivity/Connection/invoke_get.py",
    "v2.data_health": "075/v2/data_health/Check/get.py",
    "v2.datasets": "074/v2/datasets/Dataset/get.py",
    "v2.filesystem": "073/v2/filesystem/Folder/get.py",
    "v2.functions": "085/v2/functions/ValueType/invoke_get.py",
    "v2.language_models": "087/v2/language_models/OpenAiModel/embeddings.py",
    "v2.media_sets": "091/v2/media_sets/MediaSet/invoke_get.py",
    "v2.models": "087/v2/models/LiveDeployment/get.py",
    "v2.ontologies": "083/v2/ontologies/Attachment/invoke_get.py",
    "v2.orchestration": "075/v2/orchestration/Build/get.py",
    "v2.sql_queries": "089/v2/sql_queries/SqlQuery/invoke_cancel.py",
    "v2.streams": "089/v2/streams/Stream/invoke_get_records.py",
    "v2.third_party_applications": "073/v2/third_party_applications/Website/get.py",
    "v2.widgets": "091/v2/widgets/Repository/invoke_get.py",
}


def denied(*_args: object, **_kwargs: object) -> None:
    raise RuntimeError("PUBLIC_NETWORK_DENIED")


def main() -> None:
    socket.socket.connect = denied  # type: ignore[method-assign]
    socket.socket.connect_ex = denied  # type: ignore[method-assign]
    socket.create_connection = denied  # type: ignore[assignment]
    socket.getaddrinfo = denied  # type: ignore[assignment]
    probe = "unexpected success"
    try:
        socket.getaddrinfo("example.com", 443)
    except RuntimeError as exc:
        probe = str(exc)

    outcomes = []
    for namespace, relative in CASES.items():
        path = SKILL / "examples/rest" / relative
        output = io.StringIO()
        error = None
        try:
            with contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
                runpy.run_path(str(path), run_name="__main__")
        except Exception:
            error = traceback.format_exc()
        outcomes.append({
            "namespace": namespace,
            "example": path.relative_to(SKILL).as_posix(),
            "output": output.getvalue().strip(),
            "error": error,
            "passed": error is None,
        })
    payload = {"network_probe": probe, "outcomes": outcomes}
    (OUT / "case_results.json").write_text(json.dumps(payload, indent=2), encoding="utf-8")
    print(f"network={probe}; passed={sum(x['passed'] for x in outcomes)}/{len(outcomes)}")
    for x in outcomes:
        print(f"{x['namespace']}: {'PASS' if x['passed'] else 'FAIL'} {x['output']}")
        if x["error"]:
            print(x["error"])


if __name__ == "__main__":
    main()
