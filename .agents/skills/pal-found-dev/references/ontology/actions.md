# Action validation and writeback

[Development guide](../../SKILL.md) | [Ontology overview](../ontology-compute.md)

## Concept and lifecycle

An Action defines governed changes to objects/links with typed parameters,
rules, submission criteria and optional side effects. Configuring the Action,
validating inputs, submitting edits and observing a webhook are separate stages.
Permission to edit an Action's configuration differs from permission/criteria
to submit it. Function-backed Actions execute selected logic under that contract.

## Prerequisites

Prepare exact object/property/Action API names, writable configuration and
typed parameters. Object Storage v2 needs edits enabled; legacy v1 uses the
supported writeback dataset path. Confirm actual storage/configuration first.
Enrollment access is required for configuration, validation, submission and
effect checks. Local policy fixtures test declared business rules only.
Side-effect endpoints/secrets/networking require their authorized owners.

## Procedure

1. In Ontology Manager select Action types > New action type. Choose the
   target and Modify object(s) for this example, map the changed property,
   provide metadata and create. Inspect generated parameters and Rules.
2. Set parameter types/defaults/constraints. Restrict priority choices to the
   permitted business values; the display dropdown alone is not authorization.
3. In Security & Submission Criteria, add a Parameter condition on ticket
   status `Open`, plus the intended positive identity/group condition. Configure
   clear failure messages and test both accepted and rejected cases.
4. Verify schema/object/Action read/write authorization separately. Avoid
   negative membership checks as an authorization shortcut: scoped tokens may
   omit the attribute and accidentally satisfy such a negative condition.
5. Use Test run to inspect criteria/rules before effectful submission. Test
   with the selected actual inputs and allowed/restricted identities; distinguish
   validation results from committed edits and configured side effects.
6. Submit through the supported consumer or generated SDK, inspect returned
   validation/edit information, reread the target and check side-effect logs.
   Preserve correlation/target identities for uncertain-outcome reconciliation.

## Worked example

Synthetic Ticket `t1` is Open with priority P2. Action `changePriority` receives
that Ticket and `priority=P0`; submission criteria require a dispatcher identity,
Open status and priority in P0/P1/P2. Allowed submission changes P2 to P0.
Closed ticket, priority P9 or a non-dispatcher must be rejected.

The [local policy fixture](../../examples/ontology/action_fixture.py) verifies
those decisions and an uncertain edit/webhook recovery plan. Run
`python -B examples/ontology/action_fixture.py` from this skill root. Its
dictionary policy is illustrative business logic, not a platform request or
permission evaluator. Configure the equivalent actual Action and generated
parameter contract before calling it.

For a generated TypeScript2.x Action, the source invocation is
`client(changePriority).applyAction({ticket,priority:"P0"},{$returnEdits:true})`.
Use its actual generated names/types and returned union; requesting edit
information does not establish that an external webhook completed. Exact raw
SDK alternatives and error contracts are in the [local REST guide](../rest-api.md).

## Expected result and checks

Check accepted and rejected validation, actual target changes, correct identity
context and each configured side effect separately. A VALID validation response
is not an edit, and a successful edit is not proof of webhook delivery. Record
the before/after target values and correlated side-effect status. Rejected input
must leave the target unchanged in the actual tested workflow.

## Failures and recovery

For rejection, inspect parameter constraints, criteria and actual user/token
context. For uncertain submission, read the known target and correlated logs
before retrying; blindly repeating can duplicate notifications or webhooks.
For a confirmed edit with failed side effect, use the supported recovery for
that side effect and verify it separately. Reverting object data does not
automatically reverse an external operation.

Optional provenance: [configuration](https://www.palantir.com/docs/foundry/action-types/getting-started),
[criteria](https://www.palantir.com/docs/foundry/action-types/submission-criteria),
[test run](https://www.palantir.com/docs/foundry/action-types/test-run),
[side effects](https://www.palantir.com/docs/foundry/action-types/side-effects-overview).
