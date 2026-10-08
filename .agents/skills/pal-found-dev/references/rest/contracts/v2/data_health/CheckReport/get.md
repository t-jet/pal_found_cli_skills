# v2.data_health.CheckReport.get


API v2; release stage: Public Beta. Check enrollment enablement and resource access before live execution.

## Purpose and parameter meaning

Get the CheckReport with the specified rid.

## SDK invocation contract

```python
def get(self, check_rid: core_models.CheckRid, check_report_rid: core_models.CheckReportRid, *, preview: typing.Optional[core_models.PreviewMode]=None, request_timeout: typing.Optional[core.Timeout]=None, _sdk_internal: core.SdkInternal={}) -> data_health_models.CheckReport: ...
```

## Parameters and defaults

| SDK parameter | Type | Required/default | Meaning |
| --- | --- | --- | --- |
| check_rid | core_models.CheckRid | required | Value shape and constraints are in its referenced local type definition. |
| check_report_rid | core_models.CheckReportRid | required | Value shape and constraints are in its referenced local type definition. |
| preview | typing.Optional[core_models.PreviewMode] | None | Enables the use of preview functionality. |
| request_timeout | typing.Optional[core.Timeout] | None | timeout setting for this request in seconds. |
| _sdk_internal | core.SdkInternal | {} | SDK transport internals; use ordinary/raw/streaming wrapper APIs instead of treating this as application input. |

## Documented operation errors

| Error | Meaning |
| --- | --- |
| CheckReportNotFound | The given CheckReport could not be found. |
| CheckTypeNotSupported | The type of the requested check is not yet supported in the Platform API. |

## Wire request

**method**

```python
'GET'
```

**resource_path**

```python
'/v2/dataHealth/checks/{checkRid}/checkReports/{checkReportRid}'
```

**query_params**

```python
{'preview': preview}
```

**path_params**

```python
{'checkRid': check_rid, 'checkReportRid': check_report_rid}
```

**header_params**

```python
{'Accept': 'application/json'}
```

**body**

```python
None
```

**response_type**

```python
data_health_models.CheckReport
```

**request_timeout**

```python
request_timeout
```

**throwable_errors**

```python
{'CheckReportNotFound': data_health_errors.CheckReportNotFound, 'CheckTypeNotSupported': data_health_errors.CheckTypeNotSupported}
```

**response_mode**

```python
_sdk_internal.get('response_mode')
```

## Response modes

Ordinary sync return: `data_health_models.CheckReport`. Ordinary async return: `typing.Awaitable[data_health_models.CheckReport]`. Wrapper availability and exact returns from the frozen source:

| Client mode | Return annotation |
| --- | --- |
| sync_ordinary | data_health_models.CheckReport |
| sync_raw | ApiResponse[data_health_models.CheckReport] |
| sync_streaming | StreamingContextManager[data_health_models.CheckReport] |
| async_ordinary | typing.Awaitable[data_health_models.CheckReport] |
| async_raw | Awaitable[AsyncApiResponse[data_health_models.CheckReport]] |
| async_streaming | AsyncStreamingContextManager[Awaitable[data_health_models.CheckReport]] |

An absent wrapper method cannot be selected for this operation. Use an exposed mode and its actual lifetime. [Client lifetimes and finite work](../../../../client-behavior.md).

## Complete referenced models and errors

