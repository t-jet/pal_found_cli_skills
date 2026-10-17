import assert from "node:assert/strict";
import { viewState } from "./view_state.mjs";

const cases = [
  [{ isLoading: true }, { kind: "loading", canSubmit: false }],
  [{ error: new Error("denied"), data: [1], isLoading: false }, { kind: "error", canSubmit: false }],
  [{ data: [], isLoading: false }, { kind: "empty", canSubmit: false }],
  [{ data: [{ todoId: "t1" }], isLoading: true }, { kind: "refreshing", canSubmit: true }],
  [{ data: [{ todoId: "t1" }], isLoading: false, isPending: true }, { kind: "ready", canSubmit: false }],
];
for (const [input, output] of cases) assert.deepEqual(viewState(input), output);
console.log("UI fixtures passed: loading, denied, empty, retained-data refresh and pending submission");
console.log("No React hook, OAuth grant, Action or website deployment executed");
