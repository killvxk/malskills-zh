#!/usr/bin/env python3
"""Convert AgentSkills format to Claude Code Plugin format."""

import os
import re
import shutil
import json
import yaml
from pathlib import Path

SRC = Path("E:/2025/code_learn/malskill")
DST = Path("E:/2026/malskills-zh")
SKILLS_DIR = DST / "skills"

# Fields to keep in frontmatter
KEEP_FIELDS = {"name", "description"}


def find_all_skills(src: Path) -> list[Path]:
    """Find all directories containing SKILL.md."""
    results = []
    for skill_md in src.rglob("SKILL.md"):
        results.append(skill_md.parent)
    return results


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Parse YAML frontmatter and body from SKILL.md."""
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)", text, re.DOTALL)
    if not match:
        return {}, text
    fm_str, body = match.group(1), match.group(2)
    try:
        fm = yaml.safe_load(fm_str)
    except yaml.YAMLError:
        fm = {}
    return fm or {}, body


def rewrite_description(name: str, desc: str) -> str:
    """Rewrite description to Claude Code third-person trigger style."""
    if not desc:
        return f'This skill should be used when the user asks about "{name}".'

    desc = desc.strip()

    # Extract trigger phrases from "Use when..." clause
    triggers = []
    use_when_match = re.search(r"[Uu]se when\s+(.+?)(?:\.|$)", desc)
    if use_when_match:
        raw = use_when_match.group(1)
        # Split on semicolons, "or", commas followed by verbs
        parts = re.split(r";\s*|,\s+or\s+|,\s+(?=[a-z])", raw)
        for p in parts:
            p = p.strip().rstrip(".")
            if p:
                triggers.append(f'"{p}"')

    # Also extract the tool name as a trigger
    triggers.insert(0, f'"{name}"')

    # Build the functional description (everything before "Use when")
    func_desc = re.sub(r"\s*[Uu]se when\s+.+", "", desc).strip().rstrip(".")
    # Remove leading "tool-name:" prefix if present
    func_desc = re.sub(rf"^{re.escape(name)}:\s*", "", func_desc, flags=re.IGNORECASE).strip()
    # Capitalize first letter
    if func_desc:
        func_desc = func_desc[0].upper() + func_desc[1:]

    trigger_str = ", ".join(triggers[:6])  # Max 6 triggers to keep it concise
    result = f"This skill should be used when the user asks about {trigger_str}. {func_desc}."

    # Clean up double periods
    result = result.replace("..", ".")

    # Cap at 1024 chars
    if len(result) > 1024:
        result = result[:1020] + "..."

    return result


def transform_frontmatter(fm: dict) -> dict:
    """Strip unsupported fields, rewrite description."""
    name = fm.get("name", "unknown")
    desc = fm.get("description", "")

    new_fm = {
        "name": name,
        "description": rewrite_description(name, desc),
    }
    return new_fm


def render_frontmatter(fm: dict) -> str:
    """Render frontmatter as YAML string."""
    # Use block style for long description
    desc = fm["description"]
    lines = ["---"]
    lines.append(f"name: {fm['name']}")

    # Multi-line description if > 80 chars
    if len(desc) > 80:
        lines.append("description: >")
        # Wrap at ~78 chars
        words = desc.split()
        current = "  "
        for w in words:
            if len(current) + len(w) + 1 > 78:
                lines.append(current)
                current = "  " + w
            else:
                current += (" " if len(current) > 2 else "") + w
        if current.strip():
            lines.append(current)
    else:
        lines.append(f'description: "{desc}"')

    lines.append("---")
    return "\n".join(lines) + "\n"


def copy_skill(skill_dir: Path, name: str):
    """Copy skill directory to skills/{name}/, transforming SKILL.md."""
    target = SKILLS_DIR / name
    if target.exists():
        print(f"  WARNING: {name} already exists, skipping")
        return False

    # Copy the entire directory
    shutil.copytree(skill_dir, target)

    # Transform SKILL.md
    skill_md = target / "SKILL.md"
    text = skill_md.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(text)
    new_fm = transform_frontmatter(fm)
    new_text = render_frontmatter(new_fm) + "\n" + body
    skill_md.write_text(new_text, encoding="utf-8")

    return True


def create_plugin_json():
    """Create .claude-plugin/plugin.json."""
    plugin_dir = DST / ".claude-plugin"
    plugin_dir.mkdir(parents=True, exist_ok=True)

    manifest = {
        "name": "malskills-zh",
        "description": "Offensive security skills collection for authorized penetration testing, CTF challenges, and security research. Includes tools for reconnaissance, exploitation, C2 frameworks, evasion, reverse engineering, and programming patterns.",
        "version": "1.0.0",
    }

    (plugin_dir / "plugin.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Created {plugin_dir / 'plugin.json'}")


def copy_agents_md():
    """Copy and update AGENTS.md with new paths."""
    src_file = SRC / "AGENTS.md"
    if not src_file.exists():
        return

    text = src_file.read_text(encoding="utf-8")

    # Update path references
    text = text.replace(
        "knowledge/skill-creator/scripts/init_skill.py",
        "skills/skill-creator/scripts/init_skill.py",
    )
    text = text.replace(
        "knowledge/skill-creator/scripts/quick_validate.py",
        "skills/skill-creator/scripts/quick_validate.py",
    )
    text = text.replace(
        "knowledge/skill-creator/scripts/package_skill.py",
        "skills/skill-creator/scripts/package_skill.py",
    )
    text = text.replace(
        "knowledge/agent-md-creator/",
        "skills/agent-md-creator/",
    )

    # Update project structure section
    old_structure = """- `bof/` — BOF-focused skills; each skill root typically contains `SKILL.md` plus optional `assets/`, `references/`, and `scripts/`.
