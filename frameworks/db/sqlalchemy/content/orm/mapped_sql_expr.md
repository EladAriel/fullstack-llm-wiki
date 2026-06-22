---
type: "Framework Learn Page"
framework: "sqlalchemy"
source_repo: "https://github.com/sqlalchemy/sqlalchemy"
source_branch: "main"
source_path: "doc/build/orm/mapped_sql_expr.rst"
source_commit: "ddf3b6589fd6ccb2affbaea5d4f400a8c1ad02d8"
source_commit_short: "ddf3b658"
source_commit_date: "2026-06-18T14:12:36-04:00"
generated_at: "2026-06-21T07:22:30Z"
---

# SQL Expressions as Mapped Attributes

Attributes on a mapped class can be linked to SQL expressions, which can be used in queries.

## Using a Hybrid

The easiest and most flexible way to link relatively simple SQL expressions to a class is to use a so-called "hybrid attribute", described in the section `hybrids_toplevel`.  The hybrid provides for an expression that works at both the Python level as well as at the SQL expression level.  For example, below we map a class `User`, containing attributes `firstname` and `lastname`, and include a hybrid that will provide for us the `fullname`, which is the string concatenation of the two:

```
from sqlalchemy.ext.hybrid import hybrid_property

class User(Base):
    __tablename__ = "user"
    id = mapped_column(Integer, primary_key=True)
    firstname = mapped_column(String(50))
    lastname = mapped_column(String(50))

    @hybrid_property
    def fullname(self):
        return self.firstname + " " + self.lastname
```

Above, the `fullname` attribute is interpreted at both the instance and class level, so that it is available from an instance:

```
some_user = session.scalars(select(User).limit(1)).first()
print(some_user.fullname)
```

as well as usable within queries:

```
some_user = session.scalars(
    select(User).where(User.fullname == "John Smith").limit(1)
).first()
```

The string concatenation example is a simple one, where the Python expression can be dual purposed at the instance and class level.  Often, the SQL expression must be distinguished from the Python expression, which can be achieved using `.hybrid_property.expression`.  Below we illustrate the case where a conditional needs to be present inside the hybrid, using the `if statement in Python and the expression.case` construct for SQL expressions:

```
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.sql import case

class User(Base):
    __tablename__ = "user"
    id = mapped_column(Integer, primary_key=True)
    firstname = mapped_column(String(50))
    lastname = mapped_column(String(50))

    @hybrid_property
    def fullname(self):
        if self.firstname is not None:
            return self.firstname + " " + self.lastname
        else:
            return self.lastname

    @fullname.expression
    def fullname(cls):
        return case(
            (cls.firstname != None, cls.firstname + " " + cls.lastname),
            else_=cls.lastname,
        )
```

## Using column_property

The `_orm.column_property function can be used to map a SQL expression in a manner similar to a regularly mapped schema.Column`. With this technique, the attribute is loaded along with all other column-mapped attributes at load time.  This is in some cases an advantage over the usage of hybrids, as the value can be loaded up front at the same time as the parent row of the object, particularly if the expression is one which links to other tables (typically as a correlated subquery) to access data that wouldn't normally be available on an already loaded object.

Disadvantages to using `_orm.column_property for SQL expressions include that the expression must be compatible with the SELECT statement emitted for the class as a whole, and there are also some configurational quirks which can occur when using orm.column_property` from declarative mixins.

Our "fullname" example can be expressed using `_orm.column_property` as follows:

```
from sqlalchemy.orm import column_property

class User(Base):
    __tablename__ = "user"
    id = mapped_column(Integer, primary_key=True)
    firstname = mapped_column(String(50))
    lastname = mapped_column(String(50))
    fullname = column_property(firstname + " " + lastname)
```

Correlated subqueries may be used as well. Below we use the `_expression.select construct to create a sql.ScalarSelect`, representing a column-oriented SELECT statement, that links together the count of `Address` objects available for a particular `User`:

```
from sqlalchemy.orm import column_property
from sqlalchemy import select, func
from sqlalchemy import Column, Integer, String, ForeignKey

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Address(Base):
    __tablename__ = "address"
    id = mapped_column(Integer, primary_key=True)
    user_id = mapped_column(Integer, ForeignKey("user.id"))

class User(Base):
    __tablename__ = "user"
    id = mapped_column(Integer, primary_key=True)
    address_count = column_property(
        select(func.count(Address.id))
        .where(Address.user_id == id)
        .correlate_except(Address)
        .scalar_subquery()
    )
```

In the above example, we define a `_expression.ScalarSelect` construct like the following:

```
stmt = (
    select(func.count(Address.id))
    .where(Address.user_id == id)
    .correlate_except(Address)
    .scalar_subquery()
)
```

Above, we first use `_sql.select to create a sql.Select` construct, which we then convert into a `scalar subquery using the sql.Select.scalar_subquery method, indicating our intent to use this sql.Select` statement in a column expression context.

