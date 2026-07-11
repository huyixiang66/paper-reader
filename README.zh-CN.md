# Paper Reader

**AI 编程助手的零依赖论文阅读 Skill。** 一条命令读懂任意 arXiv 论文——无需 API Key、无需安装、无需配置。

专为**科研初学者**设计，帮助你系统化地阅读、理解和记录学术论文。

[![GitHub stars](https://img.shields.io/github/stars/huyixiang66/paper-reader?style=flat&logo=github)](https://github.com/huyixiang66/paper-reader/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![arXiv API](https://img.shields.io/badge/arXiv-API-free-b31b1b?style=flat)](https://arxiv.org/help/api/)
[![Semantic Scholar](https://img.shields.io/badge/Semantic_Scholar-API-free-orange?style=flat)](https://www.semanticscholar.org/product/api)

> **一句话总结：** `paper-reader 1706.03762` → 即时结构化论文摘要。

## ✨ 特性

- **零配置** — 无需 API Key、无需 pip install、无需 Docker。开箱即用。
- **三种阅读模式** — 快速概览、结构化中文笔记、深度 PDF 分析
- **双重 API 降级** — arXiv API（始终可用）+ Semantic Scholar（增强元数据）
- **智能输入解析** — 支持 arXiv ID、URL、DOI 或论文标题
- **防幻觉设计** — 区分论文主张、证据、推论和开放问题
- **双语术语** — `中文（English Term）` 格式，首次出现时 inline 解释
- **结构化输出** — 按论文自身章节顺序组织（摘要→引言→方法→实验→结论）

## 🎯 适合谁？

**Paper Reader 专为科研初学者设计。** 无论你是：

- 刚进实验室、第一次读论文研究生
- 本科生进入课题组需要快速掌握文献
- 自学者想了解前沿研究
- 觉得学术论文太难啃、想要结构化引导的人

Paper Reader 帮助你：
1. **理解** — 在深入阅读全文前获得清晰的结构化概览
2. **做笔记** — 生成按论文结构组织的中文精读笔记
3. **学术语** — 每个关键术语都有中英对照和通俗解释
4. **养成习惯** — 跟随研究者常用的阅读顺序：摘要→引言→方法→实验→讨论

## 🚀 快速开始

### 安装

将 `paper-reader` 文件夹复制到你的 agent skill 目录：

```bash
# Codex CLI
cp -r paper-reader ~/.codex/skills/paper-reader

# Claude Code
cp -r paper-reader ~/.claude/skills/paper-reader

# Cursor / 任何支持 SKILL.md 的 agent
cp -r paper-reader /path/to/your/skills/paper-reader
```

### 使用

```bash
# 快速摘要（默认）
paper-reader "1706.03762"

# 中文研究笔记（~15-20KB）
paper-reader "1706.03762" - mode: note

# 深度 PDF 分析
paper-reader "1706.03762" - mode: deep

# 从 URL
paper-reader "https://arxiv.org/abs/2401.12345"

# 从标题
paper-reader "Attention Is All You Need"
```

## 📖 模式说明

### 快速模式（默认）

快速获取元数据 + 摘要。适合判断是否值得精读。

**输出包含：**
- 论文标题、作者、会议/年份
- 引用次数（来自 Semantic Scholar）
- 完整摘要
- 3-5 个关键点

### 笔记模式

生成完整的中文 Markdown 精读笔记，按论文结构组织。

**输出包含：**
- 摘要精读
- 引言精读
- 相关工作
- 方法（最详细，30-40%）
- 实验（20-30%）
- 讨论与局限
- 结论与未来方向
- 术语 inline 中英对照解释
- 目标大小：15-20KB

### 深度模式

下载 PDF 并执行完整文本提取 + 分析。

**输出包含：**
- 本地保存的 PDF 文件
- 基于全文的结构化笔记
- 缺失/不可读部分的显式声明

## 🏗️ 项目结构

```
paper-reader/
├── SKILL.md              # Agent skill 定义
├── scripts/
│   └── fetch_metadata.py # 元数据获取脚本
├── tests/
│   └── test_metadata.py  # 单元测试
├── LICENSE
├── README.md
├── README.zh-CN.md
└── CHANGELOG.md
```

## 🔧 API 说明

### arXiv API（主力）

- **端点：** `http://export.arxiv.org/api/query`
- **速率限制：** 无（公共学术 API）
- **数据：** 标题、摘要、作者、分类、发表日期
- **可用性：** 始终可用

### Semantic Scholar API（增强）

- **端点：** `https://api.semanticscholar.org/graph/v1/paper/search`
- **速率限制：** 免费层 100 次/分钟
- **数据：** 引用数、会议、年份、TL;DR 摘要
- **降级：** 限流时自动返回空，不影响核心功能

## 🤝 贡献

欢迎贡献！请：

1. Fork 本项目
2. 创建功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'Add amazing feature'`)
4. 推送分支 (`git push origin feature/amazing-feature`)
5. 打开 Pull Request

## 📄 许可证

MIT License — 个人和商业项目均可自由使用。

## 🙏 致谢

- 基于 [arXiv API](https://arxiv.org/help/api/) 和 [Semantic Scholar API](https://www.semanticscholar.org/product/api)
- 为 [Codex CLI](https://github.com/openai/codex)、[Claude Code](https://claude.ai/code)、[Cursor](https://cursor.sh) 设计
