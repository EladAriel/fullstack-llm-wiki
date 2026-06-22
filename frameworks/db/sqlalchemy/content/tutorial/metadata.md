---
type: "Framework Learn Page"
framework: "sqlalchemy"
source_repo: "https://github.com/sqlalchemy/sqlalchemy"
source_branch: "main"
source_path: "doc/build/tutorial/metadata.rst"
source_commit: "ddf3b6589fd6ccb2affbaea5d4f400a8c1ad02d8"
source_commit_short: "ddf3b658"
source_commit_date: "2026-06-18T14:12:36-04:00"
generated_at: "2026-06-21T07:22:30Z"
---

.. include:: tutorial_nav_include.rst

# Working with Database Metadata

With engines and SQL execution down, we are ready to begin some Alchemy. The central element of both SQLAlchemy Core and ORM is the SQL Expression Language which allows for fluent, composable construction of SQL queries. The foundation for these queries are Python objects that represent database concepts like tables and columns.   These objects are known collectively as `database metadata`.

The most common foundational objects for database metadata in SQLAlchemy are known as  `_schema.MetaData, schema.Table, and schema.Column`. The sections below will illustrate how these objects are used in both a Core-oriented style as well as an ORM-oriented style.

## Setting up MetaData with Table objects

When we work with a relational database, the basic data-holding structure in the database which we query from is known as a **table**. In SQLAlchemy, the database "table" is ultimately represented by a Python object similarly named `_schema.Table`.

To start using the SQLAlchemy Expression Language, we will want to have `_schema.Table objects constructed that represent all of the database tables we are interested in working with. The schema.Table is constructed programmatically, either directly by using the schema.Table` constructor, or indirectly by using ORM Mapped classes (described later at `tutorial_orm_table_metadata`).  There is also the option to load some or all table information from an existing database, called `reflection`.

using it here to stress that creating the MetaData directly will not introduce complexity (as long as one knows to associate it w/ declarative base)

Whichever kind of approach is used, we always start out with a collection that will be where we place our tables known as the `_schema.MetaData` object.  This object is essentially a `facade around a Python dictionary that stores a series of schema.Table` objects keyed to their string name.   While the ORM provides some options on where to get this collection, we always have the option to simply make one directly, which looks like:

```
>>> from sqlalchemy import MetaData
>>> metadata_obj = MetaData()
```

Once we have a `_schema.MetaData object, we can declare some schema.Table` objects. This tutorial will start with the classic SQLAlchemy tutorial model, which has a table called `user_account` that stores, for example, the users of a website, and a related table `address`, which stores email addresses associated with rows in the `user_account table. When not using ORM Declarative models at all, we construct each schema.Table` object directly, typically assigning each to a variable that will be how we will refer to the table in application code:

```
>>> from sqlalchemy import Table, Column, Integer, String
>>> user_table = Table(
...     "user_account",
...     metadata_obj,
...     Column("id", Integer, primary_key=True),
...     Column("name", String(30)),
...     Column("fullname", String),
... )
```

With the above example, when we wish to write code that refers to the `user_account` table in the database, we will use the `user_table` Python variable to refer to it.

#### Components of `Table`

We can observe that the `_schema.Table` construct as written in Python has a resemblance to a SQL CREATE TABLE statement; starting with the table name, then listing out each column, where each column has a name and a datatype. The objects we use above are:

- `_schema.Table` - represents a database table and assigns itself
to a `_schema.MetaData` collection.

- `_schema.Column` - represents a column in a database table, and
assigns itself to a `_schema.Table object.   The schema.Column usually includes a string name and a type object.   The collection of schema.Column objects in terms of the parent schema.Table are typically accessed via an associative array located at schema.Table.c`:

```
>>> user_table.c.name
Column('name', String(length=30), table=<user_account>)

>>> user_table.c.keys()
['id', 'name', 'fullname']
```

