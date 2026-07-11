# Paper Reader

A skill for reading arXiv papers from AI coding agents. Supply an arXiv ID, URL, DOI, or title; the skill fetches metadata, optionally downloads the PDF, and produces a structured summary or a Chinese Markdown research note.

[![GitHub stars](https://img.shields.io/github/stars/huyixiang66/paper-reader?style=flat&logo=github)](https://github.com/huyixiang66/paper-reader/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![arXiv API](https://img.shields.io/badge/arXiv-API-free-b31b1b?style=flat)](https://arxiv.org/help/api/)
[![Semantic Scholar](https://img.shields.io/badge/Semantic_Scholar-API-free-orange?style=flat)](https://www.semanticscholar.org/product/api)

`paper-reader 1706.03762` returns a structured summary.
`paper-reader 1706.03762 - mode: note` generates a Chinese Markdown research note.

## What it does

The skill reads a single paper and produces one of three outputs:

| Mode | Command | Output |
|------|---------|--------|
| Quick (default) | `paper-reader "1706.03762"` | Title, authors, venue, citation count, abstract, 3--5 key points |
| Note | `paper-reader "1706.03762" - mode: note` | Chinese Markdown note (~15--20 KB) following the paper's section order |
| Deep | `paper-reader "1706.03762" - mode: deep` | PDF downloaded locally + full text analysis |

## Intended audience

The note output is written in Chinese with bilingual terminology (`中文（English Term）`) and inline explanations of novel concepts. It is aimed at readers who are new to academic literature: graduate students encountering their first paper, undergraduates entering a lab, or anyone who wants a structured guide through a paper's argument rather than a surface-level abstract.

## Installation

Copy the `paper-reader` folder into your agent's skills directory:

```bash
cp -r paper-reader ~/.codex/skills/paper-reader   # Codex CLI
cp -r paper-reader ~/.claude/skills/paper-reader   # Claude Code
cp -r paper-reader /path/to/skills/paper-reader    # Cursor, OpenCode, etc.
```

No API keys or additional packages are required. The skill uses the bundled Python runtime and pdfplumber.

## Usage

```bash
# Quick summary
paper-reader "1706.03762"

# Chinese research note
paper-reader "1706.03762" - mode: note

# PDF download + full analysis
paper-reader "1706.03762" - mode: deep

# From URL
paper-reader "https://arxiv.org/abs/2401.12345"

# From title
paper-reader "Attention Is All You Need"
```

## Note structure

The note follows the paper's own section order:

1. Abstract deep read
2. Introduction deep read
3. Related work
4. Method (most detailed section)
5. Experiments
6. Discussion and limitations
7. Conclusion and future work

Key terms appear in `中文（English Term）` format on first occurrence. Novel concepts include a short explanation and, where helpful, a concrete example. The note preserves formulas, tables, and numerical results from the paper.

## How it works

1. The skill extracts an arXiv ID from the input (bare ID, URL, DOI, or title).
2. It queries the arXiv API for title, abstract, authors, categories, and date.
3. It optionally queries the Semantic Scholar API for citation count, venue, and year.
4. Based on the mode flag, it either prints a summary, generates a Chinese note, or downloads the PDF and extracts text with pdfplumber.

The arXiv API has no rate limit. The Semantic Scholar API allows 100 requests per minute on the free tier; if it is unavailable the skill proceeds with arXiv data alone.

## Project structure

```
paper-reader/
├── SKILL.md              # Agent skill definition
├── scripts/
│   └── fetch_metadata.py # Metadata fetching and PDF download
├── tests/
│   └── test_metadata.py  # Unit tests
├── LICENSE
├── README.md
└── CHANGELOG.md
```

## Contributing

Pull requests are welcome. Please open an issue to discuss changes before submitting a PR.

## License

MIT License.
