"""Synthetic Dataset substitute; checks pandas computation, never Foundry writes."""

import runpy
import sys
import types
from pathlib import Path
from unittest.mock import patch

import pandas as pd


class SyntheticDataset:
    output = None

    @classmethod
    def get(cls, alias):
        if alias not in {"orders", "customer_totals"}:
            raise KeyError(alias)
        return cls()

    def read_table(self, format):
        assert format == "arrow"
        return self

    def to_pandas(self):
        return pd.DataFrame({"customer_id": ["c1", "c1", "c2"], "amount": [10, 7.5, None]})

    def write_table(self, frame):
        SyntheticDataset.output = frame.copy()


foundry = types.ModuleType("foundry")
transforms = types.ModuleType("foundry.transforms")
transforms.Dataset = SyntheticDataset
with patch.dict(sys.modules, {"foundry": foundry, "foundry.transforms": transforms}):
    runpy.run_path(str(Path(__file__).with_name("transform.py")))
assert SyntheticDataset.output.to_dict("records") == [
    {"customer_id": "c1", "total_amount": 17.5},
    {"customer_id": "c2", "total_amount": 0.0},
]
print("Synthetic workspace computation passed; no Foundry publication/build tested.")
