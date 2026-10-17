import assert from "node:assert/strict";
import { createTodoEnvironment, createWorkshopEnvironment } from "../../j7_j8_prepared_runtime.mjs";

const results = [];
function record(id, actual) { results.push({ id, status: "PASS", actual }); }
function expectCode(fn, code) {
  assert.throws(fn, (error) => error.code === code);
  return code;
}

// J7-4: registration values and grants must be checked before querying.
const todo = createTodoEnvironment();
const appConfig = {
  callback: todo.callback,
  origin: todo.origin,
  scopes: [todo.requiredRead, todo.requiredWrite],
  generatedType: "Todo",
  generatedAction: "completeTodo",
};
assert.equal(appConfig.callback, "http://localhost:8080/auth/callback");
assert.equal(appConfig.origin, "http://localhost:8080");
const callbackError = expectCode(() => todo.signIn({
  user: "alice", redirectUri: "http://localhost:8080/wrong", scopes: appConfig.scopes,
}), "CALLBACK_MISMATCH");
const grantError = expectCode(() => todo.signIn({
  user: "stranger", redirectUri: appConfig.callback, scopes: appConfig.scopes,
}), "APPLICATION_GRANT_DENIED");
const missingReadError = expectCode(() => todo.signIn({
  user: "alice", redirectUri: appConfig.callback, scopes: [todo.requiredWrite],
}), "READ_SCOPE_MISSING");
const deniedWriteError = expectCode(() => todo.signIn({
  user: "bob", redirectUri: appConfig.callback, scopes: appConfig.scopes,
}), "SCOPE_DENIED");
assert.equal(todo.calls.filter((call) => call.kind === "query" || call.kind === "action").length, 0);
const bob = todo.signIn({ user: "bob", redirectUri: appConfig.callback, scopes: [todo.requiredRead] });
assert.deepEqual(todo.queryIncomplete(bob), [{ todoId: "todo-1", status: "OPEN" }]);
const bobActionError = expectCode(() => todo.complete(bob, "todo-1"), "ACTION_DENIED");
record("J7-4", { appConfig, callbackError, grantError, missingReadError,
  deniedWriteError, bobActionError, preQueryActionCalls: 0,
  bobReadRows: 1 });

// J7-5: a lost response says nothing about whether the Action committed.
const alice = todo.signIn({ user: "alice", redirectUri: appConfig.callback, scopes: appConfig.scopes });
const before = todo.queryIncomplete(alice);
assert.equal(before.length, 1);
const lostReply = expectCode(() => todo.complete(alice, "todo-1", { loseReply: true }),
  "RESPONSE_TIMEOUT_EFFECT_UNKNOWN");
const after = todo.queryIncomplete(alice);
assert.deepEqual(after, []);
assert.equal(todo.calls.filter((call) => call.kind === "action" && call.user === "alice").length, 1);
assert.equal(todo.preview.kind, "local-preview");
assert.equal(todo.deployed.kind, "website-release");
assert.notEqual(todo.preview.version, todo.deployed.version);
const deployedDenied = expectCode(() => todo.signIn({
  user: "stranger", redirectUri: appConfig.callback, scopes: appConfig.scopes,
}), "APPLICATION_GRANT_DENIED");
record("J7-5", { before, lostReply, authorizedReread: after,
  replayCount: 0, aliceActionCalls: 1, preview: todo.preview,
  deployed: todo.deployed, deployedDenied });

// J8-4: host variable enters both widgets; event updates host variable.
const workshop = createWorkshopEnvironment();
const atZero = workshop.hostSetCount(0);
const atFive = workshop.hostSetCount(5);
assert.equal(atZero.reviewCounter, 0);
assert.equal(atZero.reviewSummary, 0);
assert.equal(atFive.reviewCounter, 5);
assert.equal(atFive.reviewSummary, 5);
const afterEvent = workshop.emit("countChanged", { parameterUpdates: { count: 6 } });
assert.equal(afterEvent.reviewCounter, 6);
assert.equal(afterEvent.reviewSummary, 6);
const wrongType = expectCode(() => workshop.emit("countChanged", {
  parameterUpdates: { count: "seven" },
}), "INVALID_HOST_COUNT");
assert.deepEqual(workshop.render(), afterEvent);
record("J8-4", { atZero, atFive, eventPayload: { parameterUpdates: { count: 6 } },
  afterEvent, wrongType, afterRejectedEvent: workshop.render(), trace: workshop.trace });

// J8-5: host selection changes rendered assets, without reversing data edits.
const prior = workshop.render();
assert.equal(prior.version, "1.1.0");
assert.equal(prior.asset, "counter.1.1.0.js");
const selected = workshop.selectRelease("1.0.0");
assert.equal(selected.version, "1.0.0");
assert.equal(selected.asset, "counter.1.0.0.js");
assert.equal(selected.reviewCounter, 6);
assert.equal(selected.reviewSummary, null);
const eventOnPrior = workshop.emit("countChanged", { parameterUpdates: { count: 7 } });
assert.equal(eventOnPrior.reviewCounter, 7);
assert.equal(eventOnPrior.reviewSummary, null);
record("J8-5", { prior, selected, eventOnPrior, hostSelectedVersion: workshop.render().version,
  retainedHostCount: 7, previousDataEditsUndone: false });

console.log(JSON.stringify({ runtime: "synthetic prepared state; no Foundry requests",
  publicNetworkProbe: "node --require deny_public.cjs preloaded", cases: results }, null, 2));
