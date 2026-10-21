import assert from "node:assert/strict";
import http from "node:http";
import { createTimedFetch } from "./timeout.mjs";

// Actual local HTTP/fetch abort exercise; no Foundry or public network involved.
let abortedConnections = 0;
const server = http.createServer((request, response) => {
  request.on("aborted", () => { abortedConnections++; });
  if (request.url === "/ok") {
    response.writeHead(200, { "Content-Type": "application/json" });
    response.end('{"ok":true}');
  } else if (request.url === "/denied") {
    response.writeHead(403); response.end("denied");
  } else if (request.url === "/body") {
    response.writeHead(200); response.write("partial");
  } // /headers waits without sending response headers.
});
await new Promise(resolve => server.listen(0, "127.0.0.1", resolve));
const base = `http://127.0.0.1:${server.address().port}`;
try {
  assert.throws(() => createTimedFetch(0), RangeError);
  assert.throws(() => createTimedFetch(120001), RangeError);
  assert.deepEqual(await (await createTimedFetch(1000)(`${base}/ok`)).json(), { ok: true });
  assert.equal((await createTimedFetch(1000)(`${base}/denied`)).status, 403);
  for (const route of ["headers", "body"]) {
    const started = performance.now();
    await assert.rejects(createTimedFetch(60)(`${base}/${route}`), { name: "TimeoutError" });
    assert.ok(performance.now() - started < 1000, "Deadline should abort the HTTP request");
  }
  const caller = new AbortController();
  const pending = createTimedFetch(1000)(`${base}/headers`, { signal: caller.signal });
  setTimeout(() => caller.abort(new DOMException("Canceled", "AbortError")), 20);
  await assert.rejects(pending, { name: "AbortError" });
  await new Promise(resolve => setTimeout(resolve, 30));
  assert.ok(abortedConnections >= 2, "Server should observe real canceled connections");
  // Successful request still works after timeout/cancellation: no shared poisoned signal.
  assert.equal((await createTimedFetch(1000)(`${base}/ok`)).status, 200);
  console.log(`PASS actual local HTTP: deadline before headers, during body, caller cancellation, 403 preservation, recovery; canceledConnections=${abortedConnections}`);
} finally {
  server.closeAllConnections();
  await new Promise(resolve => server.close(resolve));
}
