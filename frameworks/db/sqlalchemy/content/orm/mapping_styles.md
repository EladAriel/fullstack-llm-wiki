---
type: "Framework Learn Page"
framework: "sqlalchemy"
source_repo: "https://github.com/sqlalchemy/sqlalchemy"
source_branch: "main"
source_path: "doc/build/orm/mapping_styles.rst"
source_commit: "ddf3b6589fd6ccb2affbaea5d4f400a8c1ad02d8"
source_commit_short: "ddf3b658"
source_commit_date: "2026-06-18T14:12:36-04:00"
generated_at: "2026-06-21T07:22:30Z"
---

==========================

# ORM Mapped Class Overview

Overview of ORM class mapping configuration.

For readers new to the SQLAlchemy ORM and/or new to Python in general, it's recommended to browse through the `orm_quickstart` and preferably to work through the `unified_tutorial`, where ORM configuration is first introduced at `tutorial_orm_table_metadata`.

# ORM Mapping Styles

SQLAlchemy features two distinct styles of mapper configuration, which then feature further sub-options for how they are set up.   The variability in mapper styles is present to suit a varied list of developer preferences, including the degree of abstraction of a user-defined class from how it is to be mapped to relational schema tables and columns, what kinds of class hierarchies are in use, including whether or not custom metaclass schemes are present, and finally if there are other class-instrumentation approaches present such as if Python dataclasses_ are in use simultaneously.

In modern SQLAlchemy, the difference between these styles is mostly superficial; when a particular SQLAlchemy configurational style is used to express the intent to map a class, the internal process of mapping the class proceeds in mostly the same way for each, where the end result is always a user-defined class that has a `_orm.Mapper configured against a selectable unit, typically represented by a schema.Table` object, and the class itself has been `instrumented to include behaviors linked to relational operations both at the level of the class as well as on instances of that class. As the process is basically the same in all cases, classes mapped from different styles are always fully interoperable with each other. The protocol orm.MappedClassProtocol` can be used to indicate a mapped class when using type checkers such as mypy.

The original mapping API is commonly referred to as "classical" style, whereas the more automated style of mapping is known as "declarative" style. SQLAlchemy now refers to these two mapping styles as **imperative mapping** and **declarative mapping**.

Regardless of what style of mapping used, all ORM mappings as of SQLAlchemy 1.4 originate from a single object known as `_orm.registry`, which is a registry of mapped classes. Using this registry, a set of mapper configurations can be finalized as a group, and classes within a particular registry may refer to each other by name within the configurational process.

.. versionchanged:: 1.4  Declarative and classical mapping are now referred

## Declarative Mapping

The **Declarative Mapping** is the typical way that mappings are constructed in modern SQLAlchemy. The most common pattern is to first construct a base class using the `_orm.DeclarativeBase superclass. The resulting base class, when subclassed will apply the declarative mapping process to all subclasses that derive from it, relative to a particular orm.registry` that is local to the new base by default. The example below illustrates the use of a declarative base which is then used in a declarative table mapping:

```
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

# declarative base class
class Base(DeclarativeBase):
    pass

# an example mapping using the base
class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    fullname: Mapped[str] = mapped_column(String(30))
    nickname: Mapped[Optional[str]]
```

Above, the `_orm.DeclarativeBase` class is used to generate a new base class (within SQLAlchemy's documentation it's typically referred to as `Base`, however can have any desired name) from which new classes to be mapped may inherit from, as above a new mapped class `User` is constructed.

.. versionchanged:: 2.0 The `_orm.DeclarativeBase` superclass supersedes

The base class refers to a `_orm.registry object that maintains a collection of related mapped classes. as well as to a schema.MetaData object that retains a collection of schema.Table` objects to which the classes are mapped.

The major Declarative mapping styles are further detailed in the following sections:

- `orm_declarative_generated_base_class` - declarative mapping using a
base class.

- `orm_declarative_decorator` - declarative mapping using a decorator,
rather than a base class.

Within the scope of a Declarative mapped class, there are also two varieties of how the `_schema.Table` metadata may be declared.  These include:

