---
type: "Framework Learn Page"
framework: "sqlalchemy"
source_repo: "https://github.com/sqlalchemy/sqlalchemy"
source_branch: "main"
source_path: "doc/build/dialects/oracle.rst"
source_commit: "ddf3b6589fd6ccb2affbaea5d4f400a8c1ad02d8"
source_commit_short: "ddf3b658"
source_commit_date: "2026-06-18T14:12:36-04:00"
generated_at: "2026-06-21T07:22:30Z"
---

# Oracle

## Oracle Database Data Types

As with all SQLAlchemy dialects, all UPPERCASE types that are known to be valid with Oracle Database are importable from the top level dialect, whether they originate from `sqlalchemy.types` or from the local dialect:

```
from sqlalchemy.dialects.oracle import (
    BFILE,
    BLOB,
    BOOLEAN,
    CHAR,
    CLOB,
    DATE,
    DOUBLE_PRECISION,
    FLOAT,
    INTERVAL,
    LONG,
    NCLOB,
    NCHAR,
    NUMBER,
    NVARCHAR,
    NVARCHAR2,
    RAW,
    TIMESTAMP,
    VARCHAR,
    VARCHAR2,
    VECTOR,
)
```

Types which are specific to Oracle Database, or have Oracle-specific construction arguments, are as follows:

## python-oracledb

.. versionchanged:: 2.1

## cx_Oracle

.. versionchanged:: 2.1
