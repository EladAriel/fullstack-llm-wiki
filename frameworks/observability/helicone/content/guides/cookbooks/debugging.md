---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/guides/cookbooks/debugging.mdx"
source_commit: "607c855f787d6cc66e83692874bf90f880a08d62"
source_commit_short: "607c855"
source_commit_date: "2026-08-25T19:59:29-04:00"
generated_at: "2026-08-29T09:39:42.331622Z"
---
---
title: "Debugging LLM Applications"
sidebarTitle: "Debugging"
description: "Helicone provides an efficient platform for identifying and rectifying errors in your LLM applications, offering insights into their occurrence."
"twitter:title": "Debugging LLM Applications - Helicone OSS LLM Observability"
---

# Identifying Errors

Helicone's request page allows you to filter results by status code, a unique identifier that corresponds to various states of web requests. This feature enables you to pinpoint errors, providing essential information about their timing and location.

<Frame>
  ![Filter web request results by status code on Helicone's request
  page.](/images/use-cases/status-filter.png)
</Frame>

We are currently developing dedicated error filters to further enhance your debugging experience. If you are interested in this feature, please support us by upvoting the feature request [here](https://www.helicone.ai/roadmap).

# Debugging Prompts with Playground

<Info>Currently, only ChatGPT is supported</Info>

Helicone's 'Playground' feature offers a platform for debugging your 'prompt'. This tool enables you to test your prompt and swiftly observe the model's output for minor adjustments within the Helicone environment. Here's a step-by-step guide on how to use it:

1. Open a request.

<Frame>
  ![View detailed logging details on Helicone's Requests
  page.](/images/use-cases/view-request.png)
</Frame>

2. Click on the 'Playground' button.

<Frame>
  ![Access the Playground feature for prompt debugging in
  Helicone](/images/use-cases/playground-button.png)
</Frame>

3. Input and execute your prompt to view the results.

<Frame>
  ![Use Helicone's Playground to test prompts in a sandbox
  environment](/images/use-cases/playground.png)
</Frame>

Please note, the Playground tool is a sandbox environment, so feel free to experiment with different prompts and settings to optimize results for your project.
