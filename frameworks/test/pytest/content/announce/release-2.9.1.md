---
type: "Framework Learn Page"
framework: "pytest"
source_repo: "https://github.com/pytest-dev/pytest"
source_branch: "main"
source_path: "doc/en/announce/release-2.9.1.rst"
source_commit: "d2466e3a9655f75d25719bcc4510cdbcb39cf10d"
source_commit_short: "d2466e3a"
source_commit_date: "2026-06-21T06:49:47+02:00"
generated_at: "2026-06-21T11:47:50Z"
---

# pytest-2.9.1

pytest is a mature Python testing tool with more than 1100 tests against itself, passing on many different interpreters and platforms.

See below for the changes and see docs at:

http://pytest.org

As usual, you can upgrade from pypi via:

```
pip install -U pytest
```

Thanks to all who contributed to this release, among them:

Bruno Oliveira Daniel Hahler Dmitry Malinovsky Freya Bruhin Floris Bruynooghe Matt Bachmann Ronny Pfannschmidt TomV Vladimir Bolshakov Zearin palaviv

Happy testing, The py.test Development Team

## 2.9.1 (compared to 2.9.0)

**Bug Fixes**

- Improve error message when a plugin fails to load.
Thanks :user:`nicoddemus` for the PR.

- Fix (:issue:`1178`):
`pytest.fail` with non-ascii characters raises an internal pytest error. Thanks :user:`nicoddemus` for the PR.

- Fix (:issue:`469`): junit parses report.nodeid incorrectly, when params IDs
contain `::`. Thanks :user:`tomviner` for the PR (:pr:`1431`).

- Fix (:issue:`578`): SyntaxErrors
containing non-ascii lines at the point of failure generated an internal py.test error. Thanks :user:`asottile` for the report and :user:`nicoddemus` for the PR.

- Fix (:issue:`1437`): When passing in a bytestring regex pattern to parameterize
attempt to decode it as utf-8 ignoring errors.

- Fix (:issue:`649`): parametrized test nodes cannot be specified to run on the command line.
