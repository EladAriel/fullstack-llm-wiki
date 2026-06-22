---
type: "Framework Learn Page"
framework: "sqlalchemy"
source_repo: "https://github.com/sqlalchemy/sqlalchemy"
source_branch: "main"
source_path: "doc/build/core/defaults.rst"
source_commit: "ddf3b6589fd6ccb2affbaea5d4f400a8c1ad02d8"
source_commit_short: "ddf3b658"
source_commit_date: "2026-06-18T14:12:36-04:00"
generated_at: "2026-06-21T07:22:30Z"
---

# Column INSERT/UPDATE Defaults

Column INSERT and UPDATE defaults refer to functions that create a **default value** for a particular column in a row as an INSERT or UPDATE statement is proceeding against that row, in the case where **no value was provided to the INSERT or UPDATE statement for that column**.  That is, if a table has a column called "timestamp", and an INSERT statement proceeds which does not include a value for this column, an INSERT default would create a new value, such as the current time, that is used as the value to be INSERTed into the "timestamp" column.  If the statement does include a value  for this column, then the default does not take place.

Column defaults can be server-side functions or constant values which are defined in the database along with the schema in `DDL`, or as SQL expressions which are rendered directly within an INSERT or UPDATE statement emitted by SQLAlchemy; they may also be client-side Python functions or constant values which are invoked by SQLAlchemy before data is passed to the database.

> **Note:**  A column default handler should not be confused with a construct that
 intercepts and modifies incoming values for INSERT and UPDATE statements
 which are provided to the statement as it is invoked.  This is known
 as `data marshalling`, where a column value is modified in some way
 by the application before being sent to the database.  SQLAlchemy provides
 a few means of achieving this which include using :ref:`custom datatypes
 <types_typedecorator>`, `SQL execution events <core_sql_events>` and
 in the ORM `custom  validators <simple_validators>` as well as
 `attribute events <orm_attribute_events>`.    Column defaults are only
 invoked when there is **no value present** for a column in a SQL
 `DML` statement.

SQLAlchemy provides an array of features regarding default generation functions which take place for non-present values during INSERT and UPDATE statements. Options include:

- Scalar values used as defaults during INSERT and UPDATE operations
- Python functions which execute upon INSERT and UPDATE operations
- SQL expressions which are embedded in INSERT statements (or in some cases execute beforehand)
- SQL expressions which are embedded in UPDATE statements
- Server side default values used during INSERT
- Markers for server-side triggers used during UPDATE
The general rule for all insert/update defaults is that they only take effect if no value for a particular column is passed as an `execute()` parameter; otherwise, the given value is used.

## Scalar Defaults

The simplest kind of default is a scalar value used as the default value of a column:

```
Table("mytable", metadata_obj, Column("somecolumn", Integer, default=12))
```

Above, the value "12" will be bound as the column value during an INSERT if no other value is supplied.

A scalar value may also be associated with an UPDATE statement, though this is not very common (as UPDATE statements are usually looking for dynamic defaults):

```
Table("mytable", metadata_obj, Column("somecolumn", Integer, onupdate=25))
```

## Python-Executed Functions

The `_schema.Column.default and schema.Column.onupdate` keyword arguments also accept Python functions. These functions are invoked at the time of insert or update if no other value for that column is supplied, and the value returned is used for the column's value. Below illustrates a crude "sequence" that assigns an incrementing counter to a primary key column:

```
# a function which counts upwards
i = 0

def mydefault():
    global i
    i += 1
    return i

t = Table(
    "mytable",
    metadata_obj,
    Column("id", Integer, primary_key=True, default=mydefault),
)
```

It should be noted that for real "incrementing sequence" behavior, the built-in capabilities of the database should normally be used, which may include sequence objects or other autoincrementing capabilities. For primary key columns, SQLAlchemy will in most cases use these capabilities automatically. See the API documentation for `sqlalchemy.schema.Column including the schema.Column.autoincrement` flag, as well as the section on `sqlalchemy.schema.Sequence` later in this chapter for background on standard primary key generation techniques.

