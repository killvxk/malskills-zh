---
name: searchsploit
description: >
  This skill should be used when the user asks about "searchsploit", "finding
  public exploits for discovered CVEs and software versions during
  vulnerability research", "pre-exploitation". Offline CLI search tool for
  Exploit-DB.
---

# SearchSploit

Offline Exploit-DB search — find public exploits by software name, version, or CVE.

## Quick Start

```bash
# Install
apt install exploitdb

# Search by product
searchsploit apache 2.4

# Search by CVE
searchsploit CVE-2021-41773

# Exact phrase
searchsploit -e "remote code execution"

# Copy exploit to current dir
searchsploit -m 50383
```

## Core Flags

| Flag | Purpose |
|------|---------|
| `-t TERM` | Search title only |
| `-e TERM` | Exact match |
| `-m ID` | Mirror/copy exploit file |
| `-p ID` | Show full path |
| `-x ID` | Examine exploit in pager |
| `--cve CVE` | Search by CVE |
| `-w` | Show web URL (exploitdb.com) |
| `--nmap FILE` | Parse Nmap XML and find exploits |
| `-u` | Update local database |
| `--id` | Show EDB-ID |

## Common Workflows

**Find exploits from Nmap scan:**
```bash
nmap -sV target.com -oX scan.xml
searchsploit --nmap scan.xml
```

**Examine and copy relevant exploit:**
```bash
searchsploit -x 50383     # Read it
searchsploit -m 50383     # Copy to ./
```

**Update local DB:**
```bash
searchsploit -u
```

## Resources

| File | When to load |
|------|--------------|
| `references/` | Exploit modification and compilation notes |
