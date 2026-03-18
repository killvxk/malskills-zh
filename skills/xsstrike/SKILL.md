---
name: xsstrike
description: >
  This skill should be used when the user asks about "xsstrike", "testing for
  reflected, stored", "DOM-based XSS", "identifying injection contexts",
  "generating payloads tailored to bypass specific filters". Advanced XSS
  detection suite with context-aware payload generation, DOM XSS analysis,
  site crawler, and WAF-bypass fuzzer.
---

# XSStrike

Context-aware XSS detection and payload generation.

## Quick Start

```bash
python xsstrike.py -u "http://target.com/search?q=test"
python xsstrike.py -u "http://target.com" --crawl
python xsstrike.py -u "http://target.com/feedback" --blind
python xsstrike.py -u "http://target.com/?q=test" --fuzzer
```

## Core Flags

| Flag | Purpose |
|------|---------|
| `-u <url>` | Target URL with parameter |
| `--crawl` | Crawl and test all discovered links |
| `--blind` | Blind XSS mode (no reflection check) |
| `--fuzzer` | Fuzz with payload list |
| `-l <level>` | Crawl depth |
| `--data <post>` | POST data |
| `-p <param>` | Test specific parameter only |
| `--headers <h>` | Custom headers |
| `--proxy <proxy>` | Route through proxy |

## Resources

| File | When to load |
|------|--------------|
| `references/` | DOM XSS testing, WAF bypass techniques |