To illustrate onupdate, we assign the Python `datetime` function `now to the schema.Column.onupdate` attribute:

```
import datetime

t = Table(
    "mytable",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    # define 'last_updated' to be populated with datetime.now()
    Column("last_updated", DateTime, onupdate=datetime.datetime.now),
)
```

When an update statement executes and no value is passed for `last_updated`, the `datetime.datetime.now()` Python function is executed and its return value used as the value for `last_updated`. Notice that we provide `now` as the function itself without calling it (i.e. there are no parenthesis following) - SQLAlchemy will execute the function at the time the statement executes.

### Context-Sensitive Default Functions

The Python functions used by `_schema.Column.default and schema.Column.onupdate` may also make use of the current statement's context in order to determine a value. The `context` of a statement is an internal SQLAlchemy object which contains all information about the statement being executed, including its source expression, the parameters associated with it and the cursor. The typical use case for this context with regards to default generation is to have access to the other values being inserted or updated on the row. To access the context, provide a function that accepts a single `context` argument:

```
def mydefault(context):
    return context.get_current_parameters()["counter"] + 12

t = Table(
    "mytable",
    metadata_obj,
    Column("counter", Integer),
    Column("counter_plus_twelve", Integer, default=mydefault, onupdate=mydefault),
)
```

The above default generation function is applied so that it will execute for all INSERT and UPDATE statements where a value for `counter_plus_twelve` was otherwise not provided, and the value will be that of whatever value is present in the execution for the `counter` column, plus the number 12.

For a single statement that is being executed using "executemany" style, e.g. with multiple parameter sets passed to `_engine.Connection.execute, the user-defined function is called once for each set of parameters. For the use case of a multi-valued expression.Insert construct (e.g. with more than one VALUES clause set up via the expression.Insert.values` method), the user-defined function is also called once for each set of parameters.

When the function is invoked, the special method `.DefaultExecutionContext.get_current_parameters` is available from the context object (a subclass of `.ExecutionContext`).  This method returns a dictionary of column-key to values that represents the full set of values for the INSERT or UPDATE statement.   In the case of a multi-valued INSERT construct, the subset of parameters that corresponds to the individual VALUES clause is isolated from the full parameter dictionary and returned alone.

## Client-Invoked SQL Expressions

The `_schema.Column.default and schema.Column.onupdate` keywords may also be passed SQL expressions, which are in most cases rendered inline within the INSERT or UPDATE statement:

```
t = Table(
    "mytable",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    # define 'create_date' to default to now()
    Column("create_date", DateTime, default=func.now()),
    # define 'key' to pull its default from the 'keyvalues' table
    Column(
        "key",
        String(20),
        default=select(keyvalues.c.key).where(keyvalues.c.type="type1"),
    ),
    # define 'last_modified' to use the current_timestamp SQL function on update
    Column("last_modified", DateTime, onupdate=func.utc_timestamp()),
)
```

Above, the `create_date` column will be populated with the result of the `now()` SQL function (which, depending on backend, compiles into `NOW()` or `CURRENT_TIMESTAMP` in most cases) during an INSERT statement, and the `key` column with the result of a SELECT subquery from another table. The `last_modified` column will be populated with the value of the SQL `UTC_TIMESTAMP()` MySQL function when an UPDATE statement is emitted for this table.

> **Note:**  When using SQL functions with the `.func` construct, we "call" the
 named function, e.g. with parenthesis as in `func.now()`.   This differs
 from when we specify a Python callable as a default such as
 `datetime.datetime`, where we pass the function itself, but we don't
 invoke it ourselves.   In the case of a SQL function, invoking
 `func.now()` returns the SQL expression object that will render the
 "NOW" function into the SQL being emitted.

