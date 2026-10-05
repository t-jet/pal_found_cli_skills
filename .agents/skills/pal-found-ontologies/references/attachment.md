# Attachment operations

These records describe the `attachment` commands in `pal-found-ontologies`. Each record gives inputs, behavior, results, and examples.

### attachment.get

- **Purpose and behavior:** Get the metadata of an attachment.
- **CLI inputs:** positionals `attachment_rid`.
- **Input meaning:** `attachment_rid`: Resource identifier (RID) of the named Foundry resource.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The caller may read the target attachment; supplied identifiers must resolve in the requested scope.
- **Result:** Returns `AttachmentV2` for the selected attachment.
- **Failure:** An unknown attachment identifier, inaccessible resource, or invalid selector produces a structured error.
- **Example:** `pal-found-ontologies attachment get ri.attachments.main.attachment.bb32154e-e043-4b00-9461-93136ca96b6f`

### attachment.read

- **Purpose and behavior:** Get the content of an attachment.
- **CLI inputs:** positionals `attachment_rid`; optional `--output-filename`.
- **Input meaning:** `attachment_rid`: Resource identifier (RID) of the named Foundry resource. `--output-filename` chooses a basename for the downloaded content in the CLI download directory.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The caller can read the attachment and has room to save its file locally.
- **Result:** Saves the returned bytes as a file and prints a download metadata envelope with the path and checksums (SDK payload `bytes`).
- **Failure:** Missing access or a failed transfer produces a structured error; check the saved file and download metadata before using partial output.
- **Example:** `pal-found-ontologies attachment read ri.attachments.main.attachment.bb32154e-e043-4b00-9461-93136ca96b6f`

### attachment.upload

- **Purpose and behavior:** Upload an attachment to use in an action. Any attachment which has not been linked to an object via an action within one hour after upload will be removed. Previously mapped attachments which are not connected to any object anymore are also removed on a biweekly basis. The body of the request must contain the binary content of the file and the `Content-Type` header must be `application/octet-stream`.
- **CLI inputs:** optional `--content-length`, `--content-type`, `--body-file`, `--filename`.
- **Input meaning:** `--body-file`: Path to the local file whose bytes are uploaded. `--content-length` declares the upload body size in bytes; use the actual file length; `--content-type` sets the uploaded file's MIME type; `--filename` sets the uploaded attachment's filename.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** A readable local `--body-file` must exist. The caller needs permission to upload into the target property or attachment service.
- **Result:** Uploads file bytes and returns `AttachmentV2` identifying the stored attachment.
- **Failure:** Missing `--body-file`, an unreadable file, or a rejected upload fails before a usable attachment/media reference is returned. Check the stored resource before retrying after a timeout.
- **Example:** `pal-found-ontologies attachment upload --content-type application/octet-stream --filename attachment.pdf --body-file attachment.pdf`

### attachment.upload_with_rid

- **Purpose and behavior:** This endpoint is identical to `/v2/ontologies/attachments/upload` but additionally accepts a previously generated `AttachmentRid`.
- **CLI inputs:** positionals `attachment_rid`; optional `--content-length`, `--content-type`, `--body-file`, `--filename`, `--preview`.
- **Input meaning:** `attachment_rid`: Resource identifier (RID) of the named Foundry resource. `--body-file`: Path to the local file whose bytes are uploaded. `--content-length` declares the upload body size in bytes; use the actual file length; `--content-type` sets the uploaded file's MIME type; `--filename` sets the uploaded attachment's filename; `--preview` enables endpoint preview behavior when that feature is available.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** A readable local `--body-file` must exist. The caller needs permission to upload into the target property or attachment service.
- **Result:** Uploads file bytes and returns `AttachmentV2` identifying the stored attachment.
- **Failure:** Missing `--body-file`, an unreadable file, or a rejected upload fails before a usable attachment/media reference is returned. Check the stored resource before retrying after a timeout.
- **Example:** `pal-found-ontologies attachment upload-with-rid ri.attachments.main.attachment.bb32154e-e043-4b00-9461-93136ca96b6f --content-type application/octet-stream --filename attachment.pdf --body-file attachment.pdf`
