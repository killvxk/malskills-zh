<p align="center">
  <strong>malskills-zh &mdash; 攻击性安全技能集合（中文版）</strong>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg?style=flat" alt="License"></a>
  <img src="https://img.shields.io/badge/version-1.0.0-brightgreen?style=flat" alt="Version">
  <img src="https://img.shields.io/badge/skills-120-orange?style=flat" alt="Skills">
  <img src="https://img.shields.io/badge/categories-16-purple?style=flat" alt="Categories">
</p>

---

适用于 Claude Code 的攻击性安全技能插件。包含 **120 个技能**，覆盖渗透测试、CTF 竞赛和安全研究的全流程，已翻译为中文并转换为 Claude Code 插件格式。

## Quick Start

**Method 1: npx skills**
```
npx skills add killvxk/malskills-zh
```

**Method 2: Claude Code plugin**
```
/plugin marketplace add killvxk/malskills-zh
```

**Method 3: Manual clone**
```bash
git clone https://github.com/killvxk/malskills-zh.git
```

> 所有文件路径均使用相对引用，任何安装方式均可正常工作。

## 技能分类

| 分类 | 数量 | 示例 |
|------|------|------|
| 侦察/OSINT | 19 | nmap, amass, shodan, subfinder, masscan, httpx |
| Web 应用测试 | 15 | sqlmap, burpsuite, nuclei, ffuf, xsstrike, zap |
| Windows/AD | 13 | mimikatz, bloodhound, rubeus, crackmapexec |
| C2 框架 | 8 | sliver, cobalt-strike, covenant, merlin |
| 密码破解 | 7 | hashcat, hydra, john, lazagne |
| 免杀/载荷 | 8 | donut, veil, shellter, shellcode-fluctuation |
| BOF 开发 | 2 | c-bof, cpp-bof |
| 逆向工程 | 4 | ghidra, radare2, x64dbg, binwalk |
| 编程模式 | 13 | c-patterns, python-patterns, golang-patterns, asm-patterns |
| 网络/无线 | 6 | bettercap, wireshark, aircrack-ng, mitmproxy |
| 数据外泄/隧道 | 4 | dnsexfiltrator, ligolo-ng, reverse-ssh |
| 社工/钓鱼 | 4 | evilginx2, gophish, modlishka |
| 权限提升 | 3 | linpeas, linux-exploit-suggester, privesccheck |
| 云安全/凭据 | 7 | gitleaks, pacu, scoutsuite, trufflehog |
| 后渗透 | 3 | nanodump, weevely3, revshells |
| 元技能/工具 | 4 | skill-creator, agent-md-creator, deep-research |

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
| 插件结构 | 新增 `plugin.json` + `marketplace.json` + `index.json` |

## 目录结构

```
.claude-plugin/
├── plugin.json                    # 插件清单
└── marketplace.json               # Marketplace 元数据
skills/
├── nmap/          └── SKILL.md    # 120 个技能，扁平结构
├── sqlmap/        └── SKILL.md
├── sliver/        └── SKILL.md
├── ...
└── skill-creator/                 # 含 references/ + scripts/ + assets/
    ├── SKILL.md
    ├── references/
    ├── scripts/
    └── assets/
index.json                         # 机器可读的技能索引
```

## Skill 结构

每个技能目录包含：

```
skills/{skill-name}/
├── SKILL.md          # 必须 — YAML frontmatter (name + description) + Markdown body
├── references/       # 可选 — 深度参考文档
├── scripts/          # 可选 — 可执行辅助脚本
└── assets/           # 可选 — 模板、静态文件
```

## 法律声明

本仓库所有工具技能仅用于**已授权的安全测试、CTF 竞赛和防御性安全研究**。使用者须确保在合法授权范围内使用。

## 致谢

- [AeonDave/malskill](https://github.com/AeonDave/malskill) — 原始技能库
- [AgentSkills 规范](https://agentskills.io) — 开放的 AI agent 技能格式
- [Claude Code](https://claude.com/claude-code) — Anthropic 的 CLI 工具

## License

MIT
