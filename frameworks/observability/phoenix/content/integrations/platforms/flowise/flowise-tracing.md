---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/integrations/platforms/flowise/flowise-tracing.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.856754Z"
---
# Flowise Tracing

---
title: "Flowise Tracing"
description: "Analyzing and troubleshooting what happens under the hood can be challenging without proper insights. By integrating your Flowise application with Phoenix, you can monitor traces and gain robust observability into your chatflows and agentflows."
---

### Viewing Flowise traces in Phoenix

<Steps>
   <Step title={<span className="step-title">Access Configurations</span>}>
    Navigate to settings in your chatflow or agentflow and find configurations.

<Frame>
  <iframe src="https://cdn.iframe.ly/MU5cw6c" allowFullScreen className="aspect-video"></iframe>
</Frame>
</Step>
<Step title={<span className="step-title">Connect to Phoenix</span>}>
  Go to the **Analyze Chatflow** tab and configure your application with Phoenix. Get your API key from your Phoenix instance to create your credentials. Be sure to name your project and confirm that the Phoenix toggle is enabled before saving.

<Info>
   **Note**: Set the Endpoint field to match your Phoenix instance. See [Environments](/docs/phoenix/environments).
</Info>

<Frame>
  <iframe src="https://cdn.iframe.ly/Rkzq2g1" allowFullScreen className="aspect-video"></iframe>
</Frame>
</Step>
<Step title={<span className="step-title">View Traces</span>}>
  In Phoenix, you will find your project under the Projects tab. Click into this to view and analyze traces as you test your application.

<Frame>
  <iframe src="https://cdn.iframe.ly/kBXFsLO" allowFullScreen className="aspect-video"></iframe>
</Frame>
</Step>
<Step title={<span className="step-title">Store and Experiment</span>}>
  Optionally, you can also filter traces, store traces in a dataset to run experiments, analyze patterns, and optimize your workflows over time.

<Frame>
  <iframe src="https://cdn.iframe.ly/c0T0bBt" allowFullScreen className="aspect-video"></iframe>
</Frame>

You can also reference [Flowise documentation](https://docs.flowiseai.com/using-flowise/analytics/phoenix) here.
</Step>
</Steps>
