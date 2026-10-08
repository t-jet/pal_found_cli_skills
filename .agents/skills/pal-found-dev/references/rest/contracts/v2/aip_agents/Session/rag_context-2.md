# v2.aip_agents.Session.rag_context: continuation 2


## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/aip_agents/Session.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

## Local background for referenced concepts

- RAG context comes from data sources configured for the session; inspect retrieved context before a continuation override. [Local procedure](../../../../v2/aip_agents/Session.md).
- An Agent has a RID and published versions. Select an accessible version before opening a conversation session. [Local procedure](../../../../v2/aip_agents/Agent.md).
- Ontology object types define the records and properties an Agent or application can access; check the caller's visibility. [Local procedure](../../../../../ontology/modeling.md).

[Part 1](rag_context.md) | [Part 2](rag_context-2.md)
