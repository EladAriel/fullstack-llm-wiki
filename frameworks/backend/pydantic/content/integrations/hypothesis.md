---
type: "Framework Learn Page"
framework: "Pydantic"
source_repo: "https://github.com/pydantic/pydantic"
source_branch: "main"
source_path: "docs/integrations/hypothesis.md"
source_commit: "4bc21c0fa28323c0f3e0be93c9ad114b705029c6"
source_commit_short: "4bc21c0"
source_commit_date: "2026-08-29T11:30:40+02:00"
generated_at: "2026-08-29T09:38:50.592431Z"
---
# Hypothesis

[Hypothesis](https://hypothesis.readthedocs.io/) is the Python library for
[property-based testing](https://increment.com/testing/in-praise-of-property-based-testing/).
Hypothesis can infer how to construct type-annotated classes, and supports builtin types,
many standard library types, and generic types from the
[`typing`](https://docs.python.org/3/library/typing.html) and
[`typing_extensions`](https://pypi.org/project/typing-extensions/) modules by default.

Pydantic v2.0 drops built-in support for Hypothesis and no more ships with the integrated Hypothesis plugin.

!!! warning
    We are temporarily removing the Hypothesis plugin in favor of studying a different mechanism. For more information, see the issue [annotated-types/annotated-types#37](https://github.com/annotated-types/annotated-types/issues/37).

    The Hypothesis plugin may be back in a future release. Subscribe to [pydantic/pydantic#4682](https://github.com/pydantic/pydantic/issues/4682) for updates.
