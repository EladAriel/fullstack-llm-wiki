---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/07-2025/07-29-2025-google-genai-evals.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.903344Z"
---
# 07 29 2025 Google Genai Evals

---
title: "07.29.2025: Google GenAI evals"
---

<Update label="07.29.2025">

## Google GenAI Evals

<Frame>
    ![](https://storage.googleapis.com/arize-phoenix-assets/assets/images/phoenix-docs-images/gemini_logo.png)
</Frame>

We've added support for the `GoogleGenAIModel` in `phoenix-evals`, enabling direct access to Google's Gemini models through the official Google GenAI SDK. As of late 2024, this is the recommended approach for working with Gemini, offering a unified interface across both the Developer API and VertexAI.

**🚀 Key Features**

* **Multimodal Support**

    Run evaluations on **text**, **image**, and **audio** inputs using Gemini's multimodal capabilities.

* **Async-Ready**

    Optimized for **high-throughput evals** with full **async** compatibility.

* **Flexible Authentication**

    Supports both **API key** and **VertexAI-based** authentication methods.

* **Dynamic Rate Limiting**

    Built-in **rate limiter** with automatic adjustment based on API feedback and usage patterns.

This integration makes it easier to run robust, scalable evaluations using Gemini models directly within your `phoenix-evals` workflows.

Huge shoutout to [Siddharth Sahu](https://github.com/sahusiddharth) for this contribution!

More Information in our docs:

<Card title="Google Gen AI Evals | Phoenix" href="/docs/phoenix/integrations/llm-providers/google-gen-ai/google-gen-ai-evals" horizontal>
arize.com
</Card>
</Update>
