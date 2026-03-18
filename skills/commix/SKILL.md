---
name: commix
description: >
  This skill should be used when the user asks about "commix", "detecting and
  exploiting command injection vulnerabilities in web parameters, cookies",
  "HTTP headers", "escalating from injection to interactive shell access".
  Automated OS command injection detection and exploitation tool supporting
  classic, time-based, and file-based techniques.
---

# Commix

Automated OS command injection detection and exploitation.

## Quick Start

```bash
commix --url="http://target.com/page?ip=127.0.0.1"
commix --url="http://target.com/ping" --data="ip=127.0.0.1"
commix -r request.txt
commix --url="http://target.com/?ip=1" --os-shell
```

## Core Flags

| Flag | Purpose |
|------|---------|
| `--url <url>` | Target URL |
| `--data <data>` | POST body |
| `-r <file>` | Burp-format request file |
| `--cookie <c>` | Session cookie |
| `--os-cmd <cmd>` | Run single OS command |
| `--os-shell` | Interactive pseudo shell |
| `--technique <t>` | classic / timebased / tempfile-based / file-based |
| `--level <1-3>` | Fuzz depth |
| `--proxy <proxy>` | HTTP proxy |
| `--batch` | Non-interactive defaults |

## Resources

| File | When to load |
|------|--------------|
| `references/` | Blind injection, file upload via command injection |
