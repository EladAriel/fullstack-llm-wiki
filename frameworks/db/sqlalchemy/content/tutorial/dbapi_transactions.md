---
type: "Framework Learn Page"
framework: "sqlalchemy"
source_repo: "https://github.com/sqlalchemy/sqlalchemy"
source_branch: "main"
source_path: "doc/build/tutorial/dbapi_transactions.rst"
source_commit: "ddf3b6589fd6ccb2affbaea5d4f400a8c1ad02d8"
source_commit_short: "ddf3b658"
source_commit_date: "2026-06-18T14:12:36-04:00"
generated_at: "2026-06-21T07:22:30Z"
---

.. include:: tutorial_nav_include.rst

# Working with Transactions and the DBAPI

With the `_engine.Engine object ready to go, we can dive into the basic operation of an engine.Engine and its primary endpoints, the engine.Connection and engine.Result`. We'll also introduce the ORM's `facade for these objects, known as the orm.Session`.

As we have yet to introduce the SQLAlchemy Expression Language that is the primary feature of SQLAlchemy, we'll use a simple construct within this package called the `_sql.text` construct, to write SQL statements as **textual SQL**.   Rest assured that textual SQL is the exception rather than the rule in day-to-day SQLAlchemy use, but it's always available.

## Getting a Connection

The purpose of the `_engine.Engine is to connect to the database by providing a engine.Connection object.   When working with the Core directly, the engine.Connection object is how all interaction with the database is done.   Because the engine.Connection creates an open resource against the database, we want to limit our use of this object to a specific context. The best way to do that is with a Python context manager, also known as [the with statement](https://docs.python.org/3/reference/compound_stmts.html#with). Below we use a textual SQL statement to show "Hello World".  Textual SQL is created with a construct called sql.text` which we'll discuss in more detail later:

```pycon+sql
 >>> from sqlalchemy import text

 >>> with engine.connect() as conn:
 ...     result = conn.execute(text("select 'hello world'"))
 ...     print(result.all())
 {execsql}BEGIN (implicit)
 select 'hello world'
 [...] ()
 {stop}[('hello world',)]
 {execsql}ROLLBACK{stop}
```

In the example above, the context manager creates a database connection and executes the operation in a transaction. The default behavior of the Python DBAPI is that a transaction is always in progress; when the connection is `released, a ROLLBACK is emitted to end the transaction.   The transaction is **not committed automatically**; if we want to commit data we need to call engine.Connection.commit` as we'll see in the next section.

> **Tip:**

The result of our SELECT was returned in an object called `_engine.Result` that will be discussed later. For the moment we'll add that it's best to use this object within the "connect" block, and to not use it outside of the scope of our connection.

## Committing Changes

We just learned that the DBAPI connection doesn't commit automatically. What if we want to commit some data?   We can change our example above to create a table, insert some data and then commit the transaction using the `_engine.Connection.commit method, **inside** the block where we have the engine.Connection` object:

```pycon+sql
 # "commit as you go"
 >>> with engine.connect() as conn:
 ...     conn.execute(text("CREATE TABLE some_table (x int, y int)"))
 ...     conn.execute(
 ...         text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
 ...         [{"x": 1, "y": 1}, {"x": 2, "y": 4}],
 ...     )
 ...     conn.commit()
 {execsql}BEGIN (implicit)
 CREATE TABLE some_table (x int, y int)
 [...] ()
 <sqlalchemy.engine.cursor.CursorResult object at 0x...>
 INSERT INTO some_table (x, y) VALUES (?, ?)
 [...] [(1, 1), (2, 4)]
 <sqlalchemy.engine.cursor.CursorResult object at 0x...>
 COMMIT
```

Above, we execute two SQL statements, a "CREATE TABLE" statement [1]_ and an "INSERT" statement that's parameterized (we discuss the parameterization syntax later in `tutorial_multiple_parameters). To commit the work we've done in our block, we call the engine.Connection.commit method which commits the transaction. After this, we can continue to run more SQL statements and call engine.Connection.commit` again for those statements.  SQLAlchemy refers to this style as **commit as you go**.

There's also another style to commit data. We can declare our "connect" block to be a transaction block up front.   To do this, we use the `_engine.Engine.begin method to get the connection, rather than the engine.Engine.connect method.  This method will manage the scope of the engine.Connection` and also enclose everything inside of a transaction with either a COMMIT at the end if the block was successful, or a ROLLBACK if an exception was raised.  This style is known as **begin once**:

```pycon+sql
 # "begin once"
 >>> with engine.begin() as conn:
 ...     conn.execute(
 ...         text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
 ...         [{"x": 6, "y": 8}, {"x": 9, "y": 10}],
 ...     )
 {execsql}BEGIN (implicit)
 INSERT INTO some_table (x, y) VALUES (?, ?)
 [...] [(6, 8), (9, 10)]
 <sqlalchemy.engine.cursor.CursorResult object at 0x...>
 COMMIT
