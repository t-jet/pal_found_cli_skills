"""Read declared pipeline mounts without contacting Foundry."""

import json
from pathlib import Path


def load_bindings(token_path, alias_path, required=("incoming", "outgoing")):
    token = Path(token_path).read_text(encoding="utf-8").strip()
    if not token:
        raise ValueError("mounted token is empty")
    aliases = json.loads(Path(alias_path).read_text(encoding="utf-8"))
    if not isinstance(aliases, dict):
        raise ValueError("resource alias map must be an object")
    result = {}
    for alias in required:
        resource = aliases.get(alias)
        if not isinstance(resource, dict) or not isinstance(resource.get("rid"), str):
            raise ValueError(f"missing resource binding: {alias}")
        if not resource["rid"]:
            raise ValueError(f"empty resource RID: {alias}")
        branch = resource.get("branch")
        if branch is not None and (not isinstance(branch, str) or not branch):
            raise ValueError(f"invalid resource branch: {alias}")
        result[alias] = {"rid": resource["rid"], "branch": branch or "master"}
    return token, result
