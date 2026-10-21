"""Check only the synthetic J9/J10 records; no Foundry connection is made."""

J9 = {
    "git_branch": "feature-risk",
    "source_commit": "review-code-7",
    "build_branch": "demo",
    "fallbacks": ("demo", "master"),
    "input_transactions": {"demo": None, "master": "input-41"},
    "output_transactions": {"demo": "output-9", "master": "output-8"},
}

J10 = {
    "required_input": "input-42",
    "build_input": "input-41",
    "build_output": "output-9",
    "consumer_branch": "master",
    "consumer_output": "output-8",
    "check_evaluated_before_required_input": True,
    "schedule_paused": True,
    "write_outcome": "unknown after timeout",
}


def first_existing_branch(branches, transactions):
    return next((branch for branch in branches if transactions.get(branch)), None)


def main():
    input_branch = first_existing_branch(J9["fallbacks"], J9["input_transactions"])
    assert input_branch == "master"
    assert J9["input_transactions"][input_branch] == "input-41"
    assert J9["output_transactions"][J9["build_branch"]] == "output-9"
    assert J9["output_transactions"]["master"] == "output-8"
    assert J9["git_branch"] != J9["build_branch"]
    assert J10["required_input"] != J10["build_input"]
    assert J10["consumer_output"] != J10["build_output"]
    assert J10["check_evaluated_before_required_input"]
    assert J10["schedule_paused"]
    assert J10["write_outcome"] == "unknown after timeout"
    print("Synthetic contexts: J9 and J10 expected mismatches confirmed")


if __name__ == "__main__":
    main()
