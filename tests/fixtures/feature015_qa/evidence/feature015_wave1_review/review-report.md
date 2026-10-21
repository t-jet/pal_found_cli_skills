# FEATURE-015 first-wave REST review

Reviewed SDK 1.101.0 against frozen source commit `168d51910570b6966afa2320333ab36f6a3f7ccf`. Local candidate was `pal_found_cli_skills` HEAD `e2518d975fb383830e0418b85e8506912102ac85` during final matrix run. No tenant or public-network request was made.

## Exact operation review

[`matrix.json`](matrix.json) contains one row for every first-wave operation, with story, contract, guide heading line, example, installed SDK source file/line, reachable model count and findings. The matrix script checks the exact approved partition, local signature, every `RequestInfo` field against the installed source, stage, public composed v1/v2 client route, guide section, named errors, and source-documented error meaning. It also checks each executable example's method and timeout. Results: 171 unique IDs, no partition difference or current matrix finding. Story counts are 071:27, 072:40, 074:52, 075:29, 077:23.

The initial matrix caught nine split-guide navigation errors: `v2.admin.Group.search`, `User.revoke_all_tokens`, `User.search`, `v2.datasets.Dataset.jobs`, `put_schema`, `read_table`, `transactions`, and `v2.orchestration.Schedule.runs`, `unpause`. Their first-page manifest paths omitted the heading in `-2.md`. The author corrected the paths; the final matrix reports zero navigation errors.

Per-ID guide explanations were read through [`semantic_summary.py`](semantic_summary.py). One source-blind v1 guidance error was found and corrected: `v1.datasets.Dataset.get_schema` described the v2 `end_transaction_rid` selector. Its current guide explains v1 `branch_id`, `transaction_rid`, and nullable result at `references/rest/v1/datasets/Dataset.md:129`.

## Composed-client probes

[`composed_cases.py`](composed_cases.py) uses the actual root `FoundryClient`/v1 `FoundryClient` and in-process `httpx.MockTransport`. Four cases passed:

- Admin group creation, denied group membership, read-only reconciliation. No membership replay.
- Dataset create/upload, transaction-view file checks, lost commit reply after server commit, transaction/branch/committed-view reconciliation, then `FAILED` build interpretation. Exactly one commit request.
- v1 Ontology `Action.validate` with typed parameters and `VALID` result. No apply request.
- Admin group raw pagination with an empty intermediate page and repeated cursor. Stops after two requests and reports incomplete result.

The author's wave test suite also passed: `518 passed in 2.72s` with `python -m pytest -q pal_found_cli_skills/tests/test_offline_rest_wave1.py`.

## Remaining reader and sign-off work

The three v1 SDK error docstrings saying `todo` are localized in the operation guides: dataset schema deletion at `references/rest/v1/datasets/Dataset.md:89`, schema replacement at line 228, and file deletion at `references/rest/v1/datasets/File.md:90`. Their shared local error-parameter model pages still open with `todo` at `references/rest/models/v1/datasets/errors/DeleteSchemaPermissionDeniedParameters.md:4` and `PutSchemaPermissionDeniedParameters.md:4`. Add an explicit bounded note or operation links outside the exact copied SDK definition. `PutSchemaPermissionDenied` occurs in two different operations; its shared page must not claim one universal missing grant.

The first wave reaches 1,092 distinct model/error symbols. All resolve to local pages, but all 1,092 remain `semantic_review_status: unreviewed` in `maintainer/rest-model-register.json`. Source/API parity and fixture success do not approve their field/union/constraint explanations. Independent model reconciliation and fresh source-blind J11/J12 reader checks remain acceptance gates. Keep BUG-SUB-024 and BUG-SUB-025 failed artifacts as historical evidence until those reruns pass. These fixtures establish SDK behavior only for their synthetic cases; tenant grants and live execution were not tested.
