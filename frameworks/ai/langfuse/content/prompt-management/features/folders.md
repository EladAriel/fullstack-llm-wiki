---
type: "Framework Learn Page"
framework: "Langfuse"
source_repo: "https://github.com/langfuse/langfuse-docs"
source_branch: "main"
source_path: "content/docs/prompt-management/features/folders.mdx"
source_commit: "4a702ece53852a6af86b3883f434adf3f5cae421"
source_commit_short: "4a702ece"
source_commit_date: "2026-06-23T13:41:14Z"
generated_at: "2026-06-23T13:55:15Z"
---

---
title: Folders
sidebarTitle: Folders
description: "Organize prompts into virtual folders to group prompts with similar purposes. Use folder hierarchies to manage prompt libraries at scale."
---

# Prompt Folders

Prompt folders help you organize your prompts into logical groups. As your prompt library grows, folders keep related prompts together — by feature, team, environment, or any structure that makes sense for your workflow.

To create a folder, add slashes (`/`) to a prompt name. The UI shows every segment ending with a `/` as a folder automatically.

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
