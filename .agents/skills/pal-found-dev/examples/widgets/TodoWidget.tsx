import type { ObjectSet } from "@osdk/api";
import { useFoundryWidgetContext, FoundryWidget } from "@osdk/widget.client-react";
import { OsdkProvider, useObjectSet } from "@osdk/react";
import { Todo } from "@my/osdk";
import config from "./todo.config.js";
import { widgetClient } from "./todo-client.js";
const useTodoContext = useFoundryWidgetContext.withTypes<typeof config>();
function Rows({ objects }: { objects: ObjectSet<typeof Todo> }) {
  const query = useObjectSet(objects, { where: { isComplete: false }, pageSize: 10 });
  if (query.isLoading && !query.data) return <p>Loading tasks</p>;
  if (query.error) return <p role="alert">Task query failed</p>;
  if (!query.data?.length) return <p>No incomplete tasks in selected set</p>;
  return <section>
    {query.isLoading && <p>Refreshing tasks</p>}
    <ul>{query.data.map(todo => <li key={todo.$primaryKey}>{todo.title}</li>)}</ul>
    {query.hasMore && <button disabled={query.isLoading} onClick={() => query.fetchMore?.()}>Load more</button>}
  </section>;
}
function Content() {
  const { parameters } = useTodoContext();
  const objects = parameters.values.todos;
  return objects == null ? <p>Bind a Todo object set</p> : <Rows objects={objects.objectSet} />;
}
export function TodoWidget() {
  return <FoundryWidget config={config} client={widgetClient}>
    <OsdkProvider client={widgetClient}><Content /></OsdkProvider>
  </FoundryWidget>;
}
