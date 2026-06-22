---
type: "Framework Learn Page"
framework: "sqlalchemy"
source_repo: "https://github.com/sqlalchemy/sqlalchemy"
source_branch: "main"
source_path: "doc/build/tutorial/data_insert.rst"
source_commit: "ddf3b6589fd6ccb2affbaea5d4f400a8c1ad02d8"
source_commit_short: "ddf3b658"
source_commit_date: "2026-06-18T14:12:36-04:00"
generated_at: "2026-06-21T07:22:30Z"
---

.. include:: tutorial_nav_include.rst

## Using INSERT Statements

When using Core as well as when using the ORM for bulk operations, a SQL INSERT statement is generated directly using the `_sql.insert function - this function generates a new instance of sql.Insert` which represents an INSERT statement in SQL, that adds new data into a table.

#### The insert() SQL Expression Construct

A simple example of `_sql.Insert` illustrating the target table and the VALUES clause at once:

```
>>> from sqlalchemy import insert
>>> stmt = insert(user_table).values(name="spongebob", fullname="Spongebob Squarepants")
```

The above `stmt variable is an instance of sql.Insert`.  Most SQL expressions can be stringified in place as a means to see the general form of what's being produced:

```
>>> print(stmt)
{printsql}INSERT INTO user_account (name, fullname) VALUES (:name, :fullname)
```

The stringified form is created by producing a `_engine.Compiled form of the object which includes a database-specific string SQL representation of the statement; we can acquire this object directly using the sql.ClauseElement.compile` method:

```
>>> compiled = stmt.compile()
```

Our `_sql.Insert` construct is an example of a "parameterized" construct, illustrated previously at `tutorial_sending_parameters`; to view the `name` and `fullname` `bound parameters, these are available from the engine.Compiled` construct as well:

```
>>> compiled.params
{'name': 'spongebob', 'fullname': 'Spongebob Squarepants'}
```

#### Executing the Statement

Invoking the statement we can INSERT a row into `user_table`. The INSERT SQL as well as the bundled parameters can be seen in the SQL logging:

```pycon+sql
 >>> with engine.connect() as conn:
 ...     result = conn.execute(stmt)
 ...     conn.commit()
 {execsql}BEGIN (implicit)
 INSERT INTO user_account (name, fullname) VALUES (?, ?)
 [...] ('spongebob', 'Spongebob Squarepants')
 COMMIT
```

In its simple form above, the INSERT statement does not return any rows, and if only a single row is inserted, it will usually include the ability to return information about column-level default values that were generated during the INSERT of that row, most commonly an integer primary key value.  In the above case the first row in a SQLite database will normally return `1 for the first integer primary key value, which we can acquire using the engine.CursorResult.inserted_primary_key` accessor:

```pycon+sql
 >>> result.inserted_primary_key
 (1,)
```

> **Tip:** because a primary key may contain multiple columns.  This is known as
a `composite primary key.  The engine.CursorResult.inserted_primary_key`
is intended to always contain the complete primary key of the record just
inserted, not just a "cursor.lastrowid" kind of value, and is also intended
to be populated regardless of whether or not "autoincrement" were used, hence
to express a complete primary key it's a tuple.

.. versionchanged:: 1.4.8 the tuple returned by

#### INSERT usually generates the "values" clause automatically

The example above made use of the `_sql.Insert.values method to explicitly create the VALUES clause of the SQL INSERT statement.   If we don't actually use sql.Insert.values` and just print out an "empty" statement, we get an INSERT for every column in the table:

```
>>> print(insert(user_table))
{printsql}INSERT INTO user_account (id, name, fullname) VALUES (:id, :name, :fullname)
```

If we take an `_sql.Insert construct that has not had sql.Insert.values called upon it and execute it rather than print it, the statement will be compiled to a string based on the parameters that we passed to the engine.Connection.execute method, and only include columns relevant to the parameters that were passed.   This is actually the usual way that sql.Insert` is used to insert rows without having to type out an explicit VALUES clause.   The example below illustrates a two-column INSERT statement being executed with a list of parameters at once:

```pycon+sql
 >>> with engine.connect() as conn:
 ...     result = conn.execute(
 ...         insert(user_table),
 ...         [
 ...             {"name": "sandy", "fullname": "Sandy Cheeks"},
 ...             {"name": "patrick", "fullname": "Patrick Star"},
 ...         ],
 ...     )
 ...     conn.commit()
 {execsql}BEGIN (implicit)
 INSERT INTO user_account (name, fullname) VALUES (?, ?)
 [...] [('sandy', 'Sandy Cheeks'), ('patrick', 'Patrick Star')]
 COMMIT{stop}
```