- `_types.Integer, types.String` - these classes represent
SQL datatypes and can be passed to a `_schema.Column` with or without necessarily being instantiated.  Above, we want to give a length of "30" to the "name" column, so we instantiated `String(30)`.  But for "id" and "fullname" we did not specify these, so we can send the class itself.

> **Seealso:**  The reference and API documentation for `_schema.MetaData`,
 `_schema.Table and schema.Column` is at `metadata_toplevel`.
 The reference documentation for datatypes is at `types_toplevel`.

In an upcoming section, we will illustrate one of the fundamental functions of `_schema.Table` which is to generate `DDL on a particular database connection.  But first we will declare a second schema.Table`.

#### Declaring Simple Constraints

The first `_schema.Column` in the example `user_table includes the schema.Column.primary_key parameter which is a shorthand technique of indicating that this schema.Column should be part of the primary key for this table.  The primary key itself is normally declared implicitly and is represented by the schema.PrimaryKeyConstraint construct, which we can see on the schema.Table.primary_key attribute on the schema.Table` object:

```
>>> user_table.primary_key
PrimaryKeyConstraint(Column('id', Integer(), table=<user_account>, primary_key=True, nullable=False))
```

The constraint that is most typically declared explicitly is the `_schema.ForeignKeyConstraint` object that corresponds to a database `foreign key constraint`.  When we declare tables that are related to each other, SQLAlchemy uses the presence of these foreign key constraint declarations not only so that they are emitted within CREATE statements to the database, but also to assist in constructing SQL expressions.

A `_schema.ForeignKeyConstraint that involves only a single column on the target table is typically declared using a column-level shorthand notation via the schema.ForeignKey` object.  Below we declare a second table `address` that will have a foreign key constraint referring to the `user` table:

```
>>> from sqlalchemy import ForeignKey
>>> address_table = Table(
...     "address",
...     metadata_obj,
...     Column("id", Integer, primary_key=True),
...     Column("user_id", ForeignKey("user_account.id"), nullable=False),
...     Column("email_address", String, nullable=False),
... )
```

The table above also features a third kind of constraint, which in SQL is the "NOT NULL" constraint, indicated above using the `_schema.Column.nullable` parameter.

> **Tip:** related column, in the above example the `_types.Integer` datatype
of the `user_account.id` column.

#### Using `.TypedColumns` to get a better typing experience

A SQLAlchemy `_schema.Table can also be defined using a schema.TypedColumns` to offers better integration with type checker and IDEs. The tables defined above could be declared as follows:

```
>>> from sqlalchemy import Named, TypedColumns, Table
>>> other_meta = MetaData()
>>> class user_cols(TypedColumns):
...     id: Named[int] = Column(primary_key=True)
...     name: Named[str | None] = Column(String(30))
...     fullname: Named[str | None]

>>> typed_user_table = Table("user_account", other_meta, user_cols)

>>> class address_cols(TypedColumns):
...     id: Named[int] = Column(primary_key=True)
...     user_id: Named[int] = Column(ForeignKey("user_account.id"))
...     email_address: Named[str]
...     __row_pos__: tuple[int, int, str]

>>> typed_address_table = Table("address", other_meta, address_cols)
```

The columns are defined by subclassing `.TypedColumns, so that static type checkers can understand what columns are present in the schema.Table.c collection. Functionally the two methods of defining the metadata objects are equivalent. The optional _row_pos__` annotation is an aid to type checker so that they can correctly suggest the type to apply when selecting from the complete table, without specifying the single columns.

In the next section we will emit the completed DDL for the `user_account` and `address` table to see the completed result.

#### Emitting DDL to the Database

We've constructed an object structure that represents two database tables in a database, starting at the root `_schema.MetaData object, then into two schema.Table objects, each of which hold onto a collection of schema.Column and schema.Constraint` objects.   This object structure will be at the center of most operations we perform with both Core and ORM going forward.

