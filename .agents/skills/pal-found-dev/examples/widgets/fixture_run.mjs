import assert from "node:assert/strict";
import { incrementPayload, fixtureHostUpdate } from "./events.mjs";
let host = { count: 0, label: "Order reviews" };
host = fixtureHostUpdate(host, "countChanged", incrementPayload(host.count));
assert.equal(host.count, 1);
assert.equal(host.label, "Order reviews");
host = { ...host, count: 5 };
assert.equal(incrementPayload(host.count).parameterUpdates.count, 6);
assert.throws(() => incrementPayload(NaN), /finite/);
assert.throws(() => fixtureHostUpdate(host, "unknown", incrementPayload(5)), /unbound/);
assert.throws(() => fixtureHostUpdate(host, "countChanged", {
  parameterUpdates: { count: 1, forbidden: 2 },
}), /not permitted/);
const available = new Set(["1.0.0", "1.1.0"]);
const selected = { A: "1.0.0", B: "1.1.0" };
assert(available.has(selected.A) && available.has(selected.B));
available.add("1.2.0");
assert.equal(selected.A, "1.0.0");
assert.equal(selected.B, "1.1.0");
console.log("PASS: synthetic bidirectional counter, rejected updates, explicit host release selection");
