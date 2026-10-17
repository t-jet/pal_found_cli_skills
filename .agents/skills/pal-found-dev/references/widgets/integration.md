# Parameters and events

[Development guide](../../SKILL.md) | [Widget lifecycle](lifecycle.md)

## Concept and lifecycle

Workshop passes variables into widget parameters. A widget emits a configured
event carrying allowed parameter updates; Workshop applies bindings and may
trigger a host side effect. This is two-way state exchange, not an Ontology
Action. An OSDK Action has separate authorization and confirmed data effects.

## Prerequisites

Prepare compatible widget client/React packages and a Workshop module with
edit access. Author configuration and synthetic host fixtures locally; binding,
preview and data effects require authorized enrollment. For OSDK, Configure SDK
on the Widget Set with selected resources and prepared generated bindings.
An Information Security Officer, or role granting `Enable widget set unscoped
API access`, must enable Ontology APIs. User resource permissions still apply.

## Procedure

1. Define camelCase parameter/event IDs. Primitive types are boolean, number,
   string, date (`YYYY-MM-DD`) and timestamp (ISO8601 UTC); arrays use `type:
   "array"` and a primitive `subType`. Object sets use `type:"objectSet"` and
   a generated `allowedType`; scenario values are Ontology scenario RIDs.
   Structs and object-set filters are not first-class parameter types.
2. List each event's allowed `parameterUpdateIds`. Read host values from
   `parameters.values`; use `emitEvent(id,{parameterUpdates:{...}})`.
   Each configuration permits at most 50 parameters and 50 events.
3. Render under `FoundryWidget` with its exact config. In Workshop's Widget
   setup panel, bind parameters to matching variables and events to host events.
   Test a host input change and a widget-originated update separately.
4. For OSDK, use the widget client's generated Ontology RID,
   `window.location.origin` and `createFoundryWidgetTokenProvider()`.
   This placeholder provider uses the runtime user's permissions; do not embed
   app OAuth credentials or a personal token.
5. For an object-set parameter, pass the configured client to `FoundryWidget`.
   Read the parameter and render the query component only when it exists;
   pass its hydrated `.objectSet` to the query, not the parameter wrapper
   containing `objectSetRid` and `objectSet`.
   Use stable `useObjectSet` and `OsdkProvider` in the pinned OSDK React 2.76.0
   example. Older widget documentation names `OsdkProvider2` and
   `@osdk/react/experimental`; package 2.76.0 retains deprecated aliases.
   Inspect prepared exports before adapting an older template.
6. Reconcile host data after confirmed OSDK Actions. Set
   `refreshHostDataOnAction:true` in widget configuration or plugin defaults
   when the host's passed object sets need refreshing.

## Worked example

[counter.config.ts](../../examples/widgets/counter.config.ts) exposes label and
count. [ReviewCounter.tsx](../../examples/widgets/ReviewCounter.tsx) reads both and emits
`countChanged`, using [events.mjs](../../examples/widgets/events.mjs) to build
the payload. Workshop supplies label `Order reviews`, count `0`; clicking
Increment proposes count `1`. Bind `countChanged` to a visible host message
or variable-change event, then change count from Workshop to `5`: the next
render must show `5`. Do not keep a competing local counter.

For a Todo object-set extension use
[todo.config.ts](../../examples/widgets/todo.config.ts),
[todo-client.ts](../../examples/widgets/todo-client.ts) and
[TodoWidget.tsx](../../examples/widgets/TodoWidget.tsx). Its generated Todo
binding must match the [schema](../../examples/applications/schema.json).
Undefined input shows a binding prompt. A supplied set is queried within the
widget provider. This example requires actual prepared generated bindings;
the primitive counter works without Ontology data.

## Expected result and checks

Trace incoming variable, displayed value, emitted payload, resulting host
variable and host side effect. Confirm no undeclared parameter is updated.
For object sets test missing, empty, denied and populated inputs. Verify user
and API-enablement failures separately from binding errors. Keep synthetic
fixture output distinct from host integration and actual query/Action execution.

## Failures and recovery

No host update: check event binding and allowed update IDs. Wrong type: inspect
parameter/variable type, regenerate bindings if schema changed and retest.
Stale host data after Action: inspect refresh configuration and confirmed effect.
Widgets do not support object-set subscriptions. Allowed runtime APIs comprise
Ontologies and Functions when enabled, Upload Media and documented Admin user
lookup operations (get, batch get, current user, profile picture, search).
Do not transplant an unrestricted backend REST call into this runtime. Use
an authorized server-side integration for unsupported capabilities.

Optional provenance: [parameter/event contracts](https://www.palantir.com/docs/foundry/custom-widgets/parameters-and-events),
[widget OSDK and supported APIs](https://www.palantir.com/docs/foundry/custom-widgets/use-osdk).
