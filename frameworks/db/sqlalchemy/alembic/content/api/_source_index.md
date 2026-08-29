---
type: "Framework Learn Page"
framework: "Alembic"
source_repo: "https://github.com/sqlalchemy/alembic"
source_branch: "main"
source_path: "docs/build/api/index.rst"
source_commit: "c116cbc0f39d9df2b4ce5f1871043a622ca8774f"
source_commit_short: "c116cbc"
source_commit_date: "2026-08-14T03:25:08-04:00"
generated_at: "2026-08-29T09:39:28.244876Z"
---
.. _api:

# API Details

Alembic's internal API has many public integration points that can be used
to extend Alembic's functionality as well as to reuse its functionality
in new ways.   As the project has grown, more APIs are created and exposed
for this purpose.

Direct use of the vast majority of API details discussed here is not needed
for rudimentary use of Alembic; the only API that is used normally by end users is
the methods provided by the :class:`.Operations` class, which is discussed
outside of this subsection, and the parameters that can be passed to
the :meth:`.EnvironmentContext.configure` method, used when configuring
one's ``env.py`` environment.  However, real-world applications will
usually end up using more of the internal API, in particular being able
to run commands programmatically, as discussed in the section :doc:`/api/commands`.

**toctree:** :maxdepth: 2

   overview
   runtime
   config
   commands
   operations
   autogenerate
   script
   ddl
   plugins
   exceptions
