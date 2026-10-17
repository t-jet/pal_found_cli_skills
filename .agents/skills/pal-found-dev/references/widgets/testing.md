# Playground and Workshop previews

[Development guide](../../SKILL.md) | [Widget lifecycle](lifecycle.md)

## Concept and lifecycle

Dev mode substitutes development assets for your account. Other users retain
published assets. Playground checks isolate parameter/event behavior; Workshop
checks exercise real bindings and layout. Neither establishes production release
success. A paused or inactive dev session displays published assets.

## Prerequisites

Prepare the repository, pinned React/Vite/widget packages, project scripts and
approved development authentication. Local server uses a protected
`FOUNDRY_TOKEN` environment value; workspace authentication is Foundry-managed.
Do not place tokens in widget source or built assets. Local fixture execution
needs Node only. Actual host previews require authorized enrollment and widget
access. Parameters/event preview requires widget Vite plugin >=3.34.0.

## Procedure

1. Run `npm run dev` in a prepared local repository, or `npm run dev:remote`
   in its VS Code workspace. Open the current setup link/preview and keep
   that server running.
2. Confirm dev mode is enabled and identifies the intended local/workspace
   source. Inactive means no override for the displayed widget; check identity
   and server, then reapply the session. Sessions expire after 24 hours.
3. Use playground inputs for absent values, zero, empty text and normal values;
   inspect emitted event IDs and parameter updates. Test small and large sizes.
4. After component edits, save and check rendering. After configuration edits,
   reapply dev mode using the current setup link or refreshed workspace preview.
5. After the widget's first publication, select it in Workshop and test the
   same cases using actual variables/events. Pause dev mode and compare the
   selected published version. Stop the session when finished.
6. Run project lint, type checks, tests and build before release. Keep fixture,
   package compilation, host preview and publication evidence separate.

## Worked example

Run `node examples/widgets/fixture_run.mjs` from this skill root. It simulates
Workshop providing count `0`, an increment event returning count `1`, subsequent
host changes, invalid updates and host version selection. It shares the counter's
[pure event function](../../examples/widgets/events.mjs); it does not execute
`FoundryWidget` or validate browser rendering.

In the actual playground, set count to `0` and label to `Order reviews`, click
Increment, then inspect `countChanged` with count `1`. In Workshop bind count
to a number variable and the event to a visible side effect. Change the host
variable back to `0` and confirm the widget follows it. Record the dev mode
source and selected release with screenshots or test output.

## Expected result and checks

The host controls displayed state; an event carries the proposed update.
UI confirms the value received back from the host. No update is inferred from
button click alone. Test remount/navigation: use host variables for retained
state or approved keep-mounted display settings. Browser `localStorage`,
`sessionStorage` and IndexedDB are unavailable in the widget runtime.

## Failures and recovery

Unchanged code: check server and dev-mode source. Stale configuration: reapply
dev mode. Newly added widget absent in Workshop: publish it first.
Unexpected count reset: inspect host binding and remount behavior. External
fetch blocked: widget CSP cannot be customized; use an authorized Foundry
Function/webhook integration. Dedicated workers are supported; shared/service
workers are unavailable. An error-free local server does not prove runtime
permissions or host behavior.

Optional provenance: [development and runtime limitations](https://www.palantir.com/docs/foundry/custom-widgets/development),
[Workshop embedding](https://www.palantir.com/docs/foundry/custom-widgets/embedding-in-workshop).
