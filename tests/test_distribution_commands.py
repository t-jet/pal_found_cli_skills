"""Executable checks for commands published in the distribution README."""

import base64
from pathlib import Path
import shutil
import subprocess


ROOT = Path(__file__).parent.parent
README = ROOT / "README.md"
EXPECTED_SKILLS = {
    path.name
    for path in (ROOT / ".agents" / "skills").iterdir()
    if path.is_dir() and path.name.startswith("pal-found")
}


def _codex_powershell_block() -> str:
    text = README.read_text(encoding="utf-8")
    section = text.split("### Copy for Codex", maxsplit=1)[1]
    return section.split("```powershell", maxsplit=1)[1].split("```", maxsplit=1)[0]


def _powershell() -> str:
    executable = shutil.which("pwsh") or shutil.which("powershell")
    assert executable is not None, "PowerShell is required to test its published commands"
    return executable


def _run_copy_block(source: Path, workspace: Path) -> subprocess.CompletedProcess[str]:
    quoted_workspace = str(workspace).replace("'", "''")
    script = _codex_powershell_block().replace(
        '$Workspace = "C:\\path\\to\\workspace"',
        f"$Workspace = '{quoted_workspace}'",
        1,
    )
    encoded_script = base64.b64encode(script.encode("utf-16-le")).decode("ascii")
    return subprocess.run(
        (
            _powershell(),
            "-NoLogo",
            "-NoProfile",
            "-NonInteractive",
            "-EncodedCommand",
            encoded_script,
        ),
        cwd=source,
        capture_output=True,
        text=True,
        check=False,
    )


def _copy_source_tree(destination: Path) -> Path:
    source = destination / "clone"
    shutil.copytree(ROOT / ".agents", source / ".agents")
    shutil.copy2(README, source / "README.md")
    return source


def test_published_powershell_copy_is_complete_and_safe_to_rerun(tmp_path: Path) -> None:
    source = _copy_source_tree(tmp_path)
    workspace = tmp_path / "workspace with spaces"

    first = _run_copy_block(source, workspace)
    assert first.returncode == 0, first.stderr
    assert "Copied and verified 19 skills" in first.stdout

    destination = workspace / ".agents" / "skills"
    copied = {path.name for path in destination.iterdir() if path.is_dir()}
    assert copied == EXPECTED_SKILLS
    assert all((destination / name / "SKILL.md").is_file() for name in copied)

    sentinel = destination / "pal-found" / "SKILL.md"
    expected_sentinel = (source / ".agents" / "skills" / "pal-found" / "SKILL.md")
    sentinel.write_text("stale content", encoding="utf-8")
    stale_file = destination / "pal-found" / "removed-by-rollback.txt"
    stale_file.write_text("stale content", encoding="utf-8")
    unrelated = destination / "custom-skill"
    unrelated.mkdir()

    rerun = _run_copy_block(source, workspace)
    assert rerun.returncode == 0, rerun.stderr
    assert sentinel.read_bytes() == expected_sentinel.read_bytes()
    assert not stale_file.exists()
    assert unrelated.is_dir()
    assert not (destination / "pal-found" / "pal-found").exists()


def test_published_powershell_copy_fails_before_mutation_on_bad_source(
    tmp_path: Path,
) -> None:
    source = _copy_source_tree(tmp_path)
    shutil.rmtree(source / ".agents" / "skills" / "pal-found-widgets")
    workspace = tmp_path / "untouched-workspace"

    result = _run_copy_block(source, workspace)

    assert result.returncode != 0
    assert "Expected 19 source skills" in result.stderr
    assert not (workspace / ".agents" / "skills").exists()
