# v2 data_health: Check

[Operation catalog](../../catalog.md) | [Authentication](../../authentication.md) | [Client behavior](../../client-behavior.md)

## Capability and lifecycle

A health Check is configuration for evaluating data health. Check configuration and
check reports are separate resources. Replacing an existing check cannot change its
type; choose configuration changes compatible with the original type.

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

### create

Create the intended check configuration and retain its RID. Inspect the check and
subsequent reports separately; configuration creation does not establish data health.

[Exact parameters, request, result and error models](../../contracts/v2/data_health/Check/create.md).

[Executable SDK example](../../../../examples/rest/075/v2/data_health/Check/create.py):

```bash
python -B examples/rest/075/v2/data_health/Check/create.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| CheckAlreadyExists | A check of the given type for the given subject(s) already exists. The conflicting check will be returned if the provided token has permission to view it. |
| CheckTypeNotSupported | The type of the requested check is not yet supported in the Platform API. |
| CreateCheckPermissionDenied | Could not create the Check. |
| InvalidNumericColumnCheckConfig | The NumericColumnCheckConfig is invalid. It must contain at least one of numericBounds or trend. |
| InvalidPercentageCheckConfig | The PercentageCheckConfig is invalid. It must contain at least one of percentageBounds or medianDeviation. |
| InvalidTimeCheckConfig | The TimeCheckConfig is invalid. It must contain at least one of timeBounds or medianDeviation. |
| InvalidTransactionTimeCheckConfig | The TransactionTimeCheckConfig is invalid. It must contain at least one of timeBounds or medianDeviation. |
| InvalidTrendConfig | The TrendConfig is invalid. It must contain at least one of trendType or differenceBounds. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### delete

Confirm the check RID and owner's intended removal before deleting it. Verify remaining
dataset check configuration rather than interpreting deletion as a passing health
result.

[Exact parameters, request, result and error models](../../contracts/v2/data_health/Check/delete.md).

[Executable SDK example](../../../../examples/rest/075/v2/data_health/Check/delete.py):

```bash
python -B examples/rest/075/v2/data_health/Check/delete.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| CheckNotFound | The given Check could not be found. |
| DeleteCheckPermissionDenied | Could not delete the Check. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### get

Inspect the selected check's type and configuration before changing it or interpreting
its reports.

[Exact parameters, request, result and error models](../../contracts/v2/data_health/Check/get.md).

[Executable SDK example](../../../../examples/rest/075/v2/data_health/Check/get.py):

```bash
python -B examples/rest/075/v2/data_health/Check/get.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| CheckNotFound | The given Check could not be found. |
| CheckTypeNotSupported | The type of the requested check is not yet supported in the Platform API. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### replace

Read existing configuration and submit a compatible replacement. The check type cannot
be changed after creation; a type change needs a separately reviewed check lifecycle.

[Exact parameters, request, result and error models](../../contracts/v2/data_health/Check/replace.md).

[Executable SDK example](../../../../examples/rest/075/v2/data_health/Check/replace.py):

```bash
python -B examples/rest/075/v2/data_health/Check/replace.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response. Paged results
demonstrate one page only; use the local finite-page procedure to continue, preserve
partial results and reject repeated continuation tokens.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| CheckNotFound | The given Check could not be found. |
| CheckTypeNotSupported | The type of the requested check is not yet supported in the Platform API. |
| InvalidNumericColumnCheckConfig | The NumericColumnCheckConfig is invalid. It must contain at least one of numericBounds or trend. |
| InvalidPercentageCheckConfig | The PercentageCheckConfig is invalid. It must contain at least one of percentageBounds or medianDeviation. |
| InvalidTimeCheckConfig | The TimeCheckConfig is invalid. It must contain at least one of timeBounds or medianDeviation. |
| InvalidTransactionTimeCheckConfig | The TransactionTimeCheckConfig is invalid. It must contain at least one of timeBounds or medianDeviation. |
| InvalidTrendConfig | The TrendConfig is invalid. It must contain at least one of trendType or differenceBounds. |
| ModifyingCheckTypeNotSupported | Changing the type of a check after it has been created is not supported. |
| ReplaceCheckPermissionDenied | Could not replace the Check. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.
