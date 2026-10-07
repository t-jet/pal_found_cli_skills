export function viewState(state: {
  data?: readonly unknown[];
  error?: unknown;
  isLoading: boolean;
  isPending?: boolean;
}): { kind: "error" | "loading" | "empty" | "refreshing" | "ready"; canSubmit: boolean };
