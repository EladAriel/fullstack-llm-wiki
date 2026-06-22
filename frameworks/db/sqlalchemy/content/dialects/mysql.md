---
type: "Framework Learn Page"
framework: "sqlalchemy"
source_repo: "https://github.com/sqlalchemy/sqlalchemy"
source_branch: "main"
source_path: "doc/build/dialects/mysql.rst"
source_commit: "ddf3b6589fd6ccb2affbaea5d4f400a8c1ad02d8"
source_commit_short: "ddf3b658"
source_commit_date: "2026-06-18T14:12:36-04:00"
generated_at: "2026-06-21T07:22:30Z"
---

# MySQL and MariaDB

## MySQL SQL Constructs

## MySQL Data Types

As with all SQLAlchemy dialects, all UPPERCASE types that are known to be valid with MySQL are importable from the top level dialect:

```
from sqlalchemy.dialects.mysql import (
    BIGINT,
    BINARY,
    BIT,
    BLOB,
    BOOLEAN,
    CHAR,
    DATE,
    DATETIME,
    DECIMAL,
    DECIMAL,
    DOUBLE,
    ENUM,
    FLOAT,
    INTEGER,
    LONGBLOB,
    LONGTEXT,
    MEDIUMBLOB,
    MEDIUMINT,
    MEDIUMTEXT,
    NCHAR,
    NUMERIC,
    NVARCHAR,
    REAL,
    SET,
    SMALLINT,
    TEXT,
    TIME,
    TIMESTAMP,
    TINYBLOB,
    TINYINT,
    TINYTEXT,
    VARBINARY,
    VARCHAR,
    YEAR,
)
```

In addition to the above types, MariaDB also supports the following:

```
from sqlalchemy.dialects.mysql import (
    INET4,
    INET6,
)
```

Types which are specific to MySQL or MariaDB, or have specific construction arguments, are as follows:

in the dialect module, just imported from sqltypes.  this avoids warnings in the sphinx build

## MySQL DML Constructs

## mysqlclient (fork of MySQL-Python)

## PyMySQL

## MariaDB-Connector

## MySQL-Connector

## asyncmy

## aiomysql

## cymysql

## pyodbc
