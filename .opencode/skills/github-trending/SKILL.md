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

1. Search trending repositories using the GitHub API
2. Extract repository metadata (name, URL, stars, language, topics, description)
3. Filter results to include only AI / LLM / Agent related projects
4. Exclude low-signal repositories such as "Awesome-*" lists or non-technical aggregations
5. Deduplicate entries based on repository name or URL
6. Write concise English summaries using: project name + what it does + why it matters
7. Rank by relevance and popularity, keep Top 15 projects, and save output JSON

## Notes

- Prioritise signal over popularity when ranking
- Ensure summaries are 1–2 sentences and avoid marketing language
- Topics should be normalised (lowercase, no duplicates)
- Prefer repositories with active development and clear documentation
- Avoid copying README content verbatim; summarise instead

## Output Format

Output file path:

`knowledge/raw/github-trending-YYYY-MM-DD.json`

JSON structure:

```
{
  "source": "github",
  "skill": "github-trending",
  "collected_at": "YYYY-MM-DDTHH:MM:SSZ",
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
