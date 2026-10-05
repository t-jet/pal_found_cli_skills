"""Check that each documented operation example is a valid CLI invocation.

This is an offline syntax check. Parsing does not create a client or call Foundry.
"""

from __future__ import annotations

import importlib
from pathlib import Path
import re
import shlex
import sys
from unittest.mock import patch

from test_offline_skill_gate import FROZEN_OPERATIONS, SKILLS


TOOL_SRC = Path(__file__).resolve().parents[2] / "pal_found_cli_tool" / "src"
RECORD_HEADING = re.compile(r"^### ([a-z][a-z0-9_]*\.[a-z][a-z0-9_]*)\s*$", re.M)
EXAMPLE_LABEL = re.compile(r"(?im)^[ \t]*(?:-[ \t]*)?\*\*Example(?::\*\*|\*\*:)[ \t]*(.*)$")
INLINE_COMMAND = re.compile(r"`(pal-found-[^`\r\n]+)`")
FENCED_COMMAND = re.compile(r"(?s)^```(?:bash|sh|shell)?\s*\n(.*?)\n```")
AUDIT_OPERATIONS = {"log_file list", "log_file content"}


def _operation_records(skill_name: str) -> dict[str, list[tuple[Path, str]]]:
    records: dict[str, list[tuple[Path, str]]] = {}
    paths = (
        [SKILLS / skill_name / "SKILL.md"]
        if skill_name == "pal-found-audit"
        else sorted((SKILLS / skill_name / "references").glob("*.md"))
    )
    for path in paths:
        content = path.read_text(encoding="utf-8")
        headings = list(RECORD_HEADING.finditer(content))
        for index, heading in enumerate(headings):
            end = headings[index + 1].start() if index + 1 < len(headings) else len(content)
            key = heading.group(1).replace(".", " ", 1)
            records.setdefault(key, []).append((path, content[heading.end():end]))
    return records


def _example(record: str) -> str:
    label = EXAMPLE_LABEL.search(record)
    if label is None:
        raise ValueError("missing **Example:** label")

    remainder = record[label.end(1):].lstrip()
    inline = INLINE_COMMAND.match(label.group(1).strip())
    if inline:
        return inline.group(1)

    fence = FENCED_COMMAND.match(remainder)
    if fence:
        commands = [line.strip() for line in fence.group(1).splitlines() if line.strip()]
        if len(commands) == 1 and commands[0].startswith("pal-found-"):
            return commands[0]
        raise ValueError("example fence must contain one standalone pal-found command")

    raise ValueError("example must be an inline command or a one-command fenced block")


def _parser(skill_name: str):
    namespace = skill_name.removeprefix("pal-found-").replace("-", "_")
    module_name = f"pal_found_cli.{namespace}.scripts.pal_found_{namespace}_cli"
    module = importlib.import_module(module_name)
    cli_resource = getattr(module, "_cli_resource", lambda resource: resource.replace("_", "-"))
    return module.build_parser(), cli_resource


def _show_parser_error(_parser, message: str) -> None:
    """Preserve argparse's useful reason instead of the CLI's generic error."""
    raise ValueError(message)


def test_every_operation_example_parses_with_its_namespace_cli() -> None:
    # Import local source directly, so a stale installed wheel cannot mask a
    # documentation mismatch in this checkout.
    sys.path.insert(0, str(TOOL_SRC))
    failures: list[str] = []
    checked = 0

    operations_by_skill = dict(FROZEN_OPERATIONS)
    operations_by_skill["pal-found-audit"] = AUDIT_OPERATIONS
    for skill_name, operations in sorted(operations_by_skill.items()):
        parser, cli_resource = _parser(skill_name)
        records = _operation_records(skill_name)
        for key in sorted(operations):
            matches = records.get(key, [])
            if len(matches) != 1:
                failures.append(f"{skill_name} {key}: expected one operation record, found {len(matches)}")
                continue

            path, body = matches[0]
            location = f"{path.relative_to(SKILLS)}: {key}"
            command = "<missing>"
            try:
                command = _example(body)
                args = shlex.split(command, posix=True)
                if args[0] != skill_name:
                    raise ValueError(f"command starts with {args[0]!r}, expected {skill_name!r}")
                if skill_name == "pal-found-media-sets" and "--output" in args:
                    output = args[args.index("--output") + 1]
                    if "/" in output or "\\" in output:
                        raise ValueError("--output must be a filename under the download directory")
                with patch.object(type(parser), "error", _show_parser_error):
                    parsed = parser.parse_args(args[1:])
                resource, operation = key.split(" ", 1)
                resource, operation = cli_resource(resource), operation.replace("_", "-")
                if (parsed.resource, parsed.operation) != (resource, operation):
                    raise ValueError(
                        f"command selects {parsed.resource}.{parsed.operation}, "
                        f"expected {resource}.{operation}"
                    )
                if key == "log_file list" and not (parsed.start_date or parsed.page_token):
                    raise ValueError("initial audit list requires --start-date")
            except (IndexError, ValueError, SystemExit) as exc:
                failures.append(f"{location}: {exc}; command: {command!r}")
            else:
                checked += 1

    assert not failures, f"{checked} examples parsed; {len(failures)} invalid:\n" + "\n".join(failures)
