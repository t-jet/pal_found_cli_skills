# Offline reader results: J9 and J10

This reader used only `pal-found-dev/SKILL.md` and local links in that skill. The records are synthetic. Python check below tests reasoning over those records; no Foundry operation occurred.

Run from this directory: `python -B context_check.py`. Expected output: `Synthetic contexts: J9 and J10 expected mismatches confirmed`.

## J9: branch and release plan

The Git change is `feature-risk` at `review-code-7`, based on `main`. That identifies source code only. The requested build branch is `demo`, with ordered input fallback `demo`, then `master`. No input transaction exists on `demo`, so the supplied build must resolve its input to `master/input-41`; output is `demo/output-9`. Opening `master` shows `output-8`, not that test output. Global branch `trial-risk` is a separate configuration branch and its proposal has not merged. A shared name or branch selector cannot establish that the external SDK, dataset and Widget Set use one context. Sources: `references/branching/contexts.md` (Concept, Procedure, Worked example), `references/branching/datasets.md` (Concept, Procedure).

Use this context record before review, replacing illustrative values with actual enrollment observations:

```json
{
  "git": {"branch": "feature-risk", "commit": "review-code-7", "base": "main"},
  "build": {"branch": "demo", "fallbackOrder": ["demo", "master"], "resolvedInput": "master/input-41", "output": "demo/output-9"},
  "global": {"branch": "trial-risk", "proposal": "pending"},
  "consumer": {"branch": "master", "visibleOutput": "output-8"}
}
```

Inspect Code Repository Settings > Branches for its actual default, protection, merge modes, checks, reviewers and repository fallbacks. Configure the `demo, master` fallback for the actual build launcher too; schedule and external launchers do not inherit repository settings. Publish JobSpecs for intended commit, check input resolution in job details, compare schema/counts and run a synthetic input case on `demo` if production input cannot be used for a test. Run local fixture and repository Preview/tests, commit, inspect checks including `ci/foundry-publish`, then open a PR against the configured target. Rejected review or failed required check stops source merge. Source: `references/branching/git.md` (Procedure, Failures), `references/pipelines/releases.md` (Procedure), `references/branching/datasets.md` (Procedure).

For supported Ontology Action and Workshop module changes, save both on `trial-risk`, inspect resource dependencies, compare latest main, rebase each resource in its owning application and resolve conflicts, then rerun previews. Save Workshop before rebase. Branch Owner or space Administrator creates the proposal; all checks and required approvals must pass before merge. `Contributor` role alone does not establish proposal-creation authority, and `Viewer` project role cannot be assumed to grant resource edit access. Inspect each actual resource operation and mandatory control under the acting identity, then ask authorized owners for narrow grants or hand off edits to an authorized editor. Source: `references/branching/global.md` (Prerequisites, Procedure, Failures), `references/branching/integrations.md` (Procedure), `references/security/platform.md` (Concept, Procedure), `references/ontology/security.md` (Concept, Procedure).

Custom Widget Set assets follow their own build, version, publish and host selection. A successful Global Branching proposal does not publish a new Widget Set release or change Workshop's selected version. Build/test locally, inspect `dist/.palantir/widgets.config.json`, publish through an authorized route, select the exact released version in Workshop, then verify it under allowed and denied identities. Keep prior working host version for UI rollback. Source: `references/widgets/lifecycle.md` (Procedure), `references/widgets/distribution.md` (Procedure, Failures).

Deliver in dependency order: approved source merge and artifact publication, approved global proposal merge, production build on verified branch/input, Widget Set publication and host selection, then downstream checks. Recheck the exact source commit, input/output transaction, stable Action/Function binding if applicable, Workshop configuration and selected widget version. Source: `references/pipelines/releases.md` (Procedure, Expected result), `references/branching/integrations.md` (Expected result).

