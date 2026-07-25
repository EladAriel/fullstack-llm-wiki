---
type: "Framework Learn Page"
framework: "Langfuse"
source_repo: "https://github.com/langfuse/langfuse-docs"
source_branch: "main"
source_path: "content/docs/demo.mdx"
source_commit: "fcd1eca34a924867563c3c4e801254c4e66c0021"
source_commit_short: "fcd1eca3"
source_commit_date: "2026-07-25T00:45:45Z"
generated_at: "2026-07-25T11:51:12Z"
---

---
title: Example Project
description: Try Langfuse in action with a live example project for free. Interact with the chatbot to see new traces and user feedback (👍/👎) in Langfuse. No credit card required.
---

# Example Project

import { Button } from "@/components/ui/button";
import { ToAppButton } from "@/components/ToAppButton";

The Langfuse example project is a **live, shared project** that lets you explore Langfuse's features with real data before setting up your own account.

<Callout type="info" emoji="🎥">

Prefer videos? [**Watch end-to-end walkthroughs**](/watch-demo) of all Langfuse features.

</Callout>

## Step 1: Access the Example Project

Create a free account (no credit card required) to access the example project.

<div className="mt-3 not-prose flex">
  <ToAppButton
    signedInText="View Example project"
    signUpText="Create Example account"
    dropdownText="View Example project"
  />
</div>

## Step 2: Generate demo data

The demos below generate all the traces you see in the example project. Each interaction creates a new trace that you can inspect in Langfuse.

import { DemoTabs } from "@/components/demoTabs";

<DemoTabs className="mt-6" />

_Interested in implementation details? All demo apps are fully open source. Check out the [blog post about how the Q&A chatbot was built](/blog/qa-chatbot-for-langfuse-docs)._

## Next Steps

Ready to set up your own project?

1. **[Get Started with Tracing](/docs/observability/get-started)**: Add observability to your LLM application
2. **[Set Up Prompt Management](/docs/prompt-management/get-started)**: Move prompts out of your code
3. **[Create Your First Evaluation](/docs/evaluation/overview)**: Start measuring quality systematically