- `offensive-tools/` — category folders such as `recon/`, `web-app/`, or `windows/`; each category contains one folder per tool skill.
- `programming/` — language and pattern skills such as C/C++, Go, Python, and assembly patterns/testing/performance guidance.
- `knowledge/` — meta-skills and research helpers, including `skill-creator/`, `agent-md-creator/`, and deep-research skills."""

    new_structure = """- `skills/` — all skills in flat structure; each skill folder contains `SKILL.md` plus optional `assets/`, `references/`, and `scripts/`.
- `.claude-plugin/` — Claude Code plugin manifest."""

    text = text.replace(old_structure, new_structure)

    (DST / "AGENTS.md").write_text(text, encoding="utf-8")
    print("Copied and updated AGENTS.md")


def main():
    SKILLS_DIR.mkdir(parents=True, exist_ok=True)

    # Find all skills
    skill_dirs = find_all_skills(SRC)
    print(f"Found {len(skill_dirs)} skills in source repo\n")

    # Track results
    converted = []
    skipped = []

    for skill_dir in sorted(skill_dirs):
        # Read name from frontmatter
        skill_md = skill_dir / "SKILL.md"
        text = skill_md.read_text(encoding="utf-8")
        fm, _ = parse_frontmatter(text)
        name = fm.get("name", skill_dir.name)

        rel = skill_dir.relative_to(SRC)
        print(f"  {rel} -> skills/{name}/", end="")

        if copy_skill(skill_dir, name):
            converted.append(name)
            print(" OK")
        else:
            skipped.append(name)
            print(" SKIPPED")

    # Create plugin manifest
    print()
    create_plugin_json()

    # Copy and update AGENTS.md
    copy_agents_md()

    # Copy .gitignore
    gi_src = SRC / ".gitignore"
    if gi_src.exists():
        shutil.copy2(gi_src, DST / ".gitignore")

    print(f"\nDone: {len(converted)} converted, {len(skipped)} skipped")
    print(f"Output: {DST}")


if __name__ == "__main__":
    main()
