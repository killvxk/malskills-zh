---
name: covenant
description: >
  This skill should be used when the user asks about "covenant", "running
  .NET-native red team operations, leveraging the task library for
  post-exploitation", "training teams on visualized collaborative C2".
  Collaborative .NET C2 framework with web UI, Grunt implants over HTTP/S and
  SMB, built-in task library, and multi-operator support.
---

# Covenant

Collaborative .NET C2 with web interface and Grunt implants.

## Quick Start

```bash
docker run -it -p 7443:7443 ghcr.io/cobbr/covenant
# or: dotnet run --project Covenant/Covenant.csproj
# Access: https://localhost:7443
```

## Core Concepts

| Term | Meaning |
|------|---------|
| Grunt | Implant agent |
| Listener | HTTP/HTTPS/SMB endpoint |
| Launcher | Payload generator (binary, script, etc.) |
| Task | Post-exploitation action |

## Common Tasks

| Task | Purpose |
|------|---------|
| `Shell` | Run shell command |
| `Assembly` | Execute .NET assembly in memory |
| `PowerShell` | Run PowerShell block |
| `SharpHound` | Built-in BloodHound collection |
| `Mimikatz` | Credential dump |
| `PortScan` | Internal port scan |
| `Download / Upload` | File transfer |

## Resources

| File | When to load |
|------|--------------|
| `references/` | REST API usage, custom task creation, SMB chaining |
