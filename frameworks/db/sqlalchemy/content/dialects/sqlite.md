---
type: "Framework Learn Page"
framework: "SQLAlchemy"
source_repo: "https://github.com/sqlalchemy/sqlalchemy"
source_branch: "main"
source_path: "doc/build/dialects/sqlite.rst"
source_commit: "85cafd1a131fa8afeeeab23151940480b3fb0042"
source_commit_short: "85cafd1"
source_commit_date: "2026-08-28T20:17:49+00:00"
generated_at: "2026-08-29T09:39:27.547691Z"
---
.. _sqlite_toplevel:

# SQLite

**automodule:** sqlalchemy.dialects.sqlite.base

## SQLite Data Types

As with all SQLAlchemy dialects, all UPPERCASE types that are known to be
valid with SQLite are importable from the top level dialect, whether
they originate from :mod:`sqlalchemy.types` or from the local dialect::

    from sqlalchemy.dialects.sqlite import (
        BLOB,
        BOOLEAN,
        CHAR,
        DATE,
        DATETIME,
        DECIMAL,
        FLOAT,
        INTEGER,
        NUMERIC,
        JSON,
        SMALLINT,
        TEXT,
        TIME,
        TIMESTAMP,
        VARCHAR,
    )

**module:** sqlalchemy.dialects.sqlite

**autoclass:** DATETIME

**autoclass:** DATE

**autoclass:** JSON

**autoclass:** JSONB

**autoclass:** TIME

## SQLite DML Constructs

**autofunction:** sqlalchemy.dialects.sqlite.insert

**autoclass:** sqlalchemy.dialects.sqlite.Insert
  :members:

.. _pysqlite:

## Pysqlite

**automodule:** sqlalchemy.dialects.sqlite.pysqlite

.. _aiosqlite:

## Aiosqlite

**automodule:** sqlalchemy.dialects.sqlite.aiosqlite


.. _pysqlcipher:

## Pysqlcipher

**automodule:** sqlalchemy.dialects.sqlite.pysqlcipher