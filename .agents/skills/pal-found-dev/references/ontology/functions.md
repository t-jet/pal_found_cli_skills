# Function runtimes and publication

[Development guide](../../SKILL.md)

## Concept and lifecycle

A Function exposes typed logic to Workshop, Actions or APIs. Its source commit,
live preview, released version and consumer's selected version are separate states.
A query returns values; an Ontology edit Function returns edits applied through a
[function-backed Action](actions.md). Directly previewing returned edits does not
apply them. Platform authentication and [object permissions](security.md) still apply.

Choose the repository runtime before coding. TypeScript v1 uses exported decorated
class methods. TypeScript v2 uses a default exported function in a same-named file
and supports OSDK; changing that file path creates a different function identity.
Python uses `@function` and annotated parameters/results. Python supports Pipeline
Builder Functions; TypeScript v2 supports interface-based code. Runtime libraries
and enabled deployment features vary; do not mix their import or registration APIs.

## Prerequisites

Prepare the matching Functions repository template and its packaged dependencies,
Node/TypeScript or Python environment, editable branch and release rights. Ontology
work needs generated bindings for exactly the selected types and SDK version.
For branched schemas, TypeScript v2 and Python need a local Ontology SDK; see
[integration boundaries](../branching/integrations.md).

Pure arithmetic can be inspected locally. Live preview, tagging/releasing and invoking
published Functions need authorized enrollment. Owners configure protected branches,
review requirements and stable-tag restrictions. A package import is no access grant.

## Procedure

1. Select + New > Repository and the required Functions template. Create a sandbox
   branch. Preserve the generated source tree and dependency environment.
2. Add resource imports for required objects/links, generate bindings, and use their
   actual API names. Declare input/output types and bounded input validation.
3. Use the runtime's registration syntax below. Test pure logic, then open the
   Functions helper and Live preview; inspect result and runtime errors.
4. Commit source and wait for checks. Review/merge using the protected branch policy.
   Release from the intended branch with Tags and releases > New tag > Tag and release.
   A version tag releases repository Functions; inspect release-check completion.
5. Select the published version in the registry/consumer and Run with the same inputs.
   Confirm the consumer's version binding. A version range can advance to newer stable
   releases; a prerelease does not satisfy ordinary stable ranges.

## Worked example

These independent examples compute 2 + 3 = 5. Put each in its matching template;
these are source examples, not recorded Foundry executions.

TypeScript v1, `functions-typescript/src/index.ts`:

```typescript
import { Function, Integer } from "@foundry/functions-api";
export class Arithmetic {
    @Function()
    public add(a: Integer, b: Integer): Integer { return a + b; }
}
```

TypeScript v2, `typescript-functions/src/functions/add.ts`:

```typescript
export default function add(a: number, b: number): number { return a + b; }
```

Python, a module under the template's `python-functions` source package:

```python
from functions.api import function, Integer

@function
def add(a: Integer, b: Integer) -> Integer:
    return a + b
```

For Python edits, the generated client exposes `client.ontology.edits()`. Declare
`@function(edits=[ActualObjectType])`, obtain an editable object through
`edits.objects.ActualObjectType.edit(object_or_primary_key)`, assign the property,
and return `edits.get_edits()` as `list[OntologyEdit]`. `ActualObjectType` must be
imported from the generated bindings. Primary keys are immutable; assign a new list
for array properties because in-place list mutations can be dropped. Configure an
Action that applies these returned edits before checking persisted state.

## Expected result and checks

Record source commit, runtime/template, release version and invocation inputs/result.
Test zero, negative values and boundary values appropriate to the declared numeric
type. Preview resources/limits can differ from published execution. For edit logic,
record Action validation, submit result and a fresh object read; returned edits alone
prove only edit construction. Read-after-write queries inside a Function require the
supported staged-write feature and its availability, not ordinary object mutation.

## Failures and recovery

| Symptom | Recovery |
| --- | --- |
| Function absent | Check v1 class export/decorator, v2 default export/file name or Python decorator/type annotations; rerun checks. |
| Bindings missing | Add the exact resource import and regenerate the prepared SDK. |
| Release pending | Inspect release checks and permission propagation; preserve the prior consumer version until usable. |
| Action produces no persisted edit | Verify returned edits, Action binding and validation, then reread under the acting identity. |
| Consumer changed after release | Inspect its version range; select the approved version and retest. |

Optional source attribution: [v1 syntax](https://www.palantir.com/docs/foundry/functions/typescript-v1-getting-started),
[v2 lifecycle](https://www.palantir.com/docs/foundry/functions/typescript-v2-getting-started),
[Python lifecycle](https://www.palantir.com/docs/foundry/functions/python-getting-started),
[runtime capabilities](https://www.palantir.com/docs/foundry/functions/language-feature-support),
[Python edit behavior](https://www.palantir.com/docs/foundry/functions/python-ontology-edits).
