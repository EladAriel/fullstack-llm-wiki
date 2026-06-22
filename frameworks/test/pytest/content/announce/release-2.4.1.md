---
type: "Framework Learn Page"
framework: "pytest"
source_repo: "https://github.com/pytest-dev/pytest"
source_branch: "main"
source_path: "doc/en/announce/release-2.4.1.rst"
source_commit: "d2466e3a9655f75d25719bcc4510cdbcb39cf10d"
source_commit_short: "d2466e3a"
source_commit_date: "2026-06-21T06:49:47+02:00"
generated_at: "2026-06-21T11:47:50Z"
---

# pytest-2.4.1: fixing three regressions compared to 2.3.5

pytest-2.4.1 is a quick follow up release to fix three regressions compared to 2.3.5 before they hit more people:

- When using parser.addoption() unicode arguments to the
"type" keyword should also be converted to the respective types. thanks Floris Bruynooghe, @dnozay. (fixes issue360 and issue362)

- fix dotted filename completion when using argcomplete
thanks Anthon van der Neuth. (fixes issue361)

- fix regression when a 1-tuple ("arg",) is used for specifying
parametrization (the values of the parametrization were passed nested in a tuple).  Thanks Donald Stufft.

- also merge doc typo fixes, thanks Andy Dirnberger
as usual, docs at http://pytest.org and upgrades via:

```
pip install -U pytest
```

have fun, holger krekel
