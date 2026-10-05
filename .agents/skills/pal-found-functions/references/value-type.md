# Value type operations

These records describe the `value_type` commands in `pal-found-functions`. Each record gives inputs, behavior, results, and examples.

### value_type.get

- **Purpose and behavior:** Gets a specific value type with the given RID. The latest version is returned.
- **CLI inputs:** positionals `value_type_rid`; optional `--preview`.
- **Input meaning:** `value_type_rid`: Resource identifier (RID) of the named Foundry resource. `--preview` enables endpoint preview behavior when that feature is available.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The value type RID identifies a value type the caller may read.
- **Result:** Returns `ValueType` for the selected value type.
- **Failure:** An unknown value type identifier, inaccessible resource, or invalid selector produces a structured error.
- **Example:** `pal-found-functions value-type get <VALUE_TYPE_RID>`
