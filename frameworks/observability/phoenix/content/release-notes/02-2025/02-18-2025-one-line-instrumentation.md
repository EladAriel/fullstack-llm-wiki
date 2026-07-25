---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/02-2025/02-18-2025-one-line-instrumentation.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.905806Z"
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


