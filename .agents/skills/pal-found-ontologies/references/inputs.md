# Ontology identifiers and JSON inputs

The `ontology` argument accepts an Ontology API name such as `palantir` or an
Ontology RID. Find either with `ontology list` or in Ontology Manager. Object,
action, link, query, interface, and property arguments normally use their API
names, not display names. Inspect the corresponding `list` or `get` metadata
command before using them. An object's `primary_key` is the value configured
as that object's primary key; the CLI passes it as a positional string.

`--parameters` is a JSON object keyed by action or query parameter IDs. Read
the action type or query type metadata to learn required keys and value types.
Values use the SDK's `DataValue` JSON encoding: numbers and booleans are JSON
numbers and booleans, dates are ISO strings, object references use primary-key
values, and attachment references use attachment RIDs. For example,
`--parameters '{"id":80060,"newName":"Anna Smith-Doe"}'` matches the SDK's
`rename-employee` example. A parameter default configured in the action type
is not supplied automatically by the `action.apply` endpoint.

`--object-set` is a JSON definition with a `type` discriminator. A base set
can be `{"type":"base","objectType":"Employee"}`; filters, unions, and
references use different shapes. `--select` is a JSON array of property API
names, such as `["name"]`; omit it where optional to use the endpoint's
default selection. `--select-v2` uses property identifiers and must not be
combined with `--select` on `ontology-object-set load`. `--where`,
`--aggregation`, `--group-by`, `--edits`, and `--overrides` follow the request
types named in each SDK method. Start from that method's example or type model
instead of treating them as SQL or arbitrary key/value objects.

Batch `--requests` arguments are JSON arrays of request objects. For example,
`object-type get-by-rid-batch` elements use `objectTypeRid`, while
`action-type get-by-rid-batch` elements use `actionTypeRid`. The related SDK
request element model specifies each field. Binary uploads read actual bytes
from `--body-file`; attachment uploads also need `--filename`. The CLI infers
attachment content length from the file if it is omitted. Binary reads save a
file and report its path and checksums.
