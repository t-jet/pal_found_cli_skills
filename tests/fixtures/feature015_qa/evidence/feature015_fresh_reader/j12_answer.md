# J12 source-blind reader answer

## Capability and lifecycle

Use v2 `client.datasets.Dataset.Transaction` for an explicit open transaction, `client.datasets.Dataset.File` to stage and read the file, and `client.datasets.Dataset.Branch` to confirm the committed pointer. Use `client.orchestration.Build.get` only for a separately recorded submitted Build RID. A committed transaction does not imply that a Build was submitted. `RUNNING` is pending; `SUCCEEDED`, `FAILED` and `CANCELED` are terminal, with only `SUCCEEDED` meeting a successful build outcome.

## Prerequisites, version and identity

The prepared SDK and installed distribution are 1.101.0. The fixture supplies a synthetic dataset RID, branch `feature-offline`, file path, payload, transaction RID and recorded Build RID. The client uses v2 `FoundryClient`, `UserTokenAuth`, one SDK attempt, propagated QoS errors, and positive request timeouts. Live work needs authorized enrollment connectivity, exact dataset/branch identities, write grants, file schema and Build access. Build capability and access are distinct from dataset write permission.

## Ordered steps and example

1. Create an `APPEND` transaction on the selected branch and retain its returned RID and `OPEN` status.
2. Upload bytes with `application/octet-stream` and `transaction_rid=tx.rid`. Inspect staged metadata and bytes with `start_transaction_rid=end_transaction_rid=tx.rid`; a branch read before commit would inspect a different view.
3. Commit only the confirmed open transaction. Read `Transaction.get` for `COMMITTED`, then `Branch.get` for the same transaction RID. Read file metadata and bytes on the explicit branch to verify visibility.
4. Abort only a confirmed `OPEN` transaction when choosing to discard staging. Check that `Transaction.get` reports `ABORTED` afterward.
5. For the separately known Build RID, call `Build.get` with a two-poll budget and at least 250 ms between requests, respecting its four-per-second limit. Record `RUNNING` as pending after exhaustion. Preserve the RID for a later authorized status check.

Runnable code: [j12_reader.py](j12_reader.py). Its MockTransport asserts public composed routes, query selectors, JSON/binary bodies, authorization and result transitions. Output: [j12_output.json](j12_output.json).

## Observable results

The fixture passed seven cases: successful build, failed build, canceled build, still-running build after two polls, upload response timeout, commit response timeout, and abort of an open transaction. Every write case records its mutation sequence. The upload and commit timeout cases each issue their mutation once. The status budget returns `pending-budget` for `RUNNING`; it never reports success. DNS and socket connections were patched to fail, so this proves only synthetic SDK behavior.

## Failure and recovery

After an upload timeout, retain the known transaction RID, read its state and inspect the same transaction's staged file and bytes. If presence or content cannot be established, stop with an uncertain upload and involve the owner; do not upload blindly. After a commit timeout, read that transaction and the branch pointer. If both show the committed RID, continue with branch file checks; otherwise retain uncertainty and reconcile before any further mutation. Abort only an open transaction; an abort request or lost reply needs another state read. A failed or canceled Build requires recorded status and job diagnosis before correction or a new authorized submission. A running Build after the finite budget remains pending; read the same RID later rather than creating a duplicate. Permission, missing-resource and throttling failures require identity/target checks or finite retry decisions, not automatic write replay.

## Access boundary and exact local headings read

Local authoring and the synthetic run need the preprovisioned SDK and fixtures. Real create, upload, commit, abort, Build submission and status checks need authorized enrollment connectivity, resource access and any capability enablement. This fixture is not tenant execution or self-approval.

- `SKILL.md`: `Develop on Foundry`; `Choose a development path`; `Read by task`; `Evidence before delivery`.
- `references/rest-api.md`: `Discover and author any frozen SDK REST operation`; `Concept and lifecycle`; `Prerequisites`; `Procedure`; `Expected result and checks`; `Failures and recovery`; `Access boundary`.
- `references/rest/catalog.md`: `Services`; `Task selection`.
- `references/rest/authentication.md`: `Credentials and acting identity`; `Prepared client`.
- `references/rest/client-behavior.md`: `Client and API version`; `Response modes`; `Serialization and local types`; `Timeouts, throttling and uncertain writes`; `Errors and cleanup`.
- `references/rest/v2/datasets/Transaction.md`: `Capability and lifecycle`; `Prepare the application`; `Operations and outcome checks`; `Stage a file, commit, and verify the branch`; `abort`; `commit`; `create`; `get`.
- `references/rest/v2/datasets/File.md`: `Capability and lifecycle`; `Prepare the application`; `Client route and bounded content read`; `content`; `get`; `upload`.
- `references/rest/v2/orchestration/Build.md`: `Capability and lifecycle`; `Prepare the application`; `Operations and outcome checks`; `Wait for a submitted build`; `get`.
- `references/rest/contracts/v2/datasets/Transaction/{create,commit,get,abort}.md`, `references/rest/contracts/v2/datasets/File/upload.md`, `references/rest/contracts/v2/orchestration/Build/get.md`: `Purpose and parameter meaning`; `Public Python client route`; `SDK invocation contract`; `Parameters and defaults`; `Documented operation errors`; `Wire request`; `Response modes`; `Complete referenced models and errors`; `Identity and execution boundary`; `Application workflow`.
- `examples/rest/074/v2/datasets/staged_commit_journey.py`: local executable SDK fixture pattern.
