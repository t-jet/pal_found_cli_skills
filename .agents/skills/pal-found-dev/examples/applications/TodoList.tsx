import { Todo, completeTodo } from "@my/osdk";
import { useOsdkObjects, useOsdkAction } from "@osdk/react";
import { viewState } from "./view_state.mjs";

export function TodoList() {
  const query = useOsdkObjects(Todo, {
    where: { isComplete: false }, orderBy: { createdAt: "desc" }, pageSize: 10,
  });
  const action = useOsdkAction(completeTodo);
  const state = viewState({ ...query, isPending: action.isPending });
  if (state.kind === "error") return <p role="alert">Query failed: {query.error?.message}</p>;
  if (state.kind === "loading") return <p>Loading tasks</p>;
  if (state.kind === "empty") return <p>No incomplete tasks</p>;
  return <section>
    {state.kind === "refreshing" && <p>Refreshing tasks</p>}
    {query.isOptimistic && <p>Showing provisional list order</p>}
    {action.error && <p role="alert">{action.error.actionValidation?.message ?? String(action.error.unknown)}</p>}
    {query.data?.map(todo => <div key={todo.$primaryKey}>
      <span>{todo.title}</span>
      <button disabled={!state.canSubmit} onClick={async () => {
        try { await action.applyAction({ todo, isComplete: true }); }
        catch { /* Hook error state reports the failure; confirmed state stays visible. */ }
      }}>Complete</button>
    </div>)}
    {query.hasMore && <button disabled={query.isLoading} onClick={() => query.fetchMore?.()}>Load more</button>}
  </section>;
}
