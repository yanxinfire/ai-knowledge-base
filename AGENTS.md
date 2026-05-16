# AGENTS.md

## 1. Overview
This project is an automated AI knowledge assistant designed to continuously collect, analyse, and structure high-quality technical updates in the AI, LLM, and Agent domains. It aggregates content from sources such as GitHub Trending and Hacker News, processes it using AI models, and stores it in a structured JSON format for downstream distribution across multiple channels (e.g. Telegram and Teams).

---

## 2. Tech Stack
- Python 3.14
- OpenCode + large language models
- LangGraph (agent orchestration)
- OpenClaw (automation and execution layer)

---

## 3. Coding Standards

All code must adhere to the following conventions:

- Follow **PEP 8** strictly
- Use `snake_case` for variables, functions, and file names
- Use **Google-style docstrings** for all public functions and classes
- Type hints are required wherever applicable
- Logging must be used instead of printing
- **Bare `print()` statements are strictly prohibited**

Example:

```python
def fetch_trending_repos(limit: int) -> list[dict]:
    """Fetch top repositories from GitHub Trending.

    Args:
        limit: Number of repositories to retrieve.

    Returns:
        A list of repository metadata dictionaries.
    """
    ...
```

---

## 4. Project Structure

```
.opencode/
  agents/        # Agent definitions (collector, analyser, organiser)
    collector.md
    analyser.md
    organiser.md
  skills/        # Reusable capabilities and tools

knowledge/
  raw/           # Raw collected data (unprocessed)
  articles/      # Structured knowledge outputs (JSON)
```

---

## 5. Knowledge Entry Schema (JSON)

Each knowledge item must conform to the following schema:

```json
{
  "id": "string",
  "title": "string",
  "source": "github | hackernews | other",
  "source_url": "string",
  "summary": "string",
  "content": "string",
  "tags": ["ai", "llm", "agent"],
  "status": "raw | analysed | published",
  "created_at": "YYYY-MM-DDTHH:MM:SSZ",
  "updated_at": "YYYY-MM-DDTHH:MM:SSZ"
}
```

Requirements:
- `summary` must be concise (1–3 sentences)
- `tags` must be normalised (lowercase, no duplicates)
- `status` reflects pipeline stage
- All timestamps must be in ISO 8601 format (UTC)

---

## 6. Agent Roles Overview

| Agent      | Responsibility                                      | Input            | Output                                  | Spec File                          |
|------------|-----------------------------------------------------|------------------|------------------------------------------|------------------------------------|
| Collector  | Fetch and filter data from external sources         | None (scheduled) | Raw content (README, links, metadata)    | `.opencode/agents/collector.md`    |
| Analyser   | Extract insights and generate structured knowledge  | Raw content      | Structured JSON object                   | `.opencode/agents/analyser.md`     |
| Organiser  | Normalise, validate, and persist final outputs      | Structured data  | Clean JSON + ready-to-publish content    | `.opencode/agents/organiser.md`    |

---

## 7. Red Lines (Strictly Prohibited)

The following actions are strictly forbidden:

- Introducing hard-coded secrets (API keys, tokens, credentials)
- Using `print()` for debugging or logging
- Writing unstructured or schema-breaking JSON outputs
- Skipping validation before persisting data
- Copying large sections of source content verbatim without summarisation
- Manually modifying generated data outside the pipeline
- Adding unnecessary complexity or over-engineering solutions
- Ignoring existing project structure or conventions
- Implementing agents as Python code instead of Markdown specs

---

## Notes

- The system prioritises consistency, automation, and clarity over completeness
- Each knowledge entry should be quick to read and high in signal
- The pipeline must remain modular and extensible for future sources and distribution channels

---

## 8. Agent Implementation Rule

This project follows a **spec-first agent design**.

- Agents MUST be defined as Markdown files under `.opencode/agents/`
- DO NOT implement agents as Python code unless explicitly requested
- Agent files are:
  - `collector.md`
  - `analyser.md`
  - `organiser.md`
- These files define behaviour and responsibilities, not executable logic

All implementations (if added later) must strictly follow these specifications rather than replace them.
