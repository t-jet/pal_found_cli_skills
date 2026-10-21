import { createClient } from "@osdk/client";
import { createFoundryWidgetTokenProvider } from "@osdk/widget.client";
import { $ontologyRid } from "@my/osdk";
export const widgetClient = createClient(window.location.origin, $ontologyRid,
  createFoundryWidgetTokenProvider());
