# Ontology value type operations

These records describe the `ontology_value_type` commands in `pal-found-ontologies`. Each record gives inputs, behavior, results, and examples.

### ontology_value_type.get

- **Purpose and behavior:** Gets a specific value type with the given API name.
- **CLI inputs:** positionals `ontology`, `value_type`; optional `--preview`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `value_type`: The API name of the value type. To find the API name, use the **List value types** endpoint or check the **Ontology Manager**. `--preview` enables endpoint preview behavior when that feature is available.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The value type belongs to an ontology visible to the caller.
- **Result:** Returns `OntologyValueType` for the selected ontology value type.
- **Failure:** An unknown ontology value type identifier, inaccessible resource, or invalid selector produces a structured error.
- **Example:** `pal-found-ontologies ontology-value-type get palantir countryCode`

### ontology_value_type.list

- **Purpose and behavior:** Lists the latest versions of the value types for the given Ontology.
- **CLI inputs:** positionals `ontology`; optional `--preview`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `--preview` enables endpoint preview behavior when that feature is available.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The value type belongs to an ontology visible to the caller.
- **Result:** Returns `ListOntologyValueTypesResponse` containing the visible matching ontology value type entries; an empty page means none matched that page.
- **Failure:** Invalid filters or a denied scope produce a structured error; an empty successful page is not an error.
- **Example:** `pal-found-ontologies ontology-value-type list palantir`
