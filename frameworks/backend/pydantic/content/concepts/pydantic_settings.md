---
type: "Framework Learn Page"
framework: "Pydantic"
source_repo: "https://github.com/pydantic/pydantic"
source_branch: "main"
source_path: "docs/concepts/pydantic_settings.md"
source_commit: "4bc21c0fa28323c0f3e0be93c9ad114b705029c6"
source_commit_short: "4bc21c0"
source_commit_date: "2026-08-29T11:30:40+02:00"
generated_at: "2026-08-29T09:38:50.589891Z"
---
---
description: Support for loading a settings or config class from environment variables or secrets files.
---

# Settings Management

[Pydantic Settings](https://github.com/pydantic/pydantic-settings) provides optional Pydantic features for loading a settings or config class from environment variables or secrets files.

Settings are validated from environment variables and secrets files, so a
[`ValidationError`][pydantic_core.ValidationError] here points at an environment value that didn't match
its field. [Logfire](../errors/troubleshooting.md) can record failed validations and their structured
errors, so you can see which setting failed and why.

{{ pydantic_settings }}
