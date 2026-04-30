# AGENTS.md

## Overview
This project uses a multi-agent pipeline to collect, analyze, organize, and release AI knowledge from GitHub Trending.

Pipeline:
Collect -> Analysis -> Organization -> Release

---

## Agents

### 1. Collect Agent (Ingestion + Filter + Fetch)
Responsibility:
- Fetch top 20 daily repos from GitHub Trending
- Apply keyword filter: "ai", "llm", "agents"
- Validate AI relevance via name/description/topics
- Retrieve README content and repo metadata (stars, description, links)

Input:
- None (scheduled trigger)

Output:
- Raw content package per repo

---

### 4. Analysis Agent
Responsibility:
- Generate structured knowledge

Output fields:
- Summary (1–2 sentences)
- Why it matters
- Key ideas (3–5 bullets)
- How to use (high-level)
- When to use (use cases)
- Links

Input:
- Raw repo content

Output:
- Structured knowledge object

---

### 5. Organization Agent
Responsibility:
- Normalize output into consistent schema
- Prepare Markdown and JSON representations

Input:
- Structured knowledge object

Output:
- Markdown content
- JSON object

---

### 4. Release Agent (Validator + Verifier)
Responsibility:
- Validate required fields and JSON schema before release
- Persist outputs
- Log run status
- Enable manual spot checks

Output:
- Markdown files (human-readable)
- JSON files (machine-readable)

---

## Design Principles

- Fully automated (no manual curation)
- Lightweight outputs (no deep tutorials or code analysis)
- Markdown for humans, JSON for agents
- Daily incremental updates (no historical backfill)
