---
type: "Framework Learn Page"
framework: "Pydantic"
source_repo: "https://github.com/pydantic/pydantic"
source_branch: "main"
source_path: "docs/integrations/linting.md"
source_commit: "4bc21c0fa28323c0f3e0be93c9ad114b705029c6"
source_commit_short: "4bc21c0"
source_commit_date: "2026-08-29T11:30:40+02:00"
generated_at: "2026-08-29T09:38:50.593490Z"
---
# Linting

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
