"""One bounded stream-processing pass. Explicit enrollment execution only."""

import json
import os
import time
from urllib.parse import quote

import requests

from bindings import load_bindings


def stream_url(hostname, binding, suffix):
    rid = quote(binding["rid"], safe="")
    branch = quote(binding["branch"], safe="")
    return f"https://{hostname}/stream-proxy/api/streams/{rid}/branches/{branch}/{suffix}"


def process_once(session, hostname, token, aliases, ca_path, timeout=30,
                 max_bytes=65536, max_records=100, max_seconds=60):
    if min(timeout, max_bytes, max_records, max_seconds) <= 0:
        raise ValueError("processing budgets must be positive")
    deadline = time.monotonic() + max_seconds

    def remaining():
        seconds = deadline - time.monotonic()
        if seconds <= 0:
            raise TimeoutError("processing deadline exhausted; inspect partial output")
        return min(timeout, seconds)
    headers = {"Authorization": f"Bearer {token}"}
    response = session.get(stream_url(hostname, aliases["incoming"], "records"),
                           headers=headers, verify=ca_path, timeout=remaining(), stream=True)
    try:
        response.raise_for_status()
        payload = bytearray()
        for chunk in response.iter_content(chunk_size=8192):
            remaining()
            if len(payload) + len(chunk) > max_bytes:
                raise ValueError("response byte budget exceeded; no writes attempted")
            payload.extend(chunk)
        records = json.loads(payload)
    finally:
        response.close()
    if not isinstance(records, list):
        raise ValueError("expected stream records array")
    if len(records) > max_records:
        raise ValueError("record budget exceeded; no writes attempted")
    transformed = []
    for record in records:
        value = record["value"]["x"]
        if type(value) is not int:
            raise ValueError("record.value.x must be an integer")
        transformed.append({"twice_x": value * 2})
    completed = 0
    for record in transformed:
        response = session.post(stream_url(hostname, aliases["outgoing"], "jsonRecord"),
                                json=record, headers=headers, verify=ca_path, timeout=remaining())
        try:
            response.raise_for_status()
        finally:
            response.close()
        completed += 1
    return completed


if __name__ == "__main__":
    token, aliases = load_bindings(os.environ["BUILD2_TOKEN"], os.environ["RESOURCE_ALIAS_MAP"])
    with requests.Session() as session:
        count = process_once(session, os.environ["FOUNDRY_URL"], token, aliases,
                             os.environ["DEFAULT_CA_PATH"], float(os.environ.get("REQUEST_TIMEOUT", "30")))
    print(f"Stream writes acknowledged: {count}; verify pipeline/output state separately.")
