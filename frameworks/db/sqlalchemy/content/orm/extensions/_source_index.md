---
type: "Framework Learn Page"
framework: "SQLAlchemy"
source_repo: "https://github.com/sqlalchemy/sqlalchemy"
source_branch: "main"
source_path: "doc/build/orm/extensions/index.rst"
source_commit: "85cafd1a131fa8afeeeab23151940480b3fb0042"
source_commit_short: "85cafd1"
source_commit_date: "2026-08-28T20:17:49+00:00"
generated_at: "2026-08-29T09:39:27.714177Z"
---
.. _plugins:
.. _sqlalchemy.ext:

# ORM Extensions

SQLAlchemy has a variety of ORM extensions available, which add additional
functionality to the core behavior.

The extensions build almost entirely on public core and ORM APIs and users should
be encouraged to read their source code to further their understanding of their
behavior.   In particular the "Horizontal Sharding", "Hybrid Attributes", and
"Mutation Tracking" extensions are very succinct.

**toctree:** :maxdepth: 1

    asyncio
    associationproxy
    automap
    baked
    declarative/index
    mutable
    orderinglist
    horizontal_shard
    hybrid
    indexable
    instrumentation