The first useful thing we can do with this structure will be to emit CREATE TABLE statements, or `DDL, to our SQLite database so that we can insert and query data from them.   We have already all the tools needed to do so, by invoking the schema.MetaData.create_all method on our schema.MetaData, sending it the engine.Engine` that refers to the target database:

```pycon+sql
 >>> metadata_obj.create_all(engine)
 {execsql}BEGIN (implicit)
 PRAGMA main.table_...info("user_account")
 ...
 PRAGMA main.table_...info("address")
 ...
 CREATE TABLE user_account (
     id INTEGER NOT NULL,
     name VARCHAR(30),
     fullname VARCHAR,
     PRIMARY KEY (id)
 )
 ...
 CREATE TABLE address (
     id INTEGER NOT NULL,
     user_id INTEGER NOT NULL,
     email_address VARCHAR NOT NULL,
     PRIMARY KEY (id),
     FOREIGN KEY(user_id) REFERENCES user_account (id)
 )
 ...
 COMMIT
```

The DDL create process above includes some SQLite-specific PRAGMA statements that test for the existence of each table before emitting a CREATE.   The full series of steps are also included within a BEGIN/COMMIT pair to accommodate for transactional DDL.

The create process also takes care of emitting CREATE statements in the correct order; above, the FOREIGN KEY constraint is dependent on the `user` table existing, so the `address` table is created second.   In more complicated dependency scenarios the FOREIGN KEY constraints may also be applied to tables after the fact using ALTER.

The `_schema.MetaData object also features a schema.MetaData.drop_all` method that will emit DROP statements in the reverse order as it would emit CREATE in order to drop schema elements.

## Using ORM Declarative Forms to Define Table Metadata

When using the ORM, the process by which we declare `_schema.Table` metadata is usually combined with the process of declaring `mapped` classes. The mapped class is any Python class we'd like to create, which will then have attributes on it that will be linked to the columns in a database table. While there are a few varieties of how this is achieved, the most common style is known as `declarative <orm_declarative_mapper_config_toplevel>, and allows us to declare our user-defined classes and schema.Table` metadata at once.

#### Establishing a Declarative Base

When using the ORM, the `_schema.MetaData collection remains present, however it itself is associated with an ORM-only construct commonly referred towards as the **Declarative Base**.   The most expedient way to acquire a new Declarative Base is to create a new class that subclasses the SQLAlchemy orm.DeclarativeBase` class:

```
>>> from sqlalchemy.orm import DeclarativeBase
>>> class Base(DeclarativeBase):
...     pass
```

Above, the `Base` class is what we'll call the Declarative Base. When we make new classes that are subclasses of `Base, combined with appropriate class-level directives, they will each be established as a new **ORM mapped class** at class creation time, each one typically (but not exclusively) referring to a particular schema.Table` object.

The Declarative Base refers to a `_schema.MetaData` collection that is created for us automatically, assuming we didn't provide one from the outside. This `.MetaData collection is accessible via the orm.DeclarativeBase.metadata` class-level attribute. As we create new mapped classes, they each will reference a `.Table` within this `.MetaData` collection:

```
>>> Base.metadata
MetaData()
```

The Declarative Base also refers to a collection called `_orm.registry`, which is the central "mapper configuration" unit in the SQLAlchemy ORM.  While seldom accessed directly, this object is central to the mapper configuration process, as a set of ORM mapped classes will coordinate with each other via this registry.   As was the case with `.MetaData, our Declarative Base also created a orm.registry for us (again with options to pass our own orm.registry), which we can access via the orm.DeclarativeBase.registry` class variable:

```
>>> Base.registry
<sqlalchemy.orm.decl_api.registry object at 0x...>
```

#### Declaring Mapped Classes

With the `Base` class established, we can now define ORM mapped classes for the `user_account` and `address` tables in terms of new classes `User` and `Address`.  We illustrate below the most modern form of Declarative, which is driven from `484` type annotations using a special type `.Mapped`, which indicates attributes to be mapped as particular types:

```
>>> from typing import List
>>> from typing import Optional
>>> from sqlalchemy.orm import Mapped
>>> from sqlalchemy.orm import mapped_column
>>> from sqlalchemy.orm import relationship

>>> class User(Base):
...     __tablename__ = "user_account"
...
...     id: Mapped[int] = mapped_column(primary_key=True)
...     name: Mapped[str] = mapped_column(String(30))
...     fullname: Mapped[Optional[str]]
...
...     addresses: Mapped[List["Address"]] = relationship(back_populates="user")
...
...     def __repr__(self) -> str:
...         return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

>>> class Address(Base):
...     __tablename__ = "address"
...
...     id: Mapped[int] = mapped_column(primary_key=True)
...     email_address: Mapped[str]
...     user_id = mapped_column(ForeignKey("user_account.id"))
...
...     user: Mapped[User] = relationship(back_populates="addresses")
...
...     def __repr__(self) -> str:
...         return f"Address(id={self.id!r}, email_address={self.email_address!r})"
```

The two classes above, `User` and `Address`, are now called as **ORM Mapped Classes**, and are available for use in ORM persistence and query operations, which will be described later.  Details about these classes include:

- Each class refers to a `_schema.Table` object that was generated as
part of the declarative mapping process, which is named by assigning a string to the `_orm.DeclarativeBase.__tablename__ attribute. Once the class is created, this generated schema.Table is available from the orm.DeclarativeBase.__table__` attribute.

- As mentioned previously, this form
is known as `orm_declarative_table_configuration.  One of several alternative declaration styles would instead have us build the schema.Table object directly, and **assign** it directly to orm.DeclarativeBase.__table__`.  This style is known as `Declarative with Imperative Table <orm_imperative_table_configuration>`.

- To indicate columns in the `_schema.Table`, we use the
`_orm.mapped_column construct, in combination with typing annotations based on the orm.Mapped type.  This object will generate schema.Column objects that are applied to the construction of the schema.Table`.

- For columns with simple datatypes and no other options, we can indicate a
`_orm.Mapped` type annotation alone, using simple Python types like `int` and `str` to mean `.Integer` and `.String`. Customization of how Python types are interpreted within the Declarative mapping process is very open ended; see the sections `orm_declarative_mapped_column` and `orm_declarative_mapped_column_type_map` for background.

