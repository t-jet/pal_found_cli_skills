import { createPublicOauthClient } from "@osdk/oauth";
import { createClient } from "@osdk/client";
import { createTimedFetch } from "./timeout.mjs";

export function configureClient(config: {
  foundryUrl: string;
  ontologyRid: string;
  clientId: string;
  redirectUrl: string;
  scopes: string[];
  requestTimeoutMs?: number;
}) {
  if (!Array.isArray(config.scopes)) {
    throw new TypeError("Configure an explicit approved scopes array before sign-in");
  }
  const auth = createPublicOauthClient(
    config.clientId, config.foundryUrl, config.redirectUrl, { scopes: config.scopes },
  );
  const client = createClient(
    config.foundryUrl, config.ontologyRid, auth, undefined,
    createTimedFetch(config.requestTimeoutMs),
  );
  return { auth, client };
}
