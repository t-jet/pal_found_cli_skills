"""Execute distributed examples in a staged skill with public sockets denied.

This verifies example transport handling. Human reader decisions and source
fidelity are reviewed separately; successful execution is not full acceptance.
"""

from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import runpy
import shutil
import sys
from uuid import uuid4


def run_staged_examples(skill_source: Path, temporary_root: Path, examples: dict,
                        network_denial) -> dict:
    temporary_root = temporary_root.resolve()
    assert temporary_root.parts[-2:] == (".ept", "tmp"), "Use the approved temporary directory"
    staging = temporary_root / ("rest-isolation-" + uuid4().hex) / skill_source.name
    assert staging.resolve().is_relative_to(temporary_root)
    shutil.copytree(skill_source, staging)
    results = {}
    original_path = sys.path[:]
    local_names = {"bounded_pages", "mock_transport", "response_modes"}
    previous_modules = {name: sys.modules.pop(name) for name in local_names if name in sys.modules}
    try:
        for relative, entrypoint in examples.items():
            path = (staging / relative).resolve()
            assert path.is_relative_to(staging), "Example escapes its owning skill"
            output = StringIO()
            with network_denial(), redirect_stdout(output):
                namespace = runpy.run_path(str(path))
                namespace[entrypoint]()
            for name in local_names & sys.modules.keys():
                assert Path(sys.modules[name].__file__).resolve().is_relative_to(staging), (
                    f"{name}: example imported an unstaged helper"
                )
            results[relative] = {"entrypoint": entrypoint, "status": "passed", "stdout": output.getvalue()}
    finally:
        sys.path[:] = original_path
        for name in local_names:
            sys.modules.pop(name, None)
        sys.modules.update(previous_modules)
    return {"staging": str(staging), "examples": results,
            "scope": "Prepared SDK synthetic transport; no live enrollment or reader-decision claim"}
