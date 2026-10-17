# J7/J8 local reader artifacts

Scope: only `pal-found-dev/SKILL.md`, its local references and examples, supplied J7/J8 records, and prepared Node runtime. No public page, tenant, source oracle or expected-answer file was used. The synthetic fixtures below were run from the isolated skill root. No real application or Widget Set was created.

## J7: React Todo application

### Concept and lifecycle

Developer Console application, generated Todo/Action bindings, OAuth sign-in, authorized query, Action validation/edit, and deployed website are separate states. Login success does not confer the restricted user's Action permission. A provider shares the configured OSDK client and query cache. Trace: `references/applications/osdk.md` sections “Concept and lifecycle” and “Worked example”; `references/applications/react.md` sections “Concept and lifecycle” and “Procedure”.

### Prerequisites and access boundary

Use the prepared exact generated package/version exposing `Todo` and `completeTodo`, compatible OSDK 2.x/React packages, Node >=18, registered public OAuth client, selected Ontology RID, approved enrollment URL, redirect and origin. Browser code contains no client secret or personal token. Register the Todo and Action resources and Ontology read/write operations. Configure the localhost callback/origin pair from the guide only when approved, and request explicit `api:use-ontologies-read` and `api:use-ontologies-write` scopes. OAuth/CORS changes and missing grants require owners/administrators. Local UI fixtures need no enrollment; login, real query, Action and hosting need authorized enrollment. Trace: `references/applications/osdk.md` sections “Prerequisites”, “Procedure”, “Worked example”; `references/security/applications.md` sections “Concept and lifecycle”, “Procedure”.

### Ordered procedure and adaptable artifact

1. In Developer Console select a client-facing application. Configure the public OAuth redirect/origin, selected Ontology, Todo and `completeTodo`; generate and pin the package. Check actual exports against `examples/applications/schema.json` before compiling.
2. Configure one stable client with `configureClient({foundryUrl, ontologyRid, clientId, redirectUrl, scopes:["api:use-ontologies-read","api:use-ontologies-write"], requestTimeoutMs:15000})` from `examples/applications/client.ts`. The timeout is application policy. Mount `<Application client={client}/>` from `examples/applications/Application.tsx`; it places `<TodoList/>` under `OsdkProvider`.
3. Query incomplete Todos ordered newest first with `useOsdkObjects(Todo,{where:{isComplete:false},orderBy:{createdAt:"desc"},pageSize:10})`. Use generated `$primaryKey` for rows and `hasMore/fetchMore` for additional pages. Render loading, empty, denied/error and retained-data refresh separately.
4. Use `useOsdkAction(completeTodo)` and `await action.applyAction({todo,isComplete:true})` for an authorized user. Disable repeat submission while pending. Show validation failure from `action.error.actionValidation` and other errors separately. After confirmed effect and cache refresh, Todo `t1/Check orders/false` should leave the incomplete list. Treat optimistic display as provisional.
5. Compile against the actual generated package. For Foundry website hosting, obtain approved domain/HTTPS callback, build static assets, upload a correctly rooted archive, preview its asset, deploy the selected version, then verify each user's view. That deployment is a later enrollment step.

Trace: `references/applications/osdk.md` sections “Procedure” and “Worked example”; `references/applications/react.md` sections “Procedure” and “Worked example”; `examples/applications/client.ts`, `Application.tsx`, `TodoList.tsx`.

### Expected observations and local result

Permitted user can query accessible Todos and submit a valid Action. Denied user can still sign in but sees a specific Action authorization/error state; prior confirmed Todo state remains visible. A successful build or local state fixture does not prove a tenant edit or selected website version. Executed: `node examples/applications/fixture_run.mjs` passed loading, denied, empty, retained-data refresh and pending states. `node examples/applications/timeout_unit_fixture.mjs` passed local timeout, caller abort, transport error, timer cleanup and recovery. Neither executed React hooks, OAuth, Action or deployment. Trace: `references/applications/react.md` sections “Expected result and checks”, “Worked example”; `references/applications/osdk.md` section “Worked example”.

### Failures and bounded recovery

For login success plus Action denial, inspect acting user, application resource/operation restrictions, scopes, Ontology object/Action permissions and submission criteria. Do not relabel denial as empty data. On timeout after Action submission, the prepared transport aborts; OSDK may surface a `PalantirApiError` whose cause is `TimeoutError`. Retain target key, fetch Todo again under authorized identity and inspect any correlated side effect before retrying. A second request may duplicate external effects; escalate unresolved outcome. Use confirmed state for UI rollback, then revalidate after any release rollback. Trace: `references/applications/osdk.md` sections “Worked example”, “Failures and recovery”; `references/applications/react.md` sections “Failures and recovery”; `references/security/applications.md` sections “Failures and recovery”.