- A column can be declared as "nullable" or "not null" based on the
presence of the `Optional[<typ>]` type annotation (or its equivalents, `<typ> | None` or `Union[<typ>, None]).  The orm.mapped_column.nullable` parameter may also be used explicitly (and does not have to match the annotation's optionality).

- Use of explicit typing annotations is **completely
optional**.  We can also use `_orm.mapped_column` without annotations. When using this form, we would use more explicit type objects like `.Integer` and `.String` as well as `nullable=False as needed within each orm.mapped_column` construct.

- Two additional attributes, `User.addresses` and `Address.user`, define
a different kind of attribute called `_orm.relationship, which features similar annotation-aware configuration styles as shown.  The orm.relationship` construct is discussed more fully at `tutorial_orm_related_objects`.

- The classes are automatically given an `__init__()` method if we don't
declare one of our own.  The default form of this method accepts all attribute names as optional keyword arguments:

```
>>> sandy = User(name="sandy", fullname="Sandy Cheeks")

To automatically generate a full-featured ``__init__()`` method which
provides for positional arguments as well as arguments with default keyword
values, the dataclasses feature introduced at
:ref:`orm_declarative_native_dataclasses` may be used.  It's of course
always an option to use an explicit ``__init__()`` method as well.
```

- The `__repr__()` methods are added so that we get a readable string output;
there's no requirement for these methods to be here.  As is the case with `__init__(), a _repr__()` method can be generated automatically by using the `dataclasses <orm_declarative_native_dataclasses>` feature.

> **Seealso:**  `orm_mapping_styles` - full background on different ORM configurational
 styles.
 `orm_declarative_mapping` - overview of Declarative class mapping
 `orm_declarative_table` - detail on how to use
 `_orm.mapped_column and orm.Mapped` to define the columns
 within a `_schema.Table` to be mapped when using Declarative.

#### Emitting DDL to the database from an ORM mapping

As our ORM mapped classes refer to `_schema.Table objects contained within a schema.MetaData` collection, emitting DDL given the Declarative Base uses the same process as that described previously at `tutorial_emitting_ddl`. In our case, we have already generated the `user` and `address tables in our SQLite database. If we had not done so already, we would be free to make use of the schema.MetaData associated with our ORM Declarative Base class in order to do so, by accessing the collection from the orm.DeclarativeBase.metadata attribute and then using schema.MetaData.create_all` as before.  In this case, PRAGMA statements are run, but no new tables are generated since they are found to be present already:

```pycon+sql
 >>> Base.metadata.create_all(engine)
 {execsql}BEGIN (implicit)
 PRAGMA main.table_...info("user_account")
 ...
 PRAGMA main.table_...info("address")
 ...
 COMMIT
```

## Table Reflection

To round out the section on working with table metadata, we will illustrate another operation that was mentioned at the beginning of the section, that of **table reflection**.   Table reflection refers to the process of generating `_schema.Table and related objects by reading the current state of a database.   Whereas in the previous sections we've been declaring schema.Table` objects in Python, where we then have the option to emit DDL to the database to generate such a schema, the reflection process does these two steps in reverse, starting from an existing database and generating in-Python data structures to represent the schemas within that database.

> **Tip:** use SQLAlchemy with a pre-existing database.  It is entirely typical that
the SQLAlchemy application declares all metadata explicitly in Python,
such that its structure corresponds to the existing database.
The metadata structure also need not include tables, columns, or other
constraints and constructs in the pre-existing database that are not needed
for the local application to function.

As an example of reflection, we will create a new `_schema.Table` object which represents the `some_table object we created manually in the earlier sections of this document.  There are again some varieties of how this is performed, however the most basic is to construct a schema.Table object, given the name of the table and a schema.MetaData collection to which it will belong, then instead of indicating individual schema.Column and schema.Constraint objects, pass it the target engine.Engine using the schema.Table.autoload_with` parameter:

```pycon+sql
 >>> some_table = Table("some_table", metadata_obj, autoload_with=engine)
 {execsql}BEGIN (implicit)
 PRAGMA main.table_...info("some_table")
 [raw sql] ()
 SELECT sql FROM  (SELECT * FROM sqlite_master UNION ALL   SELECT * FROM sqlite_temp_master) WHERE name = ? AND type in ('table', 'view')
 [raw sql] ('some_table',)
 PRAGMA main.foreign_key_list("some_table")
 ...
 PRAGMA main.index_list("some_table")
 ...
 ROLLBACK{stop}
```

At the end of the process, the `some_table object now contains the information about the schema.Column objects present in the table, and the object is usable in exactly the same way as a schema.Table` that we declared explicitly:

```
>>> some_table
Table('some_table', MetaData(),
    Column('x', INTEGER(), table=<some_table>),
    Column('y', INTEGER(), table=<some_table>),
    schema=None)
```

> **Seealso:**  Read more about table and schema reflection at `metadata_reflection_toplevel`.
 For ORM-related variants of table reflection, the section
 `orm_declarative_reflected` includes an overview of the available
 options.

## Next Steps

We now have a SQLite database ready to go with two tables present, and Core and ORM table-oriented constructs that we can use to interact with these tables via a `_engine.Connection and/or ORM orm.Session`.  In the following sections, we will illustrate how to create, manipulate, and select data using these structures.
