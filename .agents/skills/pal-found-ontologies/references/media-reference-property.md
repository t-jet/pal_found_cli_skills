# Media reference property operations

These records describe the `media_reference_property` commands in `pal-found-ontologies`. Each record gives inputs, behavior, results, and examples.

### media_reference_property.get_media_content

- **Purpose and behavior:** Gets the content of a media item referenced by this property.
- **CLI inputs:** positionals `ontology`, `object_type`, `primary_key`, `property`; optional `--output-filename`, `--preview`, `--sdk-package-rid`, `--sdk-version`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `object_type`: API name defined in the ontology; discover it through the corresponding metadata command. `primary_key`: Primary-key value of an object of the selected object type. `property`: API name defined in the ontology; discover it through the corresponding metadata command. `--output-filename` chooses a basename for the downloaded content in the CLI download directory; `--preview` enables endpoint preview behavior when that feature is available; `--sdk-package-rid` identifies the generated SDK package for SDK-aware requests; `--sdk-version` identifies the generated SDK version paired with that package.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The caller can read the media reference property and has room to save its file locally.
- **Result:** Saves the returned bytes as a file and prints a download metadata envelope with the path and checksums (SDK payload `bytes`).
- **Failure:** Missing access or a failed transfer produces a structured error; check the saved file and download metadata before using partial output.
- **Example:** `pal-found-ontologies media-reference-property get-media-content palantir employee 50030 profile_picture`

### media_reference_property.get_media_metadata

- **Purpose and behavior:** Gets metadata about the media item referenced by this property.
- **CLI inputs:** positionals `ontology`, `object_type`, `primary_key`, `property`; optional `--preview`, `--sdk-package-rid`, `--sdk-version`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `object_type`: API name defined in the ontology; discover it through the corresponding metadata command. `primary_key`: Primary-key value of an object of the selected object type. `property`: API name defined in the ontology; discover it through the corresponding metadata command. `--preview` enables endpoint preview behavior when that feature is available; `--sdk-package-rid` identifies the generated SDK package for SDK-aware requests; `--sdk-version` identifies the generated SDK version paired with that package.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The object has a media reference property and the caller may read the referenced item.
- **Result:** Returns `MediaMetadata` for the selected media reference property.
- **Failure:** Missing media reference or denied media access fails; a content transfer may stop before the saved file is complete.
- **Example:** `pal-found-ontologies media-reference-property get-media-metadata palantir employee 50030 <PROPERTY>`

### media_reference_property.upload

- **Purpose and behavior:** Uploads a media item to the media set which backs the specified property. The property must be backed by a single media set and branch, otherwise an error will be thrown. The body of the request must contain the binary content of the file and the `Content-Type` header must be `application/octet-stream`.
- **CLI inputs:** positionals `ontology`, `object_type`, `property`; optional `--content-length`, `--content-type`, `--body-file`, `--media-item-path`, `--preview`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `object_type`: API name defined in the ontology; discover it through the corresponding metadata command. `property`: API name defined in the ontology; discover it through the corresponding metadata command. `--body-file`: Path to the local file whose bytes are uploaded. `--content-length` declares the upload body size in bytes; use the actual file length; `--content-type` sets the uploaded file's MIME type; `--media-item-path` sets the path of the media item within the media set; `--preview` enables endpoint preview behavior when that feature is available.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** A readable local `--body-file` must exist. The caller needs permission to upload into the target property or attachment service.
- **Result:** Uploads file bytes and returns `MediaReference` identifying the stored media reference property.
- **Failure:** Missing `--body-file`, an unreadable file, or a rejected upload fails before a usable attachment/media reference is returned. Check the stored resource before retrying after a timeout.
- **Example:** `pal-found-ontologies media-reference-property upload palantir employee profile_picture --body-file attachment.pdf`
