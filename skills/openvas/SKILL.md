---
name: openvas
description: >
  This skill should be used when the user asks about "openvas", "performing
  comprehensive vulnerability assessments against internal networks,
  generating compliance reports", "conducting authenticated scans for known
  CVEs before an engagement". OpenVAS (Greenbone Vulnerability Manager):
  full-featured open-source vulnerability scanner with 60,000+ NVTs.
---

# OpenVAS / Greenbone

Open-source comprehensive vulnerability scanner.

## Quick Start

```bash
# Docker (simplest)
docker run -d -p 9390:9390 -p 443:443 --name gvm greenbone/community-edition
# Web UI: https://localhost (admin/admin default)

# Kali native
sudo gvm-setup && sudo gvm-start
# UI: https://127.0.0.1:9392
```

## Common Workflow (GUI)

1. **Configuration → Targets**: Add hosts/CIDR
2. **Configuration → Scan Configs**: Select "Full and fast"
3. **Scans → Tasks → New Task**: Assign target + config
4. Start task, wait for completion
5. **Reports**: Export as PDF/XML/HTML

## Scan Configs

| Config | Use |
|--------|-----|
| Full and fast | Comprehensive (default) |
| Discovery | Network discovery only |
| System Discovery | Host/service enumeration |
| Host Discovery | Ping-only sweep |

## Resources

| File | When to load |
|------|--------------|
| `references/` | CLI XML API, authenticated scan setup |
