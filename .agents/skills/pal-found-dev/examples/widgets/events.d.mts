export function incrementPayload(count: number): { parameterUpdates: { count: number } };
export function fixtureHostUpdate(current: { count: number; label: string }, eventId: string,
  payload: { parameterUpdates: Record<string, number> }): { count: number; label: string };
