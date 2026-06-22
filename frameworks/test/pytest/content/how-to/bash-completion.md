---
type: "Framework Learn Page"
framework: "pytest"
source_repo: "https://github.com/pytest-dev/pytest"
source_branch: "main"
source_path: "doc/en/how-to/bash-completion.rst"
source_commit: "d2466e3a9655f75d25719bcc4510cdbcb39cf10d"
source_commit_short: "d2466e3a"
source_commit_date: "2026-06-21T06:49:47+02:00"
generated_at: "2026-06-21T11:47:50Z"
---

# How to set up bash completion

When using bash as your shell, `pytest` can use argcomplete (https://kislyuk.github.io/argcomplete/) for auto-completion. For this `argcomplete` needs to be installed **and** enabled.

Install argcomplete using:

```bash
 sudo pip install 'argcomplete>=0.5.7'
```

For global activation of all argcomplete enabled python applications run:

```bash
 sudo activate-global-python-argcomplete
```

For permanent (but not global) `pytest` activation, use:

```bash
 register-python-argcomplete pytest >> ~/.bashrc
```

For one-time activation of argcomplete for `pytest` only, use:

```bash
 eval "$(register-python-argcomplete pytest)"
```
