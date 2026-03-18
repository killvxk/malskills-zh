#!/usr/bin/env python3
"""Fix description rewriting issues in converted SKILL.md files.

Addresses 3 systemic problems:
1. "asked to" redundancy nested inside trigger phrases
2. Mid-clause truncation when splitting compound sentences
3. Trigger collapse to bare tool name when no "Use when" clause
"""

import re
import yaml
from pathlib import Path

SKILLS_DIR = Path("E:/2026/malskills-zh/skills")
# Also read originals for comparison
SRC = Path("E:/2025/code_learn/malskill")


def parse_frontmatter(text: str) -> tuple[dict, str]:
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)", text, re.DOTALL)
    if not match:
        return {}, text
    fm_str, body = match.group(1), match.group(2)
    try:
        fm = yaml.safe_load(fm_str)
    except yaml.YAMLError:
        fm = {}
    return fm or {}, body


def find_original(name: str) -> Path | None:
    """Find the original SKILL.md in the source repo."""
    for p in SRC.rglob("SKILL.md"):
        text = p.read_text(encoding="utf-8")
        fm, _ = parse_frontmatter(text)
        if fm.get("name") == name:
            return p
    return None


def extract_triggers_from_use_when(use_when_text: str) -> list[str]:
    """Smartly extract trigger phrases from a 'Use when...' clause.

    Handles compound sentences without breaking mid-phrase.
    """
    text = use_when_text.strip().rstrip(".")

    # Remove leading "asked to" / "the user asks to" / "you need to"
    text = re.sub(r"^(?:asked to|the user asks to|you need to)\s+", "", text)

    # Split on semicolons first (strongest delimiter)
    segments = [s.strip() for s in text.split(";")]

    triggers = []
    for seg in segments:
        seg = seg.strip().rstrip(".")
        if not seg:
            continue

        # Split on " or " only at the top level (not inside parentheses)
        parts = re.split(r",?\s+or\s+", seg)

        for part in parts:
            part = part.strip().rstrip(".")
            if not part:
                continue

            # Remove leading "asked to" / "the user asks to"
            part = re.sub(r"^(?:asked to|the user asks to)\s+", "", part)

            # Don't split on commas if the phrase contains parentheses
            if "(" in part:
                triggers.append(part)
                continue

            # Split on commas only if what follows looks like a new verb phrase
            # (starts with a verb-like word), not a continuation
            comma_parts = re.split(r",\s+", part)
            if len(comma_parts) > 1:
                # Check if the parts after comma start with verbs
                merged = [comma_parts[0]]
                for cp in comma_parts[1:]:
                    # If starts with a common verb or gerund, treat as new phrase
                    if re.match(r"(?:create|generate|build|run|test|scan|find|extract|dump|perform|identify|convert|use|need|debug|analyze|write|review|refactor|enumerate|crack|exploit|bypass|capture|poison|pivot|brute|fuzz|detect|monitor|intercept|relay|decrypt|resolve|discover|scrape|harvest|collect|assess|audit|map|profile|inspect|configure|deploy|install|set up|check)", cp, re.I):
                        merged.append(cp)
                    else:
                        # Continuation of previous phrase
                        merged[-1] += ", " + cp
                triggers.extend(merged)
            else:
                triggers.append(part)

    # Clean up
    cleaned = []
    for t in triggers:
        t = t.strip().rstrip(".")
        # Remove leading "or "
        t = re.sub(r"^or\s+", "", t)
        # Remove leading "and "
        t = re.sub(r"^and\s+", "", t)
        if t and len(t) > 2:
            cleaned.append(t)

    return cleaned


