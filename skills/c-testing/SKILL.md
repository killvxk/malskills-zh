---
name: c-testing
description: >
  This skill should be used when the user asks about "c-testing", "writing",
  "fixing tests for C (C11+) modules". C testing workflow for unit and
  integration tests: harness structure, CTest integration, diagnosing
  failures, and using sanitizers and fuzzing for bug-finding signal.
---

# C Testing

Pragmatic workflow for reliable C tests and bug-finding.

## When to activate

- Adding unit tests for C functions
- Building a small test harness around a module
- Debugging failing tests or memory corruption
- Enabling sanitizers or fuzzing to reproduce crashes

---

## Core rules

- Keep unit tests deterministic and isolated.
- Avoid real network/time in unit tests.
- Run ASan/UBSan in CI for memory and UB signal.

---

## Resources

Load on demand:

- `references/harness.md` — harness structure, assertions, Unity/cmocka options
- `references/cmake-ctest.md` — CMake/CTest patterns, labels, sanitizer presets, MinGW cross-compile
- `references/sanitizers-fuzzing.md` — ASan/UBSan usage and a minimal fuzz target outline
- `references/debugging.md` — gdb/lldb, Valgrind, MinGW objdump/nm, MSVC dumpbin/WinDbg, ASan env vars
