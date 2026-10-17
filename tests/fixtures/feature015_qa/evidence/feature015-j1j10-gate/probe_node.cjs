"use strict";

const assert = require("node:assert/strict");
const dns = require("node:dns");
const net = require("node:net");
const dgram = require("node:dgram");
const childProcess = require("node:child_process");
const workerThreads = require("node:worker_threads");

const cases = {
  dns: () => dns.lookup("example.com"),
  directIp: () => net.connect(443, "1.1.1.1"),
  fetch: () => fetch("https://example.com"),
  datagram: () => dgram.createSocket("udp4"),
  subprocess: () => childProcess.spawn(process.execPath, ["-e", "process.exit(0)"]),
  worker: () => new workerThreads.Worker("", { eval: true }),
};

for (const [name, invoke] of Object.entries(cases)) {
  assert.throws(invoke, /PUBLIC_NETWORK_DENIED/);
  console.log(`${name}: PUBLIC_NETWORK_DENIED`);
}
