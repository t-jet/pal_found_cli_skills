# Attachment property operations

These records describe the `attachment_property` commands in `pal-found-ontologies`. Each record gives inputs, behavior, results, and examples.

### attachment_property.get_attachment

- **Purpose and behavior:** Get the metadata of attachments parented to the given object.
- **CLI inputs:** positionals `ontology`, `object_type`, `primary_key`, `property`; optional `--sdk-package-rid`, `--sdk-version`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `object_type`: API name defined in the ontology; discover it through the corresponding metadata command. `primary_key`: Primary-key value of an object of the selected object type. `property`: API name defined in the ontology; discover it through the corresponding metadata command. `--sdk-package-rid` identifies the generated SDK package for SDK-aware requests; `--sdk-version` identifies the generated SDK version paired with that package.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The object has an attachment-valued property and the caller can read that object and attachment.
- **Result:** Returns `AttachmentMetadataResponse` for the selected attachment property.
- **Failure:** Missing attachment value, denied object access, or failed byte transfer prevents a usable result.
- **Example:** `pal-found-ontologies attachment-property get-attachment palantir employee 50030 performance`

### attachment_property.get_attachment_by_rid

- **Purpose and behavior:** Get the metadata of a particular attachment in an attachment list.
- **CLI inputs:** positionals `ontology`, `object_type`, `primary_key`, `property`, `attachment_rid`; optional `--sdk-package-rid`, `--sdk-version`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `object_type`: API name defined in the ontology; discover it through the corresponding metadata command. `primary_key`: Primary-key value of an object of the selected object type. `property`: API name defined in the ontology; discover it through the corresponding metadata command. `--sdk-package-rid` identifies the generated SDK package for SDK-aware requests; `--sdk-version` identifies the generated SDK version paired with that package; `attachment_rid` is the RID of the attachment to retrieve directly.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The object has an attachment-valued property and the caller can read that object and attachment.
- **Result:** Returns `AttachmentV2` for the selected attachment property.
- **Failure:** Missing attachment value, denied object access, or failed byte transfer prevents a usable result.
- **Example:** `pal-found-ontologies attachment-property get-attachment-by-rid palantir employee 50030 performance ri.attachments.main.attachment.bb32154e-e043-4b00-9461-93136ca96b6f`

### attachment_property.read_attachment

- **Purpose and behavior:** Get the content of an attachment.
- **CLI inputs:** positionals `ontology`, `object_type`, `primary_key`, `property`; optional `--output-filename`, `--sdk-package-rid`, `--sdk-version`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `object_type`: API name defined in the ontology; discover it through the corresponding metadata command. `primary_key`: Primary-key value of an object of the selected object type. `property`: API name defined in the ontology; discover it through the corresponding metadata command. `--output-filename` chooses a basename for the downloaded content in the CLI download directory; `--sdk-package-rid` identifies the generated SDK package for SDK-aware requests; `--sdk-version` identifies the generated SDK version paired with that package.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The caller can read the attachment property and has room to save its file locally.
- **Result:** Saves the returned bytes as a file and prints a download metadata envelope with the path and checksums (SDK payload `bytes`).
- **Failure:** Missing access or a failed transfer produces a structured error; check the saved file and download metadata before using partial output.
- **Example:** `pal-found-ontologies attachment-property read-attachment palantir employee 50030 performance`

### attachment_property.read_attachment_by_rid

- **Purpose and behavior:** Get the content of an attachment by its RID. The RID must exist in the attachment array of the property.
- **CLI inputs:** positionals `ontology`, `object_type`, `primary_key`, `property`, `attachment_rid`; optional `--output-filename`, `--sdk-package-rid`, `--sdk-version`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `object_type`: API name defined in the ontology; discover it through the corresponding metadata command. `primary_key`: Primary-key value of an object of the selected object type. `property`: API name defined in the ontology; discover it through the corresponding metadata command. `--output-filename` chooses a basename for the downloaded content in the CLI download directory; `--sdk-package-rid` identifies the generated SDK package for SDK-aware requests; `--sdk-version` identifies the generated SDK version paired with that package; `attachment_rid` is the RID of the attachment to retrieve directly.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The caller can read the attachment property and has room to save its file locally.
- **Result:** Saves the returned bytes as a file and prints a download metadata envelope with the path and checksums (SDK payload `bytes`).
- **Failure:** Missing access or a failed transfer produces a structured error; check the saved file and download metadata before using partial output.
- **Example:** `pal-found-ontologies attachment-property read-attachment-by-rid palantir employee 50030 performance ri.attachments.main.attachment.bb32154e-e043-4b00-9461-93136ca96b6f`
