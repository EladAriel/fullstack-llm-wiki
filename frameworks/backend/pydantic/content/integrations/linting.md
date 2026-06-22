---
type: "Framework Learn Page"
framework: "pydantic"
source_repo: "https://github.com/pydantic/pydantic"
source_branch: "main"
source_path: "docs/integrations/linting.md"
source_commit: "363728fe0b353db1a1fcb44aac5c38fd96a8cc20"
source_commit_short: "363728fe"
source_commit_date: "2026-06-20T11:20:58+01:00"
generated_at: "2026-06-21T11:37:01Z"
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