- `orm_declarative_table` - table columns are declared inline
within the mapped class using the `_orm.mapped_column directive (or in legacy form, using the schema.Column object directly). The orm.mapped_column directive may also be optionally combined with type annotations using the orm.Mapped class which can provide some details about the mapped columns directly.  The column directives, in combination with the _tablename__ and optional _table_args__ class level directives will allow the Declarative mapping process to construct a schema.Table` object to be mapped.

- `orm_imperative_table_configuration` - Instead of specifying table name
and attributes separately, an explicitly constructed `_schema.Table` object is associated with a class that is otherwise mapped declaratively.  This style of mapping is a hybrid of "declarative" and "imperative" mapping, and applies to techniques such as mapping classes to `reflected schema.Table` objects, as well as mapping classes to existing Core constructs such as joins and subqueries.

Documentation for Declarative mapping continues at `declarative_config_toplevel`.

## Imperative Mapping

An **imperative** or **classical** mapping refers to the configuration of a mapped class using the `_orm.registry.map_imperatively` method, where the target class does not include any declarative class attributes.

> **Tip:** originates from the very first releases of SQLAlchemy in 2006.  It's
essentially a means of bypassing the Declarative system to provide a
more "barebones" system of mapping, and does not offer modern features
such as `484` support.  As such, most documentation examples
use Declarative forms, and it's recommended that new users start
with `Declarative Table <orm_declarative_table_config_toplevel>`
configuration.

.. versionchanged:: 2.0  The `_orm.registry.map_imperatively` method

In "classical" form, the table metadata is created separately with the `_schema.Table` construct, then associated with the `User class via the orm.registry.map_imperatively method, after establishing a orm.registry instance.  Normally, a single instance of orm.registry` shared for all mapped classes that are related to each other:

```
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import registry

mapper_registry = registry()

user_table = Table(
    "user",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("fullname", String(50)),
    Column("nickname", String(12)),
)

class User:
    pass

mapper_registry.map_imperatively(User, user_table)
```

Information about mapped attributes, such as relationships to other classes, are provided via the `properties dictionary.  The example below illustrates a second schema.Table` object, mapped to a class called `Address`, then linked to `User via orm.relationship`:

```
address = Table(
    "address",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("user.id")),
    Column("email_address", String(50)),
)

mapper_registry.map_imperatively(
    User,
    user,
    properties={
        "addresses": relationship(Address, backref="user", order_by=address.c.id)
    },
)

mapper_registry.map_imperatively(Address, address)
```

Note that classes which are mapped with the Imperative approach are **fully interchangeable** with those mapped with the Declarative approach. Both systems ultimately create the same configuration, consisting of a `_schema.Table, user-defined class, linked together with a orm.Mapper object. When we talk about "the behavior of orm.Mapper`", this includes when using the Declarative system as well

- it's still used, just behind the scenes.
# Mapped Class Essential Components

With all mapping forms, the mapping of the class can be configured in many ways by passing construction arguments that ultimately become part of the `_orm.Mapper object via its constructor.  The parameters that are delivered to orm.Mapper originate from the given mapping form, including parameters passed to orm.registry.map_imperatively for an Imperative mapping, or when using the Declarative system, from a combination of the table columns, SQL expressions and relationships being mapped along with that of attributes such as _mapper_args__ <orm_declarative_mapper_options>`.

There are four general classes of configuration information that the `_orm.Mapper` class looks for:

## The class to be mapped

This is a class that we construct in our application. There are generally no restrictions on the structure of this class. [1]_ When a Python class is mapped, there can only be **one** `_orm.Mapper` object for the class. [2]_

When mapping with the `declarative <orm_declarative_mapping> mapping style, the class to be mapped is either a subclass of the declarative base class, or is handled by a decorator or function such as orm.registry.mapped`.

When mapping with the `imperative <orm_imperative_mapping> style, the class is passed directly as the orm.registry.map_imperatively.class_` argument.

## The table, or other from clause object