- [foundry_sdk._core.api_client.ResponseMode](../../../../models/_core/ResponseMode.md)
- [foundry_sdk._core.api_client.SdkInternal](../../../../models/_core/SdkInternal.md)
- [foundry_sdk._core.model_base.ModelBase](../../../../models/_core/ModelBase.md)
- [foundry_sdk._core.utils.AwareDatetime](../../../../models/_core/AwareDatetime.md)
- [foundry_sdk._core.utils.Long](../../../../models/_core/Long.md)
- [foundry_sdk._core.utils.RID](../../../../models/_core/RID.md)
- [foundry_sdk._core.utils.Timeout](../../../../models/_core/Timeout.md)
- [foundry_sdk._core.utils.UUID](../../../../models/_core/UUID.md)
- [foundry_sdk.v2.core.models.BranchName](../../../../models/v2/core/models/BranchName.md)
- [foundry_sdk.v2.core.models.CheckReportRid](../../../../models/v2/core/models/CheckReportRid.md)
- [foundry_sdk.v2.core.models.CheckRid](../../../../models/v2/core/models/CheckRid.md)
- [foundry_sdk.v2.core.models.CreatedBy](../../../../models/v2/core/models/CreatedBy.md)
- [foundry_sdk.v2.core.models.CreatedTime](../../../../models/v2/core/models/CreatedTime.md)
- [foundry_sdk.v2.core.models.DatasetRid](../../../../models/v2/core/models/DatasetRid.md)
- [foundry_sdk.v2.core.models.PreviewMode](../../../../models/v2/core/models/PreviewMode.md)
- [foundry_sdk.v2.core.models.PrincipalId](../../../../models/v2/core/models/PrincipalId.md)
- [foundry_sdk.v2.core.models.SchemaFieldType](../../../../models/v2/core/models/SchemaFieldType.md)
- [foundry_sdk.v2.core.models.UpdatedTime](../../../../models/v2/core/models/UpdatedTime.md)
- [foundry_sdk.v2.data_health.errors.CheckReportNotFound](../../../../models/v2/data_health/errors/CheckReportNotFound.md)
- [foundry_sdk.v2.data_health.errors.CheckReportNotFoundParameters](../../../../models/v2/data_health/errors/CheckReportNotFoundParameters.md)
- [foundry_sdk.v2.data_health.errors.CheckTypeNotSupported](../../../../models/v2/data_health/errors/CheckTypeNotSupported.md)
- [foundry_sdk.v2.data_health.errors.CheckTypeNotSupportedParameters](../../../../models/v2/data_health/errors/CheckTypeNotSupportedParameters.md)
- [foundry_sdk.v2.data_health.models.AllowedColumnValuesCheckConfig](../../../../models/v2/data_health/models/AllowedColumnValuesCheckConfig.md)
- [foundry_sdk.v2.data_health.models.ApproximateUniquePercentageCheckConfig](../../../../models/v2/data_health/models/ApproximateUniquePercentageCheckConfig.md)
- [foundry_sdk.v2.data_health.models.BooleanColumnValue](../../../../models/v2/data_health/models/BooleanColumnValue.md)
- [foundry_sdk.v2.data_health.models.BuildDurationCheckConfig](../../../../models/v2/data_health/models/BuildDurationCheckConfig.md)
- [foundry_sdk.v2.data_health.models.BuildStatusCheckConfig](../../../../models/v2/data_health/models/BuildStatusCheckConfig.md)
- [foundry_sdk.v2.data_health.models.Check](../../../../models/v2/data_health/models/Check.md)
- [foundry_sdk.v2.data_health.models.CheckConfig](../../../../models/v2/data_health/models/CheckConfig.md)
- [foundry_sdk.v2.data_health.models.CheckGroupRid](../../../../models/v2/data_health/models/CheckGroupRid.md)
- [foundry_sdk.v2.data_health.models.CheckIntent](../../../../models/v2/data_health/models/CheckIntent.md)
- [foundry_sdk.v2.data_health.models.CheckReport](../../../../models/v2/data_health/models/CheckReport.md)
- [foundry_sdk.v2.data_health.models.CheckResult](../../../../models/v2/data_health/models/CheckResult.md)
- [foundry_sdk.v2.data_health.models.CheckResultStatus](../../../../models/v2/data_health/models/CheckResultStatus.md)
- [foundry_sdk.v2.data_health.models.ColumnCountConfig](../../../../models/v2/data_health/models/ColumnCountConfig.md)
- [foundry_sdk.v2.data_health.models.ColumnInfo](../../../../models/v2/data_health/models/ColumnInfo.md)
- [foundry_sdk.v2.data_health.models.ColumnName](../../../../models/v2/data_health/models/ColumnName.md)
- [foundry_sdk.v2.data_health.models.ColumnTypeCheckConfig](../../../../models/v2/data_health/models/ColumnTypeCheckConfig.md)
- [foundry_sdk.v2.data_health.models.ColumnTypeConfig](../../../../models/v2/data_health/models/ColumnTypeConfig.md)
- [foundry_sdk.v2.data_health.models.ColumnValue](../../../../models/v2/data_health/models/ColumnValue.md)
- [foundry_sdk.v2.data_health.models.DatasetSubject](../../../../models/v2/data_health/models/DatasetSubject.md)
- [foundry_sdk.v2.data_health.models.DateBounds](../../../../models/v2/data_health/models/DateBounds.md)
- [foundry_sdk.v2.data_health.models.DateBoundsConfig](../../../../models/v2/data_health/models/DateBoundsConfig.md)
- [foundry_sdk.v2.data_health.models.DateColumnRangeCheckConfig](../../../../models/v2/data_health/models/DateColumnRangeCheckConfig.md)
- [foundry_sdk.v2.data_health.models.DateColumnValue](../../../../models/v2/data_health/models/DateColumnValue.md)
- [foundry_sdk.v2.data_health.models.EscalationConfig](../../../../models/v2/data_health/models/EscalationConfig.md)
- [foundry_sdk.v2.data_health.models.IgnoreEmptyTransactions](../../../../models/v2/data_health/models/IgnoreEmptyTransactions.md)
- [foundry_sdk.v2.data_health.models.JobDurationCheckConfig](../../../../models/v2/data_health/models/JobDurationCheckConfig.md)
- [foundry_sdk.v2.data_health.models.JobStatusCheckConfig](../../../../models/v2/data_health/models/JobStatusCheckConfig.md)
- [foundry_sdk.v2.data_health.models.MedianDeviation](../../../../models/v2/data_health/models/MedianDeviation.md)
- [foundry_sdk.v2.data_health.models.MedianDeviationBoundsType](../../../../models/v2/data_health/models/MedianDeviationBoundsType.md)
- [foundry_sdk.v2.data_health.models.MedianDeviationConfig](../../../../models/v2/data_health/models/MedianDeviationConfig.md)
- [foundry_sdk.v2.data_health.models.NullPercentageCheckConfig](../../../../models/v2/data_health/models/NullPercentageCheckConfig.md)
- [foundry_sdk.v2.data_health.models.NumericBounds](../../../../models/v2/data_health/models/NumericBounds.md)
- [foundry_sdk.v2.data_health.models.NumericBoundsConfig](../../../../models/v2/data_health/models/NumericBoundsConfig.md)
- [foundry_sdk.v2.data_health.models.NumericColumnCheckConfig](../../../../models/v2/data_health/models/NumericColumnCheckConfig.md)
- [foundry_sdk.v2.data_health.models.NumericColumnMeanCheckConfig](../../../../models/v2/data_health/models/NumericColumnMeanCheckConfig.md)
- [foundry_sdk.v2.data_health.models.NumericColumnMedianCheckConfig](../../../../models/v2/data_health/models/NumericColumnMedianCheckConfig.md)
- [foundry_sdk.v2.data_health.models.NumericColumnRangeCheckConfig](../../../../models/v2/data_health/models/NumericColumnRangeCheckConfig.md)
- [foundry_sdk.v2.data_health.models.NumericColumnValue](../../../../models/v2/data_health/models/NumericColumnValue.md)
- [foundry_sdk.v2.data_health.models.PercentageBounds](../../../../models/v2/data_health/models/PercentageBounds.md)
- [foundry_sdk.v2.data_health.models.PercentageBoundsConfig](../../../../models/v2/data_health/models/PercentageBoundsConfig.md)
- [foundry_sdk.v2.data_health.models.PercentageCheckConfig](../../../../models/v2/data_health/models/PercentageCheckConfig.md)
- [foundry_sdk.v2.data_health.models.PercentageValue](../../../../models/v2/data_health/models/PercentageValue.md)
- [foundry_sdk.v2.data_health.models.PrimaryKeyCheckConfig](../../../../models/v2/data_health/models/PrimaryKeyCheckConfig.md)
- [foundry_sdk.v2.data_health.models.PrimaryKeyConfig](../../../../models/v2/data_health/models/PrimaryKeyConfig.md)
- [foundry_sdk.v2.data_health.models.SchemaComparisonCheckConfig](../../../../models/v2/data_health/models/SchemaComparisonCheckConfig.md)
- [foundry_sdk.v2.data_health.models.SchemaComparisonConfig](../../../../models/v2/data_health/models/SchemaComparisonConfig.md)
- [foundry_sdk.v2.data_health.models.SchemaComparisonType](../../../../models/v2/data_health/models/SchemaComparisonType.md)
- [foundry_sdk.v2.data_health.models.SchemaInfo](../../../../models/v2/data_health/models/SchemaInfo.md)
- [foundry_sdk.v2.data_health.models.SeverityLevel](../../../../models/v2/data_health/models/SeverityLevel.md)
- [foundry_sdk.v2.data_health.models.StatusCheckConfig](../../../../models/v2/data_health/models/StatusCheckConfig.md)
- [foundry_sdk.v2.data_health.models.StringColumnValue](../../../../models/v2/data_health/models/StringColumnValue.md)
- [foundry_sdk.v2.data_health.models.TimeBounds](../../../../models/v2/data_health/models/TimeBounds.md)
- [foundry_sdk.v2.data_health.models.TimeBoundsConfig](../../../../models/v2/data_health/models/TimeBoundsConfig.md)
- [foundry_sdk.v2.data_health.models.TimeCheckConfig](../../../../models/v2/data_health/models/TimeCheckConfig.md)
- [foundry_sdk.v2.data_health.models.TimeSinceLastUpdatedCheckConfig](../../../../models/v2/data_health/models/TimeSinceLastUpdatedCheckConfig.md)
- [foundry_sdk.v2.data_health.models.TotalColumnCountCheckConfig](../../../../models/v2/data_health/models/TotalColumnCountCheckConfig.md)
- [foundry_sdk.v2.data_health.models.TransactionTimeCheckConfig](../../../../models/v2/data_health/models/TransactionTimeCheckConfig.md)
- [foundry_sdk.v2.data_health.models.TrendConfig](../../../../models/v2/data_health/models/TrendConfig.md)
- [foundry_sdk.v2.data_health.models.TrendType](../../../../models/v2/data_health/models/TrendType.md)

## Identity and execution boundary

[Authentication and effective access](../../../../authentication.md). Method source does not enumerate universal OAuth scopes or an idempotency guarantee. Use configured application grants and resource permissions; verify tenant-specific prerequisites. The domain guide supplies authored workflows, examples and outcome reconciliation.

## Application workflow

Read the [local resource guide](../../../../v2/data_health/CheckReport.md) for its authored operations and runnable examples. A guide covering selected methods does not establish coverage of other methods.

[Part 1](get.md)
