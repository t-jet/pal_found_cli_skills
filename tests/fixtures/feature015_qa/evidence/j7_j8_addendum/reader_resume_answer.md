# J7/J8 addendum reader answer

This answer used only a copied `pal-found-dev` skill, the prepared J7/J8 runtime, its four prompts, and Node. The source copy is `.ept/tmp/feature015_j7j8_addendum_resume_skill`. `reader_resume.mjs` runs local state only. Its network probe rejects fetch, DNS lookup, TCP connection, and UDP socket creation in this Node process. This cooperative guard does not prove that every subprocess or browser is disconnected. No Foundry tenant was contacted.

Snapshot manifest: 4,379 files, sorted path/SHA-256 list at `.ept/tmp/feature015_j7j8_addendum_resume_manifest.txt`, manifest SHA-256 `5CBF2FC67B3BC706262884B40942CAF7A345738EDB965DFC0A979E3D785B56B8`. Skills worktree HEAD at snapshot: `79b9f9d54dde4c572323935579c092c39be63985`; the worktree had concurrent uncommitted changes, so this manifest identifies the candidate more precisely than HEAD. Prepared runtime SHA-256 `F429C00010275E4297D2DCE371A3D3E7EB38008E7647975ABA3819930044BB00`; prompt SHA-256 `2072722D4A1EC653328E1658594A93230BBB64D12F60638DE84940A545C35520`. An earlier `reader.mjs` existed in this evidence directory before this run (SHA-256 `3F5292EF30FCDC70D86E4E39F9D3EF7637BF5B1505A33DF54651A00CEC716A04`). Its authorship is unclear; this run used separate `reader_resume.*` files and did not execute or edit that prior file.

## Sections consulted

- `SKILL.md`: tool choice and local reference routing.
- `references/applications/osdk.md`: Concept and lifecycle, Prerequisites, Procedure, Worked example, Expected result and checks, Failures and recovery.
- `references/applications/react.md`: Concept and lifecycle, Prerequisites, Procedure, Worked example, Expected result and checks, Failures and recovery.
- `references/widgets/integration.md`: Concept and lifecycle, Prerequisites, Procedure, Worked example, Expected result and checks, Failures and recovery.
- `references/widgets/lifecycle.md`: Concept and lifecycle, Procedure, Worked example, Expected result and checks, Failures and recovery.
- `references/widgets/distribution.md`: Concept and lifecycle, Prerequisites, Procedure, Worked example, Expected result and checks, Failures and recovery.
- `examples/widgets/events.mjs`, `counter.config.ts`, `summary.config.ts`, and `examples/applications/view_state.mjs` for executable local contracts.

## J7-4: registration and denied paths

Use a public OAuth authorization-code client, generated `Todo` and `completeTodo` bindings, callback `http://localhost:8080/auth/callback`, origin `http://localhost:8080`, and explicit `api:use-ontologies-read` plus `api:use-ontologies-write` scopes. Select the intended Ontology, object and Action in Developer Console; generated exports and client version must match that selection. Do not put a client secret or personal token in browser source. The prepared local HTTP values are fixture values; an approved hosted site needs its registered HTTPS callback and domain approval.

The runtime rejects wrong callback (`CALLBACK_MISMATCH`), ungranted identity (`APPLICATION_GRANT_DENIED`), missing read scope (`READ_SCOPE_MISSING`), and Bob requesting ungranted write scope (`SCOPE_DENIED`) before any query or Action. Bob can authenticate with read alone, see one incomplete Todo, and receives `ACTION_DENIED` on completion. The application editor/owner and enrollment administrator must repair client registration, resource restrictions, origin/callback and granted operations as appropriate; an authorized resource owner must grant the user access. The reader cannot grant itself access by widening requested scopes. Actual registration, grants and login need the authorized enrollment.

## J7-5: Action result, cache and website version

Alice's authorized incomplete query returns `todo-1` with `OPEN`. A confirmed completion returns `DONE`; a fresh incomplete query returns `[]`. Keep one OSDK client under `OsdkProvider`, use the generated `Todo` query and `completeTodo` Action, disable submission while pending, and render error/loading/empty/refresh states. The normalized cache shares objects by type and key and refreshes affected queries after a confirmed Action. For a supported standalone view, `streamUpdates:true` can refresh the object query; direct subscriptions need cleanup and `onOutOfDate` reload. Widget object-set subscriptions are unavailable. A local fixture cannot prove a real hook, subscription or tenant update.

A lost reply reports `RESPONSE_TIMEOUT_EFFECT_UNKNOWN`. The local trace contains one Action call, then an authorized reread returns `[]`; it does not replay the Action. If reread cannot settle the effect, keep the outcome uncertain and ask the operator to reconcile it before another write. `working-tree` local preview and website release `1.1.0` with asset `todo-app.1.1.0.js` are different selections. Publishing and checking the actual selected site release require enrollment access and hosting/domain approval. Verify the site with a permitted user and a denied user; successful local preview cannot establish either website selection or grants. A website rollback can restore UI assets but cannot reverse a completed Ontology Action.

## J8-4: host, widget event and second widget

Use `reviewCounter` with number `count`, string `label`, and `countChanged` allowing only a `count` parameter update. Bind the Workshop number variable to both `reviewCounter.count` and `reviewSummary.count`, and bind the counter event to the host update. At selected release `1.1.0`, host inputs 0 then 5 render both widgets with 0 then 5. The counter emits `{parameterUpdates:{count:6}}`; the host and second widget both show 6. A string `count` raises `TypeError: invalid host count`; host state and trace remain at 6. Do not introduce a competing local counter or treat this parameter event as an Ontology Action. Actual Workshop binding and behavior need a published Widget Set, host edit access, and authorized enrollment. OSDK inside a widget additionally needs administrator enablement and user resource permission.

## J8-5: selected release rollback

The host initially selects `1.1.0`, asset `counter.1.1.0.js`, with both widgets available. Select the previously verified `1.0.0`; the local result reports `version:1.0.0`, `asset:counter.1.0.0.js`, `reviewCounter:6`, and no `reviewSummary`. The same `countChanged` binding still updates the host to 7, while `reviewSummary` remains absent from that release. In a real host, verify the selected version, published manifest and assets, parameter/event binding, rendered counter, and an authorized and denied identity. A source checkout or new upload alone does not change a host's selected release. Selecting the prior release requires access to the published version and host configuration. It restores previous UI behavior but does not undo earlier Ontology edits or other side effects.

## Self-check for independent QA scoring

The answer supplies a lifecycle choice, explicit identity/version/access prerequisites, steps/configuration, runnable inputs and serialized results, checks, and failure recovery for all four prompts. The Node script asserts the stated synthetic behavior. Independent QA must score all six dimensions and determine whether any local fact is missing; this self-check is not QA sign-off.
