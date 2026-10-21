import { createRoot } from "react-dom/client";
import { FoundryWidget, useFoundryWidgetContext } from "@osdk/widget.client-react";
import config from "./summary.config.js";
const useSummaryContext = useFoundryWidgetContext.withTypes<typeof config>();
function Summary() {
  const { parameters } = useSummaryContext();
  return <p>Reviewed orders: {parameters.values.count ?? 0}</p>;
}
const root = document.getElementById("root");
if (!root) throw new Error("summary.html must provide #root");
createRoot(root).render(<FoundryWidget config={config}><Summary /></FoundryWidget>);
