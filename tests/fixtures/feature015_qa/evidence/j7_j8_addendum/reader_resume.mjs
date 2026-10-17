import assert from "node:assert/strict";
import dns from "node:dns";
import net from "node:net";
import dgram from "node:dgram";
import { createTodoEnvironment, createWorkshopEnvironment } from "../../j7_j8_prepared_runtime.mjs";

const denied = () => { throw new Error("PUBLIC_NETWORK_DENIED"); };
globalThis.fetch = denied;
dns.lookup = denied;
dns.promises.lookup = denied;
net.connect = denied;
net.createConnection = denied;
dgram.createSocket = denied;
assert.throws(() => fetch("https://www.palantir.com"), /PUBLIC_NETWORK_DENIED/);
assert.throws(() => dns.lookup("www.palantir.com"), /PUBLIC_NETWORK_DENIED/);
assert.throws(() => net.connect(443, "www.palantir.com"), /PUBLIC_NETWORK_DENIED/);

function expectCode(fn, code) {
  assert.throws(fn, (error) => error?.code === code);
  return code;
}

const todo = createTodoEnvironment();
const app = {
  clientKind: "public OAuth authorization-code client",
  callback: todo.callback,
  origin: todo.origin,
  scopes: [todo.requiredRead, todo.requiredWrite],
  ontologyBinding: "prepared generated Todo and completeTodo exports",
};
const loginFailures = {
  callback: expectCode(() => todo.signIn({ user: "alice", redirectUri: "http://localhost:8080/wrong", scopes: app.scopes }), "CALLBACK_MISMATCH"),
  applicationGrant: expectCode(() => todo.signIn({ user: "stranger", redirectUri: app.callback, scopes: app.scopes }), "APPLICATION_GRANT_DENIED"),
  missingReadScope: expectCode(() => todo.signIn({ user: "alice", redirectUri: app.callback, scopes: [todo.requiredWrite] }), "READ_SCOPE_MISSING"),
  deniedWriteScope: expectCode(() => todo.signIn({ user: "bob", redirectUri: app.callback, scopes: app.scopes }), "SCOPE_DENIED"),
};
assert.equal(todo.calls.filter((call) => ["query", "action"].includes(call.kind)).length, 0);
const bob = todo.signIn({ user: "bob", redirectUri: app.callback, scopes: [todo.requiredRead] });
const bobRows = todo.queryIncomplete(bob);
assert.deepEqual(bobRows, [{ todoId: "todo-1", status: "OPEN" }]);
const deniedAction = expectCode(() => todo.complete(bob, "todo-1"), "ACTION_DENIED");
const alice = todo.signIn({ user: "alice", redirectUri: app.callback, scopes: app.scopes });
const initialRows = todo.queryIncomplete(alice);
assert.equal(initialRows.length, 1);
const confirmed = todo.complete(alice, "todo-1");
assert.deepEqual(confirmed, { todoId: "todo-1", status: "DONE" });
const afterConfirmed = todo.queryIncomplete(alice);
assert.deepEqual(afterConfirmed, []);
const uncertain = createTodoEnvironment();
const authorized = uncertain.signIn({ user: "alice", redirectUri: uncertain.callback,
  scopes: [uncertain.requiredRead, uncertain.requiredWrite] });
const beforeUncertain = uncertain.queryIncomplete(authorized);
assert.equal(beforeUncertain.length, 1);
const lostReply = expectCode(() => uncertain.complete(authorized, "todo-1", { loseReply: true }), "RESPONSE_TIMEOUT_EFFECT_UNKNOWN");
const reread = uncertain.queryIncomplete(authorized);
assert.deepEqual(reread, []);
assert.equal(uncertain.calls.filter((call) => call.kind === "action").length, 1);
assert.deepEqual(todo.preview, { kind: "local-preview", version: "working-tree" });
assert.deepEqual(todo.deployed, { kind: "website-release", version: "1.1.0", asset: "todo-app.1.1.0.js" });

const workshop = createWorkshopEnvironment();
const host0 = workshop.hostSetCount(0);
const host5 = workshop.hostSetCount(5);
assert.equal(host5.reviewCounter, 5);
assert.equal(host5.reviewSummary, 5);
const afterEvent = workshop.emit("countChanged", { parameterUpdates: { count: 6 } });
assert.equal(afterEvent.reviewCounter, 6);
assert.equal(afterEvent.reviewSummary, 6);
const traceBeforeBad = structuredClone(workshop.trace);
const rejectedType = (() => {
  try { workshop.emit("countChanged", { parameterUpdates: { count: "seven" } }); }
  catch (error) { return error.name + ": " + error.message; }
  throw new Error("wrong-type event was accepted");
})();
assert.deepEqual(workshop.render(), afterEvent);
assert.deepEqual(workshop.trace, traceBeforeBad);
const afterRejected = workshop.render();
const rollback = workshop.selectRelease("1.0.0");
assert.deepEqual(rollback, { version: "1.0.0", asset: "counter.1.0.0.js", reviewCounter: 6, reviewSummary: null });
const rollbackEvent = workshop.emit("countChanged", { parameterUpdates: { count: 7 } });
assert.equal(rollbackEvent.reviewCounter, 7);
assert.equal(rollbackEvent.reviewSummary, null);

const output = {
  mode: "synthetic prepared runtime only; no Foundry tenant request",
  networkProbe: "fetch, DNS, TCP and UDP entry points denied in this Node process",
  cases: {
    "J7-4": { app, loginFailures, preQueryActionCalls: 0, bobRows, deniedAction },
    "J7-5": { initialRows, confirmed, afterConfirmed, lostReply, reread,
      uncertainActionCount: 1, preview: todo.preview, deployed: todo.deployed },
    "J8-4": { host0, host5, afterEvent, rejectedType, afterRejected,
      traceBeforeBad },
    "J8-5": { rollback, rollbackEvent, selectedRelease: rollbackEvent.version },
  },
};
console.log(JSON.stringify(output, null, 2));
