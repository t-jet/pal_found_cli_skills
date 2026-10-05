# Cipher text property operations

These records describe the `cipher_text_property` commands in `pal-found-ontologies`. Each record gives inputs, behavior, results, and examples.

### cipher_text_property.decrypt

- **Purpose and behavior:** Decrypt the value of a ciphertext property.
- **CLI inputs:** positionals `ontology`, `object_type`, `primary_key`, `property`.
- **Input meaning:** `ontology`: Ontology API name or RID; find it with `ontology list` or Ontology Manager. `object_type`: API name defined in the ontology; discover it through the corresponding metadata command. `primary_key`: Primary-key value of an object of the selected object type. `property`: API name defined in the ontology; discover it through the corresponding metadata command.
- **Input guide:** [Identifiers and JSON payloads](./inputs.md).
- **Preconditions:** The object has a cipher-text property and the caller has permission to decrypt it.
- **Result:** Returns `DecryptionResult` for this cipher text property request.
- **Failure:** Missing property or decrypt permission prevents plaintext from being returned.
- **Example:** `pal-found-ontologies cipher-text-property decrypt palantir employee 50030 performance`
