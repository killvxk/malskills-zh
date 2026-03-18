---
name: binwalk
description: >
  This skill should be used when the user asks about "binwalk", "reversing IoT
  firmware, embedded devices", "binary blobs during hardware/firmware security
  assessments". Analyze and extract firmware images, identifying embedded file
  systems, compressed archives, and executable code.
---

# Binwalk

Firmware analysis and extraction — identify and extract embedded files from binary blobs.

## Quick Start

```bash
# Install
apt install binwalk

# Scan firmware for signatures
binwalk firmware.bin

# Extract all found content
binwalk -e firmware.bin
# Output in _firmware.bin.extracted/

# Recursive extraction
binwalk -eM firmware.bin
```

## Core Flags

| Flag | Purpose |
|------|---------|
| `-e` | Extract found files |
| `-M` | Recursive extraction (matryoshka) |
| `-B` | Signature scan (default) |
| `-E` | Entropy analysis |
| `-A` | Disassemble CPU instructions |
| `-C DIR` | Output directory |
| `-q` | Quiet mode |
| `--dd TYPE:OFFSET:SIZE` | Manual extraction |
| `-l N` | Limit extraction size |

## Common Workflows

**Full firmware analysis:**
```bash
binwalk -eM firmware.bin -C ./extracted/
ls ./extracted/
```

**Find compressed/encrypted regions (entropy):**
```bash
binwalk -E firmware.bin
# High entropy = encrypted/compressed, low = plaintext
```

**Find hardcoded strings after extraction:**
```bash
binwalk -eM firmware.bin
find ./_firmware.bin.extracted/ -type f | xargs strings | grep -i "password\|admin\|key"
```

## Resources

| File | When to load |
|------|--------------|
| `references/` | Filesystem types and QEMU emulation notes |