Within the `_sql.Select` itself, we select the count of `Address.id` rows where the `Address.user_id` column is equated to `id`, which in the context of the `User class is the schema.Column` named `id` (note that `id` is also the name of a Python built in function, which is not what we want to use here - if we were outside of the `User` class definition, we'd use `User.id`).

The `_sql.Select.correlate_except method indicates that each element in the FROM clause of this expression.select` may be omitted from the FROM list (that is, correlated to the enclosing SELECT statement against `User`) except for the one corresponding to `Address`.  This isn't strictly necessary, but prevents `Address` from being inadvertently omitted from the FROM list in the case of a long string of joins between `User` and `Address` tables where SELECT statements against `Address` are nested.

For a `.column_property` that refers to columns linked from a many-to-many relationship, use `.and_` to join the fields of the association table to both tables in a relationship:

```
from sqlalchemy import and_

class Author(Base):
    # ...

    book_count = column_property(
        select(func.count(books.c.id))
        .where(
            and_(
                book_authors.c.author_id == authors.c.id,
                book_authors.c.book_id == books.c.id,
            )
        )
        .scalar_subquery()
    )
```

#### Adding column_property() to an existing Declarative mapped class

If import issues prevent the `.column_property from being defined inline with the class, it can be assigned to the class after both are configured.   When using mappings that make use of a Declarative base class (i.e. produced by the orm.DeclarativeBase superclass or legacy functions such as orm.declarative_base), this attribute assignment has the effect of calling orm.Mapper.add_property` to add an additional property after the fact:

```
# only works if a declarative base class is in use
User.address_count = column_property(
    select(func.count(Address.id)).where(Address.user_id == User.id).scalar_subquery()
)
```

When using mapping styles that don't use Declarative base classes such as the `_orm.registry.mapped decorator, the orm.Mapper.add_property method may be invoked explicitly on the underlying orm.Mapper object, which can be obtained using sa.inspect`:

```
from sqlalchemy.orm import registry

reg = registry()

@reg.mapped
class User:
    __tablename__ = "user"

    # ... additional mapping directives

# later ...

# works for any kind of mapping
from sqlalchemy import inspect

inspect(User).add_property(
    column_property(
        select(func.count(Address.id))
        .where(Address.user_id == User.id)
        .scalar_subquery()
    )
)
```

> **Seealso:** `orm_declarative_table_adding_columns`

#### Composing from Column Properties at Mapping Time

It is possible to create mappings that combine multiple `.ColumnProperty` objects together.  The `.ColumnProperty will be interpreted as a SQL expression when used in a Core expression context, provided that it is targeted by an existing expression object; this works by the Core detecting that the object has a _clause_element__()` method which returns a SQL expression.   However, if the `.ColumnProperty` is used as a lead object in an expression where there is no other Core SQL expression object to target it, the `.ColumnProperty.expression` attribute will return the underlying SQL expression so that it can be used to build SQL expressions consistently.  Below, the `File` class contains an attribute `File.path` that concatenates a string token to the `File.filename` attribute, which is itself a `.ColumnProperty`:

```
class File(Base):
    __tablename__ = "file"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(64))
    extension = mapped_column(String(8))
    filename = column_property(name + "." + extension)
    path = column_property("C:/" + filename.expression)
```

When the `File` class is used in expressions normally, the attributes assigned to `filename` and `path` are usable directly.  The use of the `.ColumnProperty.expression` attribute is only necessary when using the `.ColumnProperty` directly within the mapping definition:

```
stmt = select(File.path).where(File.filename == "foo.txt")
```

#### Using Column Deferral with `column_property()`

The column deferral feature introduced in the `queryguide_toplevel` at `orm_queryguide_column_deferral may be applied at mapping time to a SQL expression mapped by orm.column_property by using the orm.deferred function in place of orm.column_property`:

```
from sqlalchemy.orm import deferred

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    firstname: Mapped[str] = mapped_column()
    lastname: Mapped[str] = mapped_column()
    fullname: Mapped[str] = deferred(firstname + " " + lastname)
```

> **Seealso:**  `orm_queryguide_deferred_imperative`

## Using a plain descriptor

In cases where a SQL query more elaborate than what `_orm.column_property` or `.hybrid_property` can provide must be emitted, a regular Python function accessed as an attribute can be used, assuming the expression only needs to be available on an already-loaded instance.   The function is decorated with Python's own `@property` decorator to mark it as a read-only attribute.   Within the function, `.object_session` is used to locate the `.Session` corresponding to the current object, which is then used to emit a query:

```
from sqlalchemy.orm import object_session
from sqlalchemy import select, func

class User(Base):
    __tablename__ = "user"
    id = mapped_column(Integer, primary_key=True)
    firstname = mapped_column(String(50))
    lastname = mapped_column(String(50))

    @property
    def address_count(self):
        return object_session(self).scalar(
            select(func.count(Address.id)).where(Address.user_id == self.id)
        )
```

The plain descriptor approach is useful as a last resort, but is less performant in the usual case than both the hybrid and column property approaches, in that it needs to emit a SQL query upon each access.

## Query-time SQL expressions as mapped attributes

In addition to being able to configure fixed SQL expressions on mapped classes, the SQLAlchemy ORM also includes a feature wherein objects may be loaded with the results of arbitrary SQL expressions which are set up at query time as part of their state.  This behavior is available by configuring an ORM mapped attribute using `_orm.query_expression and then using the orm.with_expression` loader option at query time.  See the section `orm_queryguide_with_expression` for an example mapping and usage.
