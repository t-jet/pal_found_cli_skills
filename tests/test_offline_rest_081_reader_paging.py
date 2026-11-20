"""Exercise the published Ontology reader loops against hostile local pages."""

import ast
import re
import time
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

import pytest


ROOT = Path(__file__).resolve().parents[1]
GUIDES = ROOT / ".agents/skills/pal-found-dev/references/rest/v2/ontologies"


def published_loop(resource):
    """Extract the actual reader loop and its reported outcome from the guide."""
    guide = (GUIDES / f"{resource}.md").read_text(encoding="utf-8")
    code = re.search(r"## Worked example.*?```python\n(.*?)\n```", guide, re.S).group(1)
    tree = ast.parse(code)
    first = next(i for i, node in enumerate(tree.body)
                 if isinstance(node, ast.Assign)
                 and any(isinstance(target, ast.Name) and target.id == "page_token"
                         for target in node.targets))
    last = next(i for i, node in enumerate(tree.body)
                if isinstance(node, ast.If)
                and isinstance(node.test, ast.UnaryOp)
                and isinstance(node.test.operand, ast.Subscript)
                and getattr(node.test.operand.value, "id", None) == "list_result")
    selected = [tree.body[0], *tree.body[first:last + 1]]
    return compile(ast.Module(body=selected, type_ignores=[]), str(GUIDES / resource), "exec")


class Raw:
    """Track response closure even when decoding fails."""

    def __init__(self, data, token, fail_decode=False):
        self.data = data
        self.token = token
        self.fail_decode = fail_decode
        self.closed = False

    def decode(self):
        """Return a minimal SDK-shaped decoded page."""
        if self.fail_decode:
            raise ValueError("decode failed")
        return SimpleNamespace(
            data=[{"__primaryKey": key} for key in self.data],
            next_page_token=self.token,
        )

    def close(self):
        """Record response closure."""
        self.closed = True


class Reader:
    """Supply finite fake pages and reject unexpected extra requests."""

    def __init__(self, pages):
        self.pages = iter(pages)
        self.responses = []
        self.requests = []

    @property
    def with_raw_response(self):
        """Use the same raw-response path as the published example."""
        return self

    def list(self, **kwargs):
        """Serve OntologyObject.list."""
        return self._next(kwargs)

    def list_linked_objects(self, **kwargs):
        """Serve LinkedObject.list_linked_objects."""
        return self._next(kwargs)

    def _next(self, kwargs):
        self.requests.append(kwargs)
        data, token, *rest = next(self.pages)
        raw = Raw(data, token, bool(rest))
        self.responses.append(raw)
        return raw


def execute(resource, pages, clock=None):
    """Run the published loop with a fake client and optional monotonic clock."""
    reader = Reader(pages)
    client = SimpleNamespace(ontologies=SimpleNamespace(**{resource: reader}))
    namespace = {"client": client, "objects": reader, "links": reader}
    times = patch.object(time, "monotonic", side_effect=clock) if clock else patch.object(
        time, "monotonic", wraps=time.monotonic
    )
    with times:
        exec(published_loop(resource), namespace)
    return namespace["list_result"], reader


@pytest.mark.parametrize("resource", ["LinkedObject", "OntologyObject"])
@pytest.mark.parametrize(
    ("pages", "reason", "count", "keys"),
    [
        ([(range(2), "same"), (range(2), "same")],
         "repeated continuation token", 2, [0, 1, 0, 1]),
        ([(range(1), f"new-{i}") for i in range(20)],
         "page budget exhausted", 20, list(range(1)) * 20),
        ([(range(1001), "next")],
         "item budget exhausted", 1, list(range(1000))),
        ([([], "next"), ([80060], None)],
         None, 2, [80060]),
        ([([80060], None)],
         None, 1, [80060]),
    ],
)
def test_published_reader_bounded_outcome(resource, pages, reason, count, keys, capsys):
    """Partial result stays explicit; terminal and empty-page paths finish."""
    result, reader = execute(resource, pages)
    assert len(reader.requests) == count
    assert all(raw.closed for raw in reader.responses)
    assert result["keys"] == keys
    assert result["complete"] is (reason is None)
    assert result["incomplete_reason"] == reason
    assert ("Partial" in capsys.readouterr().out) is (reason is not None)
    assert all(1 <= request["request_timeout"] <= 30 for request in reader.requests)


@pytest.mark.parametrize("resource", ["LinkedObject", "OntologyObject"])
def test_published_reader_deadline_prevents_request(resource, capsys):
    """No request starts when the remaining budget is below one second."""
    result, reader = execute(resource, [], clock=[0, 29.5])
    assert reader.requests == []
    assert result["complete"] is False
    assert result["incomplete_reason"] == "time budget exhausted before next request"
    assert "Partial" in capsys.readouterr().out


@pytest.mark.parametrize("resource", ["LinkedObject", "OntologyObject"])
def test_published_reader_keeps_partial_page_when_time_runs_out(resource):
    """A response received at the deadline remains visible without another request."""
    result, reader = execute(resource, [([7], "next")], clock=[0, 0, 30])
    assert len(reader.requests) == 1
    assert reader.responses[0].closed
    assert result == {
        "keys": [7],
        "complete": False,
        "incomplete_reason": "time budget exhausted before next request",
        "next_page_token": "next",
    }


@pytest.mark.parametrize("resource", ["LinkedObject", "OntologyObject"])
def test_published_reader_closes_failed_decode(resource):
    """The raw response is closed when SDK decoding raises."""
    reader = Reader([([1], None, "fail")])
    client = SimpleNamespace(ontologies=SimpleNamespace(**{resource: reader}))
    with pytest.raises(ValueError, match="decode failed"):
        exec(published_loop(resource), {"client": client, "objects": reader, "links": reader})
    assert len(reader.responses) == 1
    assert reader.responses[0].closed