Default and update SQL expressions specified by `_schema.Column.default and schema.Column.onupdate` are invoked explicitly by SQLAlchemy when an INSERT or UPDATE statement occurs, typically rendered inline within the DML statement except in certain cases listed below.   This is different than a "server side" default, which is part of the table's DDL definition, e.g. as part of the "CREATE TABLE" statement, which are likely more common.   For server side defaults, see the next section `server_defaults`.

When a SQL expression indicated by `_schema.Column.default` is used with primary key columns, there are some cases where SQLAlchemy must "pre-execute" the default generation SQL function, meaning it is invoked in a separate SELECT statement, and the resulting value is passed as a parameter to the INSERT. This only occurs for primary key columns for an INSERT statement that is being asked to return this primary key value, where RETURNING or `cursor.lastrowid may not be used.   An expression.Insert` construct that specifies the `.expression.insert.inline` flag will always render default expressions inline.

When the statement is executed with a single set of parameters (that is, it is not an "executemany" style execution), the returned `sqlalchemy.engine.CursorResult will contain a collection accessible via engine.CursorResult.postfetch_cols` which contains a list of all `sqlalchemy.schema.Column objects which had an inline-executed default. Similarly, all parameters which were bound to the statement, including all Python and SQL expressions which were pre-executed, are present in the engine.CursorResult.last_inserted_params or engine.CursorResult.last_updated_params` collections on `sqlalchemy.engine.CursorResult. The engine.CursorResult.inserted_primary_key` collection contains a list of primary key values for the row inserted (a list so that single-column and composite-column primary keys are represented in the same format).

## Server-invoked DDL-Explicit Default Expressions

A variant on the SQL expression default is the `_schema.Column.server_default, which gets placed in the CREATE TABLE statement during a schema.Table.create` operation:

```python+sql
 t = Table(
     "test",
     metadata_obj,
     Column("abc", String(20), server_default="abc"),
     Column("created_at", DateTime, server_default=func.sysdate()),
     Column("index_value", Integer, server_default=text("0")),
 )
```

A create call for the above table will produce:

```sql
 CREATE TABLE test (
     abc varchar(20) default 'abc',
     created_at datetime default sysdate,
     index_value integer default 0
 )
```

The above example illustrates the two typical use cases for `_schema.Column.server_default, that of the SQL function (SYSDATE in the above example) as well as a server-side constant value (the integer "0" in the above example).  It is advisable to use the expression.text` construct for any literal SQL values as opposed to passing the raw value, as SQLAlchemy does not typically perform any quoting or escaping on these values.

Like client-generated expressions, `_schema.Column.server_default` can accommodate SQL expressions in general, however it is expected that these will usually be simple functions and expressions, and not the more complex cases like an embedded SELECT.

## Marking Implicitly Generated Values, timestamps, and Triggered Columns

Columns which generate a new value on INSERT or UPDATE based on other server-side database mechanisms, such as database-specific auto-generating behaviors such as seen with TIMESTAMP columns on some platforms, as well as custom triggers that invoke upon INSERT or UPDATE to generate a new value, may be called out using `.FetchedValue` as a marker:

```
from sqlalchemy.schema import FetchedValue

t = Table(
    "test",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("abc", TIMESTAMP, server_default=FetchedValue()),
    Column("def", String(20), server_onupdate=FetchedValue()),
)
```

The `.FetchedValue` indicator does not affect the rendered DDL for the CREATE TABLE.  Instead, it marks the column as one that will have a new value populated by the database during the process of an INSERT or UPDATE statement, and for supporting  databases may be used to indicate that the column should be part of a RETURNING or OUTPUT clause for the statement.    Tools such as the SQLAlchemy ORM then make use of this marker in order to know how to get at the value of the column after such an operation.   In particular, the `.ValuesBase.return_defaults method can be used with an expression.Insert or expression.Update` construct to indicate that these values should be returned.

For details on using `.FetchedValue` with the ORM, see `orm_server_defaults`.

