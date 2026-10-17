import assert from "node:assert/strict";

export function highValueSummary(orders, minimum) {
  const selected = orders.filter(row => typeof row.totalCents === "number" && row.totalCents >= minimum);
  const counts = {};
  for (const row of selected) counts[row.customerId] = (counts[row.customerId] ?? 0) + 1;
  return { ids: selected.map(row => row.orderId), counts };
}

const orders = [
  { orderId: "o1", customerId: "c1", totalCents: 1200 },
  { orderId: "o2", customerId: "c1", totalCents: 500 },
  { orderId: "o3", customerId: "c2", totalCents: 2000 },
  { orderId: "o4", customerId: "c1", totalCents: null },
];
assert.deepEqual(highValueSummary(orders, 1000), { ids: ["o1", "o3"], counts: { c1: 1, c2: 1 } });
assert.deepEqual(highValueSummary(orders, 3000), { ids: [], counts: {} });
console.log("Query decision fixtures passed: exact filtered IDs/group counts, null exclusion and empty selection");
console.log("No OSDK query, index, pagination or authorization executed");
