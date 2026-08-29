---
type: "Framework Learn Page"
framework: "SQLAlchemy"
source_repo: "https://github.com/sqlalchemy/sqlalchemy"
source_branch: "main"
source_path: "doc/build/orm/session_api.rst"
source_commit: "85cafd1a131fa8afeeeab23151940480b3fb0042"
source_commit_short: "85cafd1"
source_commit_date: "2026-08-28T20:17:49+00:00"
generated_at: "2026-08-29T09:39:27.582110Z"
---
**currentmodule:** sqlalchemy.orm

# Session API

## Session and sessionmaker()

**autoclass:** sessionmaker
    :members:
    :inherited-members:

**autoclass:** ORMExecuteState
    :members:

**autoclass:** Session
   :members:
   :inherited-members:

**autoclass:** SessionTransaction
   :members:

**autoclass:** SessionTransactionOrigin
   :members:

## Session Utilities

**autofunction:** close_all_sessions

**autofunction:** make_transient

**autofunction:** make_transient_to_detached

**autofunction:** object_session

**autofunction:** sqlalchemy.orm.util.was_deleted

## Attribute and State Management Utilities

These functions are provided by the SQLAlchemy attribute
instrumentation API to provide a detailed interface for dealing
with instances, attribute values, and history.  Some of them
are useful when constructing event listener functions, such as
those described in :doc:`/orm/events`.

**currentmodule:** sqlalchemy.orm.util

**autofunction:** object_state

**currentmodule:** sqlalchemy.orm.attributes

**autofunction:** del_attribute

**autofunction:** get_attribute

**autofunction:** get_history

**autofunction:** init_collection

**autofunction:** flag_modified

**autofunction:** flag_dirty

**function:** instance_state

    Return the :class:`.InstanceState` for a given
    mapped object.

    This function is the internal version
    of :func:`.object_state`.   The
    :func:`.object_state` and/or the
    :func:`_sa.inspect` function is preferred here
    as they each emit an informative exception
    if the given object is not mapped.

**autofunction:** sqlalchemy.orm.instrumentation.is_instrumented

**autofunction:** set_attribute

**autofunction:** set_committed_value

**autoclass:** History
    :members:
