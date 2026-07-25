---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/03-2026/03-30-2026-delete-prompts-api.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.889686Z"
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
