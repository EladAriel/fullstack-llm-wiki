---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/03-2025/03-07-2025-model-config-enhancements-for-prompts.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.891795Z"
---
# 03 07 2025 Model Config Enhancements For Prompts

---
title: "03.07.2025: Model config enhancements for prompts"
description: Available in Phoenix 8.11+
---

<Update label="03.07.2025">

## Model Config Enhancements For Prompts

<Frame>
  <iframe 
    src="https://cdn.iframe.ly/bqCqcAn" 
    width={1000} 
    height={400}
    allowFullScreen
  />
</Frame>

* Save and Load from Prompts: You can now save and load configurations directly from prompts.
* Save and Load from Default Model Config: Default model configurations can be saved and loaded.
* Budget Token Management: Added the ability to adjust the budget token value.
* Thinking Configuration Toggle: You can now enable or disable the "thinking" feature.

**Important Note:** The default model config does not automatically apply to saved prompts. To include default thinking settings, ensure they are saved within the specific prompt.

<Card title="Release arize-phoenix: v8.11.0 · Arize-ai/phoenix" icon="github" href="https://github.com/Arize-ai/phoenix/releases/tag/arize-phoenix-v8.11.0" horizontal>
  GitHub
</Card>

### Improvements and Bug Fixes 🐛

* [**Experiments**](https://github.com/Arize-ai/phoenix/issues/6744): Added annotations to experiment JSON downloads
* [**Playground**](https://github.com/Arize-ai/phoenix/pull/6740): Add `none` as option for tool choice for anthropic 0.49.0
* [**UI**](https://github.com/Arize-ai/phoenix/pull/6719): Port slider component to react-aria
</Update>

