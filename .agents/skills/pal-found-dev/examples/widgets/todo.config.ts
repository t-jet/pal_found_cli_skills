import { defineConfig } from "@osdk/widget.client";
import { Todo } from "@my/osdk";
export default defineConfig({
  id: "incompleteTodos", name: "Incomplete tasks",
  description: "Display the Todo object set supplied by Workshop.", type: "workshop",
  refreshHostDataOnAction: true,
  parameters: { todos: { type: "objectSet", allowedType: Todo, displayName: "Tasks" } },
  events: {},
});
