---
type: "Framework Learn Page"
framework: "pytest"
source_repo: "https://github.com/pytest-dev/pytest"
source_branch: "main"
source_path: "doc/en/announce/release-2.8.7.rst"
source_commit: "d2466e3a9655f75d25719bcc4510cdbcb39cf10d"
source_commit_short: "d2466e3a"
source_commit_date: "2026-06-21T06:49:47+02:00"
generated_at: "2026-06-21T11:47:50Z"
---

# pytest-2.8.7

This is a hotfix release to solve a regression in the builtin monkeypatch plugin that got introduced in 2.8.6.

pytest is a mature Python testing tool with more than 1100 tests against itself, passing on many different interpreters and platforms. This release is supposed to be drop-in compatible to 2.8.5.

See below for the changes and see docs at:

http://pytest.org

As usual, you can upgrade from pypi via:

```
pip install -U pytest
```

Thanks to all who contributed to this release, among them:

Ronny Pfannschmidt

Happy testing, The py.test Development Team

## 2.8.7 (compared to 2.8.6)

- fix #1338: use predictable object resolution for monkeypatch
