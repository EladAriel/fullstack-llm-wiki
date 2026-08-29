---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/tracing/llm-traces/how-to-annotate-traces.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.900888Z"
---
# How To Annotate Traces

---
title: "Annotations"
---

<Frame caption="Capture feedback in the form of annotations from humans and LLMs">
<video src="https://storage.googleapis.com/arize-phoenix-assets/assets/videos/span_annotations.mp4" width="100%" height="100%" style={{ display: 'block', objectFit: 'fill', backgroundColor: 'transparent' }} controls autoPlay muted loop />
</Frame>

In order to improve your LLM application iteratively, it's vital to collect feedback, annotate data during human review, as well as to establish an evaluation pipeline so that you can monitor your application. In Phoenix we capture this type of feedback in the form of **annotations**.

Phoenix gives you the ability to annotate traces with feedback from the UI, your application, or wherever you would like to perform evaluation. Phoenix's annotation model is simple yet powerful - given an entity such as a span that is collected, you can assign a `label` and/or a `score` to that entity.

## Next Steps

<CardGroup cols={2}>
  <Card title="Annotation Concepts" icon="book" href="/docs/phoenix/tracing/concepts-tracing/annotations-concepts">
    Understand how annotations work in Phoenix
  </Card>
  <Card title="Run Evals on Traces" icon="magnifying-glass-chart" href="/docs/phoenix/tracing/how-to-tracing/feedback-and-annotations/evaluating-phoenix-traces">
    Automatically evaluate your traces with LLM judges
  </Card>
  <Card title="Annotate in the UI" icon="browser" href="/docs/phoenix/tracing/how-to-tracing/feedback-and-annotations/annotating-in-the-ui">
    Manually review and annotate traces
  </Card>
  <Card title="Log Annotations via Code" icon="code" href="/docs/phoenix/tracing/how-to-tracing/feedback-and-annotations/capture-feedback">
    Programmatically add annotations from your app
  </Card>
</CardGroup>


