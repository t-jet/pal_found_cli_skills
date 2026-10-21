# Version id operations

These records describe the `version_id` commands in `pal-found-functions`. Each record gives inputs, behavior, results, and examples.

### version_id.get

- **Purpose and behavior:** Gets a specific value type with the given RID. The specified version is returned.
- **CLI inputs:** positionals `value_type_rid`, `version_id_version_id`; optional `--preview`.
- **Input meaning:** `value_type_rid`: RID of the value type. `version_id_version_id`: UUID identifying that value type version. Copy `versionId` from `value-type get` metadata for the latest version, or supply a known version UUID. `--preview` enables endpoint preview behavior when that feature is available.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The value type RID and version ID refer to an accessible value type version.
- **Result:** Returns `VersionId` for the selected version id.
- **Failure:** An unknown version id identifier, inaccessible resource, or invalid selector produces a structured error.
- **Example:** `pal-found-functions version-id get <VALUE_TYPE_RID> 123e4567-e89b-12d3-a456-426614174000`
