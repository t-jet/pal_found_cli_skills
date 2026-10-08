# v1 ontologies: Action

[Operation catalog](../../catalog.md) | [Authentication](../../authentication.md) | [Client behavior](../../client-behavior.md)

## Capability and lifecycle

Actions apply configured changes to Ontology objects or links. Parameter validation,
application and batch application are different operations. Object Storage V1 edits are
eventually visible; Object Storage V2 edits are visible immediately after completion.
This v1 API does not apply parameter defaults automatically.

## Prepare the application

Use prepared SDK 1.101.0 and an authorized identity for the intended enrollment. Resolve
the resource identities and complete request models linked below before calling a
method. Offline fixtures use synthetic identities and an actual SDK HTTP transport; they
need prepared Python, SDK and httpx and contact no enrollment.

Verify the application grants, resource permissions and capability enablement in the
tenant. SDK source does not enumerate a universal role or scope for every operation;
operation-specific documented requirements below take precedence. Source does not
provide a universal idempotency guarantee. For uncertain writes, retain request identity
and reconcile through authorized reads before repeating.

## Operations and outcome checks

## Synthetic action schema

The examples use synthetic action `set-asset-status`, with required string
parameters `assetId` and `status`. The example request sets `A-1` to `ready`.
Its synthetic submission criteria report VALID. No tenant mutation occurs, and
this fixture does not prove that a real asset exists or that this action is
configured in an enrollment.

For application code, read [ActionType](ActionType.md) metadata for the authorized
action API name. Supply the actual parameter IDs and types explicitly; this v1
endpoint does not supply parameter defaults. Validate the request, inspect
submission criteria, then apply it only when the change is authorized. Validation
does not check existing-object constraints. Follow up through
[OntologyObject](OntologyObject.md) using the configured primary key, accounting
for Object Storage V1 visibility delay. Use finite poll counts and a deadline;
preserve pending or ambiguous results for operator review.

### apply

Resolve action metadata, supply explicit schema-compatible parameters and apply one
action. Defaults are unsupported here. OSv1 edits become visible eventually; OSv2 edits
are visible after completion. Reconcile ambiguous submission before repeating.

[Exact parameters, request, result and error models](../../contracts/v1/ontologies/Action/apply.md).

[Executable SDK example](../../../../examples/rest/077/v1/ontologies/Action/apply.py):

```bash
python -B examples/rest/077/v1/ontologies/Action/apply.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

No named operation failures are declared by this frozen SDK method. Generic API,
authentication, transport and decoding failures remain possible; preserve the error
envelope and request identity rather than inventing a domain-specific exception.

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### apply_batch

Apply several requests for the same action type. Use at most 20 actions unless a higher
limit is explicitly established for OSv2-only actions that do not call Functions.
Defaults and notifications are unsupported. Evaluate the returned batch result before
reporting completion.

[Exact parameters, request, result and error models](../../contracts/v1/ontologies/Action/apply_batch.md).

[Executable SDK example](../../../../examples/rest/077/v1/ontologies/Action/apply_batch.py):

```bash
python -B examples/rest/077/v1/ontologies/Action/apply_batch.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

No named operation failures are declared by this frozen SDK method. Generic API,
authentication, transport and decoding failures remain possible; preserve the error
envelope and request identity rather than inventing a domain-specific exception.

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### validate

Evaluate parameter and submission-criteria validity before applying an action.
Validation skips existing-object and other Foundry-data checks, including primary-key
uniqueness and user existence; VALID is not a guarantee that application succeeds.

[Exact parameters, request, result and error models](../../contracts/v1/ontologies/Action/validate.md).

[Executable SDK example](../../../../examples/rest/077/v1/ontologies/Action/validate.py):

```bash
python -B examples/rest/077/v1/ontologies/Action/validate.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

No named operation failures are declared by this frozen SDK method. Generic API,
authentication, transport and decoding failures remain possible; preserve the error
envelope and request identity rather than inventing a domain-specific exception.

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.
