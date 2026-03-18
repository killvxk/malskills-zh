---
name: golang-patterns
description: >
  This skill should be used when the user asks about "golang-patterns",
  "writing idiomatic Go code", "reviewing Go PRs for best practices",
  "refactoring Go error handling, interfaces, or concurrency". Idiomatic Go
  patterns, best practices, and conventions for building robust, readable, and
  maintainable Go code.
---

# Go Patterns

This skill focuses on **idiomatic Go design and code review guidance**.

If your task is primarily measurement/profiling/optimization, use `golang-performance`.

## When to activate

- Writing new Go code (packages, APIs, services)
- Reviewing PRs for idioms, readability, and maintainability
- Refactoring for cleaner error handling and smaller interfaces
- Designing concurrency flows with cancellation and backpressure

---

## Core principles (high signal)

- **gofmt is non-negotiable.** Style debates end at `gofmt`.
- Prefer **clarity**: small functions, early returns, explicit control flow.
- Make the **zero value useful**.
- Keep **interfaces small**; define them where they’re consumed.
- Handle **errors explicitly**; wrap with context; avoid `panic` for control flow.
- Concurrency should be **bounded** and **cancellable**; avoid goroutine leaks.

---

## Quick review checklist

- Naming: MixedCaps for exported, no underscores, packages short and lower-case
- Errors: `fmt.Errorf("context: %w", err)`, `errors.Is/As` used correctly
- Context: `ctx` is first param; cancellation propagates; no `context.Context` stored in structs
- Interfaces: accept interfaces, return concrete types; no “kitchen-sink” interfaces
- Concurrency: goroutines have a stop condition; channels are closed by senders; backpressure exists
- Tooling: `go test ./...`, `go test -race ./...`, `go vet ./...`

---

## Resources

Load on demand (progressive disclosure):

- `references/effective-go.md` — distilled Effective Go + Code Review Comments pointers
- `references/errors.md` — wrapping, sentinel vs typed errors, validation, retryable errors
- `references/interfaces.md` — interface placement, design patterns, optional behavior
- `references/concurrency.md` — cancellation, errgroup, leaks, worker pools, backpressure
- `references/api-and-structs.md` — receiver rules, functional options, embedding
- `references/package-layout.md` — project layout, package naming, dependency injection
- `references/tooling.md` — gofmt/goimports, vet, staticcheck, golangci-lint guidance
