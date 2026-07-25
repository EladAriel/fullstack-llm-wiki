---
type: "Framework Learn Page"
framework: "pytest"
source_repo: "https://github.com/pytest-dev/pytest"
source_branch: "main"
source_path: "doc/en/announce/release-2.8.5.rst"
source_commit: "344c23787cdb3431dcc441b8b63ee9950f04b921"
source_commit_short: "344c2378"
source_commit_date: "2026-07-24T17:37:16+02:00"
generated_at: "2026-07-25T11:50:13Z"
---

# pytest-2.8.5

pytest is a mature Python testing tool with more than 1100 tests against itself, passing on many different interpreters and platforms. This release is supposed to be drop-in compatible to 2.8.4.

See below for the changes and see docs at:

http://pytest.org

As usual, you can upgrade from pypi via:

```
pip install -U pytest
```

Thanks to all who contributed to this release, among them:

Alex Gaynor aselus-hub Bruno Oliveira Ronny Pfannschmidt

Happy testing, The py.test Development Team

## 2.8.5 (compared to 2.8.4)

- fix #1243: fixed issue where class attributes injected during collection could break pytest.
PR by Alexei Kozlenok, thanks Ronny Pfannschmidt and Bruno Oliveira for the review and help.

- fix #1074: precompute junitxml chunks instead of storing the whole tree in objects
Thanks Bruno Oliveira for the report and Ronny Pfannschmidt for the PR

- fix #1238: fix `pytest.deprecated_call()` receiving multiple arguments
(Regression introduced in 2.8.4). Thanks Alex Gaynor for the report and Bruno Oliveira for the PR.
