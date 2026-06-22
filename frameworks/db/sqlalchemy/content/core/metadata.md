---
type: "Framework Learn Page"
framework: "sqlalchemy"
source_repo: "https://github.com/sqlalchemy/sqlalchemy"
source_branch: "main"
source_path: "doc/build/core/metadata.rst"
source_commit: "ddf3b6589fd6ccb2affbaea5d4f400a8c1ad02d8"
source_commit_short: "ddf3b658"
source_commit_date: "2026-06-18T14:12:36-04:00"
generated_at: "2026-06-21T07:22:30Z"
---

==================================

# Describing Databases with MetaData

This section discusses the fundamental `_schema.Table, schema.Column and schema.MetaData` objects.

> **Seealso:**  `tutorial_working_with_metadata` - tutorial introduction to
 SQLAlchemy's database metadata concept in the `unified_tutorial`

A collection of metadata entities is stored in an object aptly named `sqlalchemy.schema.MetaData`:

```
from sqlalchemy import MetaData

metadata_obj = MetaData()
```

`sqlalchemy.schema.MetaData` is a container object that keeps together many different features of a database (or multiple databases) being described.

To represent a table, use the `sqlalchemy.schema.Table` class. Its two primary arguments are the table name, then the `sqlalchemy.schema.MetaData` object which it will be associated with. The remaining positional arguments are mostly `sqlalchemy.schema.Column` objects describing each column:

```
from sqlalchemy import Table, Column, Integer, String

user = Table(
    "user",
    metadata_obj,
    Column("user_id", Integer, primary_key=True),
    Column("user_name", String(16), nullable=False),
    Column("email_address", String(60)),
    Column("nickname", String(50), nullable=False),
)
```

Above, a table called `user` is described, which contains four columns. The primary key of the table consists of the `user_id` column. Multiple columns may be assigned the `primary_key=True` flag which denotes a multi-column primary key, known as a composite primary key.

Note also that each column describes its datatype using objects corresponding to genericized types, such as `sqlalchemy.types.Integer` and `sqlalchemy.types.String`. SQLAlchemy features dozens of types of varying levels of specificity as well as the ability to create custom types. Documentation on the type system can be found at `types_toplevel`.

## Accessing Tables and Columns

The `sqlalchemy.schema.MetaData` object contains all of the schema constructs we've associated with it. It supports a few methods of accessing these table objects, such as the `sorted_tables` accessor which returns a list of each `sqlalchemy.schema.Table` object in order of foreign key dependency (that is, each table is preceded by all tables which it references):

```
>>> for t in metadata_obj.sorted_tables:
...     print(t.name)
user
user_preference
invoice
invoice_item
```

In most cases, individual `sqlalchemy.schema.Table` objects have been explicitly declared, and these objects are typically accessed directly as module-level variables in an application. Once a `sqlalchemy.schema.Table` has been defined, it has a full set of accessors which allow inspection of its properties. Given the following `sqlalchemy.schema.Table` definition:

```
employees = Table(
    "employees",
    metadata_obj,
    Column("employee_id", Integer, primary_key=True),
    Column("employee_name", String(60), nullable=False),
    Column("employee_dept", Integer, ForeignKey("departments.department_id")),
)
```

Note the `sqlalchemy.schema.ForeignKey` object used in this table - this construct defines a reference to a remote table, and is fully described in `metadata_foreignkeys`. Methods of accessing information about this table include:

```
# access the column "employee_id":
employees.columns.employee_id

# or just
employees.c.employee_id

# via string
employees.c["employee_id"]

# a tuple of columns may be returned using multiple strings
# (new in 2.0)
emp_id, name, type = employees.c["employee_id", "name", "type"]

# iterate through all columns
for c in employees.c:
    print(c)

# get the table's primary key columns
for primary_key in employees.primary_key:
    print(primary_key)

# get the table's foreign key objects:
for fkey in employees.foreign_keys:
    print(fkey)

# access the table's MetaData:
employees.metadata

# access a column's name, type, nullable, primary key, foreign key
employees.c.employee_id.name
employees.c.employee_id.type
employees.c.employee_id.nullable
employees.c.employee_id.primary_key
employees.c.employee_dept.foreign_keys

# get the "key" of a column, which defaults to its name, but can
# be any user-defined string:
employees.c.employee_name.key

# access a column's table:
employees.c.employee_id.table is employees

# get the table related by a foreign key
list(employees.c.employee_dept.foreign_keys)[0].column.table
```