```

You should mostly prefer the "begin once" style because it's shorter and shows the intention of the entire block up front.   However, in this tutorial we'll use "commit as you go" style as it's more flexible for demonstration purposes.

to create, modify, or remove schema-level constructs such as tables. DDL such as "CREATE TABLE" should be in a transaction block that ends with COMMIT, as many databases use transactional DDL such that the schema changes don't take place until the transaction is committed. However, as we'll see later, we usually let SQLAlchemy run DDL sequences for us as part of a higher level operation where we don't generally need to worry about the COMMIT.

## Basics of Statement Execution

We have seen a few examples that run SQL statements against a database, making use of a method called `_engine.Connection.execute, in conjunction with an object called sql.text, and returning an object called engine.Result`.  In this section we'll illustrate more closely the mechanics and interactions of these components.

#### Fetching Rows

We'll first illustrate the `_engine.Result` object more closely by making use of the rows we've inserted previously, running a textual SELECT statement on the table we've created:

```pycon+sql
 >>> with engine.connect() as conn:
 ...     result = conn.execute(text("SELECT x, y FROM some_table"))
 ...     for row in result:
 ...         print(f"x: {row.x}  y: {row.y}")
 {execsql}BEGIN (implicit)
 SELECT x, y FROM some_table
 [...] ()
 {stop}x: 1  y: 1
 x: 2  y: 4
 x: 6  y: 8
 x: 9  y: 10
 {execsql}ROLLBACK{stop}
```

Above, the "SELECT" string we executed selected all rows from our table. The object returned is called `_engine.Result` and represents an iterable object of result rows.

`_engine.Result has lots of methods for fetching and transforming rows, such as the engine.Result.all method illustrated previously, which returns a list of all engine.Row objects.   It also implements the Python iterator interface so that we can iterate over the collection of engine.Row` objects directly.

The `_engine.Row` objects themselves are intended to act like Python [named tuples](https://docs.python.org/3/library/collections.html#collections.namedtuple). Below we illustrate a variety of ways to access rows.

- **Tuple Assignment** - This is the most Python-idiomatic style, which is to assign variables
to each row positionally as they are received:

:

```
  result = conn.execute(text("select x, y from some_table"))

  for x, y in result:
      ...
```

- **Integer Index** - Tuples are Python sequences, so regular integer access is available too:
:

```
  result = conn.execute(text("select x, y from some_table"))

  for row in result:
      x = row[0]
```

- **Attribute Name** - As these are Python named tuples, the tuples have dynamic attribute names
matching the names of each column.  These names are normally the names that the SQL statement assigns to the columns in each row.  While they are usually fairly predictable and can also be controlled by labels, in less defined cases they may be subject to database-specific behaviors:

```
  result = conn.execute(text("select x, y from some_table"))

  for row in result:
      y = row.y

      # illustrate use with Python f-strings
      print(f"Row: {row.x} {y}")

..
```

- **Mapping Access** - To receive rows as Python **mapping** objects, which is
essentially a read-only version of Python's interface to the common `dict object, the engine.Result may be **transformed** into a engine.MappingResult object using the engine.Result.mappings modifier; this is a result object that yields dictionary-like engine.RowMapping objects rather than engine.Row` objects:

```
  result = conn.execute(text("select x, y from some_table"))

  for dict_row in result.mappings():
      x = dict_row["x"]
      y = dict_row["y"]

..
```

#### Sending Parameters

SQL statements are usually accompanied by data that is to be passed with the statement itself, as we saw in the INSERT example previously. The `_engine.Connection.execute` method therefore also accepts parameters, which are known as `bound parameters`.  A rudimentary example might be if we wanted to limit our SELECT statement only to rows that meet a certain criteria, such as rows where the "y" value were greater than a certain value that is passed in to a function.

In order to achieve this such that the SQL statement can remain fixed and that the driver can properly sanitize the value, we add a WHERE criteria to our statement that names a new parameter called "y"; the `_sql.text` construct accepts these using a colon format "`:y`".   The actual value for "`:y" is then passed as the second argument to engine.Connection.execute` in the form of a dictionary:

```pycon+sql
 >>> with engine.connect() as conn:
 ...     result = conn.execute(text("SELECT x, y FROM some_table WHERE y > :y"), {"y": 2})
 ...     for row in result:
 ...         print(f"x: {row.x}  y: {row.y}")
 {execsql}BEGIN (implicit)
 SELECT x, y FROM some_table WHERE y > ?
 [...] (2,)
 {stop}x: 2  y: 4
 x: 6  y: 8
 x: 9  y: 10
 {execsql}ROLLBACK{stop}
```

In the logged SQL output, we can see that the bound parameter `:y` was converted into a question mark when it was sent to the SQLite database. This is because the SQLite database driver uses a format called "qmark parameter style", which is one of six different formats allowed by the DBAPI specification. SQLAlchemy abstracts these formats into just one, which is the "named" format using a colon.

