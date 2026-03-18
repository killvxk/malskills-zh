---
name: wireshark
description: >
  This skill should be used when the user asks about "wireshark", "analysing
  pcap files, capturing live traffic for credential extraction, following
  TCP/HTTP streams", "investigating network anomalies during red team
  operations. CLI equivalent: tshark". Network protocol analyzer for capturing
  and inspecting packets.
---

# Wireshark / tshark

Packet capture and protocol analysis.

## Quick Start (tshark CLI)

```bash
tshark -i eth0 -w capture.pcap
tshark -r capture.pcap -Y "http" -T fields -e http.host -e http.request.uri
tshark -r capture.pcap -Y "ntlmssp" -T fields -e ip.src -e ntlmssp.auth.username
```

## Key Display Filters

| Filter | Purpose |
|--------|---------|
| `tcp.port == 445` | SMB traffic |
| `http.request.method == "POST"` | POST requests |
| `ftp.request.command == "PASS"` | FTP passwords |
| `ntlmssp` | NTLM auth |
| `kerberos` | Kerberos traffic |
| `dns` | DNS queries |
| `ip.addr == 10.0.0.5` | Traffic to/from IP |

## Common Workflows

### Follow TCP stream
```bash
tshark -r capture.pcap -q -z follow,tcp,ascii,0
```

### Export HTTP objects
Wireshark GUI: File → Export Objects → HTTP

## Resources

| File | When to load |
|------|--------------|
| `references/` | Filter cheatsheet, credential extraction patterns |
