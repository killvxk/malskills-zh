---
name: wpscan
description: >
  This skill should be used when the user asks about "wpscan", "targeting
  WordPress installations to find outdated/vulnerable plugins", "enumerate
  valid usernames for password attacks, verify xmlrpc.php exposure", "check
  for default configurations". WordPress security scanner enumerating users,
  plugins, themes, and known CVEs.
---

# WPScan

WordPress vulnerability and enumeration scanner.

## Quick Start

```bash
wpscan --url https://target.com
wpscan --url https://target.com --enumerate u,p,t --api-token <TOKEN>
wpscan --url https://target.com -U admin -P /usr/share/wordlists/rockyou.txt
```

## Core Flags

| Flag | Purpose |
|------|---------|
| `--url <url>` | Target WordPress URL |
| `--enumerate <items>` | u=users, p=plugins, t=themes, vp=vuln plugins |
| `--api-token <token>` | WPScan API token for CVE data |
| `--plugins-detection` | aggressive / passive / mixed |
| `-U <user>` | Username for brute-force |
| `-P <wordlist>` | Password wordlist |
| `--proxy <proxy>` | HTTP proxy |
| `-o <file>` | Output file |

## Common Findings

| Finding | Impact |
|---------|--------|
| Outdated plugins with CVEs | RCE / LFI / SQLi |
| User enumeration via author archive | Enables password attacks |
| xmlrpc.php enabled | Brute-force amplification |
| readme.html / license.txt | WordPress version disclosure |

## Resources

| File | When to load |
|------|--------------|
| `references/` | Authenticated scan, XML-RPC abuse |
