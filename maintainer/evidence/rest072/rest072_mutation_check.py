"""Prove dedicated domain assertions reject seven historical fixture defects."""
import importlib.util
import json
from pathlib import Path
from unittest.mock import patch

import pytest

tmp = Path(__file__).resolve().parent
path = tmp / "feature015_integration/tests/test_offline_rest_072.py"
spec = importlib.util.spec_from_file_location("rest072_tests", path)
tests = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tests)
original = tests.example
checks = []

for resource, operation, defect in [
    ("Marking", "get_batch", "empty batch result"),
    ("Role", "get_batch", "empty batch result"),
    ("CbacBanner", "get", "missing marking IDs"),
    ("CbacMarkingRestrictions", "get", "missing marking IDs"),
    ("Marking", "parse_classifications", "unaccounted classification inputs"),
    ("MarkingRoleAssignment", "add", "ADMINISTER success without target distinction"),
    ("MarkingRoleAssignment", "remove", "ADMINISTER success without target distinction"),
]:
    def mutated(selected_resource, selected_operation):
        ns = original(selected_resource, selected_operation)
        if operation == "get_batch":
            ns["SUCCESS"]["data"].clear()
        elif resource.startswith("Cbac"):
            # Change only the real call. Existing example-owned checks cannot serve as oracle.
            def invoke(client):
                return client.with_raw_response.get(preview=True, request_timeout=30)
            ns["invoke"] = invoke
        elif operation == "parse_classifications":
            ns["SUCCESS"]["parsed"].clear()
            ns["SUCCESS"]["errors"].clear()
        else:
            ns["invoke"].__defaults__ = ("ADMINISTER", "synthetic-value")
            ns["check_request"].__defaults__ = ("ADMINISTER", "synthetic-value")
        return ns

    with patch.object(tests, "example", mutated):
        with pytest.MonkeyPatch.context() as monkeypatch:
            try:
                if operation == "get_batch":
                    tests.test_batch_examples_correlate_requested_ids_with_map_keys_and_models(resource, "markingId" if resource == "Marking" else "roleId")
                elif resource.startswith("Cbac"):
                    tests.test_cbac_examples_send_marking_ids_before_claiming_specific_results(resource)
                elif operation == "parse_classifications":
                    tests.test_classification_example_accounts_for_success_and_invalid_input_separately()
                else:
                    tests.test_role_examples_distinguish_organization_administer_and_last_admin(operation, monkeypatch)
            except AssertionError:
                checks.append({"operation": resource + "." + operation, "mutation": defect, "result": "REJECTED"})
            else:
                raise AssertionError("Regression survived: " + resource + "." + operation)

(tmp / "rest072_mutation_check.json").write_text(json.dumps(checks, indent=2) + "\n", encoding="utf-8")
print(f"{len(checks)} historical mutations rejected")
