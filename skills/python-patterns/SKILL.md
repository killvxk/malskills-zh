---
name: python-patterns
description: >
  This skill should be used when the user asks about "python-patterns",
  "writing", "reviewing Python code and APIs". Pythonic patterns and best
  practices for writing readable, robust Python: typing, error handling, data
  modeling, iteration, resource management, project layout, and tooling.
---

# Python Patterns

This skill is for **day-to-day Python code quality**: readability, correctness, maintainability.

If you are doing asyncio-heavy work, prefer `python-async-patterns` for structured concurrency, cancellation, and backpressure.

## When to activate

- Writing/refactoring Python modules, libraries, services
- Reviewing PRs for idioms, clarity, and footguns
- Introducing typing or improving error handling
- Designing lightweight data models and APIs

---

## Core principles (high signal)

- Readability beats cleverness.
- Be explicit at boundaries (I/O, parsing, network). Keep inner code simple.
- Prefer small, typed functions with clear names.
- Use context managers for resource safety.
- Raise specific exceptions and preserve causes (`raise ... from e`).

---

## Quick review checklist

- No mutable default arguments; `None` sentinel used
- `is None` / `is not None` (not `== None`)
- Specific `except` clauses; no bare `except:`
- Types: public functions/classes have annotations; complex types use aliases
- Files/paths use `pathlib.Path` where appropriate
- Iteration uses comprehensions/generators only when simple

---

## Resources

Load on demand:

- `references/typing.md` — modern typing (3.11), aliases, Protocol, generics
- `references/errors.md` — exception hygiene, custom errors, chaining, boundaries
- `references/data-models.md` — dataclasses, NamedTuple, immutability, validation
- `references/iteration.md` — comprehensions vs loops, generators, itertools
- `references/resources.md` — context managers, cleanup, temp files
- `references/performance.md` — simple perf rules (avoid premature optimization)
- `references/layout-tooling.md` — project layout, ruff/mypy/pytest notes