#### Sending Multiple Parameters

In the example at `tutorial_committing_data`, we executed an INSERT statement where it appeared that we were able to INSERT multiple rows into the database at once.  For `DML statements such as "INSERT", "UPDATE" and "DELETE", we can send **multiple parameter sets** to the engine.Connection.execute` method by passing a list of dictionaries instead of a single dictionary, which indicates that the single SQL statement should be invoked multiple times, once for each parameter set.  This style of execution is known as `executemany`:

```pycon+sql
 >>> with engine.connect() as conn:
 ...     conn.execute(
 ...         text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
 ...         [{"x": 11, "y": 12}, {"x": 13, "y": 14}],
 ...     )
 ...     conn.commit()
 {execsql}BEGIN (implicit)
 INSERT INTO some_table (x, y) VALUES (?, ?)
 [...] [(11, 12), (13, 14)]
 <sqlalchemy.engine.cursor.CursorResult object at 0x...>
 COMMIT
```

The above operation is equivalent to running the given INSERT statement once for each parameter set, except that the operation will be optimized for better performance across many rows.

A key behavioral difference between "execute" and "executemany" is that the latter doesn't support returning of result rows, even if the statement includes the RETURNING clause. The one exception to this is when using a Core `_sql.insert` construct, introduced later in this tutorial at `tutorial_core_insert, which also indicates RETURNING using the sql.Insert.returning` method.  In that case, SQLAlchemy makes use of special logic to reorganize the INSERT statement so that it can be invoked for many rows while still supporting RETURNING.

> **Seealso:** `executemany` - in the `Glossary </glossary>`, describes the
DBAPI-level
[cursor.executemany()](https://peps.python.org/pep-0249/#executemany)
method that's used for most "executemany" executions.
`engine_insertmanyvalues` - in `connections_toplevel`, describes
the specialized logic used by `_sql.Insert.returning` to deliver
result sets with "executemany" executions.

## Executing with an ORM Session

As mentioned previously, most of the patterns and examples above apply to use with the ORM as well, so here we will introduce this usage so that as the tutorial proceeds, we will be able to illustrate each pattern in terms of Core and ORM use together.

The fundamental transactional / database interactive object when using the ORM is called the `_orm.Session.  In modern SQLAlchemy, this object is used in a manner very similar to that of the engine.Connection, and in fact as the orm.Session is used, it refers to a engine.Connection` internally which it uses to emit SQL.

When the `_orm.Session is used with non-ORM constructs, it passes through the SQL statements we give it and does not generally do things much differently from how the engine.Connection` does directly, so we can illustrate it here in terms of the simple textual SQL operations we've already learned.

The `_orm.Session has a few different creational patterns, but here we will illustrate the most basic one that tracks exactly with how the engine.Connection` is used which is to construct it within a context manager:

```pycon+sql
 >>> from sqlalchemy.orm import Session

 >>> stmt = text("SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y")
 >>> with Session(engine) as session:
 ...     result = session.execute(stmt, {"y": 6})
 ...     for row in result:
 ...         print(f"x: {row.x}  y: {row.y}")
 {execsql}BEGIN (implicit)
 SELECT x, y FROM some_table WHERE y > ? ORDER BY x, y
 [...] (6,){stop}
 x: 6  y: 8
 x: 9  y: 10
 x: 11  y: 12
 x: 13  y: 14
 {execsql}ROLLBACK{stop}
```

The example above can be compared to the example in the preceding section in `tutorial_sending_parameters` - we directly replace the call to `with engine.connect() as conn` with `with Session(engine) as session, and then make use of the orm.Session.execute method just like we do with the engine.Connection.execute` method.

Also, like the `_engine.Connection, the orm.Session features "commit as you go" behavior using the orm.Session.commit` method, illustrated below using a textual UPDATE statement to alter some of our data:

```pycon+sql
 >>> with Session(engine) as session:
 ...     result = session.execute(
 ...         text("UPDATE some_table SET y=:y WHERE x=:x"),
 ...         [{"x": 9, "y": 11}, {"x": 13, "y": 15}],
 ...     )
 ...     session.commit()
 {execsql}BEGIN (implicit)
 UPDATE some_table SET y=? WHERE x=?
 [...] [(11, 9), (15, 13)]
 COMMIT{stop}
```

Above, we invoked an UPDATE statement using the bound-parameter, "executemany" style of execution introduced at `tutorial_multiple_parameters`, ending the block with a "commit as you go" commit.

> **Tip:** gets a new `_engine.Connection from the engine.Engine`
the next time it needs to execute SQL against the database.

The `_orm.Session obviously has a lot more tricks up its sleeve than that, however understanding that it has a orm.Session.execute method that's used the same way as engine.Connection.execute` will get us started with the examples that follow later.

> **Seealso:**  `session_basics` - presents basic creational and usage patterns with
 the `_orm.Session` object.
