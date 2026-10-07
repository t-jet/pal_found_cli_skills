export function viewState({ data, error, isLoading, isPending = false }) {
  if (error) return { kind: "error", canSubmit: false };
  if (data == null && isLoading) return { kind: "loading", canSubmit: false };
  if (data == null || data.length === 0) return { kind: "empty", canSubmit: false };
  return { kind: isLoading ? "refreshing" : "ready", canSubmit: !isPending };
}
