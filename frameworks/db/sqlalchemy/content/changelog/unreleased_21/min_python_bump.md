---
type: "Framework Learn Page"
framework: "SQLAlchemy"
source_repo: "https://github.com/sqlalchemy/sqlalchemy"
source_branch: "main"
source_path: "doc/build/changelog/unreleased_21/min_python_bump.rst"
source_commit: "85cafd1a131fa8afeeeab23151940480b3fb0042"
source_commit_short: "85cafd1"
source_commit_date: "2026-08-28T20:17:49+00:00"
generated_at: "2026-08-29T09:39:27.737260Z"
---
# Min_Python_Bump

**change:** :tags: change

    Python 3.11 or above is now required; support for Python 3.10 is dropped,
    in addition to the drop of versions Python 3.9, 3.8 and 3.7 introduced
    in 2.1.0b1.   Python 3.10 reaches EOL in October of 2026, so dropping
    support now gives the SQLAlchemy 2.1 series an extra year of space to
    remain on current Python versions.

    .. seealso::

        :ref:`change_python_versions`