> **Warning:**  **does not** currently produce MySQL's
 "ON UPDATE CURRENT_TIMESTAMP()" clause.  See
 `mysql_timestamp_onupdate` for background on how to produce
 this clause.

> **Seealso:**  `orm_server_defaults`

## Defining Sequences

SQLAlchemy represents database sequences using the `sqlalchemy.schema.Sequence` object, which is considered to be a special case of "column default". It only has an effect on databases which have explicit support for sequences, which among SQLAlchemy's included dialects includes PostgreSQL, Oracle Database, MS SQL Server, and MariaDB.  The `sqlalchemy.schema.Sequence` object is otherwise ignored.

> **Tip:**  In newer database engines, the `.Identity` construct should likely
 be preferred vs. `.Sequence` for generation of integer primary key
 values. See the section `identity_ddl` for background on this
 construct.

The `sqlalchemy.schema.Sequence` may be placed on any column as a "default" generator to be used during INSERT operations, and can also be configured to fire off during UPDATE operations if desired. It is most commonly used in conjunction with a single integer primary key column:

```
table = Table(
    "cartitems",
    metadata_obj,
    Column(
        "cart_id",
        Integer,
        Sequence("cart_id_seq", start=1),
        primary_key=True,
    ),
    Column("description", String(40)),
    Column("createdate", DateTime()),
)
```

Where above, the table `cartitems` is associated with a sequence named `cart_id_seq`.   Emitting `.MetaData.create_all` for the above table will include:

```sql
 CREATE SEQUENCE cart_id_seq START WITH 1

 CREATE TABLE cartitems (
   cart_id INTEGER NOT NULL,
   description VARCHAR(40),
   createdate TIMESTAMP WITHOUT TIME ZONE,
   PRIMARY KEY (cart_id)
 )
```

> **Tip:** When using tables with explicit schema names (detailed at
`schema_table_schema_name`), the configured schema of the `.Table`
is **not** automatically shared by an embedded `.Sequence`, instead,
specify `.Sequence.schema`::
 Sequence("cart_id_seq", start=1, schema="some_schema")
The `.Sequence` may also be made to automatically make use of the
`.MetaData.schema` setting on the `.MetaData` in use;
see `sequence_metadata` for background.

When `_dml.Insert` DML constructs are invoked against the `cartitems` table, without an explicit value passed for the `cart_id` column, the `cart_id_seq` sequence will be used to generate a value on participating backends. Typically, the sequence function is embedded in the INSERT statement, which is combined with RETURNING so that the newly generated value can be returned to the Python process:

```sql
 INSERT INTO cartitems (cart_id, description, createdate)
 VALUES (next_val(cart_id_seq), 'some description', '2015-10-15 12:00:15')
 RETURNING cart_id
```

When using `.Connection.execute to invoke an dml.Insert` construct, newly generated primary key identifiers, including but not limited to those generated using `.Sequence`, are available from the `.CursorResult` construct using the `.CursorResult.inserted_primary_key` attribute.

When the `sqlalchemy.schema.Sequence is associated with a schema.Column` as its **Python-side** default generator, the `.Sequence will also be subject to "CREATE SEQUENCE" and "DROP SEQUENCE" DDL when similar DDL is emitted for the owning schema.Table`, such as when using `.MetaData.create_all` to generate DDL for a series of tables.

The `.Sequence` may also be associated with a `.MetaData` construct directly.  This allows the `.Sequence` to be used in more than one `.Table` at a time and also allows the `.MetaData.schema` parameter to be inherited.  See the section `sequence_metadata` for background.

### Associating a Sequence on a SERIAL column

PostgreSQL's SERIAL datatype is an auto-incrementing type that implies the implicit creation of a PostgreSQL sequence when CREATE TABLE is emitted. The `.Sequence construct, when indicated for a schema.Column`, may indicate that it should not be used in this specific case by specifying a value of `True` for the `.Sequence.optional` parameter. This allows the given `.Sequence` to be used for backends that have no alternative primary key generation system but to ignore it for backends such as PostgreSQL which will automatically generate a sequence for a particular column:

