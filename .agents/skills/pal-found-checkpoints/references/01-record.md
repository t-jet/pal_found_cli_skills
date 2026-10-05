# Checkpoint record operations

A checkpoint interrupts a sensitive Foundry interaction and asks its user for a justification. Submission creates a record with the time, acting user, checkpoint type, justification, and associated resources or objects. Users can review their own historical justifications; authorized administrators can review records across their scope. These commands retrieve records; they do not configure checkpoints or submit justifications. See the [Checkpoints overview](https://www.palantir.com/docs/foundry/checkpoints/overview) and SDK `docs/v2/Checkpoints/Record.md`.

Examples use replaceable identifiers. The CLI requires Foundry credentials and permission to view the records.

### record.get

Retrieve one checkpoint record by RID when an investigation already has its identifier. The response is a `Record` containing the justification and interaction context. No state changes. An unknown or inaccessible RID cannot yield a readable record.

**Example:**
```bash
pal-found-checkpoints record get ri.checkpoints.main.checkpoint.a1b2c3d4-e5f6-7890-abcd-ef1234567890
```

### record.get_batch

Retrieve up to 100 records in one request. `--records-json` takes a JSON array of RIDs. The API omits records that do not exist or that the caller cannot access, so compare returned RIDs with the requested list. A successful empty batch does not prove those records do not exist. More than 100 RIDs exceeds the endpoint limit; malformed JSON fails CLI validation.

**Example:**
```bash
pal-found-checkpoints record get-batch --records-json '["ri.checkpoints.main.checkpoint.a1b2c3d4-e5f6-7890-abcd-ef1234567890","ri.checkpoints.main.checkpoint.b1b2c3d4-e5f6-7890-abcd-ef1234567890"]'
```

### record.search

Search records using a typed `--where-json` filter. For example, an equality filter on `checkpointType` finds justifications for an interaction type. Results are paged; creation time defaults to reverse chronological order. A filter that matches nothing returns an empty result, while invalid filter structure fails. Use a returned continuation token with `--page-token` for the next page. The SDK default page size is 100.

**Example:**
```bash
pal-found-checkpoints record search --where-json '{"filter":{"type":"eq","field":"checkpointType","value":"CONTOUR_EXPORT"}}' --page-size 50 --sort-direction DESC
```

Filters support equality, range, text search, AND, OR, and NOT, subject to each filter type's allowed fields. The search is read-only.
