---
type: "Framework Learn Page"
framework: "pytest"
source_repo: "https://github.com/pytest-dev/pytest"
source_branch: "main"
source_path: "doc/en/naming20.rst"
source_commit: "fdba12e1708313f56e9cf713d260c029764ca2b7"
source_commit_short: "fdba12e"
source_commit_date: "2026-08-27T21:55:50+02:00"
generated_at: "2026-08-29T09:40:11.168799Z"
---
# Naming20


.. _naming20:

## New pytest names in 2.0 (flat is better than nested)

If you used older version of the ``py`` distribution (which
included the py.test command line tool and Python name space)
you accessed helpers and possibly collection classes through
the ``py.test`` Python namespaces.  The new ``pytest``
Python module flatly provides the same objects, following
these renaming rules::

    py.test.XYZ          -> pytest.XYZ
    py.test.collect.XYZ  -> pytest.XYZ
    py.test.cmdline.main -> pytest.main

The old ``py.test.*`` ways to access functionality remain
valid but you are encouraged to do global renaming according
to the above rules in your test code.