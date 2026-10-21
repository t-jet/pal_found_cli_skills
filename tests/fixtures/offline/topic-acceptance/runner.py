"""Stage one skill for fixture execution with public network calls denied.

This is a cooperative Python fixture boundary. It does not isolate a live
Foundry tenant or replace independent reader review.
"""

from contextlib import ExitStack, contextmanager
import asyncio
import hashlib
import os
from pathlib import Path
import shutil
import socket
import subprocess
from unittest.mock import patch
from uuid import uuid4


def file_hashes(skill: Path, paths: list[str]) -> dict[str, str]:
    """Hash required local files without allowing a path outside the skill."""
    result = {}
    for relative in paths:
        target = (skill / relative).resolve()
        if not target.is_relative_to(skill.resolve()) or not target.is_file():
            raise AssertionError(f"Missing or external candidate file: {relative}")
        result[relative] = hashlib.sha256(target.read_bytes()).hexdigest()
    return result


def verify_accepted_candidate(skill: Path, accepted: dict, candidate_sha: str) -> None:
    """Invalidate REST acceptance when the commit or required content differs."""
    if accepted["candidate_sha"] != candidate_sha:
        raise AssertionError("Stale accepted REST revision")
    expected = accepted["required_file_hashes"]
    actual = file_hashes(skill, list(expected))
    if expected != actual:
        raise AssertionError("Changed accepted REST/shared facts require affected checks again")


def stage_skill(skill: Path, temporary_root: Path) -> Path:
    """Copy only the owning skill to an approved temporary root."""
    temporary_root = temporary_root.resolve()
    if temporary_root.parts[-2:] != (".ept", "tmp"):
        raise AssertionError("Stage under parent .ept/tmp")
    if skill.name != "pal-found-dev" or not (skill / "SKILL.md").is_file():
        raise AssertionError("Expected a development skill source")
    destination = temporary_root / f"topic-isolation-{uuid4().hex}" / skill.name
    shutil.copytree(skill, destination)
    return destination


@contextmanager
def denied_public_network():
    """Fail DNS, sockets and subprocess escape during a Python fixture run."""
    def deny(*_args, **_kwargs):
        raise AssertionError("Public network denied in offline fixture")

    import httpx
    import requests

    with ExitStack() as stack:
        for owner, name in (
            (socket, "getaddrinfo"), (socket, "create_connection"),
            (socket.socket, "connect"), (socket.socket, "connect_ex"),
            (socket.socket, "send"), (socket.socket, "sendall"),
            (socket.socket, "sendto"), (subprocess, "Popen"),
            (os, "system"), (os, "popen"),
            (asyncio, "create_subprocess_exec"), (asyncio, "create_subprocess_shell"),
            (httpx.HTTPTransport, "handle_request"),
            (httpx.AsyncHTTPTransport, "handle_async_request"),
            (requests.adapters.HTTPAdapter, "send"),
        ):
            stack.enter_context(patch.object(owner, name, deny))
        yield
