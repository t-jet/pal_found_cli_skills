// Prepared local state for J7/J8 reader tasks. No Foundry request runs here.
import { join } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const defaultSkill = fileURLToPath(new URL("../../../.agents/skills/pal-found-dev/", import.meta.url));
const skillRoot = process.env.FEATURE015_SKILL_ROOT ?? defaultSkill;
const eventsUrl = pathToFileURL(join(skillRoot, "examples/widgets/events.mjs")).href;
const { fixtureHostUpdate } = await import(eventsUrl);

function denied(code) {
  return Object.assign(new Error(code), { code });
}

export function createTodoEnvironment() {
  const callback = "http://localhost:8080/auth/callback";
  const origin = "http://localhost:8080";
  const requiredRead = "api:use-ontologies-read";
  const requiredWrite = "api:use-ontologies-write";
  const grants = {
    alice: new Set([requiredRead, requiredWrite]),
    bob: new Set([requiredRead]),
  };
  const rows = new Map([["todo-1", { todoId: "todo-1", status: "OPEN" }]]);
  const calls = [];

  function signIn({ user, redirectUri, scopes }) {
    calls.push({ kind: "sign-in", user });
    if (redirectUri !== callback) throw denied("CALLBACK_MISMATCH");
    if (!grants[user]) throw denied("APPLICATION_GRANT_DENIED");
    if (!Array.isArray(scopes) || !scopes.includes(requiredRead)) {
      throw denied("READ_SCOPE_MISSING");
    }
    if (scopes.some((scope) => !grants[user].has(scope))) {
      throw denied("SCOPE_DENIED");
    }
    return { user, scopes: new Set(scopes) };
  }

  function queryIncomplete(session) {
    calls.push({ kind: "query", user: session?.user ?? null });
    if (!session?.scopes.has(requiredRead)) throw denied("READ_DENIED");
    return [...rows.values()].filter((row) => row.status === "OPEN").map((row) => ({ ...row }));
  }

  function complete(session, todoId, { loseReply = false } = {}) {
    calls.push({ kind: "action", user: session?.user ?? null, todoId });
    if (!session?.scopes.has(requiredWrite)) throw denied("ACTION_DENIED");
    const row = rows.get(todoId);
    if (!row) throw denied("TODO_NOT_FOUND");
    row.status = "DONE";
    if (loseReply) throw denied("RESPONSE_TIMEOUT_EFFECT_UNKNOWN");
    return { todoId, status: "DONE" };
  }

  const preview = { kind: "local-preview", version: "working-tree" };
  const deployed = { kind: "website-release", version: "1.1.0", asset: "todo-app.1.1.0.js" };
  return { callback, origin, requiredRead, requiredWrite, signIn, queryIncomplete,
    complete, preview, deployed, calls };
}

export function createWorkshopEnvironment() {
  let host = { count: 0, selectedRelease: "1.1.0" };
  const releases = new Map([
    ["1.0.0", { asset: "counter.1.0.0.js", widgets: ["reviewCounter"] }],
    ["1.1.0", { asset: "counter.1.1.0.js", widgets: ["reviewCounter", "reviewSummary"] }],
  ]);
  const trace = [];

  function hostSetCount(value) {
    if (!Number.isFinite(value)) throw denied("INVALID_HOST_PARAMETER");
    host = { ...host, count: value };
    trace.push({ kind: "host-parameter", count: value });
    return render();
  }

  function render() {
    const release = releases.get(host.selectedRelease);
    return { version: host.selectedRelease, asset: release.asset,
      reviewCounter: host.count,
      reviewSummary: release.widgets.includes("reviewSummary") ? host.count : null };
  }

  function emit(eventId, payload) {
    host = fixtureHostUpdate(host, eventId, payload);
    trace.push({ kind: "widget-event", eventId, count: host.count });
    return render();
  }

  function selectRelease(version) {
    if (!releases.has(version)) throw denied("RELEASE_NOT_FOUND");
    host = { ...host, selectedRelease: version };
    trace.push({ kind: "host-release", version });
    return render();
  }

  return { hostSetCount, render, emit, selectRelease, trace };
}
