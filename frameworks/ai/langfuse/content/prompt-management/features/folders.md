---
type: "Framework Learn Page"
framework: "Langfuse"
source_repo: "https://github.com/langfuse/langfuse-docs"
source_branch: "main"
source_path: "content/docs/prompt-management/features/folders.mdx"
source_commit: "fcd1eca34a924867563c3c4e801254c4e66c0021"
source_commit_short: "fcd1eca3"
source_commit_date: "2026-07-25T00:45:45Z"
generated_at: "2026-07-25T11:51:12Z"
---

---
title: Folders
sidebarTitle: Folders
description: "Organize prompts into virtual folders to group prompts with similar purposes. Use folder hierarchies to manage prompt libraries at scale."
---

# Prompt Folders

Prompt folders help you organize your prompts into logical groups. As your prompt library grows, folders keep related prompts together — by feature, team, environment, or any structure that makes sense for your workflow.

To create a folder, add slashes (`/`) to a prompt name. The UI shows every segment ending with a `/` as a folder automatically. Like this you can structure into folders.

<Callout type="info">

**Note**: accessing prompts in folders via the Python SDK requires `langfuse >= 3.0.2`.

</Callout>

## Create a folder

Use the Langfuse UI to create a folder by adding a slash (`/`) to a prompt name.

<Video
  src="https://static.langfuse.com/docs-videos/prompt-folders.mp4"
  aspectRatio={16 / 9}
  gifStyle
/>