In the vast majority of common cases this is an instance of `_schema.Table.  For more advanced use cases, it may also refer to any kind of sql.FromClause object, the most common alternative objects being the sql.Subquery and sql.Join` object.

When mapping with the `declarative <orm_declarative_mapping> mapping style, the subject table is either generated by the declarative system based on the _tablename__ attribute and the schema.Column objects presented, or it is established via the _table__` attribute.  These two styles of configuration are presented at `orm_declarative_table` and `orm_imperative_table_configuration`.

When mapping with the `imperative <orm_imperative_mapping> style, the subject table is passed positionally as the orm.registry.map_imperatively.local_table` argument.

In contrast to the "one mapper per class" requirement of a mapped class, the `_schema.Table or other sql.FromClause object that is the subject of the mapping may be associated with any number of mappings. The orm.Mapper applies modifications directly to the user-defined class, but does not modify the given schema.Table or other sql.FromClause` in any way.

## The properties dictionary

This is a dictionary of all of the attributes that will be associated with the mapped class.    By default, the `_orm.Mapper generates entries for this dictionary derived from the given schema.Table, in the form of orm.ColumnProperty objects which each refer to an individual schema.Column of the mapped table.  The properties dictionary will also contain all the other kinds of orm.MapperProperty objects to be configured, most commonly instances generated by the orm.relationship` construct.

When mapping with the `declarative <orm_declarative_mapping>` mapping style, the properties dictionary is generated by the declarative system by scanning the class to be mapped for appropriate attributes.  See the section `orm_declarative_properties` for notes on this process.

When mapping with the `imperative <orm_imperative_mapping>` style, the properties dictionary is passed directly as the `properties parameter to orm.registry.map_imperatively, which will pass it along to the orm.Mapper.properties` parameter.

## Other mapper configuration parameters

When mapping with the `declarative <orm_declarative_mapping> mapping style, additional mapper configuration arguments are configured via the _mapper_args__` class attribute.   Examples of use are available at `orm_declarative_mapper_options`.

When mapping with the `imperative <orm_imperative_mapping> style, keyword arguments are passed to the to orm.registry.map_imperatively method which passes them along to the orm.Mapper` class.

The full range of parameters accepted are documented at  `_orm.Mapper`.

# Mapped Class Behavior

Across all styles of mapping using the `_orm.registry` object, the following behaviors are common:

## Default Constructor

The `_orm.registry applies a default constructor, i.e. _init__ method, to all mapped classes that don't explicitly have their own _init__` method.   The behavior of this method is such that it provides a convenient keyword constructor that will accept as optional keyword arguments all the attributes that are named.   E.g.:

```
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    fullname: Mapped[str]
```

An object of type `User` above will have a constructor which allows `User` objects to be created as:

```
u1 = User(name="some name", fullname="some fullname")
```

> **Tip:**  The `orm_declarative_native_dataclasses` feature provides an alternate
 means of generating a default `__init__()` method by using
 Python dataclasses, and allows for a highly configurable constructor
 form.

> **Warning:**  The `__init__()` method of the class is called only when the object is
 constructed in Python code, and **not when an object is loaded or refreshed
 from the database**.  See the next section `mapped_class_load_events`
 for a primer on how to invoke special logic when objects are loaded.

A class that includes an explicit `__init__()` method will maintain that method, and no default constructor will be applied.

To change the default constructor used, a user-defined Python callable may be provided to the `_orm.registry.constructor` parameter which will be used as the default constructor.

The constructor also applies to imperative mappings:

```
from sqlalchemy.orm import registry

mapper_registry = registry()

user_table = Table(
    "user",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
)

class User:
    pass

mapper_registry.map_imperatively(User, user_table)
```

The above class, mapped imperatively as described at `orm_imperative_mapping, will also feature the default constructor associated with the orm.registry`.

.. versionadded:: 1.4  classical mappings now support a standard configuration-level

## Maintaining Non-Mapped State Across Loads

The `__init__()` method of the mapped class is invoked when the object is constructed directly in Python code:

```
u1 = User(name="some name", fullname="some fullname")
```

