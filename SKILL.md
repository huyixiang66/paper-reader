---
name: paper-reader
description: Read and summarize academic papers from arXiv, DOI, or URL. Supports three modes: (1) quick overview — fetches metadata + abstract and returns a structured summary, (2) structured note — generates a Chinese Markdown research note following the paper's own section order with bilingual terminology and inline explanations, (3) deep read — downloads PDF, extracts text with pdfplumber, and produces a full analysis. Use when the user provides an arXiv ID, DOI, URL, or paper title and wants to understand, summarize, or take notes on a specific paper. Does not replace broad literature search or multi-paper surveys.
argument-hint: [arxiv-id | doi | url | title]
allowed-tools: Bash(*), Read, Write
---

# Paper Reader

Read a paper: $ARGUMENTS

## Overview

A lightweight, zero-dependency paper reader. Three modes:

| Mode | Trigger | What it does |
|------|-----------|------------|
| Quick (default) | bare ID / URL / title | Metadata + abstract → structured summary |
| Note | `- mode: note` | Chinese Markdown research note (~15-20KB) following paper structure |
| Deep | `- mode: deep` | Downloads PDF → extracts text → full analysis |

## Prerequisites

- Python 3.10+ with pdfplumber (bundled with Codex runtime)
- Internet access to arXiv API and Semantic Scholar API
- No API keys needed

## Workflow

### Step 1: Parse Input

Extract the paper identifier from `$ARGUMENTS`. Accept:

- Bare arXiv ID: `2501.00001`, `2606.10401v2`
- arXiv URL: `https://arxiv.org/abs/2501.00001`, `https://arxiv.org/pdf/...`
- DOI: `10.1145/3623538`
- Title: free-text paper title

Strip version suffixes (`v1`, `v2`, ...) for API calls.

Detect mode override:
- `- mode: note` → structured Chinese research note
- `- mode: deep` → download PDF + full text extraction
- Default → quick metadata summary

### Step 2: Fetch Metadata

Run the metadata fetcher:

```bash
python3 "<SKILL_DIR>/scripts/fetch_metadata.py" metadata "<paper_id>"
```

This returns JSON with arXiv metadata + Semantic Scholar data (citations, references, venue).

If the fetcher fails, fall back to `curl` to arXiv API:

```bash
curl -sL "http://export.arxiv.org/api/query?id_list=<paper_id>&max_results=1"
```

### Step 3: Mode Dispatch

#### Quick Mode (default)

Present a structured summary with title, authors, arXiv link, venue/year, citation count, abstract, and 3-5 key points.

#### Note Mode (`- mode: note`)

Generate a Chinese Markdown research note following the paper's own section order. Target size: 15-20KB.

**Structure:**

```markdown
# [Paper Title] — 精读笔记

## 1. 摘要精读（Abstract）
## 2. 引言精读（Introduction）
## 3. 相关工作（Related Work）
## 4. 方法（Method）
## 5. 实验（Experiments）
## 6. 讨论与局限（Discussion & Limitations）
## 7. 结论与未来方向（Conclusion & Future Work）
```

**Key rules:**
- Use `中文（English Term）` format for key terms on first appearance
- Novel terms require detailed explanation with examples
- Method section is most detailed (30-40%), experiments next (20-30%)
- Preserve formulas, core architecture, main results
- End with summary: what problem solved, limitations, future directions

#### Deep Mode (`- mode: deep`)

1. Download PDF: `python3 "<SKILL_DIR>/scripts/fetch_metadata.py" pdf "<paper_id>" "<outdir>"`
2. Extract text with pdfplumber
3. If extraction is noisy or incomplete, state the limitation explicitly
4. Produce the same structured note as Note Mode, but with richer content from full text

### Step 4: Anti-Hallucination Rules

- Separate `paper claim`, `evidence`, `inference`, and `open question`
- Do not invent citations, metrics, datasets, or novelty claims not in the paper
- If only metadata is available, mark the note as `metadata-only`
- If PDF extraction is incomplete, state which sections were missed

## Output

- Quick mode: print to stdout
- Note mode: save to `<paper_id>-note.md` + print summary
- Deep mode: save PDF + note to `<outdir>` + print summary

## Examples

```bash
# Quick summary
python3 scripts/fetch_metadata.py metadata "2401.12345"

# Note mode
# → Add "- mode: note" to $ARGUMENTS

# Deep mode
# → Add "- mode: deep" to $ARGUMENTS
```
