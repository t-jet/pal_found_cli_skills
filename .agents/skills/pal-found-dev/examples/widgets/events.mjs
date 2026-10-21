export function incrementPayload(count) {
  if (!Number.isFinite(count)) throw new TypeError("count must be finite");
  return { parameterUpdates: { count: count + 1 } };
}

// Synthetic host model; this is not a Foundry client.
export function fixtureHostUpdate(current, eventId, payload) {
  if (eventId !== "countChanged") throw new Error("unbound event");
  const updates = payload.parameterUpdates;
  if (Object.keys(updates).some(key => key !== "count")) throw new Error("parameter not permitted by event");
  if (!Number.isFinite(updates.count)) throw new TypeError("invalid host count");
  return { ...current, ...updates };
}
