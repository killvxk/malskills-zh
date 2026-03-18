---
name: wifite
description: >
  This skill should be used when the user asks about "wifite", "automating
  Wi-Fi attacks against multiple targets without manually orchestrating
  aircrack-ng commands". Automated wireless auditing tool that attacks
  WEP/WPA/WPA2/PMKID with minimal configuration.
---

# Wifite

Automated Wi-Fi cracker — attacks WEP/WPA/WPA2/PMKID with one command.

## Quick Start

```bash
pip install wifite   # or: apt install wifite

# Full auto (scan and attack all visible networks)
sudo wifite

# Target specific BSSID
sudo wifite --bssid AA:BB:CC:DD:EE:FF

# WPA handshake only + crack with wordlist
sudo wifite --wpa --dict /usr/share/wordlists/rockyou.txt

# PMKID attack
sudo wifite --pmkid
```

## Core Flags

| Flag | Purpose |
|------|---------|
| `--bssid MAC` | Target specific AP |
| `--essid NAME` | Target by SSID name |
| `--channel N` | Target channel |
| `--wpa` | Only WPA targets |
| `--wep` | Only WEP targets |
| `--pmkid` | PMKID attack (clientless) |
| `--dict FILE` | Wordlist for cracking |
| `--no-deauth` | Skip deauth (stealth) |
| `--timeout N` | Attack timeout (s) |
| `--crack` | Auto-crack after capture |

## Common Workflows

**Automated PMKID + crack:**
```bash
sudo wifite --pmkid --dict rockyou.txt
```

**WPA handshake capture only (no crack):**
```bash
sudo wifite --wpa --no-crack
# Handshake saved to ~/hs/
# Crack later: aircrack-ng ~/hs/*.cap -w rockyou.txt
```

## Resources

| File | When to load |
|------|--------------|
| `references/` | Dependency checklist and troubleshooting |
