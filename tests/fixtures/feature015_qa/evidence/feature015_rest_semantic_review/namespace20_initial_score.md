# Independent score: first 20 namespace reader submissions

Frozen submissions: `.ept/tmp/feature015_namespace_reader/v1_*.md`, `v2_*.md`, `case_results.json`, `run_cases.py`. Prompt: `pal_found_cli_skills/tests/fixtures/offline/rest-acceptance/prompts.json`. Rubric: six dimensions in `reader_coverage.json`. This score applies to the first 28-line reports only; any revised reader run needs a separate score.

The runner blocked socket connect and DNS and all 20 per-operation fixtures exited zero. It ran fixtures from the mutable authoring tree (`run_cases.py:ROOT / "pal_found_cli_skills/.agents/skills/pal-found-dev"`), not an isolated staged copy. Each report's code is a direct resource-client `def invoke(client)` calling `with_raw_response`; none shows the public composed `FoundryClient` route, `raw.decode()`, `raw.close()` or an application result assertion. The linked fixtures do those operations internally, but a user cannot paste the report's code into a configured root client and finish the stated task. The reports do not order the result/lifetime steps. Thus each lacks the procedure and adaptable-code dimensions. Fixture output supplies an observable synthetic operation check for simple reads, but not a combined or live outcome.

| Namespace | Selected operation | Capability | Prerequisites | Procedure | Adaptable code | Success check | Recovery | Score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| v1.datasets | Dataset.get | P | P | F | F | P | P | 4/6 |
| v1.ontologies | Attachment.get | P | P | F | F | P | P | 4/6 |
| v2.admin | Group.get | P | P | F | F | P | P | 4/6 |
| v2.aip_agents | AgentVersion.get | P | P | F | F | P | P | 4/6 |
| v2.audit | LogFile.list | P | P | F | F | F | P | 3/6 |
| v2.checkpoints | Record.get | P | P | F | F | P | P | 4/6 |
| v2.connectivity | Connection.get | P | P | F | F | P | P | 4/6 |
| v2.data_health | Check.get | P | P | F | F | P | P | 4/6 |
| v2.datasets | Dataset.get | P | P | F | F | P | P | 4/6 |
| v2.filesystem | Folder.get | P | P | F | F | P | P | 4/6 |
| v2.functions | ValueType.get | P | P | F | F | P | P | 4/6 |
| v2.language_models | OpenAiModel.embeddings | P | P | F | F | P | P | 4/6 |
| v2.media_sets | MediaSet.get | P | P | F | F | P | P | 4/6 |
| v2.models | LiveDeployment.get | P | P | F | F | P | P | 4/6 |
| v2.ontologies | Attachment.get | P | P | F | F | P | P | 4/6 |
| v2.orchestration | Build.get | P | P | F | F | P | P | 4/6 |
| v2.sql_queries | SqlQuery.cancel | P | P | F | F | F | P | 3/6 |
| v2.streams | Stream.get_records | P | P | F | F | P | P | 4/6 |
| v2.third_party_applications | Website.get | P | P | F | F | P | P | 4/6 |
| v2.widgets | Repository.get | P | P | F | F | P | P | 4/6 |

For audit, the fixture calls one raw page without a finite page/item budget, repeated-token rejection or an end-to-end completeness assertion. It therefore does not establish the prompt's bounded enumeration. For SQL cancel, a 204/raw response proves the cancellation request was accepted; the report explicitly says that does not prove a downstream result, and supplies no state read to establish cancellation outcome. Recovery prose states bounded diagnosis and access boundaries, so that dimension passes as guidance even though runnable recovery code is absent. This result demonstrates 20 local method examples, not 20 complete reader tasks and not all 425 operations.
