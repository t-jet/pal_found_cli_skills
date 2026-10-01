"""Regression checks for local credential ignore rules and doc-only skills."""

from pathlib import Path
import re
import subprocess


ROOT = Path(__file__).parent.parent
SKILLS = ROOT / ".agents" / "skills"
README = ROOT / "README.md"
IGNORED_CREDENTIAL_PATHS = (
    ".env",
    ".env.local",
    ".env.production",
    "qa-private-key.pem",
    "qa-private.key",
    "qa-certificate.p12",
    "qa-certificate.pfx",
)
TRACKABLE_ENV_PATHS = (".env.example", ".env.template")
STALE_SCRIPT_RE = re.compile(r"python\s+pal_found_|pal_found_[a-z_]+_cli\.py|scripts/")


def _git(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ("git", "-C", str(ROOT), *args),
        check=False,
        capture_output=True,
        text=True,
    )


def test_local_credential_paths_are_ignored() -> None:
    for path in IGNORED_CREDENTIAL_PATHS:
        result = _git("check-ignore", "--quiet", "--", path)
        assert result.returncode == 0, f"expected {path} to be ignored: {result.stderr}"


def test_placeholder_environment_files_remain_trackable() -> None:
    for path in TRACKABLE_ENV_PATHS:
        result = _git("check-ignore", "--quiet", "--", path)
        assert result.returncode == 1, f"expected {path} to remain trackable"


def test_no_live_credential_pattern_is_tracked() -> None:
    result = _git("ls-files")
    assert result.returncode == 0, result.stderr

    unsafe = []
    for tracked_path in result.stdout.splitlines():
        name = Path(tracked_path).name
        is_live_env = name == ".env" or (
            name.startswith(".env.") and name not in TRACKABLE_ENV_PATHS
        )
        if is_live_env or Path(name).suffix.lower() in {".pem", ".key", ".p12", ".pfx"}:
            unsafe.append(tracked_path)

    assert not unsafe, f"tracked credential-pattern files: {unsafe}"


def test_no_skill_md_contains_stale_python_script_references() -> None:
    # FEATURE-011 (DEV-STORY-040 AC-D-012-02): no SKILL.md may reference a
    # python launcher or scripts/ directory; every skill is documentation-only
    # and invokes the installed pal-found-* command.
    for skill_file in SKILLS.glob("pal-found-*/SKILL.md"):
        text = skill_file.read_text(encoding="utf-8")
        assert not STALE_SCRIPT_RE.search(text), (
            f"{skill_file} still contains a stale python/scripts reference"
        )


def test_distribution_readme_states_doc_only_model_and_install_prerequisite() -> None:
    # FEATURE-011 (DEV-STORY-040 AC-D-012-06/08): distribution states skills are
    # documentation-only and the pal_found_cli package must be installed first.
    text = README.read_text(encoding="utf-8")
    assert "documentation only" in text
    assert "pal_found_cli" in text
    assert "conda install -c t-jet pal_found_cli" in text
    assert "pip install pal_found_cli" in text
    assert "uv tool install pal_found_cli" in text
