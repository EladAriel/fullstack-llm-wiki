---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/09-2025/09-24-2025-custom-http-headers-for-requests-in-playground.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.867983Z"
---
# 09 24 2025 Custom Http Headers For Requests In Playground

---
title: "09.24.2025: Custom HTTP headers for requests in Playground"
description: Available in Phoenix 11.36+
---

<Update label="09.24.2025">

<Frame>
<img src="https://storage.googleapis.com/arize-phoenix-assets/assets/images/custom-headers-playground.png" alt="" />
</Frame>

This feature allows users to add custom HTTP headers to playground requests, enabling injection of provider-specific metadata (e.g. request IDs) via a JSON editor in the model config panel. The change extends the `GenerativeModelInput` schema to include `customHeaders`, with validation, per-provider storage, and conditional support.&#x20;

<Card title="feat(playground): custom http headers for playground requests by RogerHYang · Pull Request #9560 · Arize-ai/phoenixGitHub" href="https://github.com/Arize-ai/phoenix/pull/9560" icon="github"  horizontal>
Github
</Card>
</Update>
