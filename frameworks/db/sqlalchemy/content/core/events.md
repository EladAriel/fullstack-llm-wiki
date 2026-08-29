---
type: "Framework Learn Page"
framework: "SQLAlchemy"
source_repo: "https://github.com/sqlalchemy/sqlalchemy"
source_branch: "main"
source_path: "doc/build/core/events.rst"
source_commit: "85cafd1a131fa8afeeeab23151940480b3fb0042"
source_commit_short: "85cafd1"
source_commit_date: "2026-08-28T20:17:49+00:00"
generated_at: "2026-08-29T09:39:27.524090Z"
---
.. _core_event_toplevel:

# Core Events

This section describes the event interfaces provided in
SQLAlchemy Core.
For an introduction to the event listening API, see :ref:`event_toplevel`.
ORM events are described in :ref:`orm_event_toplevel`.

**autoclass:** sqlalchemy.event.base.Events
   :members:

## Connection Pool Events

**autoclass:** sqlalchemy.events.PoolEvents
   :members:

**autoclass:** sqlalchemy.events.PoolResetState
   :members:

.. _core_sql_events:

## SQL Execution and Connection Events

**autoclass:** sqlalchemy.events.ConnectionEvents
    :members:

**autoclass:** sqlalchemy.events.DialectEvents
    :members:

## Schema Events

**autoclass:** sqlalchemy.events.DDLEvents
    :members:

**autoclass:** sqlalchemy.events.SchemaEventTarget
    :members:
