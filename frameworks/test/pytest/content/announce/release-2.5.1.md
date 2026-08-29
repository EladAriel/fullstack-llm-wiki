---
type: "Framework Learn Page"
framework: "pytest"
source_repo: "https://github.com/pytest-dev/pytest"
source_branch: "main"
source_path: "doc/en/announce/release-2.5.1.rst"
source_commit: "fdba12e1708313f56e9cf713d260c029764ca2b7"
source_commit_short: "fdba12e"
source_commit_date: "2026-08-27T21:55:50+02:00"
generated_at: "2026-08-29T09:40:11.189858Z"
---
# pytest-2.5.1: fixes and new home page styling

pytest is a mature Python testing tool with more than 1000 tests
against itself, passing on many different interpreters and platforms.

The 2.5.1 release maintains the "zero-reported-bugs" promise by fixing
the three bugs reported since the last release a few days ago.  It also
features a new home page styling implemented by Tobias Bieniek, based on
the flask theme from Armin Ronacher:

    http://pytest.org

If you have anything more to improve styling and docs,
we'd be very happy to merge further pull requests.

On the coding side, the release also contains a little enhancement to
fixture decorators allowing to directly influence generation of test
ids, thanks to Floris Bruynooghe.  Other thanks for helping with
this release go to Anatoly Bubenkoff and Ronny Pfannschmidt.

As usual, you can upgrade from pypi via::

    pip install -U pytest

have fun and a nice remaining "bug-free" time of the year :)
holger krekel

## 2.5.1

- merge new documentation styling PR from Tobias Bieniek.

- fix issue403: allow parametrize of multiple same-name functions within
  a collection node.  Thanks Andreas Kloeckner and Alex Gaynor for reporting
  and analysis.

- Allow parameterized fixtures to specify the ID of the parameters by
  adding an ids argument to pytest.fixture() and pytest.yield_fixture().
  Thanks Floris Bruynooghe.

- fix issue404 by always using the binary xml escape in the junitxml
  plugin.  Thanks Ronny Pfannschmidt.

- fix issue407: fix addoption docstring to point to argparse instead of
  optparse. Thanks Daniel D. Wright.