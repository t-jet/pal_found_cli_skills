"use strict";

const dns = require("node:dns");
const net = require("node:net");
const tls = require("node:tls");
const http = require("node:http");
const https = require("node:https");
const dgram = require("node:dgram");
const childProcess = require("node:child_process");
const workerThreads = require("node:worker_threads");

function deny() {
  throw new Error("PUBLIC_NETWORK_DENIED");
}

for (const name of ["lookup", "resolve", "resolve4", "resolve6"]) {
  dns[name] = deny;
}
net.Socket.prototype.connect = deny;
net.connect = deny;
net.createConnection = deny;
tls.connect = deny;
http.request = deny;
http.get = deny;
https.request = deny;
https.get = deny;
globalThis.fetch = deny;
if (typeof globalThis.WebSocket === "function") globalThis.WebSocket = deny;
dgram.createSocket = deny;
for (const name of ["spawn", "spawnSync", "exec", "execSync", "execFile", "execFileSync", "fork"]) {
  childProcess[name] = deny;
}
workerThreads.Worker = deny;
