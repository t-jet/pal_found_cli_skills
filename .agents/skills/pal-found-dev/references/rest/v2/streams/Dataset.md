# Streaming dataset creation

[Streams operations](index.md) | [REST client behavior](../../client-behavior.md)

## Concept and prerequisites

`Dataset.create` creates a dataset and its first stream together. The stream belongs to the specified branch or, when omitted, the enrollment's default branch (usually `master`). Prepare a parent folder where the identity may create datasets, a name, and a stream schema that producers can satisfy. Choose partition count, compression and other optional settings from the operation contract before publishing records.

## Procedure and worked example

Call [Dataset.create](../../contracts/v2/streams/Dataset/create.md) once with the intended schema and parent. Retain the returned dataset and stream identity. The [offline SDK fixture](../../../../examples/rest/089/v2/streams/Dataset/invoke_create.py) checks request body, decoded result and named errors without an enrollment. Run it with `python -B` from the skill root. For live use, read the new [Stream](Stream.md) by dataset RID and branch to verify schema, partition count and view RID before giving producers access.

## Expected result, recovery and access boundary

Creation succeeds when the dataset exists in the parent folder and the intended branch has a usable stream. A timeout after submission is ambiguous; inspect the parent and stream before repeating the create. Schema and permission errors need correction before any producer writes. The fixture proves serialization only; creating live resources and writing records require authorized enrollment access.
