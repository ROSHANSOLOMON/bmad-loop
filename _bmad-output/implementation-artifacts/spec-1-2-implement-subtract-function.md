---
title: 'Implement subtract function'
type: 'feature'
created: '2026-11-19'
status: 'done'
baseline_revision: '3916e3655a9aaa36c893878749cc67029aaf4072'
baseline_commit: '3916e3655a9aaa36c893878749cc67029aaf4072'
review_loop_iteration: 0
followup_review_recommended: false
context: []
warnings: []
deferred: []
---

<intent-contract>

## Intent

**Problem:** `calculator.py` provides addition and multiplication but does not provide the requested subtraction operation.

**Approach:** Add a simple `subtract(a, b)` function that returns `a - b` and add basic unit tests for the operation.

## Boundaries & Constraints

**Always:** Preserve the existing `add` and `multiply` behavior. Keep the implementation simple.

**Never:** Add unrelated calculator operations, dependencies, or input-validation policy not required by the request.

## I/O & Edge-Case Matrix

| Scenario | Input / State | Expected Output / Behavior | Error Handling |
|----------|--------------|---------------------------|----------------|
| Integer operands | `subtract(9, 4)` | Returns `5` | No error expected |
| Fractional operands | `subtract(5.5, 2)` | Returns `3.5` | No error expected |
| Negative result | `subtract(3, 8)` | Returns `-5` | No error expected |

</intent-contract>

## Code Map

- `calculator.py` -- Contains `add(a, b)` and `multiply(a, b)`; add `subtract(a, b)` beside these functions and preserve the existing module behavior.
- `requirement.md:11-18` -- Defines the requested subtraction operation and basic-test requirement.
- `tests/test_calculator.py` -- Existing calculator unit-test module; add focused subtraction cases here.

## Tasks & Acceptance

**Execution:**
- [x] `calculator.py` -- Add `subtract(a, b)` that returns `a - b` -- Implements the requested operation.
- [x] `tests/test_calculator.py` -- Add unit tests for integer, fractional, negative-result, and zero operands -- Verifies the subtraction behavior.

**Acceptance Criteria:**
- Given two numeric operands, when `subtract(a, b)` is called, then it returns the first operand minus the second operand.
- Given the existing calculator operations, when `calculator.py` is used, then `add(a, b)` and `multiply(a, b)` continue to return their original results.
- Given the focused calculator tests, when they are run, then all subtraction cases pass.

## Spec Change Log

## Review Triage Log

| Verdict | Evidence |
|---------|----------|
| false | The I/O matrix omission finding does not describe a code defect: zero operands are covered by `test_subtract_zero_operands`, and the matrix omission was outside the implementation diff. |
| false | The verification command was executed and its output showed all 10 unit tests passing; the absence of stored command output in the diff is not a runtime verification gap. |
| low | The calculator file lacks a trailing newline after its unchanged `__main__` block, but this is cosmetic, existed before the change, and would not affect everyday use. |
| false | Boolean, string, and other unsupported operand types are explicitly outside the spec's simple numeric-operand contract, and the spec forbids added input-validation policy. |
| false | Negative first operands and both-negative operands are handled by direct Python subtraction; no special guard or separate behavior is required. |
| false | The unchanged `__main__` demonstration is not part of the subtraction acceptance criteria, and preserving existing behavior does not require updating it. |

## Verification

**Commands:**
- `python -m unittest discover -s tests -v` -- expected: all calculator unit tests pass.
## Auto Run Result

Status: done

_Appended by the bmad-loop orchestrator (missing-marker repair, #224): the session finalized this spec's frontmatter without its `## Auto Run Result` marker, so the orchestrator synthesized the result from the frontmatter and appended this section._

Synthesized by the bmad-loop orchestrator from frontmatter status `done` for story `1-2-implement-subtract-function` (session finalized the spec without appending its marker).
