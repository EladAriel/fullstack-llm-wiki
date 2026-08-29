---
type: "Framework Learn Page"
framework: "LangSmith"
source_repo: "https://github.com/langchain-ai/docs.git"
source_branch: "main"
source_path: "src/langsmith/set-up-feedback-criteria.mdx"
source_commit: "a174f9cf7c91ee5eb14ee2382eb48bfe6e4956e9"
source_commit_short: "a174f9c"
source_commit_date: "2026-08-28T17:04:12-07:00"
generated_at: "2026-08-29T09:39:50.646163Z"
---
# Set Up Feedback Criteria

---
title: Set up feedback criteria
sidebarTitle: Set up feedback criteria
---

<Tip>
**Recommended Reading**

Before diving into this content, it might be helpful to read the following:

- [Conceptual guide on tracing and feedback](/langsmith/observability-concepts)
- [Reference guide on feedback data format](/langsmith/feedback-data-format)

</Tip>

Feedback criteria are represented in the application as feedback tags. For human feedback, you can set up new feedback criteria as continuous feedback or categorical feedback.

<Info>
You can also manage feedback configs programmatically with the SDK. Refer to [Manage feedback & annotation queues programmatically](/langsmith/annotation-queues-sdk).
</Info>

<Tip>
For free-form acceptance criteria a reviewer writes per-run (rather than a fixed set of rubric scores), refer to [Use assertions](/langsmith/assertions).
</Tip>

To set up a new feedback criteria, follow [this link](https://smith.langchain.com/settings/workspaces/feedbacks) to view all existing tags for your workspace, then click **New Tag**.

## Continuous feedback

For continuous feedback, you can enter a feedback tag name, then select a minimum and maximum value. Every value, including floating-point numbers, within this range will be accepted as feedback scores.

![Cont feedback](/langsmith/images/cont-feedback.png)

## Categorical feedback

For categorical feedback, you can enter a feedback tag name, then add a list of categories, each category mapping to a score. When you provide feedback, you can select one of these categories as the feedback score.
Both the category label and the score will be logged as feedback in `value` and `score` fields, respectively.

![Cat feedback](/langsmith/images/cat-feedback.png)
