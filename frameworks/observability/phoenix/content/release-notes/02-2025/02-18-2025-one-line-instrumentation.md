---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/02-2025/02-18-2025-one-line-instrumentation.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.849978Z"
---
# 02 18 2025 One Line Instrumentation

---
title: "02.18.2025: One line instrumentation"
description: Available in Phoenix 8.0+
---

<Update label="02.18.2025" description="">

## One Line Instrumentation

<Frame>
  <iframe 
    src="https://cdn.iframe.ly/vMqnP30" 
    width={1000} 
    height={400}
    allowFullScreen
  />
</Frame>

Phoenix has made it even simpler to get started with tracing by introducing one-line auto-instrumentation. By using `register(auto_instrument=True)`, you can enable automatic instrumentation in your application, which will set up instrumentors based on your installed packages.

```python
from phoenix.otel import register

register(auto_instrument=True)
```

For more details, you can check the docs and explore further [tracing](/docs/phoenix/tracing/how-to-tracing/setup-tracing) options.
</Update>


