"""Pure integer calculation; no platform calls."""

from typing import TypedDict


class ScoreInput(TypedDict):
    amount: int
    factor: int


def score(context, event: ScoreInput) -> int:
    amount, factor = event["amount"], event["factor"]
    if type(amount) is not int or type(factor) is not int:
        raise ValueError("amount and factor must be integers")
    if amount < 0 or factor < 0:
        raise ValueError("amount and factor must be non-negative")
    return amount * factor
