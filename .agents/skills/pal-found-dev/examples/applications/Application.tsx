import type { Client } from "@osdk/client";
import { OsdkProvider } from "@osdk/react";
import { TodoList } from "./TodoList.js";

// Create the client once with approved configuration before rendering this root.
export function Application({ client }: { client: Client }) {
  return <OsdkProvider client={client}><TodoList /></OsdkProvider>;
}