## J8: two widgets and Workshop host

### Concept and lifecycle

One Widget Set can hold multiple widget entry points. Source, local build/manifest, first published release, Workshop host version and later release are separate states. Playground exercises widget parameter/event behavior; Workshop checks actual bindings after publication. Trace: `references/widgets/lifecycle.md` sections “Concept and lifecycle”, “Procedure”; `references/widgets/testing.md` section “Concept and lifecycle”; `references/widgets/distribution.md` section “Concept and lifecycle”.

### Prerequisites and access boundary

Use the approved Widget Set project/folder, two prepared React/Vite entries, compatible widget packages, project scripts, declared parameter/event schema and authorized publisher. In Files create a Widget Set and check inherited permissions. Local Node fixture/build needs prepared dependencies; dev mode, Workshop, upload/tag publication and host selection need enrollment access. Plugin >=3.34.0 is required for parameter/event preview; Marketplace build, if used, needs >=3.1.0. Token stays outside widget source/assets. Trace: `references/widgets/lifecycle.md` section “Prerequisites”; `references/widgets/testing.md` section “Prerequisites”; `references/widgets/distribution.md` section “Prerequisites”.

### Ordered procedure and adaptable artifact

1. Create `reviewCounter` with `count:number` and `label:string`; declare `countChanged` with `parameterUpdateIds:["count"]`. Use `examples/widgets/counter.config.ts`, `ReviewCounter.tsx`, `counter.tsx` and `counter.html`. Build with `vite.config.ts` listing its HTML entry. Inspect `dist/.palantir/widgets.config.json` for the ID, entry assets and intended version.
2. Run local playground dev mode and test count `0`, label `Order reviews`. Clicking Increment emits `countChanged` with `{parameterUpdates:{count:1}}`. Bind Workshop count to a number variable and the event to a host update. Change host count back to `0` or to `5`; render must follow host value. The host owns retained state. `examples/widgets/events.mjs` rejects an event with undeclared update or nonnumeric count.
3. Publish the first release containing `reviewCounter`. Workshop cannot select a widget that has never appeared in a published release; a local playground preview is insufficient.
4. Add `reviewSummary` from `summary.config.ts`, `summary.tsx`, `summary.html` and include both HTML inputs in `vite.config.ts`. Rebuild, verify two manifest entries and publish a later version, for example `1.1.0` after a `1.0.0` first release. Verify each host's selected version; choose `1.1.0` in Workshop when it should show the new widget. Hosts still pinned to `1.0.0` retain that version until changed.
5. Test bindings under normal, zero, absent and invalid values in Playground, then the actual host. Publish through the authorized repository tag, prepared CLI or root-level archive upload route. Verify exact release and host selections. Keep a verified prior host version for UI rollback.

Trace: `references/widgets/lifecycle.md` sections “Procedure”, “Worked example”; `references/widgets/integration.md` sections “Procedure”, “Worked example”; `references/widgets/testing.md` sections “Procedure”, “Worked example”; `references/widgets/distribution.md` sections “Procedure”, “Worked example”.

### Expected observations and local result

Local fixture should show count `0` supplied by host, `countChanged` update `1`, later host value applied, wrong-type update rejected and explicit release selection. Executed: `node examples/widgets/fixture_run.mjs` passed those synthetic decisions. It did not render `FoundryWidget`, create a release or verify Workshop. Real acceptance requires built manifest entries, first and later release identities, actual Workshop binding/event observations, allowed and denied users, and host-selected version. Trace: `references/widgets/testing.md` sections “Expected result and checks”, “Worked example”; `references/widgets/lifecycle.md` section “Expected result and checks”; `references/widgets/distribution.md` section “Expected result and checks”.

### Failures and bounded recovery

If first widget is absent from Workshop, publish it successfully, then select that release. For wrong event type, keep the host value unchanged, correct the parameter schema/payload and retest before release. If a host stays on the earlier version, explicitly select and verify the later release; source HEAD or Widget Set publication alone does not switch it. If a new release regresses UI behavior, select the previously verified host version and recheck bindings. This cannot undo Ontology Actions already taken. For stale dev configuration, reapply the current setup link; for denied OSDK access, check Widget Set API enablement and user grants. Trace: `references/widgets/lifecycle.md` section “Failures and recovery”; `references/widgets/integration.md` section “Failures and recovery”; `references/widgets/testing.md` section “Failures and recovery”; `references/widgets/distribution.md` section “Failures and recovery”.
