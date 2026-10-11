# foundry_sdk.v2.connectivity.models.S3ConnectionConfiguration


`bucket_url` needs a trailing slash. Select the bucket region and authentication mode; a public bucket may omit authentication. A custom S3 endpoint needs its own reachability and possibly signing region. Omitted timeout, connection and retry fields use the SDK source defaults shown in the field table; do not infer a tenant-specific bucket or role.

## Exact SDK definition

Python names are SDK attributes; `alias` values are wire names. `Optional` permits null; a default controls omission. A nullable field without a default remains required. `Literal` lists values; `Annotated` retains constraints and discriminators. Request TypedDicts and response Pydantic models are distinct shapes.

## Fields and wire names

Model fields use their declared defaults and aliases. Nullable and omittable are separate; SDK model serialization uses aliases and excludes None values.

| SDK field | Wire name | Type | Omission/default | Meaning |
| --- | --- | --- | --- | --- |
| bucket_url | bucketUrl | str | required; no default | The URL of the S3 bucket. The URL should contain a trailing slash. |
| s3_endpoint | s3Endpoint | typing.Optional[str] | default None | The endpoint of the S3 service. This is used to connect to a custom S3 service that is not AWS S3.<br>    If not specified, defaults to the AWS S3 endpoint.<br>    Warning: Specifying a region and a custom endpoint containing a region can lead to unexpected behavior. |
| region | region | typing.Optional[Region] | None | The region representing the location of the S3 bucket.<br>    Warning: Specifying a region and a custom endpoint containing a region can lead to unexpected behavior. |
| authentication_mode | authenticationMode | typing.Optional[S3AuthenticationMode] | default None | The authentication mode to use to connect to the S3 external system. No authentication mode is required<br>    to connect to publicly accessible AWS S3 buckets. |
| s3_endpoint_signing_region | s3EndpointSigningRegion | typing.Optional[Region] | default None | The region used when constructing the S3 client using a custom endpoint.<br>    This is often not required and would only be needed if you are using the S3 connector with an S3-compliant third-party API,<br>    and are also setting a custom endpoint that requires a non-default region. |
| client_kms_configuration | clientKmsConfiguration | typing.Optional[S3KmsConfiguration] | default None | The client-side KMS key to use for encryption and decryption of data in the S3 bucket.<br>    If not specified, the default KMS key for the bucket is used. |
| sts_role_configuration | stsRoleConfiguration | typing.Optional[StsRoleConfiguration] | default None | The configuration needed to assume a role to connect to the S3 external system. |
| proxy_configuration | proxyConfiguration | typing.Optional[S3ProxyConfiguration] | default None | The configuration needed to connect to the S3 external system through a proxy. |
| max_connections | maxConnections | typing.Optional[int] | default None | The maximum number of HTTP connections to the S3 service per sync.<br>    If not specified, defaults to 50 as defined by the AWS SDK default. |
| connection_timeout_millis | connectionTimeoutMillis | typing.Optional[core.Long] | default None | The amount of time (in milliseconds) to wait when initially establishing a connection before giving up and timing out.<br>    If not specified, defaults to 10000 as defined by the AWS SDK default. |
| socket_timeout_millis | socketTimeoutMillis | typing.Optional[core.Long] | default None | The amount of time (in milliseconds) to wait for data to be transferred over an established, open connection.<br>    If not specified, defaults to 50000 as defined by the AWS SDK default. |
| max_error_retry | maxErrorRetry | typing.Optional[int] | default None | The maximum number of retry attempts for failed requests to the S3 service.<br>    If not specified, defaults to 3 as defined by the AWS SDK default. |
| match_subfolder_exactly | matchSubfolderExactly | typing.Optional[bool] | default None | If true, only files in the subfolder specified in the bucket URL will be synced.<br>    If false, all files in the bucket will be synced.<br>    If not specified, defaults to false. |
| enable_requester_pays | enableRequesterPays | typing.Optional[bool] | default None | Defaults to false, unless set and overwritten.<br>    If true, includes the requester pays header<br>    in requests, allowing reads from requester pays buckets. |
| type | type | typing.Literal['s3'] | 's3' | No additional field description in SDK source. |

