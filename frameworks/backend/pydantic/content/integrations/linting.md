---
type: "Framework Learn Page"
framework: "pydantic"
source_repo: "https://github.com/pydantic/pydantic"
source_branch: "main"
source_path: "docs/integrations/linting.md"
source_commit: "a2a6577d4c329dd574a45dbb01a8feaa16b1ad3d"
source_commit_short: "a2a6577d"
source_commit_date: "2026-07-23T15:38:17Z"
generated_at: "2026-07-25T11:50:12Z"
---

## Flake8 plugin

If using Flake8 in your project, a [plugin](https://pypi.org/project/flake8-pydantic/) is available
and can be installed using the following:

```bash
pip install flake8-pydantic
```

The lint errors provided by this plugin are namespaced under the `PYDXXX` code. To ignore some unwanted
rules, the Flake8 configuration can be adapted:

```ini
[flake8]
extend-ignore = PYD001,PYD002
```
