import { useFoundryWidgetContext } from "@osdk/widget.client-react";
import type CounterConfig from "./counter.config.js";
import { incrementPayload } from "./events.mjs";

const useCounterContext = useFoundryWidgetContext.withTypes<typeof CounterConfig>();
export function ReviewCounter() {
  const { parameters, emitEvent } = useCounterContext();
  const count = parameters.values.count ?? 0;
  return <section>
    <h2>{parameters.values.label ?? "Reviewed orders"}</h2>
    <output aria-live="polite">{count}</output>
    <button disabled={!Number.isFinite(count)} onClick={() => {
      emitEvent("countChanged", incrementPayload(count));
    }}>Increment</button>
  </section>;
}
