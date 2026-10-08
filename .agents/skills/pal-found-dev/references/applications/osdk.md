# Application registration and generated SDK

[Development guide](../../SKILL.md) | [Application overview](../applications-branching-security.md)

## Concept and lifecycle

Developer Console registers an application, its OAuth client and permitted
resources/operations. Generated OSDK bindings describe selected Ontology types.
Application registration, SDK generation, browser authentication and authorized
data access are separate outcomes. An OAuth login does not bypass the user's
permissions or the application's resource restrictions.

Effective access combines user/service identity, application resource and
operation restrictions, and requested token operation scopes. Restricted
applications use `api:use-*` scopes for public APIs. An explicit empty array `[]`
defaults to configured client restrictions; an unrestricted authorization-code client
must explicitly request scopes. Allow each needed operation and cross-namespace
dependency; one namespace grant does not implicitly grant another.

## Prerequisites

Prepare Node >=18, a compatible TypeScript OSDK2.x client/API/OAuth dependency
set, the application-specific generated package and its exact version, selected
Ontology RID, enrollment URL, client ID and redirect URL. Keep these values in
the project's approved configuration; browser applications use public OAuth
and must not contain a client secret or a personal token in source.

Creation needs the application's folder create operation and the organization
workflow for linked third-party clients. OAuth/CORS changes are administrator
controlled. Local synthetic UI fixtures run without connectivity. Registration,
generation, authentication and actual queries require authorized enrollment.

## Procedure

1. In Developer Console select New application and choose client-facing
   application for browser users, or the supported backend-service path for a
   service identity. Do not silently substitute a service user for browser users.
2. Configure authorization-code redirect and matching origin policy. For the
   documented local example, callback is `http://localhost:8080/auth/callback`
   and origin `http://localhost:8080`; an approved HTTPS-localhost configuration
   is an alternative when the HTTP origin cannot be enabled.
3. Select the Ontology and exact object/Action resources. After generation,
   that application's selected Ontology cannot be changed. Add necessary
   Platform SDK resources/operations separately when using platform APIs.
4. Create the application and generate its first SDK version. The selected
   resources determine bindings and default OAuth resource restrictions. Inspect
   prepared generated exports and lockfile before authoring imports.
5. Configure a stable client instance with enrollment URL, Ontology RID and
   the public OAuth client. Complete the approved callback/sign-in flow and
   test actual users against the selected resources and operations.

## Worked example

The local [schema contract](../../examples/applications/schema.json) declares
a synthetic Todo type (`todoId`, `title`, `isComplete`, `createdAt`) and
`completeTodo(todo,isComplete)`. `@my/osdk` in the example means the prepared
generated package for that exact schema; it is not a universal Foundry package.
Verify those names/types against your generated version before adapting code.

[client.ts](../../examples/applications/client.ts) uses the documented
`createPublicOauthClient` and `createClient` APIs. Pass approved configuration;
its factory contains no enrollment-specific credentials. Query a bounded first
page with `client(Todo).fetchPage({$pageSize:10})`. A permitted user should see
the configured accessible objects. A user denied the underlying type or an
application lacking that resource remains denied even after successful login.

Use `auth.signIn()` at the configured callback/sign-in boundary and
`auth.signOut()` when the user signs out. The helper requires an explicit approved
`scopes` array before sign-in. For this query/Action example, use
`scopes: ["api:use-ontologies-read", "api:use-ontologies-write"]` after those
operations/resources are allowed. A query-only app should request only
`["api:use-ontologies-read"]`; it must not execute `completeTodo`.

In pinned `@osdk/oauth`1.14.0, omitted or `undefined` scopes differ from `[]`:
the library supplies `api:read-data`, `api:write-data`,
`api:use-ontologies-read` and `api:use-ontologies-write`. This helper rejects
omission to avoid relying on those defaults. An explicit nonempty array requests
exactly the approved operations; restrictions and user permissions still apply.

Set `requestTimeoutMs` in `configureClient` to bound this app's JSON query/Action
HTTP requests. The helper defaults to 15000ms and accepts integer 1–120000ms;
these are example policy limits, not Foundry server limits. Pinned client2.76.0
supports a custom fetch as `createClient`'s fifth argument. The local
[transport](../../examples/applications/timeout.mjs) aborts real fetch through
AbortController, keeps the deadline through response-body consumption, preserves
caller cancellation and clears timers/listeners. Direct transport calls reject
with `TimeoutError`; OSDK 2.76.0 wraps a fetch timeout in `PalantirApiError`.
Inspect its cause or original error before treating it as a timeout. An HTTP 403
stays a response for SDK error handling. Reconcile uncertain Action effects
through a fresh authorized read before retrying. Buffering suits this
small JSON app; do not use it for streaming/media. It does not bound OAuth
sign-in/token retrieval or WebSocket subscription lifetimes. Widgets retain
their supported host transport and cannot perform arbitrary external HTTP calls.
Run `node timeout_fixture.mjs` from the prepared application example directory
to exercise an actual local HTTP server's stalled headers/body and cancellation;
this proves local abort behavior, not Foundry execution.

The [version contract](../../examples/applications/versions.json) pins checked
client/React/widget APIs. OSDK1.x code using `legacyClient.ontology.objects`
cannot be reused directly: OSDK2.x uses `client(Type).fetchPage`,
`client(Action).applyAction`, and `client(Query).executeFunction`. Regenerate
selected bindings for 2.x and check responses/types before migrating behavior.

Application permission also governs configuration editing and website access.
Viewer can use/view the configured application; Editor can modify resources,
OAuth parameters and generate versions; Owner can share. These roles can be
customized, and enrollment current/legacy permission models differ. For
LMS-backed Actions in an OSDK frontend, application Viewer access is an
additional requirement; successful execution from Workshop is separate evidence.

## Expected result and checks

Record application identity, selected Ontology/resources, generated package
version and callback/origin configuration. Verify imports, a bounded actual
query and an intended denied query. Distinguish user authorization, application
restriction and missing generated binding. Use the local schema/fixture without
claiming it created the Developer Console application or granted permissions.

## Failures and recovery

For callback/origin failure, compare exact approved redirect and origin settings.
For missing exports, compare the selected resource and generated version; an
unrelated SDK package cannot supply the binding. For denied queries, inspect
user/application grants and resource restrictions rather than broadening access
without an owner decision. Refresh/re-authenticate through the prepared flow
when credentials expire. Never log or commit tokens during diagnosis.

Optional provenance: [application creation](https://www.palantir.com/docs/foundry/developer-console/create-application),
[permissions](https://www.palantir.com/docs/foundry/developer-console/permissions),
[client APIs](https://www.palantir.com/docs/foundry/developer-console/how-to-add-to-existing-typescript),
[restrictions](https://www.palantir.com/docs/foundry/developer-console/application-restrictions),
[TypeScript2.x](https://www.palantir.com/docs/foundry/ontology-sdk/typescript-osdk),
[migration](https://www.palantir.com/docs/foundry/ontology-sdk/typescript-osdk-migration).
