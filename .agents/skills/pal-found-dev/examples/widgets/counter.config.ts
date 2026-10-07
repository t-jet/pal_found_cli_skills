import { defineConfig } from "@osdk/widget.client";

export default defineConfig({
  id: "reviewCounter", name: "Review counter",
  description: "Count reviewed orders through a Workshop number variable.",
  type: "workshop",
  parameters: {
    count: { type: "number", displayName: "Reviewed orders" },
    label: { type: "string", displayName: "Counter label" },
  },
  events: { countChanged: { displayName: "Review count changed", parameterUpdateIds: ["count"] } },
});
