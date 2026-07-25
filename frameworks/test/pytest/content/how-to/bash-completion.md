---
type: "Framework Learn Page"
framework: "pytest"
source_repo: "https://github.com/pytest-dev/pytest"
source_branch: "main"
source_path: "doc/en/how-to/bash-completion.rst"
source_commit: "344c23787cdb3431dcc441b8b63ee9950f04b921"
source_commit_short: "344c2378"
source_commit_date: "2026-07-24T17:37:16+02:00"
generated_at: "2026-07-25T11:50:13Z"
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