However, when an object is loaded using the ORM `_orm.Session, the _init__()` method is **not** called:

```
u1 = session.scalars(select(User).where(User.name == "some name")).first()
```

The reason for this is that when loaded from the database, the operation used to construct the object, in the above example the `User`, is more analogous to **deserialization**, such as unpickling, rather than initial construction.  The majority of the object's important state is not being assembled for the first time, it's being re-loaded from database rows.

Therefore to maintain state within the object that is not part of the data that's stored to the database, such that this state is present when objects are loaded as well as constructed, there are two general approaches detailed below.

1. Use Python descriptors like `@property`, rather than state, to dynamically
compute attributes as needed.

For simple attributes, this is the simplest approach and the least error prone. For example if an object `Point` with `Point.x` and `Point.y` wanted an attribute with the sum of these attributes:

```
  class Point(Base):
      __tablename__ = "point"
      id: Mapped[int] = mapped_column(primary_key=True)
      x: Mapped[int]
      y: Mapped[int]

      @property
      def x_plus_y(self):
          return self.x + self.y

An advantage of using dynamic descriptors is that the value is computed
every time, meaning it maintains the correct value as the underlying
attributes (``x`` and ``y`` in this case) might change.

Other forms of the above pattern include Python standard library
`cached_property <https://docs.python.org/3/library/functools.html#functools.cached_property>`_
decorator (which is cached, and not re-computed each time), as well as SQLAlchemy's :class:`.hybrid_property` decorator which
allows for attributes that can work for SQL querying as well.
```

2. Establish state on-load using `.InstanceEvents.load`, and optionally
supplemental methods `.InstanceEvents.refresh` and `.InstanceEvents.refresh_flush`.

These are event hooks that are invoked whenever the object is loaded from the database, or when it is refreshed after being expired.   Typically only the `.InstanceEvents.load` is needed, since non-mapped local object state is not affected by expiration operations.   To revise the `Point` example above looks like:

```
  from sqlalchemy import event

  class Point(Base):
      __tablename__ = "point"
      id: Mapped[int] = mapped_column(primary_key=True)
      x: Mapped[int]
      y: Mapped[int]

      def __init__(self, x, y, **kw):
          super().__init__(x=x, y=y, **kw)
          self.x_plus_y = x + y

  @event.listens_for(Point, "load")
  def receive_load(target, context):
      target.x_plus_y = target.x + target.y

If using the refresh events as well, the event hooks can be stacked on
top of one callable if needed, as::

  @event.listens_for(Point, "load")
  @event.listens_for(Point, "refresh")
  @event.listens_for(Point, "refresh_flush")
  def receive_load(target, context, attrs=None):
      target.x_plus_y = target.x + target.y

Above, the ``attrs`` attribute will be present for the ``refresh`` and
``refresh_flush`` events and indicate a list of attribute names that are
being refreshed.
```

## Runtime Introspection of Mapped classes, Instances and Mappers

A class that is mapped using `_orm.registry` will also feature a few attributes that are common to all mappings:

- The `__mapper__ attribute will refer to the orm.Mapper` that
is associated with the class:

```
mapper = User.__mapper__

This :class:`_orm.Mapper` is also what's returned when using the
:func:`_sa.inspect` function against the mapped class::

from sqlalchemy import inspect

mapper = inspect(User)

..
```

- The `__table__ attribute will refer to the schema.Table`, or
more generically to the `.FromClause` object, to which the class is mapped:

```
table = User.__table__

This :class:`.FromClause` is also what's returned when using the
:attr:`_orm.Mapper.local_table` attribute of the :class:`_orm.Mapper`::

table = inspect(User).local_table

For a single-table inheritance mapping, where the class is a subclass that
does not have a table of its own, the :attr:`_orm.Mapper.local_table` attribute as well
as the ``.__table__`` attribute will be ``None``.   To retrieve the
"selectable" that is actually selected from during a query for this class,
this is available via the :attr:`_orm.Mapper.selectable` attribute::

table = inspect(User).selectable

