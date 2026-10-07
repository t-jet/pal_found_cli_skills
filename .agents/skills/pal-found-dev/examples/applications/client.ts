import { createPublicOauthClient } from "@osdk/oauth";
import { createClient } from "@osdk/client";

export function configureClient(config: {
  foundryUrl: string;
  ontologyRid: string;
  clientId: string;
  redirectUrl: string;
  scopes?: string[];
}) {
  const auth = createPublicOauthClient(
    config.clientId, config.foundryUrl, config.redirectUrl, { scopes: config.scopes },
  );
  const client = createClient(config.foundryUrl, config.ontologyRid, auth);
  return { auth, client };
}
