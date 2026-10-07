# Widget and Marketplace distribution

[Development guide](../../SKILL.md) | [Widget lifecycle](lifecycle.md)

## Concept and lifecycle

Publishing stores a Widget Set release. Each Workshop host chooses its version;
publication does not change that choice. A Marketplace product groups resources
for reuse in another project/environment. Product version, Widget Set version
and host-selected version remain separate release identities.

## Prerequisites

Prepare tested production assets, pinned project scripts and authorized publish
identity. Local lint/build/archive checks need prepared dependencies; uploads,
tag-build checks and host verification require authorized Foundry connectivity.
Marketplace requires product/output configuration access; OSDK API enablement
requires the administrator workflow in [integration](integration.md).
Marketplace widget builds require widget Vite plugin >=3.1.0.

## Procedure

1. Run project lint/tests/type checks and `npm run build`. Inspect
   `.palantir/widgets.config.json` in the build output and its version.
   `foundry.config.json`'s `widgetSet.autoVersion.type` chooses `package-json`
   (package version) or `git-describe` (tags/commits). Preserve the project's
   configured strategy; inspect the result before uploading.
2. Choose one authorized route: Foundry repository tag build; prepared local
   `@osdk/cli` executable's `widgetset deploy`; or Widget Set Upload release.
   For manual upload, zip the output's contents including hidden `.palantir`,
   with manifest/assets at archive root, without a wrapping `dist` folder.
3. Verify publication and exact manifest version. In each host select the
   intended release, test bindings, then publish the host through its own
   approved workflow. Retain the previous verified selection for UI rollback.
4. For Marketplace, add the Widget Set through product outputs > Add files,
   or include a Workshop module that embeds it; its set is included automatically.
   Publish the product through the organization's approved product workflow.
5. After product deployment, manually enable Ontology APIs on the destination
   Widget Set once when it uses OSDK. That configuration persists through product
   upgrades. Map Ontology inputs with the same API names as source, or deploy
   without prefixes. Verify a destination user's access and actual host version.

## Worked example

In a prepared repository, these commands perform local checks and use its
already provisioned CLI without public package resolution:

```sh
npm run lint
npm run build
npm exec --offline -- osdk widgetset deploy
```

The last command publishes to Foundry: run only with authorized release access
and configured target, after inspecting output. Confirm the prepared executable
is `@osdk/cli` and its `widgetset deploy` help before use. Alternatively choose
Upload release with the checked archive. Use the project's actual tag/version
convention for a Foundry repository; pushing a tag triggers publication.

For example, publish set `1.1.0`, verify hosts A=`1.0.0`, B=`1.1.0`, then test B
before changing A. [fixture_run.mjs](../../examples/widgets/fixture_run.mjs)
checks this synthetic selection scenario without performing publication.

[foundry-config.example.json](../../examples/widgets/foundry-config.example.json)
shows the configuration shape, including output directory and version strategy.
Its `.invalid` domain and all-zero RID are synthetic. Use the prepared project's
actual target for authorized publication; do not deploy this fixture.

## Expected result and checks

Record source commit, build/manifest version, release identity, host selections
and destination grants. Check a user with intended access and a denied identity.
Marketplace-installed repository source supports debugging, not developing new
releases. OSDK versioned Functions in these products use only the latest version;
do not claim preservation of a source-side Function version pin.

## Failures and recovery

Bad archive: inspect root entries including hidden manifest, rebuild/repack.
Host still old: explicitly select new version. Destination OSDK denied: inspect
API enablement and user grants. Missing resources: inspect API-name mappings.
Failed product upgrade: use the organization's product rollback procedure and
recheck host/resource versions; widget rollback does not undo data writes.

Optional provenance: [publishing](https://www.palantir.com/docs/foundry/custom-widgets/publish),
[Marketplace behavior](https://www.palantir.com/docs/foundry/custom-widgets/marketplace).
