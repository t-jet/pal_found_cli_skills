# Agent identifiers and conversation inputs

An agent RID identifies a published AIP agent. `session create --agent-rid`
creates a server session and stores its RID under the supplied local `--alias`.
Use that alias on later session, content, and trace commands. `agent-version
get` also takes a version string. Session list operations are scoped to an
agent and the calling client as described in the method records.

Continue and RAG context calls require two JSON objects. For example,
`--user-input-json '{"text":"What is the order status?"}'` supplies the user
message. `--parameter-inputs-json '{}'` is valid when the agent has no
required application variables. Otherwise use configured variable IDs as
keys; a string variable value can look like
`{"customerName":{"type":"string","value":"Titan Technologies"}}`.
Object set variables use `type: "objectSet"` and an Ontology object set
definition. Read the agent's application state configuration before choosing
variable keys.

`--contexts-override-json` is an array of explicit input contexts. Supplying
it skips automatic retrieval for that exchange. `session rag-context` can
preload context before a continue call. `session cancel --message-id` uses the
ID of an active streamed exchange, not a session RID. `session-trace get`
requires the session trace ID returned by an exchange.
