---
type: "Framework Learn Page"
framework: "sqlalchemy"
source_repo: "https://github.com/sqlalchemy/sqlalchemy"
source_branch: "main"
source_path: "doc/build/core/type_basics.rst"
source_commit: "ddf3b6589fd6ccb2affbaea5d4f400a8c1ad02d8"
source_commit_short: "ddf3b658"
source_commit_date: "2026-06-18T14:12:36-04:00"
generated_at: "2026-06-21T07:22:30Z"
---

# The Type Hierarchy

SQLAlchemy provides abstractions for most common database data types, as well as several techniques for customization of datatypes.

Database types are represented using Python classes, all of which ultimately extend from the base type class known as `_types.TypeEngine`. There are two general categories of datatypes, each of which express themselves within the typing hierarchy in different ways. The category used by an individual datatype class can be identified based on the use of two different naming conventions, which are "CamelCase" and "UPPERCASE".

> **Seealso:**  `tutorial_core_metadata` - in the `unified_tutorial`.  Illustrates
 the most rudimental use of `_types.TypeEngine` type objects to
 define `_schema.Table` metadata and introduces the concept
 of type objects in tutorial form.

## The "CamelCase" datatypes

The rudimental types have "CamelCase" names such as `_types.String, types.Numeric, types.Integer, and types.DateTime. All of the immediate subclasses of types.TypeEngine` are "CamelCase" types. The "CamelCase" types are to the greatest degree possible **database agnostic**, meaning they can all be used on any database backend where they will behave in such a way as appropriate to that backend in order to produce the desired behavior.

An example of a straightforward "CamelCase" datatype is `_types.String`. On most backends, using this datatype in a `table specification <metadata_describing>` will correspond to the `VARCHAR` database type being used on the target backend, delivering string values to and from the database, as in the example below:

```
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String

metadata_obj = MetaData()

user = Table(
    "user",
    metadata_obj,
    Column("user_name", String, primary_key=True),
    Column("email_address", String(60)),
)
```

When using a particular `_types.TypeEngine class in a schema.Table` definition or in any SQL expression overall, if no arguments are required it may be passed as the class itself, that is, without instantiating it with `()`. If arguments are needed, such as the length argument of 60 in the `"email_address"` column above, the type may be instantiated.

Another "CamelCase" datatype that expresses more backend-specific behavior is the `_types.Boolean datatype. Unlike types.String`, which represents a string datatype that all databases have, not every backend has a real "boolean" datatype; some make use of integers or BIT values 0 and 1, some have boolean literal constants `true` and `false while others dont.   For this datatype, types.Boolean` may render `BOOLEAN` on a backend such as PostgreSQL, `BIT` on the MySQL backend and `SMALLINT` on Oracle Database.  As data is sent and received from the database using this type, based on the dialect in use it may be interpreting Python numeric or boolean values.

The typical SQLAlchemy application will likely wish to use primarily "CamelCase" types in the general case, as they will generally provide the best basic behavior and be automatically portable to all backends.

Reference for the general set of "CamelCase" datatypes is below at `types_generic`.

## The "UPPERCASE" datatypes

In contrast to the "CamelCase" types are the "UPPERCASE" datatypes. These datatypes are always inherited from a particular "CamelCase" datatype, and always represent an **exact** datatype.   When using an "UPPERCASE" datatype, the name of the type is always rendered exactly as given, without regard for whether or not the current backend supports it.   Therefore the use of "UPPERCASE" types in a SQLAlchemy application indicates that specific datatypes are required, which then implies that the application would normally, without additional steps taken, be limited to those backends which use the type exactly as given.   Examples of UPPERCASE types include `_types.VARCHAR, types.NUMERIC, types.INTEGER, and types.TIMESTAMP, which inherit directly from the previously mentioned "CamelCase" types types.String, types.Numeric, types.Integer, and types.DateTime`, respectively.

The "UPPERCASE" datatypes that are part of `sqlalchemy.types` are common SQL types that typically expect to be available on at least two backends if not more.

Reference for the general set of "UPPERCASE" datatypes is below at `types_sqlstandard`.

## Backend-specific "UPPERCASE" datatypes

Most databases also have their own datatypes that are either fully specific to those databases, or add additional arguments that are specific to those databases.   For these datatypes, specific SQLAlchemy dialects provide **backend-specific** "UPPERCASE" datatypes, for a SQL type that has no analogue on other backends.  Examples of backend-specific uppercase datatypes include PostgreSQL's `_postgresql.JSONB, SQL Server's mssql.IMAGE and MySQL's mysql.TINYTEXT`.

Specific backends may also include "UPPERCASE" datatypes that extend the arguments available from that same "UPPERCASE" datatype as found in the `sqlalchemy.types` module. An example is when creating a MySQL string datatype, one might want to specify MySQL-specific arguments such as `charset` or `national, which are available from the MySQL version of mysql.VARCHAR as the MySQL-only parameters mysql.VARCHAR.charset and mysql.VARCHAR.national`.

API documentation for backend-specific types are in the dialect-specific documentation, listed at `dialect_toplevel`.

## Using "UPPERCASE" and Backend-specific types for multiple backends

Reviewing the presence of "UPPERCASE" and "CamelCase" types leads to the natural use case of how to make use of "UPPERCASE" datatypes for backend-specific options, but only when that backend is in use.   To tie together the database-agnostic "CamelCase" and backend-specific "UPPERCASE" systems, one makes use of the `_types.TypeEngine.with_variant` method in order to **compose** types together to work with specific behaviors on specific backends.

Such as, to use the `_types.String datatype, but when running on MySQL to make use of the mysql.VARCHAR.charset parameter of mysql.VARCHAR when the table is created on MySQL or MariaDB, types.TypeEngine.with_variant` may be used as below:

```
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.dialects.mysql import VARCHAR

metadata_obj = MetaData()

user = Table(
    "user",
    metadata_obj,
    Column("user_name", String(100), primary_key=True),
    Column(
        "bio",
        String(255).with_variant(VARCHAR(255, charset="utf8"), "mysql", "mariadb"),
    ),
)
```

In the above table definition, the `"bio"` column will have string-behaviors on all backends. On most backends it will render in DDL as `VARCHAR`. However on MySQL and MariaDB (indicated by database URLs that start with `mysql` or `mariadb`), it will render as `VARCHAR(255) CHARACTER SET utf8`.

> **Seealso:**  `_types.TypeEngine.with_variant` - additional usage examples and notes

## Generic "CamelCase" Types

Generic types specify a column that can read, write and store a particular type of Python data.  SQLAlchemy will choose the best database column type available on the target database when issuing a `CREATE TABLE` statement.  For complete control over which column type is emitted in `CREATE TABLE`, such as `VARCHAR` see `types_sqlstandard` and the other sections of this chapter.

## SQL Standard and Multiple Vendor "UPPERCASE" Types

This category of types refers to types that are either part of the SQL standard, or are potentially found within a subset of database backends. Unlike the "generic" types, the SQL standard/multi-vendor types have **no** guarantee of working on all backends, and will only work on those backends that explicitly support them by name.  That is, the type will always emit its exact name in DDL with `CREATE TABLE` is issued.
