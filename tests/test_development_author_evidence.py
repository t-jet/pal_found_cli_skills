"""Keep authored topic evidence tied to the exact local guide revision."""

import hashlib
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
GUIDE = ROOT / ".agents/skills/pal-found-dev"
LEDGER = ROOT / "maintainer/development-author-source-evidence.json"
REGISTER = ROOT / "tests/fixtures/offline/topic-register.json"
REQUIRED_SECTIONS = {
    "Concept and lifecycle",
    "Prerequisites",
    "Procedure",
    "Worked example",
    "Expected result and checks",
    "Failures and recovery",
}
SOURCE_URL = re.compile(r"https://www\.palantir\.com/docs/foundry/[^)\s,]+")


def test_authored_topics_have_current_guides_and_source_attribution() -> None:
    rows = json.loads(LEDGER.read_text(encoding="utf-8"))["topics"]
    registered = {
        row["id"]: row
        for row in json.loads(REGISTER.read_text(encoding="utf-8"))["topics"]
    }
    assert {row["topic"] for row in rows} == {f"T{n:02}" for n in range(1, 37)}
    for row in rows:
        topic = row["topic"]
        assert row["authored"], f"{topic}: authoring evidence pending"
        assert row["customer_topic"] == registered[topic]["title"], topic
        registered_path, registered_anchor = registered[topic]["root"].split("#", 1)
        assert row["registered_path"] == registered_path, topic
        heading_anchor = re.sub(r"[^a-z0-9 -]", "", row["registered_heading"].lower())
        assert heading_anchor.replace(" ", "-") == registered_anchor, topic
        page = (GUIDE / row["registered_path"]).resolve()
        assert page.is_relative_to(GUIDE.resolve()) and page.is_file(), topic
        content = page.read_text(encoding="utf-8")
        headings = {
            line.lstrip("# ").strip()
            for line in content.splitlines()
            if line.startswith("#")
        }
        assert row["registered_heading"] in headings, topic
        assert REQUIRED_SECTIONS <= headings, topic
        assert row["heading_matches"], topic
        assert row["sha256"] == hashlib.sha256(page.read_bytes()).hexdigest(), topic
        assert row["lines"] == len(content.splitlines()), topic
        assert row["source_urls"] == sorted(set(SOURCE_URL.findall(content))), topic
