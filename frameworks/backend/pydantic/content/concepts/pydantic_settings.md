---
type: "Framework Learn Page"
framework: "pydantic"
source_repo: "https://github.com/pydantic/pydantic"
source_branch: "main"
source_path: "docs/concepts/pydantic_settings.md"
source_commit: "a2a6577d4c329dd574a45dbb01a8feaa16b1ad3d"
source_commit_short: "a2a6577d"
source_commit_date: "2026-07-23T15:38:17Z"
generated_at: "2026-07-25T11:50:12Z"
---

---
description: Support for loading a settings or config class from environment variables or secrets files.
---

# Settings Management

[Pydantic Settings](https://github.com/pydantic/pydantic-settings) provides optional Pydantic features for loading a settings or config class from environment variables or secrets files.

Settings are validated from environment variables and secrets files, so a
[`ValidationError`][pydantic_core.ValidationError] here points at an environment value that didn't match
its field. [Logfire](../errors/troubleshooting.md) records each validation and its structured errors, so
you can see which setting failed and why.

{{ pydantic_settings }}
