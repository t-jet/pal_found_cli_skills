import { defineConfig } from "@osdk/widget.client";
export default defineConfig({
  id: "reviewSummary", name: "Review summary",
  description: "Display the same host count without changing it.", type: "workshop",
  parameters: { count: { type: "number", displayName: "Reviewed orders" } }, events: {},
});