def extract_triggers_from_description(desc: str, name: str) -> list[str]:
    """Extract triggers from the full description when no 'Use when' clause exists.

    Extracts key verb phrases and noun phrases from the description.
    """
    # Remove the tool name prefix if present
    cleaned = re.sub(rf"^{re.escape(name)}:\s*", "", desc, flags=re.IGNORECASE).strip()

    # Try to find action verbs and their objects
    triggers = []

    # Look for phrases with key action patterns
    action_patterns = [
        r"(?:for|supports?|enables?|performs?|provides?)\s+(.+?)(?:\.|,\s*and\s|$)",
        r"(?:dump|extract|capture|scan|enumerate|crack|exploit|analyze|detect|intercept)\w*\s+(.+?)(?:\.|,|;|$)",
    ]

    for pattern in action_patterns:
        for m in re.finditer(pattern, cleaned, re.IGNORECASE):
            phrase = m.group(1).strip().rstrip(".")
            if len(phrase) > 5 and len(phrase) < 80:
                triggers.append(phrase)

    # If still no triggers, take key noun phrases
    if not triggers:
        # Split on commas and "and"
        parts = re.split(r",\s+|\s+and\s+", cleaned)
        for p in parts:
            p = p.strip().rstrip(".")
            if len(p) > 5 and len(p) < 60:
                triggers.append(p)

    return triggers[:5]


def build_description(name: str, original_desc: str) -> str:
    """Build a high-quality Claude Code description from the original."""
    if not original_desc:
        return f'This skill should be used when the user asks about "{name}".'

    desc = original_desc.strip()

    # Split into functional part and "Use when" part
    use_when_match = re.search(r"[Uu]se (?:when|for)\s+(.+?)$", desc, re.DOTALL)

    if use_when_match:
        func_part = desc[:use_when_match.start()].strip().rstrip(".")
        use_when_part = use_when_match.group(1)
        triggers = extract_triggers_from_use_when(use_when_part)
    else:
        func_part = desc.strip().rstrip(".")
        triggers = extract_triggers_from_description(desc, name)

    # Clean up functional part - remove tool name prefix
    func_part = re.sub(rf"^{re.escape(name)}:\s*", "", func_part, flags=re.IGNORECASE).strip()
    if func_part:
        func_part = func_part[0].upper() + func_part[1:]

    # Build trigger phrases, always include tool name first
    trigger_phrases = [f'"{name}"']
    for t in triggers[:5]:  # Max 5 additional triggers
        # Skip if it's just the tool name repeated
        if t.lower().strip('"') == name.lower():
            continue
        trigger_phrases.append(f'"{t}"')

    trigger_str = ", ".join(trigger_phrases)

    result = f"This skill should be used when the user asks about {trigger_str}. {func_part}."

    # Clean up
    result = result.replace("..", ".")
    result = result.replace("  ", " ")

    if len(result) > 1024:
        result = result[:1020] + "..."

    return result


def render_frontmatter(fm: dict) -> str:
    desc = fm["description"]
    lines = ["---"]
    lines.append(f"name: {fm['name']}")

    if len(desc) > 80:
        lines.append("description: >")
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


def main():
    fixed = 0
    errors = []

    for skill_dir in sorted(SKILLS_DIR.iterdir()):
        if not skill_dir.is_dir():
            continue

        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            continue

        name = skill_dir.name

        # Read original description from source repo
        original_path = find_original(name)
        if not original_path:
            errors.append(f"{name}: original not found in source repo")
            continue

        orig_text = original_path.read_text(encoding="utf-8")
        orig_fm, _ = parse_frontmatter(orig_text)
        orig_desc = orig_fm.get("description", "")

        # Read current converted file
        conv_text = skill_md.read_text(encoding="utf-8")
        _, body = parse_frontmatter(conv_text)

        # Build new description from ORIGINAL (not the already-converted one)
        new_desc = build_description(name, orig_desc)

        new_fm = {"name": name, "description": new_desc}
        new_text = render_frontmatter(new_fm) + "\n" + body

        skill_md.write_text(new_text, encoding="utf-8")
        fixed += 1
        print(f"  {name}: OK ({len(new_desc)} chars)")

    print(f"\nFixed: {fixed}")
    if errors:
        print(f"Errors: {len(errors)}")
        for e in errors:
            print(f"  {e}")


if __name__ == "__main__":
    main()
