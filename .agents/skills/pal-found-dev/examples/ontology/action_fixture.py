"""Synthetic Action business policy; not a Foundry permission evaluator."""


def validate_priority(ticket, priority, groups):
    if "dispatchers" not in groups:
        return "identity denied"
    if ticket["status"] != "Open":
        return "ticket closed"
    if priority not in {"P0", "P1", "P2"}:
        return "priority invalid"
    return "accepted"


def recover_submission(edit_observed, webhook_observed):
    if edit_observed is None:
        return "inspect known target and correlated logs before replay"
    if edit_observed and not webhook_observed:
        return "recover side effect separately; do not replay object edit"
    return "verify target and side-effect evidence"


def main():
    ticket = {"id": "t1", "status": "Open", "priority": "P2"}
    assert validate_priority(ticket, "P0", {"dispatchers"}) == "accepted"
    assert validate_priority(ticket, "P9", {"dispatchers"}) == "priority invalid"
    assert validate_priority({**ticket, "status": "Closed"}, "P0", {"dispatchers"}) == "ticket closed"
    assert validate_priority(ticket, "P0", set()) == "identity denied"
    assert recover_submission(None, False) == "inspect known target and correlated logs before replay"
    assert recover_submission(True, False) == "recover side effect separately; do not replay object edit"
    assert ticket["priority"] == "P2"
    print("Action decision fixtures passed: accepted/rejected inputs, denied identity and uncertain/partial effects")


if __name__ == "__main__":
    main()
