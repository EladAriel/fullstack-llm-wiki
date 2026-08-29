---
type: "Framework Learn Page"
framework: "SQLAlchemy"
source_repo: "https://github.com/sqlalchemy/sqlalchemy"
source_branch: "main"
source_path: "doc/build/orm/session.rst"
source_commit: "85cafd1a131fa8afeeeab23151940480b3fb0042"
source_commit_short: "85cafd1"
source_commit_date: "2026-08-28T20:17:49+00:00"
generated_at: "2026-08-29T09:39:27.576352Z"
---
.. _session_toplevel:

# Using the Session

**module:** sqlalchemy.orm.session

The declarative base and ORM mapping functions described at
:ref:`mapper_config_toplevel` are the primary configurational interface for the
ORM. Once mappings are configured, the primary usage interface for
persistence operations is the
:class:`.Session`.

**toctree:** :maxdepth: 3

    session_basics
    session_state_management
    cascades
    session_transaction
    persistence_techniques
    contextual
    session_events
    session_api
