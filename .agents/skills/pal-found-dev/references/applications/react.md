# React query and release lifecycle

[Development guide](../../SKILL.md) | [Registration and bindings](osdk.md)

## Concept and lifecycle

An OSDK React application couples generated Ontology types with React lifecycle
and governed queries/Actions. `@osdk/react` provides typed hooks and a shared
normalized cache. UI loading, cached revalidation, Action validation, optimistic
display, confirmed edits and released website versions are distinct states.

## Prerequisites

Prepare the registered application/client and bindings from the
[local registration guide](osdk.md), React/ReactDOM and compatible
`@osdk/react`, `@osdk/api`, `@osdk/client` dependencies in the project's pinned
environment. The worked Todo schema and generated exports must match the
[local contract](../../examples/applications/schema.json).

Local state fixtures need Node; actual hooks need the prepared packages and
provider. Actual data, Actions and publishing need authorized enrollment access.
Hosting/deployment and domain approvals are separate permissions; a local
render cannot establish website deployment or authorization.

## Procedure

1. Create one configured client and wrap the root in
   `<OsdkProvider client={client}>`. Hooks must be inside the provider; creating
   a new client every render loses the intended shared client/cache context.
2. Query with generated types and explicit filters/order. Use
   `useOsdkObjects(Todo,{where:{isComplete:false},orderBy:{createdAt:"desc"}})`.
   Preserve loading/error/empty states and use generated primary keys for rows.
3. A query may retain data while revalidating. Show refresh separately from the
   initial empty-loading state. Bounded pagination uses hook `fetchMore`/`hasMore`;
   do not assume the first loaded page is the entire dataset.
4. Use the prepared Action hook with exact generated parameter types. Disable
   repeated submission while pending. Validation does not execute an edit.
   Distinguish Action validation errors from unknown transport/server failures.
5. Test rejected/empty/loading/data/refresh/pending states. Normalized cache
   shares objects by type/key and queries by their definition; Actions refresh
   affected objects. Optimistic display must be marked provisional and reconciled
   on failure. Subscriptions need lifecycle cleanup and authorized connectivity;
   avoid a competing cache or unbounded resubscription on every render.
6. Build/test the exact app version using prepared project tooling. Publish
   through its authorized hosting workflow, verify actual selected website
   version and users, and retain a previously verified release for rollback.

For a supported standalone app needing live updates, set `streamUpdates:true`
on its object query. This is unavailable in custom widgets and unsupported for
link traversal (`pivotTo`) or derived-property queries. Direct TypeScript
subscriptions require generated/client OSDK >=2.1; keep one subscription per
query, call its `unsubscribe()` during cleanup, reload the object set on
`onOutOfDate`, and treat `onError` as a closed subscription. Missing properties
in a change notification do not mean they were cleared.

For Foundry hosting, request the website domain in Developer Console > Website
hosting and obtain ISO approval. Use an HTTPS `/auth/callback` redirect in both
code and registration. Build static assets, zip their contents without the
output folder, and choose Upload new asset. Preview that asset before Deploy
to production, then View site and verify user sharing. Hosting supports browser
assets, not Node/Python servers; maximum upload is 1,000 files/20MB. If required
scanning is asynchronous, configure `site.uploadOnly:true`, await completion,
then deploy the scanned asset. Coordinate unsupported domain/TLS/ingress setup
with enrollment administrators before expecting hosting to work.

## Worked example

[TodoList.tsx](../../examples/applications/TodoList.tsx) uses documented
query/Action hooks beneath [Application.tsx](../../examples/applications/Application.tsx)'s
provider. Pass the stable client returned by the registration example, then render
that root with the project's prepared React entry point. The list uses a shared
[state selector](../../examples/applications/view_state.mjs). The selector is
exercised by `node examples/applications/fixture_run.mjs` from this skill root.
The fixture verifies initial loading, denied error, empty results, retained-data
refresh, and pending submission. It does not run hooks or contact Foundry.

With synthetic Todo `t1/Check orders/false`, the actual generated binding should
display one row. `completeTodo` accepts that object and `isComplete:true`.
After confirmed execution/cache refresh the incomplete list excludes it. A
restricted identity shows failure and retains accurate state; the UI must not
announce success from optimistic display or validation alone.

The source component expects its generated SDK package and prepared provider.
Its schema file describes the required example contract; it is not a generated
SDK replacement. Record actual package versions and generated resource bindings
before compiling or treating tenant effects as verified.

With the prepared [dependency versions](../../examples/applications/versions.json),
run `tsc -p examples/applications/api-check.tsconfig.json` from this skill root.
The [schema type fixture](../../examples/applications/schema-fixture.d.ts)
checks example call shapes against real library declarations; it is hand-authored
synthetic metadata and does not verify tenant-generated bindings. Compile again
in the actual project against its prepared generated package before release.

## Expected result and checks

Each state has a visible correct outcome and stable keys. Verify generated
imports/provider, exact query shape, result ordering, empty and rejected cases,
confirmed Action effect and cache reconciliation. Record local fixture output,
prepared-runtime render tests and actual enrollment effect separately. A
successful app build does not identify which website version users receive.

## Failures and recovery

For provider errors, check root coverage and stable client identity. For stale
data, inspect query definitions, cache dependencies and actual effect before
invalidating/refetching. For Action failures, retain/restore confirmed state and
show the source error; reconcile uncertain effects before replaying. For release
regressions, select the verified prior website version and recheck users/data;
website rollback does not undo already committed Ontology edits.

Optional provenance: [React hooks](https://www.palantir.com/docs/foundry/ontology-sdk-react-applications/osdk-react),
[provider](https://palantir.github.io/osdk-ts/react/getting-started/),
[queries](https://palantir.github.io/osdk-ts/react/querying-data/),
[Actions](https://palantir.github.io/osdk-ts/react/actions/),
[cache](https://palantir.github.io/osdk-ts/react/cache-management/),
[subscriptions](https://www.palantir.com/docs/foundry/ontology-sdk/typescript-subscriptions),
[Foundry hosting](https://www.palantir.com/docs/foundry/developer-console/deploy-custom-application-on-foundry).
