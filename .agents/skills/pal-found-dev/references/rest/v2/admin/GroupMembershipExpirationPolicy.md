# v2 admin: GroupMembershipExpirationPolicy

[Operation catalog](../../catalog.md) | [Authentication](../../authentication.md) | [Client behavior](../../client-behavior.md)

## Capability and lifecycle

A membership expiration policy belongs to a group and defines its membership lifecycle.
Read the current policy and its complete model before replacing it. Changing policy is
different from adding or removing a particular member.

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

### get

Read the policy for the selected group and inspect its complete local model before
deciding whether membership should expire. Absence, a default and an explicit expiration
setting have different meanings in the model.

[Exact parameters, request, result and error models](../../contracts/v2/admin/GroupMembershipExpirationPolicy/get.md).

[Executable SDK example](../../../../examples/rest/071/v2/admin/GroupMembershipExpirationPolicy/get.py):

```bash
python -B examples/rest/071/v2/admin/GroupMembershipExpirationPolicy/get.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| GroupMembershipExpirationPolicyNotFound | The given GroupMembershipExpirationPolicy could not be found. |
| GroupNotFound | The given Group could not be found. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.

### replace

Read existing policy, construct the intended replacement from its model, and verify the
returned policy. Confirm the policy owner's intended expiration behavior before changing
group administration.

[Exact parameters, request, result and error models](../../contracts/v2/admin/GroupMembershipExpirationPolicy/replace.md).

[Executable SDK example](../../../../examples/rest/071/v2/admin/GroupMembershipExpirationPolicy/replace.py):

```bash
python -B examples/rest/071/v2/admin/GroupMembershipExpirationPolicy/replace.py
```

The example checks the serialized HTTP method, path, query, headers and body, decodes
the synthetic success result, and checks each source-declared named error. It uses one
raw response with a 30-second timeout and closes that response.

Declared failures for this operation:

| Error | Meaning |
| --- | --- |
| GroupNotFound | The given Group could not be found. |
| ReplaceGroupMembershipExpirationPolicyPermissionDenied | Could not replace the GroupMembershipExpirationPolicy. |

For a permission failure, verify grants and access for the exact target. For a missing
target, check identity and visibility before choosing a replacement. For invalid input,
compare the request and tenant schema with the complete local model. Keep service
failures distinct from a successful domain result; review uncertain mutations before
retrying.
