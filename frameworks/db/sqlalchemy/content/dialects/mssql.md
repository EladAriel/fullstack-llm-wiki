---
type: "Framework Learn Page"
framework: "sqlalchemy"
source_repo: "https://github.com/sqlalchemy/sqlalchemy"
source_branch: "main"
source_path: "doc/build/dialects/mssql.rst"
source_commit: "aa1a5575358d3aa14953b04dced02f4763fed2e7"
source_commit_short: "aa1a5575"
source_commit_date: "2026-07-23T18:02:59Z"
generated_at: "2026-07-25T11:50:45Z"
---

# Microsoft SQL Server

## SQL Server SQL Constructs

## SQL Server Data Types

As with all SQLAlchemy dialects, all UPPERCASE types that are known to be valid with SQL server are importable from the top level dialect, whether they originate from `sqlalchemy.types` or from the local dialect:

```
from sqlalchemy.dialects.mssql import (
    BIGINT,
    BINARY,
    BIT,
    CHAR,
    DATE,
    DATETIME,
    DATETIME2,
    DATETIMEOFFSET,
    DECIMAL,
    DOUBLE_PRECISION,
    FLOAT,
    IMAGE,
    INTEGER,
    JSON,
    MONEY,
    NCHAR,
    NTEXT,
    NUMERIC,
    NVARCHAR,
    REAL,
    SMALLDATETIME,
    SMALLINT,
    SMALLMONEY,
    SQL_VARIANT,
    TEXT,
    TIME,
    TIMESTAMP,
    TINYINT,
    UNIQUEIDENTIFIER,
    VARBINARY,
    VARCHAR,
)
```

Types which are specific to SQL Server, or have SQL Server-specific construction arguments, are as follows:

in the dialect module, just imported from sqltypes.  this avoids warnings in the sphinx build

## PyODBC

## mssql-python

## pymssql

## aioodbc