> **Tip:** The `_sql.FromClause.c` collection, synonymous with the
`_sql.FromClause.columns` collection, is an instance of
`_sql.ColumnCollection`, which provides a **dictionary-like interface**
to the collection of columns.   Names are ordinarily accessed like
attribute names, e.g. `employees.c.employee_name`.  However for special names
with spaces or those that match the names of dictionary methods such as
`_sql.ColumnCollection.keys or sql.ColumnCollection.values`,
indexed access must be used, such as `employees.c['values']` or
`employees.c["some column"].  See sql.ColumnCollection` for
further information.

## Creating and Dropping Database Tables

Once you've defined some `sqlalchemy.schema.Table` objects, assuming you're working with a brand new database one thing you might want to do is issue CREATE statements for those tables and their related constructs (as an aside, it's also quite possible that you don't want to do this, if you already have some preferred methodology such as tools included with your database or an existing scripting system - if that's the case, feel free to skip this section - SQLAlchemy has no requirement that it be used to create your tables).

The usual way to issue CREATE is to use `sqlalchemy.schema.MetaData.create_all` on the `sqlalchemy.schema.MetaData` object. This method will issue queries that first check for the existence of each individual table, and if not found will issue the CREATE statements:

```python+sql
 engine = create_engine("sqlite:///:memory:")

 metadata_obj = MetaData()

 user = Table(
     "user",
     metadata_obj,
     Column("user_id", Integer, primary_key=True),
     Column("user_name", String(16), nullable=False),
     Column("email_address", String(60), key="email"),
     Column("nickname", String(50), nullable=False),
 )

 user_prefs = Table(
     "user_prefs",
     metadata_obj,
     Column("pref_id", Integer, primary_key=True),
     Column("user_id", Integer, ForeignKey("user.user_id"), nullable=False),
     Column("pref_name", String(40), nullable=False),
     Column("pref_value", String(100)),
 )

 metadata_obj.create_all(engine)
 {execsql}PRAGMA table_info(user){}
 CREATE TABLE user(
         user_id INTEGER NOT NULL PRIMARY KEY,
         user_name VARCHAR(16) NOT NULL,
         email_address VARCHAR(60),
         nickname VARCHAR(50) NOT NULL
 )
 PRAGMA table_info(user_prefs){}
 CREATE TABLE user_prefs(
         pref_id INTEGER NOT NULL PRIMARY KEY,
         user_id INTEGER NOT NULL REFERENCES user(user_id),
         pref_name VARCHAR(40) NOT NULL,
         pref_value VARCHAR(100)
 )
```

`sqlalchemy.schema.MetaData.create_all` creates foreign key constraints between tables usually inline with the table definition itself, and for this reason it also generates the tables in order of their dependency. There are options to change this behavior such that `ALTER TABLE` is used instead.

Dropping all tables is similarly achieved using the `sqlalchemy.schema.MetaData.drop_all` method. This method does the exact opposite of `sqlalchemy.schema.MetaData.create_all` - the presence of each table is checked first, and tables are dropped in reverse order of dependency.

Creating and dropping individual tables can be done via the `create()` and `drop()` methods of `sqlalchemy.schema.Table`. These methods by default issue the CREATE or DROP regardless of the table being present:

```python+sql
 engine = create_engine("sqlite:///:memory:")

 metadata_obj = MetaData()

 employees = Table(
     "employees",
     metadata_obj,
     Column("employee_id", Integer, primary_key=True),
     Column("employee_name", String(60), nullable=False, key="name"),
     Column("employee_dept", Integer, ForeignKey("departments.department_id")),
 )
 employees.create(engine)
 {execsql}CREATE TABLE employees(
     employee_id SERIAL NOT NULL PRIMARY KEY,
     employee_name VARCHAR(60) NOT NULL,
     employee_dept INTEGER REFERENCES departments(department_id)
 )
 {}
```

`drop()` method:

```python+sql
 employees.drop(engine)
 {execsql}DROP TABLE employees
 {}
```

To enable the "check first for the table existing" logic, add the `checkfirst=True` argument to `create()` or `drop()`:

```
employees.create(engine, checkfirst=True)
employees.drop(engine, checkfirst=False)
```

## Altering Database Objects through Migrations

While SQLAlchemy directly supports emitting CREATE and DROP statements for schema constructs, the ability to alter those constructs, usually via the ALTER statement as well as other database-specific constructs, is outside of the scope of SQLAlchemy itself.  While it's easy enough to emit ALTER statements and similar by hand, such as by passing a `_expression.text construct to engine.Connection.execute` or by using the `.DDL` construct, it's a common practice to automate the maintenance of database schemas in relation to application code using schema migration tools.

The SQLAlchemy project offers the  [Alembic](https://alembic.sqlalchemy.org) migration tool for this purpose.   Alembic features a highly customizable environment and a minimalistic usage pattern, supporting such features as transactional DDL, automatic generation of "candidate" migrations, an "offline" mode which generates SQL scripts, and support for branch resolution.

Alembic supersedes the [SQLAlchemy-Migrate](https://github.com/openstack/sqlalchemy-migrate)   project, which is the original migration tool for SQLAlchemy and is now  considered legacy.

## Specifying the Schema Name

Most databases support the concept of multiple "schemas" - namespaces that refer to alternate sets of tables and other constructs.  The server-side geometry of a "schema" takes many forms, including names of "schemas" under the scope of a particular database (e.g. PostgreSQL schemas), named sibling databases (e.g. MySQL / MariaDB access to other databases on the same server), as well as other concepts like tables owned by other usernames (Oracle Database, SQL Server) or even names that refer to alternate database files (SQLite ATTACH) or remote servers (Oracle Database DBLINK with synonyms).

What all of the above approaches have (mostly) in common is that there's a way of referencing this alternate set of tables using a string name.  SQLAlchemy refers to this name as the **schema name**.  Within SQLAlchemy, this is nothing more than a string name which is associated with a `_schema.Table` object, and is then rendered into SQL statements in a manner appropriate to the target database such that the table is referenced in its remote "schema", whatever mechanism that is on the target database.

The "schema" name may be associated directly with a `_schema.Table using the schema.Table.schema` argument; when using the ORM with `declarative table <orm_declarative_table_config_toplevel> configuration, the parameter is passed using the _table_args__` parameter dictionary.

The "schema" name may also be associated with the `_schema.MetaData object where it will take effect automatically for all schema.Table objects associated with that schema.MetaData that don't otherwise specify their own name.  Finally, SQLAlchemy also supports a "dynamic" schema name system that is often used for multi-tenant applications such that a single set of schema.Table` metadata may refer to a dynamically configured set of schema names on a per-connection or per-statement basis.

> **Seealso:**  `orm_declarative_table_schema_name` - schema name specification when using the ORM
 `declarative table <orm_declarative_table_config_toplevel>` configuration

The most basic example is that of the `_schema.Table.schema argument using a Core schema.Table` object as follows:

```
metadata_obj = MetaData()

financial_info = Table(
    "financial_info",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("value", String(100), nullable=False),
    schema="remote_banks",
)
```

SQL that is rendered using this `_schema.Table`, such as the SELECT statement below, will explicitly qualify the table name `financial_info` with the `remote_banks` schema name:

```pycon+sql
 >>> print(select(financial_info))
 {printsql}SELECT remote_banks.financial_info.id, remote_banks.financial_info.value
 FROM remote_banks.financial_info
```

When a `_schema.Table object is declared with an explicit schema name, it is stored in the internal schema.MetaData namespace using the combination of the schema and table name.  We can view this in the schema.MetaData.tables` collection by searching for the key `'remote_banks.financial_info'`:

```
>>> metadata_obj.tables["remote_banks.financial_info"]
Table('financial_info', MetaData(),
Column('id', Integer(), table=<financial_info>, primary_key=True, nullable=False),
Column('value', String(length=100), table=<financial_info>, nullable=False),
schema='remote_banks')
```

This dotted name is also what must be used when referring to the table for use with the `_schema.ForeignKey or schema.ForeignKeyConstraint` objects, even if the referring table is also in that same schema:

```
customer = Table(
    "customer",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("financial_info_id", ForeignKey("remote_banks.financial_info.id")),
    schema="remote_banks",
)
```

The `_schema.Table.schema` argument may also be used with certain dialects to indicate a multiple-token (e.g. dotted) path to a particular table.  This is particularly important on a database such as Microsoft SQL Server where there are often dotted "database/owner" tokens.  The tokens may be placed directly in the name at once, such as:

```
schema = "dbo.scott"
```

> **Seealso:**  `multipart_schema_names` - describes use of dotted schema names
 with the SQL Server dialect.
 `metadata_reflection_schemas`

#### Specifying a Default Schema Name with MetaData

The `_schema.MetaData object may also set up an explicit default option for all schema.Table.schema parameters by passing the schema.MetaData.schema argument to the top level schema.MetaData` construct:

```
metadata_obj = MetaData(schema="remote_banks")

financial_info = Table(
    "financial_info",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("value", String(100), nullable=False),
)
```

Above, for any `_schema.Table object (or schema.Sequence object directly associated with the schema.MetaData) which leaves the schema.Table.schema` parameter at its default of `None` will instead act as though the parameter were set to the value `"remote_banks".  This includes that the schema.Table is cataloged in the schema.MetaData` using the schema-qualified name, that is:

```
metadata_obj.tables["remote_banks.financial_info"]
```

When using the `_schema.ForeignKey or schema.ForeignKeyConstraint` objects to refer to this table, either the schema-qualified name or the non-schema-qualified name may be used to refer to the `remote_banks.financial_info` table:

```
# either will work:

refers_to_financial_info = Table(
    "refers_to_financial_info",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("fiid", ForeignKey("financial_info.id")),
)

# or

refers_to_financial_info = Table(
    "refers_to_financial_info",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("fiid", ForeignKey("remote_banks.financial_info.id")),
)
```

When using a `_schema.MetaData object that sets schema.MetaData.schema, a schema.Table that wishes to specify that it should not be schema qualified may use the special symbol schema.BLANK_SCHEMA`:

```
from sqlalchemy import BLANK_SCHEMA

metadata_obj = MetaData(schema="remote_banks")

financial_info = Table(
    "financial_info",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("value", String(100), nullable=False),
    schema=BLANK_SCHEMA,  # will not use "remote_banks"
)
```

> **Seealso:**  `_schema.MetaData.schema`

#### Applying Dynamic Schema Naming Conventions

The names used by the `_schema.Table.schema` parameter may also be applied against a lookup that is dynamic on a per-connection or per-execution basis, so that for example in multi-tenant situations, each transaction or statement may be targeted at a specific set of schema names that change. The section `schema_translating` describes how this feature is used.

> **Seealso:**  `schema_translating`

#### Setting a Default Schema for New Connections

The above approaches all refer to methods of including an explicit schema-name within SQL statements.  Database connections in fact feature the concept of a "default" schema, which is the name of the "schema" (or database, owner, etc.) that takes place if a table name is not explicitly schema-qualified. These names are usually configured at the login level, such as when connecting to a PostgreSQL database, the default "schema" is called "public".

There are often cases where the default "schema" cannot be set via the login itself and instead would usefully be configured each time a connection is made, using a statement such as "SET SEARCH_PATH" on PostgreSQL or "ALTER SESSION" on Oracle Database.  These approaches may be achieved by using the `_pool.PoolEvents.connect` event, which allows access to the DBAPI connection when it is first created.  For example, to set the Oracle Database CURRENT_SCHEMA variable to an alternate name:

```
from sqlalchemy import event
from sqlalchemy import create_engine

engine = create_engine(
    "oracle+oracledb://scott:tiger@localhost:1521?service_name=freepdb1"
)

@event.listens_for(engine, "connect", insert=True)
def set_current_schema(dbapi_connection, connection_record):
    cursor_obj = dbapi_connection.cursor()
    cursor_obj.execute("ALTER SESSION SET CURRENT_SCHEMA=%s" % schema_name)
    cursor_obj.close()
```

Above, the `set_current_schema() event handler will take place immediately when the above engine.Engine` first connects; as the event is "inserted" into the beginning of the handler list, it will also take place before the dialect's own event handlers are run, in particular including the one that will determine the "default schema" for the connection.

For other databases, consult the database and/or dialect documentation for specific information regarding how default schemas are configured.

.. versionchanged:: 1.4.0b2  The above recipe now works without the need to

> **Seealso:**  `postgresql_alternate_search_path` - in the `postgresql_toplevel` dialect documentation.

#### Schemas and Reflection

The schema feature of SQLAlchemy interacts with the table reflection feature introduced at `metadata_reflection_toplevel`.  See the section `metadata_reflection_schemas` for additional details on how this works.

## Alternate CREATE TABLE forms: CREATE VIEW, CREATE TABLE AS

.. versionadded:: 2.1 SQLAlchemy 2.1 introduces new table creation DDL

The `.MetaData.create_all` sequence discussed at `metadata_creating_and_dropping` makes use of a `.DDL` construct called `.CreateTable` in order to emit the actual `CREATE TABLE` statement. SQLAlchemy 2.1 features additional DDL constructs that can create tables and views from SELECT statements: `.CreateTableAs` and `.CreateView. Both classes are constructed with a sql.select` object that serves as the source of data. Once constructed, they each provide access to a dynamically-generated `.Table` object that contains the correct name and `.Column` configuration; this `.Table can then be used in subsequent sql.select` statements to query the new table or view. To emit the actual `CREATE TABLE AS` or `CREATE VIEW` statement to a database, the `.CreateTableAs` or `.CreateView` objects may be invoked directly via `.Connection.execute`, or they will be invoked automatically via the `.Table.create` method or `.MetaData.create_all` if a `.MetaData` is provided to the constructor.

#### Using `.CreateView`

The `.CreateView` construct provides support for the `CREATE VIEW` DDL construct, which allows the creation of database views that represent the result of a SELECT statement. Unlike a table, a view does not store data directly; instead, it dynamically evaluates the underlying SELECT query whenever the view is accessed. A compatible SQL syntax is supported by all included SQLAlchemy backends.

A `.CreateView expression may be produced from a sql.select` created against any combinations of tables:

```
>>> from sqlalchemy.sql.ddl import CreateView
>>> select_stmt = select(user.c.user_id, user.c.user_name).where(user.c.status == "active")
>>> create_view = CreateView(select_stmt, "active_users")
```

Stringifying this construct illustrates the `CREATE VIEW` syntax:

```
>>> print(create_view)
CREATE VIEW active_users AS SELECT "user".user_id, "user".user_name
FROM "user"
WHERE "user".status = 'active'
```

A `.Table` object corresponding to the structure of the view that would be created can be accessed via the `.CreateView.table attribute as soon as the object is constructed.  New Core sql.select` objects can use this `.Table` like any other selectable:

```
>>> view_stmt = select(create_view.table).where(create_view.table.c.user_id > 5)
>>> print(view_stmt)
SELECT active_users.user_id, active_users.user_name
FROM active_users
WHERE active_users.user_id > :user_id_1
```

The DDL for `.CreateView` may be executed in a database either by calling standard `.Table.create` or `.MetaData.create_all` methods, or by executing the construct directly:

```pycon+sql
 >>> with engine.begin() as connection:
 ...     connection.execute(create_view)
 {opensql}BEGIN (implicit)
 CREATE VIEW active_users AS SELECT user.user_id, user.user_name
 FROM user
 WHERE user.status = 'active'
 COMMIT
```

The database now has a new view `active_users` which will dynamically evaluate the SELECT statement whenever the view is queried.

`.CreateView` interacts with a `.MetaData` collection; an explicit `.MetaData` may be passed using the `.CreateView.metadata` parameter, where operations like `.MetaData.create_all` and `.MetaData.drop_all` may be used to emit a CREATE / DROP DDL within larger DDL sequences.   `.CreateView` includes itself in the new `.Table` via the `.Table.set_creator_ddl` method and also applies `.DropView` to the `.Table.set_dropper_ddl` elements, so that `CREATE VIEW` and `DROP VIEW` will be emitted for the `.Table`:

```pycon+sql
 >>> create_view = CreateView(select_stmt, "active_users", metadata=metadata_obj)
 >>> metadata_obj.create_all(engine)
 {opensql}BEGIN (implicit)
 PRAGMA main.table_info("active_users")
 ...
 CREATE VIEW active_users AS SELECT user.user_id, user.user_name
 FROM user
 WHERE user.status = 'active'
 COMMIT
```

DROP may be emitted for this view alone using `.Table.drop` against `.CreateView.table`, just like it would be used for any other table; the `.DropView` DDL construct will be invoked:

```pycon+sql
 >>> create_view.table.drop(engine)
 {opensql}DROP VIEW active_users
 COMMIT
```

`.CreateView` supports optional flags such as `TEMPORARY`, `OR REPLACE`, and `MATERIALIZED` where supported by the target database:

```
>>> # Create a view with OR REPLACE
>>> stmt = CreateView(
...     select(user.c.user_id, user.c.user_name),
...     "user_snapshot",
...     or_replace=True,
... )
>>> print(stmt)
CREATE OR REPLACE VIEW user_snapshot AS SELECT user.user_id, user.user_name
FROM user
```

The `OR REPLACE` clause renders in all forms, including a simple use of `.Table.create`, which does not use a "checkfirst" query by default:

```
>>> stmt.table.create(engine)
BEGIN (implicit)
CREATE OR REPLACE VIEW user_snapshot AS SELECT user.user_id, user.user_name
FROM user
COMMIT
```

> **Tip:**  The exact phrase `OR REPLACE` is supported by PostgreSQL, Oracle
 Database, MySQL and MariaDB.   When `.CreateView` with
 `.CreateView.or_replace` is used on Microsoft SQL Server, the
 equivalent keywords `OR ALTER` is emitted instead.   The remaining
 SQLAlchemy-native dialect, SQLite, remains an outlier - for SQLite, the
 dialect-specific parameter `sqlite_if_not_exists` may be used to create a
 view with a check for already existing::
     stmt = CreateView(
         select(user.c.user_id, user.c.user_name),
         "user_snapshot",
         sqlite_if_not_exists=True,
     )
 `sqlite_if_not_exists` is separate from `.CreateView.or_replace`
 since it has a different meaning, leaving an existing view unmodified
 whereas `.CreateView.or_replace` will update the definition of
 an existing view.

The `MATERIALIZED` keyword may be emitted by specifying `.CreateView.materialized`:

```
>>> stmt = CreateView(
...     select(user.c.user_id, user.c.user_name),
...     "user_snapshot",
...     materialized=True,
... )
>>> print(stmt)
CREATE MATERIALIZED VIEW user_snapshot AS SELECT user.user_id, user.user_name
FROM user
```

Materialized views store the query results physically and can offer performance benefits for complex queries, though they typically need to be refreshed periodically using database-specific commands.   The Oracle and PostgreSQL backends currently support `MATERIALIZED`; however it may be the case that `MATERIALIZED` cannot be combined with `OR REPLACE`.

#### Using `.CreateTableAs` or `.Select.into`

The `.CreateTableAs` construct, along with a complementing method `.Select.into`, provides support for the "CREATE TABLE AS" / "SELECT INTO" DDL constructs, which allows the creation of new tables in the database that represent the contents of an arbitrary SELECT statement. A compatible SQL syntax is supported by all included SQLAlchemy backends.

A `_schema.CreateTableAs expression may be produced from a sql.select` created against any combinations of tables:

```
>>> from sqlalchemy import select, CreateTableAs
>>> select_stmt = select(user.c.user_id, user.c.user_name).where(
...     user.c.user_name.like("sponge%")
... )
>>> create_table_as = CreateTableAs(select_stmt, "spongebob_users")
```

The equivalent `.Select.into` method may also be used; this creates a `.CreateTableAs` construct as well:

```
>>> create_table_as = select_stmt.into("spongebob_users")
```

Stringifying this construct on most backends illustrates the `CREATE TABLE AS` syntax:

```
>>> print(create_table_as)
CREATE TABLE spongebob_users AS SELECT "user".user_id, "user".user_name
FROM "user"
WHERE "user".user_name LIKE 'sponge%'
```

On Microsoft SQL Server, SELECT INTO is generated instead:

```
>>> from sqlalchemy.dialects import mssql
>>> print(create_table_as.compile(dialect=mssql.dialect()))
SELECT [user].user_id, [user].user_name INTO spongebob_users
FROM [user]
WHERE [user].user_name LIKE 'sponge%'
```

A `.Table` object corresponding to the structure of the view that would be created can be accessed via the `.CreateTableAs.table attribute as soon as the object is constructed.  New Core sql.select` objects can use this `.Table` like any other selectable:

```
>>> ctas_stmt = select(create_table_as.table).where(create_table_as.table.c.user_id > 5)
>>> print(ctas_stmt)
SELECT spongebob_users.user_id, spongebob_users.user_name
FROM spongebob_users
WHERE spongebob_users.user_id > :user_id_1
```

The DDL for `.CreateTableAs` may be executed in a database either by calling standard `.Table.create` or `.MetaData.create_all` methods, or by executing the construct directly:

```pycon+sql
 >>> with engine.begin() as connection:
 ...     connection.execute(create_table_as)
 {opensql}BEGIN (implicit)
 CREATE TABLE spongebob_users AS SELECT user.user_id, user.user_name
 FROM user
 WHERE user.user_name LIKE 'sponge%'
 COMMIT
```

The database now has a new table `spongebob_users` which contains all the columns and rows that would be returned by the SELECT statement.   This is a real table in the database that will remain until we drop it (unless it's a temporary table that automatically drops, or if transactional DDL is rolled back).

Like `.CreateView`, `.CreateTableAs` interacts with a `.MetaData` collection; an explicit `.MetaData` may be passed using the `.CreateTableAs.metadata` parameter, where operations like `.MetaData.create_all` and `.MetaData.drop_all` may be used to emit a CREATE / DROP DDL within larger DDL sequences.   `.CreateView` includes itself in the new `.Table` via the `.Table.set_creator_ddl` method, so that `CREATE TABLE AS <statement>` will be emitted for the `.Table`:

```pycon+sql
 >>> create_table_as = CreateTableAs(select_stmt, "spongebob_users", metadata=metadata_obj)
 >>> metadata_obj.create_all(engine)
 {opensql}BEGIN (implicit)
 PRAGMA main.table_info("spongebob_users")
 ...
 CREATE TABLE spongebob_users AS SELECT user.user_id, user.user_name
 FROM user
 WHERE user.user_name LIKE 'sponge%'
 COMMIT
```

DROP may be emitted for this table alone using `.Table.drop` against `.CreateTableAs.table`, just like it would be used for any other table:

```pycon+sql
 >>> create_table_as.table.drop(engine)
 {opensql}DROP TABLE spongebob_users
 COMMIT
```

`.CreateTableAs` and `.Select.into` both support optional flags such as `TEMPORARY` and `IF NOT EXISTS` where supported by the target database:

```
>>> # Create a temporary table with IF NOT EXISTS
>>> stmt = select(user.c.user_id, user.c.user_name).into(
...     "temp_snapshot", temporary=True, if_not_exists=True
... )
>>> print(stmt)
CREATE TEMPORARY TABLE IF NOT EXISTS temp_snapshot AS SELECT user_account.id, user_account.name
FROM user_account
```

The `IF NOT EXISTS` clause renders in all forms, including a simple use of `.Table.create`, which does not use a "checkfirst" query by default:

```
>>> stmt.table.create(engine)
BEGIN (implicit)
CREATE TEMPORARY TABLE IF NOT EXISTS temp_snapshot AS SELECT user.user_id, user.user_name
FROM user
COMMIT
```

## Backend-Specific Options for `.Table`

`sqlalchemy.schema.Table` supports database-specific options. For example, MySQL has different table backend types, including "MyISAM" and "InnoDB". This can be expressed with `sqlalchemy.schema.Table` using `mysql_engine`:

```
addresses = Table(
    "engine_email_addresses",
    metadata_obj,
    Column("address_id", Integer, primary_key=True),
    Column("remote_user_id", Integer, ForeignKey(users.c.user_id)),
    Column("email_address", String(20)),
    mysql_engine="InnoDB",
)
```

Other backends may support table-level options as well - these would be described in the individual documentation sections for each dialect.

## Column, Table, MetaData API