..
```

### Inspection of Mapper objects

As illustrated in the previous section, the `_orm.Mapper` object is available from any mapped class, regardless of method, using the `core_inspection_toplevel system.  Using the sa.inspect function, one can acquire the orm.Mapper` from a mapped class:

```
>>> from sqlalchemy import inspect
>>> insp = inspect(User)
```

Detailed information is available including `_orm.Mapper.columns`:

```
>>> insp.columns
<sqlalchemy.util._collections.OrderedProperties object at 0x102f407f8>
```

This is a namespace that can be viewed in a list format or via individual names:

```
>>> list(insp.columns)
[Column('id', Integer(), table=<user>, primary_key=True, nullable=False), Column('name', String(length=50), table=<user>), Column('fullname', String(length=50), table=<user>), Column('nickname', String(length=50), table=<user>)]
>>> insp.columns.name
Column('name', String(length=50), table=<user>)
```

Other namespaces include `_orm.Mapper.all_orm_descriptors`, which includes all mapped attributes as well as hybrids, association proxies:

```
>>> insp.all_orm_descriptors
<sqlalchemy.util._collections.ImmutableProperties object at 0x1040e2c68>
>>> insp.all_orm_descriptors.keys()
['fullname', 'nickname', 'name', 'id']
```

As well as `_orm.Mapper.column_attrs`:

```
>>> list(insp.column_attrs)
[<ColumnProperty at 0x10403fde0; id>, <ColumnProperty at 0x10403fce8; name>, <ColumnProperty at 0x1040e9050; fullname>, <ColumnProperty at 0x1040e9148; nickname>]
>>> insp.column_attrs.name
<ColumnProperty at 0x10403fce8; name>
>>> insp.column_attrs.name.expression
Column('name', String(length=50), table=<user>)
```

> **Seealso:**  `.Mapper`

### Inspection of Mapped Instances

The `_sa.inspect` function also provides information about instances of a mapped class.  When applied to an instance of a mapped class, rather than the class itself, the object returned is known as `.InstanceState`, which will provide links to not only the `.Mapper` in use by the class, but also a detailed interface that provides information on the state of individual attributes within the instance including their current value and how this relates to what their database-loaded value is.

Given an instance of the `User` class loaded from the database:

```
>>> u1 = session.scalars(select(User)).first()
```

The `_sa.inspect` function will return to us an `.InstanceState` object:

```
>>> insp = inspect(u1)
>>> insp
<sqlalchemy.orm.state.InstanceState object at 0x7f07e5fec2e0>
```

With this object we can see elements such as the `.Mapper`:

```
>>> insp.mapper
<Mapper at 0x7f07e614ef50; User>
```

The `_orm.Session` to which the object is `attached`, if any:

```
>>> insp.session
<sqlalchemy.orm.session.Session object at 0x7f07e614f160>
```

Information about the current `persistence state <session_object_states>` for the object:

```
>>> insp.persistent
True
>>> insp.pending
False
```

Attribute state information such as attributes that have not been loaded or `lazy loaded` (assume `addresses refers to a orm.relationship` on the mapped class to a related class):

```
>>> insp.unloaded
{'addresses'}
```

Information regarding the current in-Python status of attributes, such as attributes that have not been modified since the last flush:

```
>>> insp.unmodified
{'nickname', 'name', 'fullname', 'id'}
```

as well as specific history on modifications to attributes since the last flush:

```
>>> insp.attrs.nickname.value
'nickname'
>>> u1.nickname = "new nickname"
>>> insp.attrs.nickname.history
History(added=['new nickname'], unchanged=(), deleted=['nickname'])
```

> **Seealso:**  `.InstanceState`
 `.InstanceState.attrs`
 `.AttributeState`

kind of class that isn't compatible.    When running code on Python 2, all classes must extend from the Python `object` class.  Under Python 3 this is always the case.

additional `_orm.Mapper` objects may be associated with a class that's already mapped, however they don't apply instrumentation to the class.  This feature is deprecated as of SQLAlchemy 1.3.
