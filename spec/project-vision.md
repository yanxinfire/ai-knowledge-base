# AI knowledge base project vision v0.1

## Do
- Grab info from Github Trending: Every day, fetch top 20 repos from GitHub Trending (daily), filtered by keywords "ai", "llm", "agents"
- Use Agent to analyse contents: For each repo, produce structured knowledge including (1) what it is (1–2 sentence summary), (2) why it matters, (3) key ideas (3–5 bullets), (4) how to use it (high-level), (5) when to use it (use cases), (6) links (repo and docs if available)
- Output knowledge items: Primary format is Markdown for readability; additionally generate a structured JSON version for downstream agent processing (same content, normalized fields)

## Don't do
- No full tutorials
- No deep code analysis
- No historical backfill
- No manual curation (fully automated processing without human editing or selection)

## Boundaries & Acceptance
- Generates 20 knowledge items per day successfully (aligned with ingestion)
- Each item contains all required fields (summary, why it matters, key ideas, how to use, when to use, links)
- Output is readable and useful within 2 minutes per item

## how to verify
- Daily run produces a Markdown file and corresponding JSON for ~20 items
- Automated check validates JSON schema/required fields
- Spot check 1–2 items per run for quality (clarity, usefulness)

## System Architecture (v1)

- Scheduler: triggers a daily run
- Collect Agent (Ingestion + Filter + Fetch):
  - fetches top 20 repos from GitHub Trending (filtered by ai/llm/agents)
  - validates AI relevance via keywords/topics
  - retrieves README and repo metadata (stars, description, links)
- Analysis Agent:
  - produces knowledge fields (summary, why it matters, key ideas, how to use, when to use, links)
- Organization Agent:
  - normalizes fields into a fixed schema
  - prepares Markdown + JSON payloads
- Release Agent (Validator + Verifier included):
  - validates required fields and JSON schema before release
  - writes Markdown (human-readable)
  - writes JSON (machine-readable mirror)
  - logs run status and supports spot-check workflow
