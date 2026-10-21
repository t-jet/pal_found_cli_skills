import assert from "node:assert/strict";
import { incrementPayload } from "../../../.agents/skills/pal-found-dev/examples/widgets/events.mjs";
import { createTodoEnvironment, createWorkshopEnvironment } from "./j7_j8_prepared_runtime.mjs";

const auth = createTodoEnvironment();
const scopes = [auth.requiredRead, auth.requiredWrite];
assert.throws(() => auth.signIn({ user: "alice", redirectUri: "/wrong", scopes }),
  { code: "CALLBACK_MISMATCH" });
assert.throws(() => auth.signIn({ user: "blocked", redirectUri: auth.callback, scopes }),
  { code: "APPLICATION_GRANT_DENIED" });
assert.throws(() => auth.signIn({ user: "bob", redirectUri: auth.callback, scopes }),
  { code: "SCOPE_DENIED" });
assert.equal(auth.calls.filter((call) => call.kind === "query").length, 0);

const reader = auth.signIn({ user: "bob", redirectUri: auth.callback,
  scopes: [auth.requiredRead] });
assert.deepEqual(auth.queryIncomplete(reader), [{ todoId: "todo-1", status: "OPEN" }]);
assert.throws(() => auth.complete(reader, "todo-1"), { code: "ACTION_DENIED" });
const writer = auth.signIn({ user: "alice", redirectUri: auth.callback, scopes });
assert.throws(() => auth.complete(writer, "todo-1", { loseReply: true }),
  { code: "RESPONSE_TIMEOUT_EFFECT_UNKNOWN" });
assert.deepEqual(auth.queryIncomplete(writer), []);
assert.equal(auth.calls.filter((call) => call.kind === "action").length, 2);
assert.notEqual(auth.preview.version, auth.deployed.version);

const host = createWorkshopEnvironment();
assert.equal(host.render().reviewCounter, 0);
assert.equal(host.hostSetCount(5).reviewCounter, 5);
const afterEvent = host.emit("countChanged", incrementPayload(5));
assert.equal(afterEvent.reviewCounter, 6);
assert.equal(afterEvent.reviewSummary, 6);
assert.throws(() => host.emit("countChanged", { parameterUpdates: { count: "6" } }),
  { name: "TypeError" });
assert.equal(host.render().reviewCounter, 6);
const old = host.selectRelease("1.0.0");
assert.equal(old.version, "1.0.0");
assert.equal(old.asset, "counter.1.0.0.js");
assert.equal(old.reviewCounter, 6);
assert.equal(old.reviewSummary, null);
assert.deepEqual(host.trace.map((entry) => entry.kind),
  ["host-parameter", "widget-event", "host-release"]);
console.log("PASS J7/J8 prepared local auth, Action reconciliation, host roundtrip and release selection");