```python
class S3ConnectionConfiguration(core.ModelBase):
    """
    The configuration needed to connect to an [AWS S3 external system (or any other S3-like external systems that
    implement the s3a protocol)](https://palantir.com/docs/foundry/available-connectors/amazon-s3/#amazon-s3).
    """

    bucket_url: str = pydantic.Field(alias=str("bucketUrl"))  # type: ignore[literal-required]
    """The URL of the S3 bucket. The URL should contain a trailing slash."""

    s3_endpoint: typing.Optional[str] = pydantic.Field(alias=str("s3Endpoint"), default=None)  # type: ignore[literal-required]
    """
    The endpoint of the S3 service. This is used to connect to a custom S3 service that is not AWS S3.
    If not specified, defaults to the [AWS S3 endpoint](https://docs.aws.amazon.com/general/latest/gr/s3.html).
    Warning: Specifying a region and a custom endpoint containing a region can lead to unexpected behavior.
    """

    region: typing.Optional[Region] = None
    """
    The region representing the location of the S3 bucket.
    Warning: Specifying a region and a custom endpoint containing a region can lead to unexpected behavior.
    """

    authentication_mode: typing.Optional[S3AuthenticationMode] = pydantic.Field(alias=str("authenticationMode"), default=None)  # type: ignore[literal-required]
    """
    The authentication mode to use to connect to the S3 external system. No authentication mode is required
    to connect to publicly accessible AWS S3 buckets.
    """

    s3_endpoint_signing_region: typing.Optional[Region] = pydantic.Field(alias=str("s3EndpointSigningRegion"), default=None)  # type: ignore[literal-required]
    """
    The region used when constructing the S3 client using a custom endpoint.
    This is often not required and would only be needed if you are using the S3 connector with an S3-compliant third-party API,
    and are also setting a custom endpoint that requires a non-default region.
    """

    client_kms_configuration: typing.Optional[S3KmsConfiguration] = pydantic.Field(alias=str("clientKmsConfiguration"), default=None)  # type: ignore[literal-required]
    """
    The client-side KMS key to use for encryption and decryption of data in the S3 bucket.
    If not specified, the default KMS key for the bucket is used.
    """

    sts_role_configuration: typing.Optional[StsRoleConfiguration] = pydantic.Field(alias=str("stsRoleConfiguration"), default=None)  # type: ignore[literal-required]
    """The configuration needed to assume a role to connect to the S3 external system."""

    proxy_configuration: typing.Optional[S3ProxyConfiguration] = pydantic.Field(alias=str("proxyConfiguration"), default=None)  # type: ignore[literal-required]
    """The configuration needed to connect to the S3 external system through a proxy."""

    max_connections: typing.Optional[int] = pydantic.Field(alias=str("maxConnections"), default=None)  # type: ignore[literal-required]
    """
    The maximum number of HTTP connections to the S3 service per sync.
    If not specified, defaults to 50 as defined by the [AWS SDK default](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/ClientConfiguration.html#DEFAULT_MAX_CONNECTIONS).
    """

    connection_timeout_millis: typing.Optional[core.Long] = pydantic.Field(alias=str("connectionTimeoutMillis"), default=None)  # type: ignore[literal-required]
    """
    The amount of time (in milliseconds) to wait when initially establishing a connection before giving up and timing out.
    If not specified, defaults to 10000 as defined by the [AWS SDK default](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/ClientConfiguration.html#DEFAULT_CONNECTION_TIMEOUT).
    """

    socket_timeout_millis: typing.Optional[core.Long] = pydantic.Field(alias=str("socketTimeoutMillis"), default=None)  # type: ignore[literal-required]
    """
    The amount of time (in milliseconds) to wait for data to be transferred over an established, open connection.
    If not specified, defaults to 50000 as defined by the [AWS SDK default](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/ClientConfiguration.html#DEFAULT_SOCKET_TIMEOUT).
    """

    max_error_retry: typing.Optional[int] = pydantic.Field(alias=str("maxErrorRetry"), default=None)  # type: ignore[literal-required]
    """
    The maximum number of retry attempts for failed requests to the S3 service.
    If not specified, defaults to 3 as defined by the [AWS SDK default](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/retry-strategy.html#retry-strategies).
    """

    match_subfolder_exactly: typing.Optional[bool] = pydantic.Field(alias=str("matchSubfolderExactly"), default=None)  # type: ignore[literal-required]
    """
    If true, only files in the subfolder specified in the bucket URL will be synced.
    If false, all files in the bucket will be synced.
    If not specified, defaults to false.
    """

    enable_requester_pays: typing.Optional[bool] = pydantic.Field(alias=str("enableRequesterPays"), default=None)  # type: ignore[literal-required]
    """
    Defaults to false, unless set and overwritten.
    If true, includes the [requester pays header](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html)
    in requests, allowing reads from requester pays buckets.
    """

    type: typing.Literal["s3"] = "s3"
```

## Referenced definitions

- [foundry_sdk._core.model_base.ModelBase](../../../_core/ModelBase.md)
- [foundry_sdk._core.utils.Long](../../../_core/Long.md)
- [foundry_sdk.v2.connectivity.models.Region](Region.md)
- [foundry_sdk.v2.connectivity.models.S3AuthenticationMode](S3AuthenticationMode.md)
- [foundry_sdk.v2.connectivity.models.S3KmsConfiguration](S3KmsConfiguration.md)
- [foundry_sdk.v2.connectivity.models.S3ProxyConfiguration](S3ProxyConfiguration.md)
- [foundry_sdk.v2.connectivity.models.StsRoleConfiguration](StsRoleConfiguration.md)

SDK 1.101.0. Definition adapted from Palantir's Apache-2.0 licensed SDK; Copyright 2024 Palantir Technologies, Inc. [license and notices](../../../../../../assets/rest/LICENSE).

[Part 1](S3ConnectionConfiguration.md)
