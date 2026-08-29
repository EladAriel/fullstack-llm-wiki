---
type: "Framework Learn Page"
framework: "pytest"
source_repo: "https://github.com/pytest-dev/pytest"
source_branch: "main"
source_path: "doc/en/announce/release-2.4.1.rst"
source_commit: "fdba12e1708313f56e9cf713d260c029764ca2b7"
source_commit_short: "fdba12e"
source_commit_date: "2026-08-27T21:55:50+02:00"
generated_at: "2026-08-29T09:40:11.189145Z"
---
# pytest-2.4.1: fixing three regressions compared to 2.3.5

pytest-2.4.1 is a quick follow up release to fix three regressions
compared to 2.3.5 before they hit more people:

- When using parser.addoption() unicode arguments to the
  "type" keyword should also be converted to the respective types.
  thanks Floris Bruynooghe, @dnozay. (fixes issue360 and issue362)

- fix dotted filename completion when using argcomplete
  thanks Anthon van der Neuth. (fixes issue361)

- fix regression when a 1-tuple ("arg",) is used for specifying
  parametrization (the values of the parametrization were passed
  nested in a tuple).  Thanks Donald Stufft.

- also merge doc typo fixes, thanks Andy Dirnberger

as usual, docs at http://pytest.org and upgrades via::

    pip install -U pytest

have fun,
holger krekel