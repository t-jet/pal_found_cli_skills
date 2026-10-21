import assert from "node:assert/strict";
import { createTimedFetch } from "./timeout.mjs";

// Injected transport exercises cancellation without opening a socket.
const observed = [];
const pendingTransport = (_input, init) => new Promise((_resolve, reject) => {
  observed.push(init.signal);
  init.signal.addEventListener("abort", () => reject(init.signal.reason), { once: true });
});

assert.throws(() => createTimedFetch(0), RangeError);
assert.throws(() => createTimedFetch(120001), RangeError);

await assert.rejects(
  createTimedFetch(10, pendingTransport)("https://example.invalid/stall"),
  { name: "TimeoutError" },
);
assert.equal(observed[0].aborted, true);

const caller = new AbortController();
const canceled = createTimedFetch(1000, pendingTransport)(
  "https://example.invalid/cancel", { signal: caller.signal },
);
caller.abort(new DOMException("Canceled", "AbortError"));
await assert.rejects(canceled, { name: "AbortError" });
assert.equal(observed[1].aborted, true);

const transportError = new Error("transport failed");
await assert.rejects(
  createTimedFetch(100, async () => { throw transportError; })("https://example.invalid/error"),
  error => error === transportError,
);

const successfulSignals = [];
const immediateTransport = async (_input, init) => {
  successfulSignals.push(init.signal);
  return new Response('{"ok":true}', { status: 200, headers: { "Content-Type": "application/json" } });
};
const timedFetch = createTimedFetch(20, immediateTransport);
assert.deepEqual(await (await timedFetch("https://example.invalid/first")).json(), { ok: true });
await new Promise(resolve => setTimeout(resolve, 30));
assert.equal(successfulSignals[0].aborted, false, "success clears deadline timer");
assert.deepEqual(await (await timedFetch("https://example.invalid/again")).json(), { ok: true });
console.log("PASS network-free timeout, caller abort, transport error, timer cleanup and recovery");
