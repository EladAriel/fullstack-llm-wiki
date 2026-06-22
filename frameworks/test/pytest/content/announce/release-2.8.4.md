---
type: "Framework Learn Page"
framework: "pytest"
source_repo: "https://github.com/pytest-dev/pytest"
source_branch: "main"
source_path: "doc/en/announce/release-2.8.4.rst"
source_commit: "d2466e3a9655f75d25719bcc4510cdbcb39cf10d"
source_commit_short: "d2466e3a"
source_commit_date: "2026-06-21T06:49:47+02:00"
generated_at: "2026-06-21T11:47:50Z"
---

# pytest-2.8.4

pytest is a mature Python testing tool with more than 1100 tests against itself, passing on many different interpreters and platforms. This release is supposed to be drop-in compatible to 2.8.2.

See below for the changes and see docs at:

http://pytest.org

As usual, you can upgrade from pypi via:

```
pip install -U pytest
```

Thanks to all who contributed to this release, among them:

Bruno Oliveira Freya Bruhin Jeff Widman Mehdy Khoshnoody Nicholas Chammas Ronny Pfannschmidt Tim Chan

Happy testing, The py.test Development Team

## 2.8.4 (compared to 2.8.3)

- fix #1190: `deprecated_call()` now works when the deprecated
function has been already called by another test in the same module. Thanks Mikhail Chernykh for the report and Bruno Oliveira for the PR.

- fix #1198: `--pastebin` option now works on Python 3. Thanks
Mehdy Khoshnoody for the PR.

- fix #1219: `--pastebin` now works correctly when captured output contains
non-ascii characters. Thanks Bruno Oliveira for the PR.

- fix #1204: another error when collecting with a nasty __getattr__().
Thanks Freya Bruhin for the PR.

- fix the summary printed when no tests did run.
Thanks Freya Bruhin for the PR.

- a number of documentation modernizations wrt good practices.
Thanks Bruno Oliveira for the PR.
