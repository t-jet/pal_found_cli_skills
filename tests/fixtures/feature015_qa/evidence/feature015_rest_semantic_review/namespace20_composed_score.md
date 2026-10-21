# Independent score: revised isolated namespace reader pass

Frozen artifacts: `.ept/tmp/feature015_namespace_reader/composed_reports/`, `run_composed.py`, `composed_results.json`, `snapshot_manifest.json`. This is a new score. The first 20 reports and their failures remain recorded in `namespace20_initial_score.md`.

The revised runner uses only `.ept/tmp/feature015_namespace_reader/isolated-pal-found-dev`, denies DNS and socket connections, and routes calls through public v1/v2 `FoundryClient` resources. I verified all 23 outcomes report pass and all 46 referenced staged files match their SHA256 entries in the snapshot manifest. These are synthetic SDK calls, with no tenant execution.

For 19 of the 20 namespace prompts, all six local reader dimensions have observable evidence: resource/lifecycle decision, SDK version and authorization boundary, a configured public composed client call, raw decode and close, exact synthetic request/result/error assertions, and bounded recovery guidance. This is provisional local task completion for the selected one-operation prompts. It does not extend to every operation in those namespaces.

| Namespace case | Selected operation | Six-dimension result |
| --- | --- | --- |
| v1.datasets | Dataset.get | 6/6 provisional local pass |
| v1.ontologies | Attachment.get | 6/6 provisional local pass |
| v2.admin | Group.get | 6/6 provisional local pass |
| v2.aip_agents | AgentVersion.get | 6/6 provisional local pass |
| v2.audit | LogFile.list | **3/6 fail** |
| v2.checkpoints | Record.get | 6/6 provisional local pass |
| v2.connectivity | Connection.get | 6/6 provisional local pass |
| v2.data_health | Check.get | 6/6 provisional local pass |
| v2.datasets | Dataset.get | 6/6 provisional local pass |
| v2.filesystem | Folder.get | 6/6 provisional local pass |
| v2.functions | ValueType.get | 6/6 provisional local pass |
| v2.language_models | OpenAiModel.embeddings | 6/6 provisional local pass; synthetic one-input/one-vector result only |
| v2.media_sets | MediaSet.get | 6/6 provisional local pass |
| v2.models | LiveDeployment.get | 6/6 provisional local pass |
| v2.ontologies | Attachment.get | 6/6 provisional local pass |
| v2.orchestration | Build.get | 6/6 provisional local pass; reading build status does not establish committed output |
| v2.sql_queries | SqlQuery.cancel | 6/6 provisional local pass for accepted cancel request; later query outcome is separate |
| v2.streams | Stream.get_records | 6/6 provisional local pass |
| v2.third_party_applications | Website.get | 6/6 provisional local pass |
| v2.widgets | Repository.get | 6/6 provisional local pass |

`v2.audit.LogFile.list` task asks to enumerate files within a finite result budget. Its composed code calls one raw page with no `page_size`, `page_token`, `max_pages`, `max_items`, repeated-token check or completion flag. Runner returns one synthetic page and proves that call only. Capability, prerequisites and recovery guidance pass; ordered enumeration, adaptable bounded code and observable completeness fail. The named `MissingStartDate` error is exercised, but the example omits `start_date`; a real enrollment may require one. The skill has a reusable page helper; the reader did not use it.

Three extra File reports (`v1.datasets.File.get`, `v2.datasets.File.get`, `v2.datasets.File.content`) prove corrected public composed routes and one synthetic result each. They are route smoke evidence. The `v2.datasets.File.content` report uses buffered raw decoding and explicitly says strict byte limiting requires streaming; no byte-budget stream test appears here. These extra reports do not retroactively pass J11 (historical 3/6) or J12 (historical 4/6). Full 425-operation semantic acceptance and complete 14-journey QA remain separate gates.
