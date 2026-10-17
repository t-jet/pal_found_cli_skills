# Application and Ontology permission checks

[Branching and security](../applications-branching-security.md) · [Development guide](../../SKILL.md)

## Concept and lifecycle

Application access combines the acting user's or service user's resource permissions,
OAuth client's restrictions and requested operation scopes. Generated OSDK bindings
supply names/types; they grant no authorization. Browser authorization-code clients act
for the logged-in user. Confidential backend clients can act through a service user;
that identity may see different data than the developer or browser caller.

The application's configuration permissions are separate from its data operations.
Compass-managed applications inherit project/folder controls where enabled; legacy
permission models remain possible. Use [registration](../applications/osdk.md) for its
complete preparation and [Ontology security](../ontology/security.md) for instance/Action rules.

## Prerequisites

Prepare enrollment hostname, OAuth registration/security mode, exact permitted resources,
operation list, generated SDK version and allowed/denied users. Browser code needs a
public client and approved callback/origin, never a client secret. Backend secrets stay
in approved credential storage. Local mock tests verify UI/result handling; real OAuth,
queries and Actions require enrollment access. Owners/admins configure restrictions/grants.

## Procedure

1. In Developer Console inspect the application's selected resources and OAuth & restrictions.
   Match backend/user permission mode to the intended product behavior.
2. For a restricted client, add allowed project resources in Platform SDK and each needed
   operation namespace; add Ontology resources/bindings through its OSDK selection.
   Include cross-namespace dependencies explicitly.
3. Request supported operation scopes. Current public API clients use `api:use-*`;
   legacy standalone clients and certain approved internal-service uses have `api:*`.
   Unrestricted public API apps also normally use `api:use-*`. Verify this registration's
   security mode before adapting a legacy code sample.
4. Complete authentication with the prepared SDK and approved redirect. Test a bounded query
   under the actual user/service identity. Then validate an Action before submitting it.
5. Test denied resource/operation cases and present them separately from empty results.
   Inspect the failed endpoint/identity/scopes and target policy before requesting any change.

## Worked example

Illustrative read-only Shipment app: selected Shipment bindings, logistics project allowed,
Ontology read operation allowed, request `api:use-ontologies-read`. Dispatcher A may view
NORTH shipments; Dispatcher B cannot access that project. A should receive only permitted
objects; B's denied request must become a clear authorization state in the UI.

Adding a Dispatch Action requires its binding, allowed operation and underlying Action
permissions/criteria. Adding an administrative current-user API call can additionally
need that endpoint's namespace permission; Ontology read does not automatically allow
all dependent public namespaces. Follow [React result handling](../applications/react.md)
for auth/loading/empty/error states and fresh reads after edits.

## Expected result and checks

Evidence records client ID (no secret), identity, security mode, scope set, resource/version,
endpoint/result and denied outcome. Compare login success with the first actual data call.
For LMS-backed logic invoked through Actions by an OSDK frontend, the logged-in user also
needs application Viewer access; Object Explorer/Workshop may use different permission flows.

## Failures and recovery

| Observation | Recovery |
| --- | --- |
| Login works, data denied | Inspect all access layers, resource restrictions and exact operation. |
| ApiUsageDenied after migration | Add the allowed public endpoint/namespace and compatible use-* scopes. |
| Browser sees service-user data | Fix authentication mode before release; retest each user's intended visibility. |
| Query empty | Inspect authorized filter/context separately; do not label every empty result denied. |
| Action works in Workshop but not custom app | Inspect application restrictions and, for LMS, application Viewer grant. |

Optional source attribution: [OAuth restrictions and scopes](https://www.palantir.com/docs/foundry/developer-console/application-restrictions),
[application configuration permissions](https://www.palantir.com/docs/foundry/developer-console/permissions).
