# Applications, branching, and security

[Back to Foundry development topics](../SKILL.md)

This guide covers custom applications built against the Ontology, React widgets
hosted in Workshop, the branch models used during development, and the
permissions that apply when the work runs. Use the linked Palantir pages for
version-specific setup and API details.

## React applications with the Ontology SDK

The Ontology SDK (OSDK) generates typed access to the object types, actions,
functions, and other Ontology resources selected for an application. A custom
React application can use those bindings to search objects, follow links,
aggregate object sets, invoke actions, and call functions. Developer Console
also lets an application select Platform API operations when it needs resources
outside the Ontology. Select the smallest resource set the application needs:
the selection determines both generated bindings and default OAuth resource
restrictions. An OSDK package remains tied to its selected Ontology after
generation. See [OSDK overview](https://www.palantir.com/docs/foundry/ontology-sdk),
[Developer Console application creation](https://www.palantir.com/docs/foundry/developer-console/create-application),
and [TypeScript OSDK](https://www.palantir.com/docs/foundry/ontology-sdk/typescript-osdk).

For a browser application, create a client-facing application in Developer
Console, configure its OAuth redirect and allowed origin, choose Ontology and
Platform API resources, then generate the first SDK version. Bootstrap a
TypeScript application or add the OSDK to an existing one. Client-facing apps
use user permissions and the authorization-code OAuth flow; never put a client
secret in browser code. A backend service can instead use application
permissions and a service user with a client-credentials flow. Choose which
identity should read or edit data before designing the UI. The
[TypeScript bootstrap guide](https://www.palantir.com/docs/foundry/developer-console/how-to-bootstrapping-typescript)
and [React application overview](https://www.palantir.com/docs/foundry/ontology-sdk-react-applications/overview)
show the setup sequence; [Developer Console permissions](https://www.palantir.com/docs/foundry/developer-console/permissions)
explain both identity modes.

`@osdk/react` supplies hooks for objects, object sets, links, aggregations,
actions, and functions, with loading and cache behavior suited to React.
Develop locally or in a Foundry Code Repository, run the repository's lint,
test, and build checks, and preview pull requests before release. A pull
request preview uses committed code and requires permission on the Developer
Console application. For hosting, configure and deploy the application in
Foundry after its OAuth and resource settings are correct. See
[OSDK React](https://www.palantir.com/docs/foundry/ontology-sdk-react-applications/osdk-react),
[React development](https://www.palantir.com/docs/foundry/ontology-sdk-react-applications/development),
and [Foundry hosting](https://www.palantir.com/docs/foundry/developer-console/deploy-custom-application-on-foundry).

If an older application uses TypeScript OSDK 1.x, check the
[2.x migration guide](https://www.palantir.com/docs/foundry/ontology-sdk/typescript-osdk-migration)
before changing imports or API calls. Use
[subscriptions](https://www.palantir.com/docs/foundry/ontology-sdk/typescript-subscriptions)
when the interface needs Ontology change notifications, rather than assuming
every read automatically refreshes.

## Custom React widgets inside Workshop

A Widget Set packages React widgets for Workshop. Create a Widget Set from a
Foundry Code Repository or an external repository; configure OSDK if the
widget needs Ontology data. OSDK calls also require Ontology APIs to be
enabled for the Widget Set by an authorized administrator. Develop with the
Widget Set's React/Vite setup and preview unpublished code in the playground
or a VS Code workspace. Foundry starts the first release automatically for a
Foundry repository; external repositories use the publish flow. A widget must
have a first published release before it appears in Workshop's widget selector.
After that, Workshop dev mode can preview unpublished code, parameters, and
events. See
[create a Widget Set](https://www.palantir.com/docs/foundry/custom-widgets/create),
[widget development](https://www.palantir.com/docs/foundry/custom-widgets/development),
and [Workshop embedding](https://www.palantir.com/docs/foundry/custom-widgets/embedding-in-workshop).

Define the contract with Workshop in the widget configuration. Parameters
carry values from Workshop variables into the widget, including supported
object sets. Events let the widget request parameter updates or trigger
Workshop behavior. Bind both in Workshop's Widget setup panel and test the
interaction in Workshop dev mode. For example, a selected object set can feed
a custom chart; a click event can update a Workshop selection variable. When
using an object set parameter with React hooks, pass an OSDK client to the
widget and configure the OSDK provider as shown in the official example. See
[parameters and events](https://www.palantir.com/docs/foundry/custom-widgets/parameters-and-events),
[OSDK in widgets](https://www.palantir.com/docs/foundry/custom-widgets/use-osdk),
and [Workshop embedding](https://www.palantir.com/docs/foundry/custom-widgets/embedding-in-workshop).

Add further widgets to the set when they share release ownership. Publish
tested versions through Foundry's tag/build flow or the supported external
CI/CD flow, then choose a version in Workshop. For distribution across
enrollments, package the Widget Set into a Marketplace product. See
[additional widgets](https://www.palantir.com/docs/foundry/custom-widgets/additional-widget),
[publishing](https://www.palantir.com/docs/foundry/custom-widgets/publish),
and [Marketplace packaging](https://www.palantir.com/docs/foundry/custom-widgets/marketplace).

## Choose the right branch

| Branch | Scope | Typical use |
| --- | --- | --- |
| Code Repository / Git branch | Source commits in one repository | Review code through commits, checks, and pull requests. |
| Dataset branch | A dataset's transaction history | Isolate data versions and writes. |
| Build branch | Job specification and output resolution for a build | Run a pipeline against branch data with configured fallbacks. |
| Global branch | Supported resources across Foundry applications | Test a coordinated pipeline, Ontology, Function, and application change before a proposal merges. |

The branch selector in VS Code can expose both a repository branch and a
Global branch. They are distinct. A Global branch spans supported platform
resources and is based on repository `main` for supported Code Repositories;
check the integration list before assuming a resource participates. For source
work alone, use normal repository branches and pull requests. See
[VS Code branch distinction](https://www.palantir.com/docs/foundry/vs-code/global-branching),
[Code Repository navigation](https://www.palantir.com/docs/foundry/code-repositories/navigation),
and [Global Branching integrations](https://www.palantir.com/docs/foundry/global-branching/integrations).

Dataset branches hold isolated transaction histories. A build chooses a build
branch and fallback sequence to resolve job specifications and inputs. It
opens output transactions on the build branch, may create missing output
branches, and does not modify other dataset branches or create branches on
input datasets. Confirm fallback behavior before expecting a branch build to
use the same code and data versions as `main`. See
[data branching](https://www.palantir.com/docs/foundry/data-integration/branching),
[datasets](https://www.palantir.com/docs/foundry/data-integration/datasets),
and [builds](https://www.palantir.com/docs/foundry/data-integration/builds).

A Global branch has a proposal and review lifecycle. Prepare the supported
resources, run their checks, review conflicts and required approvals, then
merge the proposal. The merge flow offers build choices for affected resources;
choose based on whether downstream data must update immediately. Resource
integration varies: Ontology edits, Functions, and Pipeline Builder have their
own branch behavior. Read the corresponding integration page before changing
one of these resources. See [Global Branching concepts](https://www.palantir.com/docs/foundry/global-branching/core-concepts),
[branching the Ontology](https://www.palantir.com/docs/foundry/ontologies/branching-ontology),
[branching Functions](https://www.palantir.com/docs/foundry/functions/branching-functions),
and [Pipeline Builder branches](https://www.palantir.com/docs/foundry/pipeline-builder/branches-overview).

## Security and governance during development

Projects and folders organize resource access. Roles grant operations on
resources; organizations, markings, and classification controls can further
restrict data access and propagate to derived data. Put pipeline stages and
applications in projects whose roles match the teams that maintain them.
Check upstream data access and downstream markings when a build or application
works for one developer but fails for another. See
[projects and roles](https://www.palantir.com/docs/foundry/security/projects-and-roles),
[pipeline security](https://www.palantir.com/docs/foundry/building-pipelines/security-overview),
and [recommended project structure](https://www.palantir.com/docs/foundry/building-pipelines/recommended-project-structure).

Ontology access has separate layers: permission to see or edit the Ontology
resource, permission to see object instances and properties, and permission
to invoke an Action. Current project-based Ontology permissions apply where
enabled; some existing Ontologies still use prior models. Datasource-backed
objects can also require backing datasource access, while object security
policies can control objects and properties. Validate the effective access of
the intended user before relying on an application view or Action. See
[Ontology permissions](https://www.palantir.com/docs/foundry/object-permissioning/ontology-permissions),
[object security policies](https://www.palantir.com/docs/foundry/object-permissioning/object-security-policies),
[Action permissions](https://www.palantir.com/docs/foundry/action-types/permissions),
and [Action read/write authorizations](https://www.palantir.com/docs/foundry/action-types/read-write-authorizations).

Developer Console applications have sharing, OAuth, and resource restrictions.
With user permissions, the user's Foundry rights govern data access. With
application permissions, a service user's rights govern access, independent of
the caller's rights. A client-facing app must use user permissions. In either
mode, the token's scopes and the application's resource restrictions can narrow
access; they do not grant missing resource permissions. Check the effective
identity, requested scopes, selected resources, and restrictions when a call
is denied. Project permissions also control application configuration and
hosted or previewed pages. See [Developer Console permissions](https://www.palantir.com/docs/foundry/developer-console/permissions)
and [application restrictions](https://www.palantir.com/docs/foundry/developer-console/application-restrictions).

Global branch roles govern branch management; they do not grant edit access
to resources on the branch. A contributor still needs the resource or project
permissions required for each change. Review the branch's organization scope,
resource approvals, and proposal checks before merging. See
[Global Branch security](https://www.palantir.com/docs/foundry/global-branching/branch-security)
and [branch concepts](https://www.palantir.com/docs/foundry/global-branching/core-concepts).
