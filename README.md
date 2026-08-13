# Palantir Foundry skills

This repository is the file-based distribution for the `pal_found_cli_skills`
project. It contains skill folders under `.agents/skills/`.

## Clone

```bash
git clone https://github.com/t-jet/pal_found_cli_skills.git
cd pal_found_cli_skills
git checkout <release-tag>
```

## Copy into a harness

Copy each `pal-found-*` folder from `.agents/skills/` into the target folder.

| Harness | Target folder | Verification |
| --- | --- | --- |
| Codex and other standard-layout harnesses | `<workspace>/.agents/skills/` | Confirm a copied `SKILL.md` exists below the target. |
| Claude Code | `<workspace>/.claude/skills/` | Start a new session and confirm the skill appears in the available skills list. |

Use the harness's documented skills directory when it has a different path.
Do not copy the repository's `.git` directory.

## Update

```bash
git fetch --tags
git checkout <release-tag>  # or: git pull --ff-only
```

Re-copy the skill folders after every update. If an update is bad, check out
the last known-good tag and copy again. No package manager or credential is
needed for distribution.
