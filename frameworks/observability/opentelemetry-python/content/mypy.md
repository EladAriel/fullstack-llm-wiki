---
type: "Framework Learn Page"
framework: "OpenTelemetry Python"
source_repo: "https://github.com/open-telemetry/opentelemetry.io.git"
source_branch: "main"
source_path: "content/en/docs/languages/python/mypy.md"
source_commit: "669d1a40e56ed2dd914d48340b31e16a83610d40"
source_commit_short: "669d1a4"
source_commit_date: "2026-08-29T01:16:15+00:00"
generated_at: "2026-08-29T09:39:55.751324Z"
---
# Mypy

---
title: Using mypy
weight: 120
cSpell:ignore: mypy
---

If you're using [mypy](https://mypy-lang.org/), you'll need to turn on
[namespace packages](https://mypy.readthedocs.io/en/stable/command_line.html#cmdoption-mypy-no-namespace-packages),
otherwise `mypy` won't be able to run correctly.

To turn on namespace packages, do one of the following:

Add the following to your project configuration file:

```toml
[tool.mypy]
namespace_packages = true
```

Or, use a command-line switch:

```shell
mypy --namespace-packages
```
