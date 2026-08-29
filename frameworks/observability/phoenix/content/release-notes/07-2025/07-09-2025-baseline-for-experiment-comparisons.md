---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/07-2025/07-09-2025-baseline-for-experiment-comparisons.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.848386Z"
---
# 07 09 2025 Baseline For Experiment Comparisons

---
title: "07.09.2025: Baseline for experiment comparisons"
description: Available in Phoenix 11.4+
---

<Update label="07.09.2025">

## Baseline for Experiment Comparisons

<Frame>
<video controls width="800">
<source src="https://storage.googleapis.com/arize-phoenix-assets/assets/videos/experiment-baseline-comparison.mp4" type="video/mp4"/>
Your browser does not support the video tag or cannot load the video from this source.
</video>
</Frame>

You can now set a **baseline run** when comparing multiple experiments. This is especially useful when one run represents a known-good output (e.g. a previous model version or a CI-approved run), and you want to evaluate changes relative to it.

For example, in an evaluation like `accuracy`, you can easily see where the value flipped from `correct → incorrect` or `incorrect → correct` between your baseline and the current comparison - helping you quickly spot regressions or improvements.

This feature makes it easier to isolate the impact of changes like a new prompt, model, or dataset.

<Card title="feat(experiments): add baseline to compare experiments page by axiomofjoy · Pull Request #8461 · Arize-ai/phoenix" icon="github" href="https://github.com/Arize-ai/phoenix/pull/8461" horizontal>
  GitHub
</Card>
</Update>