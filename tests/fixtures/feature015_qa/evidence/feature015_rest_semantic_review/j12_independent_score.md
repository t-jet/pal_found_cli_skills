# Independent J12 reader score

Submission: `.ept/tmp/feature015-j12-reader/reader-results.md`. Rubric: six dimensions in `reader_coverage.json`. Reviewed after the reader submitted its answer. SDK 1.101.0 composed client paths and signatures checked with installed runtime. No combined workflow was executed.

| Dimension | Result | Evidence and limit |
| --- | --- | --- |
| Capability and lifecycle | Pass | Correctly separates open transaction, explicit staged file upload, commit or abort, and independently known build RID. Source routes resolve as `client.datasets.Dataset.Transaction`, `client.datasets.Dataset.File`, `client.orchestration.Build`. |
| Prerequisites, version, identity and access | Pass | SDK 1.101.0, dataset/branch/file, identity, resource grants, enrollment versus synthetic transport, and finite budgets are stated. |
| Ordered procedure | Pass with gap | Prose orders create, stage, inspect, commit, verify and bounded build lookup. Code omits the promised staged-file inspection; that affects executable example and checks below. |
| Adaptable example inputs and results | Fail | Code has valid installed signatures for create/upload/get/commit/build-get, but `# Verify the staged file view and intended content before this mutation.` is a placeholder. It never calls `File.get`/`content` for the staged view. It uses `<known-build-rid>`, which cannot pass RID validation without replacement; explicitly labeled adaptation skeleton. Six separate resource fixtures do not exercise composition. |
| Observable success checks | Fail | `COMMITTED` status checks do not verify expected file content/visibility on the intended branch. The code does not assert the staged bytes before commit or the resulting file after commit. It checks build terminal status but leaves the caller to distinguish successful `SUCCEEDED` from `FAILED`/`CANCELED`; prose makes that distinction. |
| Bounded failure and recovery | Pass with gap | Text explains upload/commit uncertainty, status reconciliation, permission/missing/invalid states, and finite build polling. Code does not implement the timeout branches; reader labels skeleton, so this dimension passes as a documented recovery decision, not runnable recovery. |

Result: 4 clear passes, 2 fails; J12 combined workflow remains unproven. Six isolated SDK fixtures exited zero but prove only each method's synthetic request/result/error handling. The reader explicitly disclosed that public-network denial was instructed but not instrumented, so no claim of enforced offline runtime follows from its run.