If a rebase fails, resolve the conflicting field in its owning application, save and retest. If the proposal rejects access or checks, stop merge and obtain the specific permission/review. For a partial merge, inspect succeeded and failed resources; partial merges cannot currently be reverted. If code merges but data looks old, inspect build branch/fallback and launch a reviewed production build; source merge does not merge dataset transactions. Local work can produce code, tests and the context plan. Branch creation, authorization checks, proposal, publication and data verification require enrollment; owners/admins handle grants and protection. Source: `references/branching/global.md` (Failures), `references/branching/datasets.md` (Expected result, Failures), `references/security/platform.md` (Prerequisites).

## J10: stale output, monitoring and recovery

Supplied build succeeded on `demo`, but read `input-41`; business requires `input-42`, available on `master`. Its committed output is `demo/output-9`. Consumer reads `master/output-8`, so neither the input nor the output seen by the consumer proves freshness. Latest health PASS occurred before `input-42`; it has no evidentiary value for that revision. The `demo` schedule is paused, so observed triggers during the pause will be ignored; resumption needs explicit input and target review. Source: `references/operations/lineage.md` (Concept, Procedure), `references/operations/monitoring.md` (Concept, Expected result), `references/operations/support.md` (Concept, Procedure).

In Data Lineage, select output and verify graph branch/fallback. Expand the upstream input and downstream consumer. In Build timeline, select relevant time window and jobs; record build/job/schedule IDs, source commit, resolved input `input-41`, output `output-9`, execution identity and individual job states. Compare against a healthy job in Builds > Compare > Input Changes and Code Changes where output transactions permit it. Inspect current `master/input-42` and consumer `master/output-8`. Do not infer freshness from a green build banner. Source: `references/operations/lineage.md` (Procedure), `references/operations/support.md` (Procedure).

Configuration proposal, requiring actual dataset/schedule IDs, agreed cadence and owner:

1. In Dataset Preview > Health, add output Time Since Last Updated with approved threshold and severity. If committed empty transactions could pass it while business rows remain old, add a content or timestamp check matched to the business revision requirement. Use schedule Metrics > Health for schedule status. Record rule, evaluation mode and current evaluation timestamp.
2. Expand each check and select Watch > All failures or Only critical according to the support agreement. Enable permitted notification preference; name primary and backup responders. Where available, enable automatic issue creation and assign authorized owner.
3. In Data Lineage open output Actions > Manage Schedules > Create schedule. Select intended production targets, exclusions, trigger, build scope and approved execution scope. Inspect graph branch/fallback before saving. Since current `demo` schedule is paused, verify missed inputs and scope before resuming; check new run's linked build and each output transaction.

Source: `references/operations/monitoring.md` (Procedure, Worked example), `references/operations/support.md` (Procedure).

First reconcile the timeout's unknown write by inspecting its known transaction/target and logs. If it committed, do not replay blindly, especially for APPEND, stream or external side effects. If it did not commit, determine approved retry or recompute method. Correct the launcher branch/fallback or prepare an authorized input on the intended branch; perform reviewed code repair only if comparison shows a code defect. Rebuild the intended production context under approved identity. Verify new job and committed output from `input-42`, consumer's selected `master` branch and visible rows, a new check evaluation after the repair, and a subsequent schedule run. Preserve logs before canceling a hung build. If upstream or platform fault remains, hand off IDs, times, affected resources and recorded evidence to its owner. Source: `references/operations/support.md` (Procedure, Failures), `references/operations/lineage.md` (Expected result), `references/branching/datasets.md` (Failures), `references/pipelines/transactions.md` (Failures and recovery).

Expected success: a new committed production output derived from `input-42`, visible to the consumer, with a post-repair PASS evaluation and a schedule history tied to the correct build. Expected failure: branch still resolves `input-41`, consumer remains on `output-8`, latest PASS predates repair, or write state stays uncertain. These are live validation conditions, not observed tenant results. Local Python check confirms supplied context mismatches only. Actual check creation, watches, schedules, build and consumer verification need enrollment and authorized resource owners.
