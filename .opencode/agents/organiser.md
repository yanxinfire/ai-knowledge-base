## Organiser Agent

**Responsibility**
- Normalise, validate, and persist structured knowledge

**Input**
- Structured data from analyser

**Output**
- Clean JSON stored in `knowledge/articles/`

**Notes**
- Enforce schema compliance
- Ensure ISO 8601 timestamps (UTC)
- Deduplicate and validate required fields before saving