```
table = Table(
    "cartitems",
    metadata_obj,
    Column(
        "cart_id",
        Integer,
        # use an explicit Sequence where available, but not on
        # PostgreSQL where SERIAL will be used
        Sequence("cart_id_seq", start=1, optional=True),
        primary_key=True,
    ),
    Column("description", String(40)),
    Column("createdate", DateTime()),
)
```

In the above example, `CREATE TABLE` for PostgreSQL will make use of the `SERIAL` datatype for the `cart_id` column, and the `cart_id_seq` sequence will be ignored.  However on Oracle Database, the `cart_id_seq` sequence will be created explicitly.

> **Tip:**  This particular interaction of SERIAL and SEQUENCE is fairly legacy, and
 as in other cases, using `.Identity` instead will simplify the
 operation to simply use `IDENTITY` on all supported backends.

### Executing a Sequence Standalone

A SEQUENCE is a first class schema object in SQL and can be used to generate values independently in the database.   If you have a `.Sequence` object, it can be invoked with its "next value" instruction by passing it directly to a SQL execution method:

```
with my_engine.connect() as conn:
    seq = Sequence("some_sequence", start=1)
    nextid = conn.execute(seq)
```

In order to embed the "next value" function of a `.Sequence` inside of a SQL statement like a SELECT or INSERT, use the `.Sequence.next_value` method, which will render at statement compilation time a SQL function that is appropriate for the target backend:

```pycon+sql
 >>> my_seq = Sequence("some_sequence", start=1)
 >>> stmt = select(my_seq.next_value())
 >>> print(stmt.compile(dialect=postgresql.dialect()))
 {printsql}SELECT nextval('some_sequence') AS next_value_1
```

### Associating a Sequence with the MetaData

For a `.Sequence` that is to be associated with arbitrary `.Table` objects, the `.Sequence may be associated with a particular schema.MetaData`, using the `.Sequence.metadata` parameter:

```
seq = Sequence("my_general_seq", metadata=metadata_obj, start=1)
```

Such a sequence can then be associated with columns in the usual way:

```
table = Table(
    "cartitems",
    metadata_obj,
    seq,
    Column("description", String(40)),
    Column("createdate", DateTime()),
)
```

In the above example, the `.Sequence` object is treated as an independent schema construct that can exist on its own or be shared among tables.

Explicitly associating the `.Sequence with schema.MetaData` allows for the following behaviors:

- The `.Sequence will inherit the schema.MetaData.schema`
parameter specified to the target `_schema.MetaData`, which affects the production of CREATE / DROP DDL as well as how the `.Sequence.next_value` function is rendered in SQL statements.

- The `_schema.MetaData.create_all and schema.MetaData.drop_all`
methods will emit CREATE / DROP for this `.Sequence`, even if the `.Sequence is not associated with any schema.Table / schema.Column that's a member of this schema.MetaData`.

### Associating a Sequence as the Server Side Default

> **Note:** database.  It does not work with Oracle Database.

The preceding sections illustrate how to associate a `.Sequence with a schema.Column` as the **Python side default generator**:

```
Column(
    "cart_id",
    Integer,
    Sequence("cart_id_seq", metadata=metadata_obj, start=1),
    primary_key=True,
)
```

In the above case, the `.Sequence will automatically be subject to CREATE SEQUENCE / DROP SEQUENCE DDL when the related schema.Table` is subject to CREATE / DROP.  However, the sequence will **not** be present as the server-side default for the column when CREATE TABLE is emitted.

If we want the sequence to be used as a server-side default, meaning it takes place even if we emit INSERT commands to the table from the SQL command line, we can use the `_schema.Column.server_default` parameter in conjunction with the value-generation function of the sequence, available from the `.Sequence.next_value` method.  Below we illustrate the same `.Sequence being associated with the schema.Column` both as the Python-side default generator as well as the server-side default generator:

```
cart_id_seq = Sequence("cart_id_seq", metadata=metadata_obj, start=1)
table = Table(
    "cartitems",
    metadata_obj,
    Column(
        "cart_id",
        Integer,
        cart_id_seq,
        server_default=cart_id_seq.next_value(),
        primary_key=True,
    ),
    Column("description", String(40)),
    Column("createdate", DateTime()),
)
```

or with the ORM:

```
class CartItem(Base):
    __tablename__ = "cartitems"

    cart_id_seq = Sequence("cart_id_seq", metadata=Base.metadata, start=1)
    cart_id = Column(
        Integer, cart_id_seq, server_default=cart_id_seq.next_value(), primary_key=True
    )
    description = Column(String(40))
    createdate = Column(DateTime)
```

When the "CREATE TABLE" statement is emitted, on PostgreSQL it would be emitted as:

```sql
 CREATE TABLE cartitems (
     cart_id INTEGER DEFAULT nextval('cart_id_seq') NOT NULL,
     description VARCHAR(40),
     createdate TIMESTAMP WITHOUT TIME ZONE,
     PRIMARY KEY (cart_id)
 )
```

Placement of the `.Sequence` in both the Python-side and server-side default generation contexts ensures that the "primary key fetch" logic works in all cases.  Typically, sequence-enabled databases also support RETURNING for INSERT statements, which is used automatically by SQLAlchemy when emitting this statement.  However if RETURNING is not used for a particular insert, then SQLAlchemy would prefer to "pre-execute" the sequence outside of the INSERT statement itself, which only works if the sequence is included as the Python-side default generator function.

The example also associates the `.Sequence with the enclosing schema.MetaData` directly, which again ensures that the `.Sequence is fully associated with the parameters of the schema.MetaData` collection including the default schema, if any.

> **Seealso:**  `postgresql_sequences` - in the PostgreSQL dialect documentation
 `oracle_returning` - in the Oracle Database dialect documentation

## Computed Columns (GENERATED ALWAYS AS)

The `.Computed construct allows a schema.Column to be declared in DDL as a "GENERATED ALWAYS AS" column, that is, one which has a value that is computed by the database server.    The construct accepts a SQL expression typically declared textually using a string or the expression.text` construct, in a similar manner as that of `.CheckConstraint`.   The SQL expression is then interpreted by the database server in order to determine the value for the column within a row.

Example:

```
from sqlalchemy import Table, Column, MetaData, Integer, Computed

metadata_obj = MetaData()

square = Table(
    "square",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("side", Integer),
    Column("area", Integer, Computed("side * side")),
    Column("perimeter", Integer, Computed("4 * side")),
)
```

