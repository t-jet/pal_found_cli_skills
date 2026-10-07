# Object and Action authorization

[Development guide](../../SKILL.md)

## Concept and lifecycle

Ontology configuration permissions govern who can view, edit and manage type definitions.
Instance permissions govern which objects and properties a user can read. Action
permissions and submission criteria govern which changes they can apply. A type editor,
object reader and Action submitter can therefore have different outcomes.

With project permissions enabled, Ontology resources use the filesystem's project
roles for configuration. Older resources may need migration; inspect their Security tab
before changing grants. Object security policies filter rows independently of backing
dataset visibility; property policies additionally filter columns. A hidden property
can appear as null while a hidden object is absent. These read-time rules do not
propagate into derived outputs or exports; use mandatory controls for that boundary.

## Prerequisites

Prepare an isolated object type and Action, actual primary keys, object security model,
test identities and expected visibility/edit rules. Read the type's Security tab and
[project boundaries](../security/platform.md). Policy configuration needs its authorized
owner. Migration, marking changes and organization access may require administrators.
Local truth tables can check intended rules; tenant permissions and Action effects
must be tested under real authorized identities in the enrollment.

## Procedure

1. In Ontology Manager open the object's Security tab. Identify whether permissions
   are project-managed or legacy, then inspect configuration and instance requirements.
2. Define allowed rows/properties through the enabled object security policy or backing
   Restricted View mechanism. Keep object identifiers and required Action inputs visible
   only to intended users. Validate policy under both allowed and denied identities.
3. Open the Action type's permissions and submission criteria. Separate view/edit
   configuration from applying the Action. Check every edited object/link type and
   datasource requirement. Do not infer apply access from the visible button.
4. In Workshop use the Action Check access panel to inspect dependency and criterion
   failures. Test validation before submission in an isolated environment.
5. Submit one permitted mutation and freshly read its target. Test an intentionally
   denied mutation without broadening grants. Record expected denial and unchanged state.

## Worked example

Illustrative schema: Shipment(primary key shipmentId, region, status, cost).
A regional dispatcher may see only region NORTH, may read status but not cost,
and may submit a dispatch Action only when status is READY. Configure equivalent
policies/criteria using the enrollment's available policy editor; these values are
business rules, not universal policy JSON or platform API names.

| Identity/input | Expected read | Expected Action result |
| --- | --- | --- |
| NORTH dispatcher, NORTH/READY shipment | Object visible; cost hidden/null | Pass only if all Action permissions also pass. |
| NORTH dispatcher, NORTH/CLOSED shipment | Object visible | Criterion denies dispatch; state remains CLOSED. |
| NORTH dispatcher, SOUTH shipment | Object absent | No authorized target; do not attempt to bypass filtering. |

Use the [Action example](actions.md) for parameter validation and submitting edits.
Even if a user can see an object, edits beyond Actions can require writeback-dataset
edit access or a Restricted View edit policy, depending on the configured model.

## Expected result and checks

Record identity, type/API name, primary key, property visibility, criterion result,
submission result and fresh state. Empty query results can reflect filters; they are
not proof of a nonexistent source row. Separately verify backing dataset access and
object visibility. Removing read restrictions from derived outputs requires approved
mandatory-control design, not merely copying visible fields into a new dataset.

Where enabled, Action read authorizations cap marked data the Action may consume;
write authorizations set minimum security for results. They supplement user permissions
and criteria and confer no access. These features are availability-dependent Beta.

## Failures and recovery

| Observation | Recovery |
| --- | --- |
| Can edit configuration but cannot read objects | Inspect instance policy and mandatory controls under that identity. |
| Property unexpectedly null | Check property authorization before treating null as source-data absence. |
| Visible Action denies submission | Inspect target/link/datasource permissions and every criterion in Check access. |
| Edit submitted but state unchanged | Verify target key, Action result and indexing/fresh read before repeating. |
| Export loses intended row protection | Stop distribution; require marking/classification protection for downstream use. |

Optional source attribution: [Ontology configuration permissions](https://www.palantir.com/docs/foundry/object-permissioning/ontology-permissions),
[object policies](https://www.palantir.com/docs/foundry/object-permissioning/object-security-policies),
[Action permissions](https://www.palantir.com/docs/foundry/action-types/permissions),
[read/write authorizations](https://www.palantir.com/docs/foundry/action-types/read-write-authorizations).