The execution above features "executemany" form first illustrated at `tutorial_multiple_parameters, however unlike when using the sql.text construct, we didn't have to spell out any SQL. By passing a dictionary or list of dictionaries to the engine.Connection.execute method in conjunction with the sql.Insert construct, the engine.Connection ensures that the column names which are passed will be expressed in the VALUES clause of the sql.Insert` construct automatically.

> **Tip:**  When passing a list of dictionaries to `_engine.Connection.execute`
 along with a Core `_sql.Insert`, **only the first dictionary in the
 list determines what columns will be in the VALUES clause**. The rest of
 the dictionaries are not scanned. This is both because within traditional
 `executemany()`, the INSERT statement can only have one VALUES clause for
 all parameters, and additionally SQLAlchemy does not want to add overhead
 by scanning every parameter dictionary to verify each contains the identical
 keys as the first one.
 Note this behavior is distinctly different from that of an :ref:`ORM
 enabled INSERT <tutorial_orm_bulk>`, introduced later in this tutorial,
 which performs a full scan of parameter sets in terms of an ORM entity.

> **Tip:** without including any explicit values at all is generated if we indicate
`_sql.Insert.values` with no arguments; not every database backend
supports this, but here's what SQLite produces::
 >>> print(insert(user_table).values().compile(engine))
 {printsql}INSERT INTO user_account DEFAULT VALUES

#### INSERT...RETURNING

The RETURNING clause for supported backends is used automatically in order to retrieve the last inserted primary key value as well as the values for server defaults.   However the RETURNING clause may also be specified explicitly using the `_sql.Insert.returning method; in this case, the engine.Result` object that's returned when the statement is executed has rows which can be fetched:

```
>>> insert_stmt = insert(address_table).returning(
...     address_table.c.id, address_table.c.email_address
... )
>>> print(insert_stmt)
{printsql}INSERT INTO address (id, user_id, email_address)
VALUES (:id, :user_id, :email_address)
RETURNING address.id, address.email_address
```

It can also be combined with `_sql.Insert.from_select`, as in the example below that builds upon the example stated in `tutorial_insert_from_select`:

```
>>> select_stmt = select(user_table.c.id, user_table.c.name + "@aol.com")
>>> insert_stmt = insert(address_table).from_select(
...     ["user_id", "email_address"], select_stmt
... )
>>> print(insert_stmt.returning(address_table.c.id, address_table.c.email_address))
{printsql}INSERT INTO address (user_id, email_address)
SELECT user_account.id, user_account.name || :name_1 AS anon_1
FROM user_account RETURNING address.id, address.email_address
```

> **Tip:**  The RETURNING feature is also supported by UPDATE and DELETE statements,
 which will be introduced later in this tutorial.
 For INSERT statements, the RETURNING feature may be used
 both for single-row statements as well as for statements that INSERT
 multiple rows at once.  Support for multiple-row INSERT with RETURNING
 is dialect specific, however is supported for all the dialects
 that are included in SQLAlchemy which support RETURNING.  See the section
 `engine_insertmanyvalues` for background on this feature.

> **Seealso:**  Bulk INSERT with or without RETURNING is also supported by the ORM.  See
 `orm_queryguide_bulk_insert` for reference documentation.

#### INSERT...FROM SELECT

A less used feature of `_sql.Insert, but here for completeness, the sql.Insert construct can compose an INSERT that gets rows directly from a SELECT using the sql.Insert.from_select method. This method accepts a sql.select` construct, which is discussed in the next section, along with a list of column names to be targeted in the actual INSERT.  In the example below, rows are added to the `address` table which are derived from rows in the `user_account` table, giving each user a free email address at `aol.com`:

```
>>> select_stmt = select(user_table.c.id, user_table.c.name + "@aol.com")
>>> insert_stmt = insert(address_table).from_select(
...     ["user_id", "email_address"], select_stmt
... )
>>> print(insert_stmt)
{printsql}INSERT INTO address (user_id, email_address)
SELECT user_account.id, user_account.name || :name_1 AS anon_1
FROM user_account
```

This construct is used when one wants to copy data from some other part of the database directly into a new set of rows, without actually fetching and re-sending the data from the client.

> **Seealso:**  `_sql.Insert` - in the SQL Expression API documentation
