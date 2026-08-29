---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/07-2025/07-29-2025-google-genai-evals.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.849376Z"
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
