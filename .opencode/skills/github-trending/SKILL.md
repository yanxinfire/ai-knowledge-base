---
name: github-trending
description: Use this skill when collecting trending open-source projects from GitHub
allowed-tools:
  - Read
  - Grep
  - Glob
  - WebFetch
---

## Usage Scenarios

- Collect daily or weekly trending repositories from GitHub
- Identify high-signal AI, LLM, and Agent-related projects
- Feed downstream analysis and knowledge structuring pipelines

## Execution Steps

1. Fetch repositories (MULTI-SOURCE, MANDATORY):
   - Use WebFetch to retrieve data from:
     - GitHub Trending (weekly)
     - GitHub Search API (e.g. sort by stars or recently created/pushed)
   - Combine results into a single candidate pool
   - If WebFetch is not used, FAIL the run
2. Extract repository metadata:
   - name, url, stars, language, topics, description
3. Filter results:
   - Include only AI / LLM / Agent related projects
   - Exclude "Awesome-*" lists and low-signal repositories
4. Deduplicate entries based on repository name or URL
5. Write concise English summaries:
   - Format: project name + what it does + why it matters
   - 1–2 sentences, no marketing language
6. Rank results and select up to Top 15 projects:
   - Prioritise recent momentum (stars gained, activity)
   - Break ties using total stars and relevance to AI/LLM/Agent
7. Pre-output validation (STRICT, FAIL FAST):
   - Items count must be between 1 and 15
   - Every item must have:
     - valid GitHub URL (https://github.com/...)
     - stars > 0
     - non-empty summary
   - No placeholder or fabricated entries allowed
   - Do NOT fabricate or expand results to reach 15
   - If any check fails, FAIL the run
8. Output JSON and save to file

## Notes

- Prioritise signal over popularity when ranking
- Ensure summaries are 1–2 sentences and avoid marketing language
- Topics should be normalised (lowercase, no duplicates)
- Prefer repositories with active development and clear documentation
- Avoid copying README content verbatim; summarise instead
- Do not fabricate or hallucinate repositories
- All items must be traceable to fetched GitHub data

## Output Format

Output file path:

`knowledge/raw/github-trending-YYYY-MM-DD.json`

JSON structure:

```
{
  "source": "github",
  "skill": "github-trending",
  "collected_at": "YYYY-MM-DDTHH:MM:SSZ",
  "fetched_from": "string",
  "items": [
    {
      "name": "string",
      "url": "string",
      "summary": "string",
      "stars": number,
      "language": "string",
      "topics": ["string"]
    }
  ]
}
```

Constraints:
- `items` must contain at most 15 entries
- `items` must contain at least 1 entry
- `url` must start with `https://github.com/`
- `stars` must be a positive integer
- `topics` must be lowercase and deduplicated