The DDL for the `square` table when run on a PostgreSQL 18 backend [#pgnote]_ will look like:

```sql
 CREATE TABLE square (
     id SERIAL NOT NULL,
     side INTEGER,
     area INTEGER GENERATED ALWAYS AS (side * side),
     perimeter INTEGER GENERATED ALWAYS AS (4 * side),
     PRIMARY KEY (id)
 )
```

Whether the value is persisted upon INSERT and UPDATE, or if it is calculated on fetch, is an implementation detail of the database; the former is known as "stored" and the latter is known as "virtual".  Some database implementations support both, but some only support one or the other.  The optional `.Computed.persisted` flag may be specified as `True` or `False` to indicate if the "STORED" or "VIRTUAL" keyword should be rendered in DDL, however this will raise an error if the keyword is not supported by the target backend; leaving it unset will use  a working default for the target backend.

The `.Computed` construct is a subclass of the `.FetchedValue object, and will set itself up as both the "server default" and "server onupdate" generator for the target schema.Column`, meaning it will be treated as a default generating column when INSERT and UPDATE statements are generated, as well as that it will be fetched as a generating column when using the ORM. This includes that it will be part of the RETURNING clause of the database for databases which support RETURNING and the generated values are to be eagerly fetched.

> **Note:** construct may not store any value outside of that which the server applies
to it;  SQLAlchemy's behavior when a value is passed for such a column
to be written in INSERT or UPDATE is currently that the value will be
ignored.

"GENERATED ALWAYS AS" is currently known to be supported by:

- MySQL version 5.7 and onwards
- MariaDB 10.x series and onwards
- PostgreSQL as of version 12 [#pgnote]_
- Oracle Database - with the caveat that RETURNING does not work correctly with
UPDATE (a warning will be emitted to this effect when the UPDATE..RETURNING that includes a computed column is rendered)

- Microsoft SQL Server
- SQLite as of version 3.31
When `.Computed` is used with an unsupported backend, if the target dialect does not support it, a `.CompileError` is raised when attempting to render the construct.  Otherwise, if the dialect supports it but the particular database server version in use does not, then a subclass of `.DBAPIError`, usually `.OperationalError`, is raised when the DDL is emitted to the database.

> **Seealso:**  `.Computed` - produces a GENERATED ALWAYS AS phrase for `.Column`
 .. [#pgnote] `postgresql_computed_column_notes` - notes for GENERATED ALWAYS AS
    on PostgreSQL including behavioral changes as of PostgreSQL 18

## Identity Columns (GENERATED { ALWAYS | BY DEFAULT } AS IDENTITY)

.. versionadded:: 1.4

The `.Identity construct allows a schema.Column` to be declared as an identity column and rendered in DDL as "GENERATED { ALWAYS | BY DEFAULT } AS IDENTITY".  An identity column has its value automatically generated by the database server using an incrementing (or decrementing) sequence. The construct shares most of its option to control the database behaviour with `.Sequence`.

Example:

```
from sqlalchemy import Table, Column, MetaData, Integer, Identity, String

metadata_obj = MetaData()

data = Table(
    "data",
    metadata_obj,
    Column("id", Integer, Identity(start=42, cycle=True), primary_key=True),
    Column("data", String),
)
```

The DDL for the `data` table when run on a PostgreSQL 12 backend will look like:

```sql
 CREATE TABLE data (
     id INTEGER GENERATED BY DEFAULT AS IDENTITY (START WITH 42 CYCLE) NOT NULL,
     data VARCHAR,
     PRIMARY KEY (id)
 )
```

The database will generate a value for the `id` column upon insert, starting from `42`, if the statement did not already contain a value for the `id column. An identity column can also require that the database generates the value of the column, ignoring the value passed with the statement or raising an error, depending on the backend. To activate this mode, set the parameter schema.Identity.always` to `True` in the `.Identity` construct. Updating the previous example to include this parameter will generate the following DDL:

```sql
 CREATE TABLE data (
     id INTEGER GENERATED ALWAYS AS IDENTITY (START WITH 42 CYCLE) NOT NULL,
     data VARCHAR,
     PRIMARY KEY (id)
 )
```

The `.Identity` construct is a subclass of the `.FetchedValue object, and will set itself up as the "server default" generator for the target schema.Column`, meaning it will be treated as a default generating column when INSERT statements are generated, as well as that it will be fetched as a generating column when using the ORM. This includes that it will be part of the RETURNING clause of the database for databases which support RETURNING and the generated values are to be eagerly fetched.

The `.Identity` construct is currently known to be supported by:

- PostgreSQL as of version 10.
- Oracle Database as of version 12. It also supports passing `always=None` to
enable the default generated mode and the parameter `on_null=True` to specify "ON NULL" in conjunction with a "BY DEFAULT" identity column.

- Microsoft SQL Server. MSSQL uses a custom syntax that only supports the
`start` and `increment` parameters, and ignores all other.

When `.Identity` is used with an unsupported backend, it is ignored, and the default SQLAlchemy logic for autoincrementing columns is used.

An error is raised when a `_schema.Column` specifies both an `.Identity and also sets schema.Column.autoincrement` to `False`.

> **Seealso:**  `.Identity`

## Default Objects API
