"""Synthetic fixture only; no SDK worker, deployment, grants or Foundry execution."""

import json
from types import SimpleNamespace
from unittest.mock import patch

from bindings import load_bindings
from logic import score
from pipeline import process_once


def fake_read(path, encoding="utf-8"):
    if str(path) == "fixture-token":
        return "synthetic-not-a-token"
    return json.dumps({"incoming": {"rid": "fixture-input", "branch": None},
                       "outgoing": {"rid": "fixture-output", "branch": "demo"}})


assert score({}, {"amount": 12, "factor": 3}) == 36
assert score({}, {"amount": 0, "factor": 3}) == 0
for payload in ({"amount": -1, "factor": 3}, {"amount": True, "factor": 3}):
    try:
        score({}, payload)
    except ValueError:
        pass
    else:
        raise AssertionError("invalid input accepted")
with patch("pathlib.Path.read_text", fake_read):
    token, bindings = load_bindings("fixture-token", "fixture-map")
    assert token == "synthetic-not-a-token"
    assert bindings["incoming"]["branch"] == "master"
    assert bindings["outgoing"]["branch"] == "demo"
    try:
        load_bindings("fixture-token", "fixture-map", ("missing",))
    except ValueError:
        pass
    else:
        raise AssertionError("missing binding accepted")

class SyntheticSession:
    def __init__(self):
        self.writes = []

    def get(self, url, **kwargs):
        assert url.endswith("/fixture-input/branches/master/records")
        assert kwargs["timeout"] == 5 and kwargs["verify"] == "fixture-ca"
        return SimpleNamespace(raise_for_status=lambda: None, close=lambda: None,
                               iter_content=lambda chunk_size: [json.dumps(
                                   [{"value": {"x": 4}}, {"value": {"x": -2}}]).encode()])

    def post(self, url, **kwargs):
        assert url.endswith("/fixture-output/branches/demo/jsonRecord")
        assert kwargs["timeout"] == 5 and kwargs["verify"] == "fixture-ca"
        self.writes.append(kwargs["json"])
        return SimpleNamespace(raise_for_status=lambda: None, close=lambda: None)


session = SyntheticSession()
assert process_once(session, "synthetic.invalid", token, bindings, "fixture-ca", timeout=5) == 2
assert session.writes == [{"twice_x": 8}, {"twice_x": -4}]
for budgets in ({"max_records": 1}, {"max_bytes": 4}):
    oversized = SyntheticSession()
    try:
        process_once(oversized, "synthetic.invalid", token, bindings,
                     "fixture-ca", timeout=5, **budgets)
    except ValueError:
        assert oversized.writes == []
    else:
        raise AssertionError("oversized input accepted")

with patch("pathlib.Path.read_text", lambda path, encoding: "token" if str(path) == "token" else "[]"):
    try:
        load_bindings("token", "map")
    except ValueError as error:
        assert "must be an object" in str(error)
    else:
        raise AssertionError("list alias map accepted")

class PartialTimeoutSession(SyntheticSession):
    def post(self, url, **kwargs):
        if self.writes:
            raise TimeoutError("synthetic second-write timeout; outcome unknown")
        return super().post(url, **kwargs)

partial = PartialTimeoutSession()
try:
    process_once(partial, "synthetic.invalid", token, bindings, "fixture-ca", timeout=5)
except TimeoutError:
    assert partial.writes == [{"twice_x": 8}]
else:
    raise AssertionError("partial-write timeout hidden")

with patch("pipeline.time.monotonic", side_effect=[0, 61]):
    exhausted = SyntheticSession()
    try:
        process_once(exhausted, "synthetic.invalid", token, bindings, "fixture-ca", timeout=5)
    except TimeoutError:
        assert exhausted.writes == []
    else:
        raise AssertionError("exhausted elapsed budget accepted")
print("Synthetic compute fixture passed; no Foundry deployment tested.")
