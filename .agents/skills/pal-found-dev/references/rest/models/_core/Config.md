# foundry_sdk._core.config.Config


Configuration for the HTTP session.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| default_headers | default_headers | Optional[Dict[str, str]] | None | HTTP headers to include with all requests. |
| proxies | proxies | Optional[Dict[Literal['http', 'https'], str]] | None | Proxies to use for HTTP and HTTPS requests. |
| timeout | timeout | Optional[Union[int, float]] | None | The default timeout for all requests in seconds. |
| verify | verify | Union[bool, str] | True | SSL verification, can be a boolean or a path to a CA bundle. When using an HTTPS proxy,<br>    connection this value will be passed to the proxy's SSL context as well. |
| default_params | default_params | Optional[Dict[str, Any]] | None | URL query parameters to include with all requests. |
| scheme | scheme | Literal['http', 'https'] | 'https' | URL scheme to use ('http' or 'https'). Defaults to 'https'. |
| max_retries | max_retries | Optional[int] | None | The maximum number of times a failed request is retried.<br>    If no value is provided, it defaults to 4. |
| propagate_qos | propagate_qos | Optional[Literal['AUTOMATIC_RETRY', 'PROPAGATE_429_AND_503_TO_CALLER']] | None | Indicates whether 429 and 503 status codes should be propagated as exceptions or retried. |
| backoff_slot_size_ms | backoff_slot_size_ms | Optional[int] | None | The size of one backoff time slot in milliseconds for call retries. For example,<br>    an exponential backoff retry algorithm may choose a backoff time in [0, backoffSlotSize * 2^c]<br>    for the c-th retry.<br>    If no value is provided, it defaults to 250 milliseconds. |

```python
@dataclass
class Config:
    """
    Configuration for the HTTP session.
    """

    default_headers: Optional[Dict[str, str]] = None
    """HTTP headers to include with all requests."""

    proxies: Optional[Dict[Literal["http", "https"], str]] = None
    """Proxies to use for HTTP and HTTPS requests."""

    timeout: Optional[Union[int, float]] = None
    """The default timeout for all requests in seconds."""

    verify: Union[bool, str] = True
    """
    SSL verification, can be a boolean or a path to a CA bundle. When using an HTTPS proxy,
    connection this value will be passed to the proxy's SSL context as well.
    """

    default_params: Optional[Dict[str, Any]] = None
    """URL query parameters to include with all requests."""

    scheme: Literal["http", "https"] = "https"
    """URL scheme to use ('http' or 'https'). Defaults to 'https'."""

    max_retries: Optional[int] = None
    """
    The maximum number of times a failed request is retried.
    If no value is provided, it defaults to 4.
    """

    propagate_qos: Optional[Literal["AUTOMATIC_RETRY", "PROPAGATE_429_AND_503_TO_CALLER"]] = None
    """Indicates whether 429 and 503 status codes should be propagated as exceptions or retried."""

    backoff_slot_size_ms: Optional[int] = None
    """
    The size of one backoff time slot in milliseconds for call retries. For example,
    an exponential backoff retry algorithm may choose a backoff time in [0, backoffSlotSize * 2^c]
    for the c-th retry.
    If no value is provided, it defaults to 250 milliseconds.
    """
```

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../assets/rest/LICENSE).

[Part 1](Config.md)
