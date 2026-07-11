# Paper Reader

**Zero-dependency paper reading skill for AI coding agents.** Read any arXiv paper with a single command — no API keys, no setup, no installation.

[![GitHub stars](https://img.shields.io/github/stars/huyixiang66/paper-reader?style=flat&logo=github)](https://github.com/huyixiang66/paper-reader/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![arXiv API](https://img.shields.io/badge/arXiv-API-free-b31b1b?style=flat)](https://arxiv.org/help/api/)
[![Semantic Scholar](https://img.shields.io/badge/Semantic_Scholar-API-free-orange?style=flat)](https://www.semanticscholar.org/product/api)

> **TL;DR:** `paper-reader 1706.03762` → instant structured paper summary.  
> Designed for **beginners in scientific research** who want to quickly understand, summarize, and take structured notes on academic papers.

## ✨ Features

- **Zero setup** — no API keys, no pip install, no Docker. Just works.
- **Three reading modes** — Quick overview, structured Chinese note, or deep PDF analysis
- **Dual API fallback** — arXiv API (always available) + Semantic Scholar (enhanced metadata)
- **Smart input parsing** — accepts arXiv IDs, URLs, DOIs, or paper titles
- **Anti-hallucination** — separates paper claims, evidence, inference, and open questions
- **Bilingual terminology** — `中文（English Term）` format with inline explanations
- **Structured output** — follows the paper's own section order (Abstract → Introduction → Method → Experiments → Conclusion)

## 🎯 Who is this for?

**Paper Reader is designed for beginners in scientific research.** Whether you are:

- A graduate student reading your first paper
- An undergraduate entering a lab and need to quickly grasp new literature
- A self-learner trying to understand cutting-edge research
- Anyone who finds academic papers intimidating and wants a structured, guided reading experience

Paper Reader helps you:
1. **Understand** — Get a clear, structured overview before diving into the full text
2. **Take notes** — Generate comprehensive Chinese research notes following the paper's own structure
3. **Learn terminology** — Every key term is explained in bilingual format with inline examples
4. **Build habits** — Follow the same reading order researchers use: abstract → intro → method → experiments → discussion

## 🚀 Quick Start

### Installation

Copy the `paper-reader` folder to your agent's skills directory:

```bash
# For Codex CLI
cp -r paper-reader ~/.codex/skills/paper-reader

# For Claude Code
cp -r paper-reader ~/.claude/skills/paper-reader

# For Cursor / any SKILL.md-compatible agent
cp -r paper-reader /path/to/your/skills/paper-reader
```

### Usage

```bash
# Quick summary (default)
paper-reader "1706.03762"

# Chinese research note (~15-20KB)
paper-reader "1706.03762" - mode: note

# Deep PDF analysis
paper-reader "1706.03762" - mode: deep

# From URL
paper-reader "https://arxiv.org/abs/2401.12345"

# From title
paper-reader "Attention Is All You Need"
```

## 📖 Modes Explained

### Quick Mode (Default)

Fast metadata + abstract summary. Perfect for deciding whether to read a paper in depth.

**Output includes:**
- Paper title, authors, venue, year
- Citation count (from Semantic Scholar)
- Full abstract
- 3-5 key points

### Note Mode

Comprehensive Chinese Markdown research note following the paper's structure.

**Output includes:**
- 摘要精读 (Abstract deep read)
- 引言精读 (Introduction deep read)
- 相关工作 (Related Work)
- 方法 (Method) — most detailed section
- 实验 (Experiments)
- 讨论与局限 (Discussion & Limitations)
- 结论与未来方向 (Conclusion & Future Work)
- Inline bilingual terminology with explanations
- Target size: 15-20KB

### Deep Mode

Downloads PDF and performs full text extraction + analysis.

**Output includes:**
- PDF saved to local directory
- Full structured note from extracted text
- Explicit notes on any missing/unreadable sections

## 🏗️ Architecture

```
paper-reader/
├── SKILL.md              # Agent skill definition
├── scripts/
│   └── fetch_metadata.py # Python script for API calls
├── tests/
│   └── test_metadata.py  # Unit tests
├── LICENSE
├── README.md
└── CHANGELOG.md
```

### How It Works

1. **Input Parsing** — Extracts arXiv ID from various input formats (bare ID, URL, DOI, title)
2. **Metadata Fetching** — Queries arXiv API (primary) + Semantic Scholar API (optional enhancement)
3. **Mode Dispatch** — Routes to Quick/Note/Deep mode based on flags
4. **Output Generation** — Structured summary or full Chinese research note

## 🔧 API Details

### arXiv API (Primary)

- **Endpoint:** `http://export.arxiv.org/api/query`
- **Rate limit:** None (public academic API)
- **Data:** Title, abstract, authors, categories, publication date
- **Fallback:** Always available

### Semantic Scholar API (Enhancement)

- **Endpoint:** `https://api.semanticscholar.org/graph/v1/paper/search`
- **Rate limit:** 100 requests/minute (free tier)
- **Data:** Citation count, venue, year, TL;DR summary
- **Graceful degradation:** Returns empty if rate-limited or unavailable

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

MIT License — feel free to use for personal or commercial projects.

## 🙏 Acknowledgments

- Built on [arXiv API](https://arxiv.org/help/api/) and [Semantic Scholar API](https://www.semanticscholar.org/product/api)
- Designed for [Codex CLI](https://github.com/openai/codex), [Claude Code](https://claude.ai/code), [Cursor](https://cursor.sh), and other AI coding agents
