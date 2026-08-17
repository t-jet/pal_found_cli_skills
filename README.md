# Palantir Foundry skills

This repository distributes 19 skills. The canonical source is
`.agents/skills/`; each skill has one `SKILL.md` and uses its `pal-found` name.
Copy only those skill folders. Do not copy `.git` or a harness's legacy pointer.

## Clone

```bash
git clone https://github.com/t-jet/pal_found_cli_skills.git
cd pal_found_cli_skills
git checkout <release-tag>
```

Use `git checkout <release-tag>` for a pinned release. Omit it to use the
repository's default branch.

## Canonical inventory

The distribution contains these folders under `.agents/skills/`:

`pal-found`, `pal-found-admin`, `pal-found-aip-agents`,
`pal-found-audit`, `pal-found-checkpoints`, `pal-found-connectivity`,
`pal-found-data-health`, `pal-found-datasets`, `pal-found-filesystem`,
`pal-found-functions`, `pal-found-language-models`, `pal-found-media-sets`,
`pal-found-models`, `pal-found-ontologies`, `pal-found-orchestration`,
`pal-found-sql-queries`, `pal-found-streams`,
`pal-found-third-party-applications`, `pal-found-widgets`.

## Supported harnesses

| Harness | Discovery mode | Target | Result to verify |
| --- | --- | --- | --- |
| Codex | Native | `<workspace>/.agents/skills/` | A new session lists `pal-found` and a namespace skill. |
| Claude Code | Configured link | `<workspace>/.claude/skills/` linked to `.agents/skills/` | A new session lists `pal-found` and a namespace skill. |

Codex reads the standard `.agents/skills/` location directly. Claude Code
expects `.claude/skills/`, so point that path at the canonical directory. The
link keeps one copy of each skill.

### Copy for Codex

PowerShell:

```powershell
$Workspace = "C:\path\to\workspace"
$Source = Join-Path -Path (Get-Location) -ChildPath ".agents\skills"
$Destination = Join-Path -Path $Workspace -ChildPath ".agents\skills"
$ExpectedSkillNames = @(
  "pal-found",
  "pal-found-admin",
  "pal-found-aip-agents",
  "pal-found-audit",
  "pal-found-checkpoints",
  "pal-found-connectivity",
  "pal-found-data-health",
  "pal-found-datasets",
  "pal-found-filesystem",
  "pal-found-functions",
  "pal-found-language-models",
  "pal-found-media-sets",
  "pal-found-models",
  "pal-found-ontologies",
  "pal-found-orchestration",
  "pal-found-sql-queries",
  "pal-found-streams",
  "pal-found-third-party-applications",
  "pal-found-widgets"
)
$Skills = @(
  Get-ChildItem -LiteralPath $Source -Directory |
    Where-Object { $_.Name -like "pal-found*" }
)
$ActualSkillNames = @($Skills | ForEach-Object { $_.Name })
$InventoryDifference = @(
  Compare-Object -ReferenceObject $ExpectedSkillNames -DifferenceObject $ActualSkillNames
)
if ($InventoryDifference.Count -ne 0) {
  throw "Source skill inventory does not match the canonical 19 names in $Source"
}
foreach ($SkillName in $ExpectedSkillNames) {
  $SourceSentinel = Join-Path -Path $Source -ChildPath "$SkillName\SKILL.md"
  if (-not (Test-Path -LiteralPath $SourceSentinel -PathType Leaf)) {
    throw "Missing source $SkillName/SKILL.md"
  }
}
New-Item -ItemType Directory -Force -Path $Destination | Out-Null
foreach ($SkillName in $ExpectedSkillNames) {
  $SourceSkill = Join-Path -Path $Source -ChildPath $SkillName
  $Target = Join-Path -Path $Destination -ChildPath $SkillName
  if (Test-Path -LiteralPath $Target) {
    Remove-Item -LiteralPath $Target -Recurse -Force
  }
  Copy-Item -LiteralPath $SourceSkill -Destination $Destination -Recurse -Force
}
$Copied = @(
  Get-ChildItem -LiteralPath $Destination -Directory |
    Where-Object { $_.Name -like "pal-found*" }
)
$CopiedSkillNames = @($Copied | ForEach-Object { $_.Name })
$CopiedDifference = @(
  Compare-Object -ReferenceObject $ExpectedSkillNames -DifferenceObject $CopiedSkillNames
)
if ($CopiedDifference.Count -ne 0) {
  throw "Copied skill inventory does not match the canonical 19 names in $Destination"
}
foreach ($SkillName in $ExpectedSkillNames) {
  $CopiedSentinel = Join-Path -Path $Destination -ChildPath "$SkillName\SKILL.md"
  if (-not (Test-Path -LiteralPath $CopiedSentinel -PathType Leaf)) {
    throw "Missing copied $SkillName/SKILL.md"
  }
}
Write-Host "Copied and verified $($Copied.Count) skills in $Destination"
```

