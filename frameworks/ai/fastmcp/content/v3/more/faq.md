---
type: "Framework Learn Page"
framework: "FastMCP"
source_repo: "https://github.com/PrefectHQ/fastmcp.git"
source_branch: "main"
source_path: "docs/v3/more/faq.mdx"
source_commit: "44c0907dda78618f882b08de26e31c4428bd74b8"
source_commit_short: "44c0907"
source_commit_date: "2026-07-29T10:22:17-05:00"
generated_at: "2026-07-30T03:45:36.592886Z"
---
# Faq

---
title: FAQ
description: Answers to common questions about installing and using FastMCP
icon: circle-question
---

## `import fastmcp` stopped working after I upgraded with pip

This can happen when you upgrade to FastMCP 3.3 or later from FastMCP 3.2 or earlier with `pip`. The quick fix is `pip install --force-reinstall fastmcp`. See [Troubleshooting](/getting-started/installation#troubleshooting) for the clean-reinstall fallback and an explanation of why it happens.

## What's the difference between `fastmcp` and `fastmcp-slim`?

`fastmcp` is the full distribution. Installing it gives you the complete framework — server, client, CLI, and the common integrations — and is the right choice for most users:

```bash
pip install fastmcp
```

`fastmcp-slim` ships the same importable `fastmcp` package with a minimal set of required dependencies. You opt into the pieces you need through extras, which keeps environments lean when you only use part of the framework:

```bash
pip install "fastmcp-slim[client]"
```

Both distributions expose the same `import fastmcp`, so application code is identical regardless of which one you install.
