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
2. Validate input integrity (STRICT):
   - Load all items from the input file
   - Record the exact set of `(name, url)` pairs
   - If the file is empty or malformed, abort
3. Analyse each item (NO ADDITIONS):
   - Write a summary (≤ 50 words)
   - Extract 2–3 technical highlights based on concrete facts
   - Assign a score from 1–10 with reasoning
   - Suggest relevant tags
4. Enforce constraints (STRICT):
   - Output MUST contain exactly the same number of items as input
   - Every output item MUST match an input `(name, url)` pair exactly
   - Do NOT introduce, rename, or omit any items
   - Do NOT drop any items during analysis; all input items must be included
   - At most 2 items may have scores 9–10
   - Avoid hype-based scoring; be evidence-driven
5. Identify trends:
   - Common themes
   - Emerging concepts
6. Pre-output validation (FAIL FAST):
   - Verify item count equality (input == output)
   - Verify all `(name, url)` pairs match the input set
   - Verify no items were dropped or omitted
   - Verify score constraints are satisfied
   - If any check fails, regenerate until valid
7. Output structured analysis JSON (READ-ONLY; do not write files)

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
- Do not introduce any items not present in the input file
- Do not change names or URLs; preserve exact values from input
- The analyser is read-only: it must not write or modify files

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
