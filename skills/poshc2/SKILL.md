---
name: poshc2
description: >
  This skill should be used when the user asks about "poshc2", "operating in
  environments with available PowerShell and network proxies", "needing
  proxy-aware beacons", "performing post-exploitation with built-in credential
  access and lateral movement modules". Proxy-aware Python C2 framework with
  implants in PowerShell, C#, Python, and C.
---

# PoshC2

Proxy-aware C2 with PowerShell, C#, Python, C implants.

## Quick Start

```bash
curl -sSL https://raw.githubusercontent.com/nettitude/PoshC2/master/Install.sh | bash
posh-project -n MyOp
posh-server
posh
posh-payloads
```

## Handler REPL Commands

| Command | Purpose |
|---------|---------|
| `listimplants` | Show active implants |
| `implant <id>` | Interact with implant |
| `run <cmd>` | Run system command |
| `loadmodule <module>` | Load post-ex module |
| `inject-shellcode` | Inject shellcode into process |
| `invoke-mimikatz` | Run Mimikatz |
| `sharphound` | BloodHound collection |
| `get-system` | Attempt privilege escalation |

## Resources

| File | When to load |
|------|--------------|
| `references/` | Module list, proxy config, C implant usage |
