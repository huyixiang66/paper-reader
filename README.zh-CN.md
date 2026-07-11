# Paper Reader

一个供 AI 编程助手使用的论文阅读 Skill。输入 arXiv ID、URL、DOI 或论文标题，Skill 获取元数据、可选下载 PDF，并生成结构化摘要或中文 Markdown 研究笔记。

[![GitHub stars](https://img.shields.io/github/stars/huyixiang66/paper-reader?style=flat&logo=github)](https://github.com/huyixiang66/paper-reader/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![arXiv API](https://img.shields.io/badge/arXiv-API-free-b31b1b?style=flat)](https://arxiv.org/help/api/)
[![Semantic Scholar](https://img.shields.io/badge/Semantic_Scholar-API-free-orange?style=flat)](https://www.semanticscholar.org/product/api)

`paper-reader 1706.03762` 返回结构化摘要。
`paper-reader 1706.03762 - mode: note` 生成中文 Markdown 研究笔记。

## 功能

该 Skill 读取一篇论文，输出三种结果之一：

| 模式 | 命令 | 输出 |
|------|------|------|
| 快速（默认） | `paper-reader "1706.03762"` | 标题、作者、会议、引用数、摘要、3--5 个关键点 |
| 笔记 | `paper-reader "1706.03762" - mode: note` | 中文 Markdown 笔记（约 15--20 KB），按论文章节顺序组织 |
| 深度 | `paper-reader "1706.03762" - mode: deep` | 下载 PDF 本地文件 + 全文分析 |

## 适用对象

笔记模式以中文撰写，关键术语采用 `中文（English Term）` 格式，并对新颖概念附以简短解释和实例。笔记面向初次接触学术文献的读者：初入实验室的研究生、需要快速掌握文献的本科生，以及希望获得结构化阅读引导而非表面摘要的任何读者。

## 安装

将 `paper-reader` 文件夹复制到你的 agent skill 目录：

```bash
cp -r paper-reader ~/.codex/skills/paper-reader   # Codex CLI
cp -r paper-reader ~/.claude/skills/paper-reader   # Claude Code
cp -r paper-reader /path/to/skills/paper-reader    # Cursor, OpenCode 等
```

无需 API Key 或额外安装包。Skill 使用 Codex 内置的 Python 运行时和 pdfplumber。

## 使用

```bash
# 快速摘要
paper-reader "1706.03762"

# 中文研究笔记
paper-reader "1706.03762" - mode: note

# PDF 下载 + 全文分析
paper-reader "1706.03762" - mode: deep

# 从 URL
paper-reader "https://arxiv.org/abs/2401.12345"

# 从标题
paper-reader "Attention Is All You Need"
```

## 笔记结构

笔记按论文自身章节顺序组织：

1. 摘要精读
2. 引言精读
3. 相关工作
4. 方法（最详细部分）
5. 实验
6. 讨论与局限
7. 结论与未来方向

关键术语在首次出现时使用 `中文（English Term）` 格式。新颖概念附有简短解释，必要时配有具体例子。笔记保留论文中的公式、表格和数值结果。

## 工作原理

1. Skill 从输入中提取 arXiv ID（支持 bare ID、URL、DOI 或标题）。
2. 查询 arXiv API 获取标题、摘要、作者、分类和发表日期。
3. 可选查询 Semantic Scholar API 获取引用数、会议和年份。
4. 根据模式标志，打印摘要、生成中文笔记，或使用 pdfplumber 下载 PDF 并提取文本。

arXiv API 无速率限制。Semantic Scholar API 免费层为每分钟 100 次请求；若该 API 不可用，Skill 仅使用 arXiv 数据继续工作。

## 项目结构

```
paper-reader/
├── SKILL.md              # Agent skill 定义
├── scripts/
│   └── fetch_metadata.py # 元数据获取和 PDF 下载
├── tests/
│   └── test_metadata.py  # 单元测试
├── LICENSE
├── README.md
└── CHANGELOG.md
```

## 贡献

欢迎提交 Pull Request。建议在提交 PR 前通过 Issue 讨论变更。

## 许可证

MIT License.
