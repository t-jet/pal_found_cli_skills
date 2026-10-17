"""SDK 1.101.0 fixture adapters: real SDK serialization, synthetic HTTP results.

The patched HTTP-client constructors are a version-specific test seam. Live
application code uses ordinary SDK clients and an authorized identity instead.
"""

from contextlib import asynccontextmanager, contextmanager
from unittest.mock import patch

import httpx
from foundry_sdk import Config, UserTokenAuth


@contextmanager
def mock_resource(resource_type, handler):
    with httpx.Client(transport=httpx.MockTransport(handler), timeout=30) as transport:
        with patch("foundry_sdk._core.api_client.HttpClient", return_value=transport):
            resource = resource_type(
                auth=UserTokenAuth(token="offline-fixture-token"),
                hostname="offline.example.invalid",
                config=Config(timeout=30, max_retries=1,
                              propagate_qos="PROPAGATE_429_AND_503_TO_CALLER"),
            )
        yield resource


@asynccontextmanager
async def mock_async_resource(resource_type, handler):
    async with httpx.AsyncClient(transport=httpx.MockTransport(handler), timeout=30) as transport:
        with patch("foundry_sdk._core.api_client.AsyncHttpClient", return_value=transport):
            resource = resource_type(
                auth=UserTokenAuth(token="offline-fixture-token"),
                hostname="offline.example.invalid",
                config=Config(timeout=30, max_retries=1,
                              propagate_qos="PROPAGATE_429_AND_503_TO_CALLER"),
            )
        yield resource
