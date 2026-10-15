"""Validate synthetic payloads using the prepared SDK; never contacts Foundry."""

import json
from pathlib import Path
from pydantic import TypeAdapter, ValidationError
from foundry_sdk.v2.data_health.models import CheckConfig, ReplaceCheckConfig


def reject(adapter, payload):
    try:
        adapter.validate_python(payload)
    except ValidationError:
        return
    raise AssertionError("invalid payload unexpectedly parsed")


def validate_check_choices(payload):
    """Check documented cross-field choices that SDK parsing does not enforce.

    This checks five documented error conditions, not all server validation.
    """
    numeric = payload.get("numericColumnCheckConfig")
    if numeric is not None:
        if numeric.get("numericBounds") is None and numeric.get("trend") is None:
            raise ValueError("InvalidNumericColumnCheckConfig")
        trend = numeric.get("trend")
        if trend is not None and trend.get("trendType") is None and trend.get("differenceBounds") is None:
            raise ValueError("InvalidTrendConfig")
    percentage = payload.get("percentageCheckConfig")
    if percentage is not None and percentage.get("percentageBounds") is None and percentage.get("medianDeviation") is None:
        raise ValueError("InvalidPercentageCheckConfig")
    time = payload.get("timeCheckConfig")
    if time is not None and time.get("timeBounds") is None and time.get("medianDeviation") is None:
        error = "InvalidTransactionTimeCheckConfig" if payload["type"] == "timeSinceLastUpdated" else "InvalidTimeCheckConfig"
        raise ValueError(error)


def reject_choice(payload, error_name):
    try:
        validate_check_choices(payload)
    except ValueError as error:
        assert str(error) == error_name
        return
    raise AssertionError("empty semantic check choice unexpectedly accepted")


def main():
    create = TypeAdapter(CheckConfig)
    replace = TypeAdapter(ReplaceCheckConfig)
    files = sorted((Path(__file__).parent / "check-config").glob("*.json"))
    assert len(files) == 16
    for file in files:
        item = json.loads(file.read_text(encoding="utf-8"))
        assert create.validate_python(item["create"]).type == item["type"]
        assert replace.validate_python(item["replace"]).type == item["type"]
        validate_check_choices(item["create"])
        validate_check_choices(item["replace"])
    build = json.loads(next(file for file in files if file.stem == "buildStatus").read_text())
    reject(create, {**build["create"], "type": "unknownCheckType"})
    reject(create, {k: v for k, v in build["create"].items() if k != "subject"})
    reject(replace, {**build["replace"], "statusCheckConfig": {"severity": "SEVERE"}})
    reject_choice({"type": "numericColumnMean", "numericColumnCheckConfig": {"columnName": "amount"}}, "InvalidNumericColumnCheckConfig")
    reject_choice({"type": "numericColumnMean", "numericColumnCheckConfig": {"columnName": "amount", "trend": {"severity": "MODERATE"}}}, "InvalidTrendConfig")
    reject_choice({"type": "nullPercentage", "percentageCheckConfig": {"columnName": "status"}}, "InvalidPercentageCheckConfig")
    reject_choice({"type": "buildDuration", "timeCheckConfig": {}}, "InvalidTimeCheckConfig")
    reject_choice({"type": "timeSinceLastUpdated", "timeCheckConfig": {"ignoreEmptyTransactions": True}}, "InvalidTransactionTimeCheckConfig")
    print("32 configuration payloads parsed; wrong type, missing subject and invalid severity rejected")
    print("No check saved, dataset evaluated or permission verified")
    print("Five documented empty cross-field choices rejected by local preflight")


if __name__ == "__main__":
    main()
