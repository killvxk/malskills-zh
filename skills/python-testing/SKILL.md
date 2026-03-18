---
name: python-testing
description: >
  This skill should be used when the user asks about "python-testing",
  "writing", "reviewing Python tests to improve correctness and reduce
  flakiness". Python testing patterns with pytest: TDD loop, fixtures,
  parametrization, mocking, test organization, async testing, coverage, and CI
  hygiene.
---

# Python Testing

High-signal guidance for writing tests that are **deterministic**, **readable**, and **maintainable**.

## When to activate

- Adding tests (unit/integration) for new or existing code
- Refactoring tests to reduce flakiness
- Designing fixtures and test organization
- Adding coverage, CI checks, or async tests

---

## Core rules

- Prefer **small unit tests** for logic; use integration tests for boundaries.
- Use pytest fixtures to remove duplication, but avoid fixture overengineering.
- Avoid sleeping in tests; synchronize via conditions/events.
- Mock at boundaries (network, time, DB), not everywhere.
- Coverage is a signal: aim for meaningful assertions, not line-hits.

---

## Resources

Load on demand:

- `references/tdd-and-structure.md` — TDD loop, naming, organizing tests
- `references/fixtures-parametrize.md` — fixtures (scopes, autouse), parametrization patterns
- `references/mocking.md` — unittest.mock, patching correctly, async mocks
- `references/async.md` — pytest-asyncio patterns and pitfalls
- `references/coverage-ci.md` — pytest-cov, coverage hygiene, CI tips
- `references/commands.md` — common pytest commands and selectors
