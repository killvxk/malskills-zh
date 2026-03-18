# malskills-zh — Claude Code Plugin

Offensive security skills collection (120 skills) for authorized penetration testing, CTF challenges, and security research.

## Commands

```bash
# Scaffold a new skill
python skills/skill-creator/scripts/init_skill.py <skill-name> --path skills/<skill-name> --resources references

# Validate one skill
python skills/skill-creator/scripts/quick_validate.py skills/<skill-name>

# Package one skill
python skills/skill-creator/scripts/package_skill.py skills/<skill-name>

# Validate all skills
for d in skills/*/; do python skills/skill-creator/scripts/quick_validate.py "$d"; done
```

## Project structure

- `skills/` — 120 skills in flat structure; each folder contains `SKILL.md` plus optional `assets/`, `references/`, `scripts/`
- `.claude-plugin/plugin.json` — Claude Code plugin manifest
- `convert.py` / `fix_descriptions.py` — format conversion utilities (from AgentSkills format)

## Conventions

- Every skill folder must contain `SKILL.md` with YAML frontmatter (`name` + `description` only)
- `name` must match the folder name, lowercase hyphens only
- `description` must use third-person trigger style: "This skill should be used when the user asks about..."
- Keep `SKILL.md` under 500 lines / 2000 words; move detail to `references/`
- `scripts/` for deterministic helpers, `assets/` for templates/static files
- Each skill folder is independent; read the local `SKILL.md` before editing

## Testing

- After changing a skill, validate with `quick_validate.py` before finishing
- After changing shared scaffolding in `skills/skill-creator/`, revalidate affected skills
- Prefer the smallest relevant validation command first

## Boundaries

- Ask before large restructures across many skill folders or mass renames
- Never add fake commands or placeholder paths
- Code comments in English, technical, precise, brief
