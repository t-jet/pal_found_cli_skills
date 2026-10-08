// Bounded buffered HTTP transport for this app's JSON queries and Actions.
export function createTimedFetch(timeoutMs = 15_000, transport = globalThis.fetch) {
  if (!Number.isInteger(timeoutMs) || timeoutMs < 1 || timeoutMs > 120_000) {
    throw new RangeError("requestTimeoutMs must be an integer from 1 to 120000");
  }
  return async (input, init = {}) => {
    const controller = new AbortController();
    const callerSignal = init.signal ?? (input instanceof Request ? input.signal : undefined);
    const forwardAbort = () => controller.abort(callerSignal.reason);
    if (callerSignal?.aborted) forwardAbort();
    else callerSignal?.addEventListener("abort", forwardAbort, { once: true });
    const timer = setTimeout(() => controller.abort(
      new DOMException(`HTTP request exceeded ${timeoutMs}ms`, "TimeoutError"),
    ), timeoutMs);
    try {
      const response = await transport(input, { ...init, signal: controller.signal });
      // Keep the deadline active through the body, not just until headers arrive.
      const bytes = await response.arrayBuffer();
      const body = [204, 205, 304].includes(response.status) ? null : bytes;
      return new Response(body, {
        status: response.status, statusText: response.statusText, headers: response.headers,
      });
    } catch (error) {
      if (controller.signal.aborted) throw controller.signal.reason;
      throw error;
    } finally {
      clearTimeout(timer);
      callerSignal?.removeEventListener("abort", forwardAbort);
    }
  };
}
