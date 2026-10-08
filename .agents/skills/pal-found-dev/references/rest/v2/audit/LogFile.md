# LogFile: audit operations

[REST catalog](../../catalog.md) | [Authentication and identity](../../authentication.md)

Audit log files expose records for an authorized audit workflow. Decide a bounded time or page window and retain the file identity used for later review. Content is a byte response; close its stream and enforce a size limit.

Prepare SDK 1.101.0 and an identity authorized for the exact tenant resource. Check each contract for its API stage and endpoint-specific restrictions. No universal role or retry guarantee is implied by these operations. For an uncertain write, read the exact RID and effect before repeating it.

## Operations

### content

Read one selected log file as bytes. Limit total bytes and close the response; preserve file identity and retrieval window for audit traceability.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/audit/LogFile/content.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/audit/LogFile/content.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.

### list

Discover available log files with bounded pagination. Carry the returned continuation token and record partial discovery if the budget ends.

Read [exact SDK arguments, HTTP request, result and errors](../../contracts/v2/audit/LogFile/list.md) and run the [offline SDK fixture](../../../../examples/rest/073/v2/audit/LogFile/list.py) from the skill root. The fixture checks serialization, synthetic response decoding and source-declared errors without contacting an enrollment.
