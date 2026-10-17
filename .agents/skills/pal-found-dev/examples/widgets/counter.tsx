import { createRoot } from "react-dom/client";
import { FoundryWidget } from "@osdk/widget.client-react";
import config from "./counter.config.js";
import { ReviewCounter } from "./ReviewCounter.js";
const root = document.getElementById("root");
if (!root) throw new Error("counter.html must provide #root");
createRoot(root).render(<FoundryWidget config={config}><ReviewCounter /></FoundryWidget>);
