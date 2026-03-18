# malskills-zh

Offensive security skills 中文版 — 适用于 Claude Code 插件格式。

## 概述

本仓库包含 **120 个安全技能**，覆盖渗透测试、CTF 竞赛和安全研究的各个领域，已翻译为中文并转换为 Claude Code 插件格式。

## 原始项目

- **原始仓库**: [AeonDave/malskill](https://github.com/AeonDave/malskill)
- **原始格式**: [AgentSkills 开放规范](https://agentskills.io/specification)（适用于所有 AI agent）
- **原始作者**: AeonDave
- **原始许可证**: MIT

## 本仓库的改动

| 改动项 | 说明 |
|--------|------|
| 格式转换 | AgentSkills → Claude Code Plugin |
| 目录扁平化 | 深层分类目录 → `skills/` 扁平结构 |
| Frontmatter 精简 | 移除 `license`/`compatibility`/`metadata`，仅保留 `name` + `description` |
| Description 改写 | 通用描述 → Claude Code 第三人称触发式 |
| 语言翻译 | 英文 → 中文（代码块保持英文） |
| 新增 CLAUDE.md | Claude Code 原生项目指令（自动加载） |

## 技能分类

| 分类 | 数量 | 示例 |
|------|------|------|
| 侦察/OSINT | ~20 | nmap, amass, shodan, subfinder |
| Web 应用测试 | ~18 | sqlmap, burpsuite, ffuf, nuclei |
| Windows/AD | ~16 | mimikatz, bloodhound, rubeus, crackmapexec |
| C2 框架 | ~14 | sliver, cobalt-strike, covenant |
| 密码破解 | ~9 | hashcat, hydra, john |
| 免杀/载荷 | ~10 | donut, veil, shellter |
| BOF 开发 | 2 | c-bof, cpp-bof |
| 逆向工程 | 4 | ghidra, radare2, x64dbg, binwalk |
| 编程模式 | 13 | c-patterns, python-patterns, golang-patterns |
| 元技能 | 4 | skill-creator, agent-md-creator, deep-research |
| 其他 | ~10 | 社工、无线、数据外泄、提权 |

## 安装使用

```bash
# 作为 Claude Code 插件加载
claude --plugin-dir /path/to/malskills-zh

# 或将 skills/ 目录链接到 .claude/skills/
```

## 法律声明

本仓库所有工具技能仅用于**已授权的安全测试、CTF 竞赛和防御性安全研究**。使用者须确保在合法授权范围内使用。

## 致谢

- [AeonDave/malskill](https://github.com/AeonDave/malskill) — 原始技能库
- [AgentSkills 规范](https://agentskills.io) — 开放的 AI agent 技能格式
- [Claude Code](https://claude.com/claude-code) — Anthropic 的 CLI 工具
