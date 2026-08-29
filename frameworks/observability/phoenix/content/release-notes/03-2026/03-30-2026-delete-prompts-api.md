---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/03-2026/03-30-2026-delete-prompts-api.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.856738Z"
---
---
title: "Release Notes"
---

# Delete Prompts and Prompt Version Tags via REST API

March 30, 2026

**Available in arize-phoenix 13.20.0+**

Two new REST endpoints let you delete prompts and remove tags from prompt versions programmatically.

`DELETE /v1/prompts/{prompt_identifier}` deletes a prompt and all of its versions, tags, and labels in one operation. The `prompt_identifier` can be the prompt name or its numeric ID.

`DELETE /v1/prompt_versions/{prompt_version_id}/tags/{tag_name}` removes a single named tag from a specific prompt version. The tag is resolved within the scope of the prompt linked to that version.

- **`DELETE /v1/prompts/{prompt_identifier}`** — permanently deletes the prompt and every version, tag, and label associated with it
- **`DELETE /v1/prompt_versions/{prompt_version_id}/tags/{tag_name}`** — removes a tag from a prompt version without affecting other tags or the version itself
- Both endpoints return **204 No Content** on success; attempting to delete a non-existent tag returns **404 Not Found**
