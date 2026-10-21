"""Run cooperative local fixtures with public network and child calls denied."""

from __future__ import annotations

import contextlib
import io
import json
import os
from pathlib import Path
import runpy
import socket
import subprocess
import multiprocessing
import sys
import traceback


ROOT = Path(__file__).resolve().parent / "pal-found-dev"
CASES = {
    "J1_J2": "examples/pipelines/fixture_run.py",
    "J3_SQL": "examples/sql/verify_fixture.py",
    "J3_WORKSPACE": "examples/workspaces/verify_fixture.py",
    "J4_MODEL": "examples/ontology/model_fixture.py",
    "J5_ACTION": "examples/ontology/action_fixture.py",
    "J6_COMPUTE": "examples/compute/verify_fixture.py",
    "J9_J10_CONTEXT": ROOT.parent.parent / "reader-j9-j10-7767009254d84ed9bdebb27aa85752b3/context_check.py",
}


def deny(*_args: object, **_kwargs: object) -> None:
    raise RuntimeError("PUBLIC_NETWORK_DENIED")


def main() -> None:
    socket.socket.connect = deny  # type: ignore[method-assign]
    socket.socket.connect_ex = deny  # type: ignore[method-assign]
    socket.socket.send = deny  # type: ignore[method-assign]
    socket.socket.sendall = deny  # type: ignore[method-assign]
    socket.socket.sendto = deny  # type: ignore[method-assign]
    if hasattr(socket.socket, "sendmsg"):
        socket.socket.sendmsg = deny  # type: ignore[method-assign]
    socket.create_connection = deny  # type: ignore[assignment]
    socket.getaddrinfo = deny  # type: ignore[assignment]
    socket.gethostbyname = deny  # type: ignore[assignment]
    subprocess.Popen.__init__ = deny  # type: ignore[method-assign]
    os.system = deny  # type: ignore[assignment]
    multiprocessing.Process.start = deny  # type: ignore[method-assign]

    def probe(label: str, call: object) -> None:
        try:
            call()  # type: ignore[operator]
        except RuntimeError as exc:
            assert str(exc) == "PUBLIC_NETWORK_DENIED", (label, str(exc))
            print(f"{label}: PUBLIC_NETWORK_DENIED")
        else:
            raise AssertionError(f"{label} denial probe failed")

    probe("dns", lambda: socket.getaddrinfo("example.com", 443))
    probe("direct_ip", lambda: socket.socket().connect(("1.1.1.1", 443)))
    probe("udp", lambda: socket.socket(type=socket.SOCK_DGRAM).sendto(b"x", ("1.1.1.1", 53)))
    probe("subprocess", lambda: subprocess.Popen([sys.executable, "-V"]))
    probe("os_system", lambda: os.system("exit 0"))
    probe("multiprocessing", lambda: multiprocessing.Process(target=lambda: None).start())
    os.chdir(ROOT)
    outcomes = []
    for case, relative in CASES.items():
        output = io.StringIO()
        error = None
        script = Path(relative)
        if not script.is_absolute():
            script = ROOT / script
        sys.path.insert(0, str(script.parent))
        try:
            with contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
                runpy.run_path(str(script), run_name="__main__")
        except Exception:
            error = traceback.format_exc()
        finally:
            sys.path.pop(0)
        outcomes.append({"case": case, "path": str(relative), "output": output.getvalue().strip(), "error": error})
    result = {"network_probe": "PUBLIC_NETWORK_DENIED", "guard_scope": "cooperative Python socket/DNS and child-process paths", "outcomes": outcomes}
    (ROOT.parent / "python_results.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    for row in outcomes:
        print(f"{row['case']}: {'FAIL' if row['error'] else 'PASS'} {row['output']}")
        if row["error"]:
            print(row["error"])
    if any(row["error"] for row in outcomes):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
