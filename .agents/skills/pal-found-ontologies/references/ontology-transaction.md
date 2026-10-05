# Ontology transaction operations

These records describe the `ontology_transaction` commands in `pal-found-ontologies`. Each record gives inputs, behavior, results, and examples.

### ontology_transaction.post_edits

- **Purpose and behavior:** Applies a set of edits to a transaction in order.
- **CLI inputs:** positionals `ontology`, `transaction_id`; optional `--edits`, `--preview`, `--sdk-package-rid`, `--sdk-version`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `transaction_id`: The ID of the transaction to apply edits to. Transactions are an experimental feature and all workflows may not be supported. `--edits` contains the list of Ontology edits to post in the transaction; `--preview` enables endpoint preview behavior when that feature is available; `--sdk-package-rid` identifies the generated SDK package for SDK-aware requests; `--sdk-version` identifies the generated SDK version paired with that package.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The transaction ID identifies a writable ontology transaction and the edits match its supported schema.
- **Result:** Returns `PostTransactionEditsResponse` for this ontology transaction request.
- **Failure:** Invalid edits, expired/unknown transaction ID, or denied write access fails; after timeout inspect transaction state before retrying.
- **Example:** `pal-found-ontologies ontology-transaction post-edits palantir <TRANSACTION_ID> --edits '[]'`
