# Widget Set creation and releases

[Development guide](../../SKILL.md) | [Application overview](../applications-branching-security.md)

## Concept and lifecycle

A Widget Set is a permissioned filesystem resource containing versions of
frontend assets. Each version can contain several widgets with separate entry
points. A source commit, successful build, published version, and Workshop's
selected version describe different states. Keep those identities together in
your release record.

## Prerequisites

Use a prepared React/Vite repository with pinned widget dependencies and its
Node runtime, project/folder create permission, and Widget Set edit/publish
access. Creation and release verification require authorized Foundry access;
source editing and fixture checks can run locally. OSDK configuration additionally
needs generated bindings and the administrator grant described in
[integration](integration.md). These are environment prerequisites.

## Procedure

1. In Files, open the target project/folder and choose New > Widget set. Name
   it and choose In Foundry for a repository with tag-build publishing, or
   Outside of Foundry for external source. Check inherited permissions.
2. Define a unique widget ID, metadata, parameters and events, then render it
   inside `FoundryWidget`. Include its HTML entry in Vite's build inputs.
3. Build the project and inspect the generated
   `dist/.palantir/widgets.config.json`: widget identity, entry assets and
   version must match the intended source. Do not hand-edit the built manifest
   to conceal missing entry points.
4. For an In Foundry template, inspect the initial tag's checks and resulting
   release; creation starts that first release. For external source, use the
   local [publication procedure](distribution.md).
5. Preview unpublished code in the playground. Workshop selection requires
   that particular widget to appear in a published release first.
6. To add another widget, create its configuration, component/HTML entry and
   Vite input. Rebuild, verify both manifest entries, then publish another
   version. A set supports at most 50 widgets. Preserve existing IDs so host
   bindings continue identifying the same widget.

## Worked example

The [counter configuration](../../examples/widgets/counter.config.ts),
[component](../../examples/widgets/ReviewCounter.tsx),
[entry](../../examples/widgets/counter.tsx),
[HTML](../../examples/widgets/counter.html), and
[Vite configuration](../../examples/widgets/vite.config.ts) form a complete
primitive widget source example. Adapt approved project metadata rather than
inventing a Widget Set RID. A second widget is included in
[summary.config.ts](../../examples/widgets/summary.config.ts),
[summary.tsx](../../examples/widgets/summary.tsx) and
[summary.html](../../examples/widgets/summary.html).

Release `1.0.0` can contain only `reviewCounter`. Adding `reviewSummary` produces
a new release, for example `1.1.0`. Existing hosts selecting `1.0.0` continue
using its counter. Select `1.1.0` before expecting the new summary in Workshop.
These version values are an example release plan, not evidence of publication.

## Expected result and checks

Check build inputs against manifest entries and actual published version.
Record which host selects which version. Test an existing counter host after
adding the summary; sharing one set does not require changing its bindings.
Run the [local widget fixture](../../examples/widgets/fixture_run.mjs) for
synthetic host/version checks. It does not create resources or publish releases.

## Failures and recovery

Missing widget: inspect its HTML input, configuration import and manifest,
then rebuild. Missing selector entry: verify successful first publication of
that widget. Failed tag build: inspect checks and correct source before making
a new release. Unexpected host version: inspect selection, not only source HEAD.
Re-select a verified prior version to recover UI behavior; this does not reverse
Ontology Actions already executed by users.

Optional provenance: [core concepts](https://www.palantir.com/docs/foundry/custom-widgets/core-concepts),
[creation](https://www.palantir.com/docs/foundry/custom-widgets/create),
[additional widgets](https://www.palantir.com/docs/foundry/custom-widgets/additional-widget).
