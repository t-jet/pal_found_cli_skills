# Formal execution evidence

`rest085_formal_execute.py` is the byte-preserved harness used for TESTEXEC-082.
It ran from the parent workspace's `.ept/tmp` directory against the adjacent
`feature015_integration` checkout. Its relative paths describe that execution
layout; this archived copy is evidence, not a portable command entry point.

`rest085_formal_execute.log` records the 91 checks from that run. The two closure
exports record the observed tracker state. The acceptance manifest at
`../rest-domain-formal-qa-085-acceptance.json` binds these files to their hashes.

Run `python -m pytest -q tests/test_offline_rest_085_review.py` from the skills
repository to verify the archived evidence, current source and asset identities,
case coverage, and accepted operation records. Live tenant behavior remains
outside this execution's scope.