POSIX shell:

```bash
workspace=/path/to/workspace
mkdir -p "$workspace/.agents/skills"
find .agents/skills -mindepth 1 -maxdepth 1 -type d -name 'pal-found*' \
  -exec cp -R {} "$workspace/.agents/skills/" \;
```

Verify the copied tree before starting the session:

```powershell
$skills = @(Get-ChildItem -Directory "$Workspace\.agents\skills" -Filter "pal-found*")
if ($skills.Count -ne 19) { throw "Expected 19 skills, found $($skills.Count)" }
if (-not (Test-Path "$Workspace\.agents\skills\pal-found\SKILL.md")) { throw "Missing pal-found/SKILL.md" }
```

Start a new Codex session in the workspace and confirm that its available
skills include `pal-found` and at least one namespace skill such as
`pal-found-datasets`.

### Onboard Claude Code without a duplicate copy

First copy the 19 folders into `<workspace>/.agents/skills/`. If the workspace
contains this migration pointer at `.claude/skills/README.md`, remove only
that empty pointer directory, then create a link to the canonical tree.

PowerShell (junction, no administrator permission required):

```powershell
$legacy = Join-Path $Workspace ".claude\skills"
$entries = @(Get-ChildItem -Force $legacy -ErrorAction SilentlyContinue)
if ($entries.Count -gt 0 -and ($entries.Name -ne "README.md" -or $entries.Count -ne 1)) {
  throw "Refusing to replace non-pointer content at $legacy"
}
if (Test-Path "$legacy\README.md") { Remove-Item -LiteralPath "$legacy\README.md" }
if (Test-Path $legacy) { Remove-Item -LiteralPath $legacy }
New-Item -ItemType Junction -Path $legacy -Target (Join-Path $Workspace ".agents\skills") | Out-Null
```

POSIX shell:

```bash
workspace=/path/to/workspace
legacy="$workspace/.claude/skills"
test ! -e "$legacy" || test "$(find "$legacy" -mindepth 1 -maxdepth 1 ! -name README.md -print)" = ""
rm -f "$legacy/README.md"
rmdir "$legacy" 2>/dev/null || true
ln -s "$workspace/.agents/skills" "$legacy"
```

Start a new Claude Code session and confirm that its available skills include
`pal-found` and a namespace skill. If the harness still shows no skills,
inspect the link target and repeat the count and sentinel checks above.

The source repository's `.claude/skills/README.md` is a migration pointer,
not a skill. Do not copy it into either harness.

## Update

```bash
git fetch --tags
git checkout <release-tag>
# Or follow the default branch:
git pull --ff-only
```

Re-copy the 19 `pal-found*` folders after every update. If an update is bad,
check out the last known-good tag and copy again. The PowerShell command is safe
to rerun: it replaces only the 19 validated target skill folders, so removed or
stale files do not survive an update or rollback. Distribution needs only git
and file-copy tools; no package manager or credential is required.
