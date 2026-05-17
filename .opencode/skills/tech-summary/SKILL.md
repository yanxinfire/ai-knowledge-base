---
name: tech-summary
description: Use this skill when performing deep analysis and summarisation of collected technical content
allowed-tools:
  - Read
  - Grep
  - Glob
  - WebFetch
---

## Usage Scenarios

- Analyse collected GitHub trending data for technical significance
- Generate concise, high-signal summaries for downstream publishing
- Identify patterns and emerging trends across multiple projects

## Execution Steps

1. Read the latest collected file from `knowledge/raw/`
2. Analyse each item:
   - Write a summary (≤ 50 words)
   - Extract 2–3 technical highlights based on concrete facts
   - Assign a score from 1–10 with reasoning
   - Suggest relevant tags
3. Identify trends:
   - Common themes
   - Emerging concepts
4. Output structured analysis JSON

## Notes

- Scoring rules:
  - 9–10: paradigm-changing
  - 7–8: directly useful
  - 5–6: worth knowing
  - 1–4: low-value / skippable
- Among 15 projects, no more than 2 projects may receive a score of 9–10
- Avoid hype-based scoring; prioritise technical depth and real-world applicability
- Keep all analysis concise and evidence-driven
- Tags must be normalised (lowercase, no duplicates)

## Output Format

Output JSON structure:

```
{
  "source": "github",
  "skill": "tech-summary",
  "analysed_at": "YYYY-MM-DDTHH:MM:SSZ",
  "items": [
    {
      "name": "string",
      "url": "string",
      "summary": "string",
      "highlights": ["string"],
      "score": number,
      "reason": "string",
      "tags": ["string"]
    }
  ],
  "trends": {
    "themes": ["string"],
    "emerging_concepts": ["string"]
  }
}
```
