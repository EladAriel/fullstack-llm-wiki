---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/09-2025/09-24-2025-custom-http-headers-for-requests-in-playground.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.893549Z"
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
