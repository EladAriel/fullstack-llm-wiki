---
type: "Framework Learn Page"
framework: "sqlalchemy"
source_repo: "https://github.com/sqlalchemy/sqlalchemy"
source_branch: "main"
source_path: "doc/build/orm/declarative_styles.rst"
source_commit: "ddf3b6589fd6ccb2affbaea5d4f400a8c1ad02d8"
source_commit_short: "ddf3b658"
source_commit_date: "2026-06-18T14:12:36-04:00"
generated_at: "2026-06-21T07:22:30Z"
---

==========================

# Declarative Mapping Styles

As introduced at `orm_declarative_mapping`, the **Declarative Mapping** is the typical way that mappings are constructed in modern SQLAlchemy.   This section will provide an overview of forms that may be used for Declarative mapper configuration.

## Using a Declarative Base Class

The most common approach is to generate a "Declarative Base" class by subclassing the `_orm.DeclarativeBase` superclass:

```
from sqlalchemy.orm import DeclarativeBase

# declarative base class
class Base(DeclarativeBase):
    pass
```

The Declarative Base class may also be created given an existing `_orm.registry` by assigning it as a class variable named `registry`:

```
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import registry

reg = registry()

# declarative base class
class Base(DeclarativeBase):
    registry = reg
```

.. versionchanged:: 2.0 The `_orm.DeclarativeBase` superclass supersedes

With the declarative base class, new mapped classes are declared as subclasses of the base:

```
from datetime import datetime
from typing import List
from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy import func
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user"

    id = mapped_column(Integer, primary_key=True)
    name: Mapped[str]
    fullname: Mapped[Optional[str]]
    nickname: Mapped[Optional[str]] = mapped_column(String(64))
    create_date: Mapped[datetime] = mapped_column(insert_default=func.now())

    addresses: Mapped[List["Address"]] = relationship(back_populates="user")

class Address(Base):
    __tablename__ = "address"

    id = mapped_column(Integer, primary_key=True)
    user_id = mapped_column(ForeignKey("user.id"))
    email_address: Mapped[str]

    user: Mapped["User"] = relationship(back_populates="addresses")
```

Above, the `Base` class serves as a base for new classes that are to be mapped, as above new mapped classes `User` and `Address` are constructed.

For each subclass constructed, the body of the class then follows the declarative mapping approach which defines both a `_schema.Table as well as a orm.Mapper` object behind the scenes which comprise a full mapping.

> **Seealso:**  `orm_declarative_table_config_toplevel` - describes how to specify
 the components of the mapped `_schema.Table` to be generated,
 including notes and options on the use of the `_orm.mapped_column`
 construct and how it interacts with the `_orm.Mapped` annotation
 type
 `orm_declarative_mapper_config_toplevel` - describes all other
 aspects of ORM mapper configuration within Declarative including
 `_orm.relationship` configuration, SQL expressions and
 `_orm.Mapper` parameters

## Declarative Mapping using a Decorator (no declarative base)

As an alternative to using the "declarative base" class is to apply declarative mapping to a class explicitly, using either an imperative technique similar to that of a "classical" mapping, or more succinctly by using a decorator.  The `_orm.registry.mapped` function is a class decorator that can be applied to any Python class with no hierarchy in place.  The Python class otherwise is configured in declarative style normally.

The example below sets up the identical mapping as seen in the previous section, using the `_orm.registry.mapped decorator rather than using the orm.DeclarativeBase` superclass:

```
from datetime import datetime
from typing import List
from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy import func
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import registry
from sqlalchemy.orm import relationship

mapper_registry = registry()

@mapper_registry.mapped
class User:
    __tablename__ = "user"

    id = mapped_column(Integer, primary_key=True)
    name: Mapped[str]
    fullname: Mapped[Optional[str]]
    nickname: Mapped[Optional[str]] = mapped_column(String(64))
    create_date: Mapped[datetime] = mapped_column(insert_default=func.now())

    addresses: Mapped[List["Address"]] = relationship(back_populates="user")

@mapper_registry.mapped
class Address:
    __tablename__ = "address"

    id = mapped_column(Integer, primary_key=True)
    user_id = mapped_column(ForeignKey("user.id"))
    email_address: Mapped[str]

    user: Mapped["User"] = relationship(back_populates="addresses")
```

When using the above style, the mapping of a particular class will **only** proceed if the decorator is applied to that class directly. For inheritance mappings (described in detail at `inheritance_toplevel`), the decorator should be applied to each subclass that is to be mapped:

```
from sqlalchemy.orm import registry

mapper_registry = registry()

@mapper_registry.mapped
class Person:
    __tablename__ = "person"

    person_id = mapped_column(Integer, primary_key=True)
    type = mapped_column(String, nullable=False)

    __mapper_args__ = {
        "polymorphic_on": type,
        "polymorphic_identity": "person",
    }

@mapper_registry.mapped
class Employee(Person):
    __tablename__ = "employee"

    person_id = mapped_column(ForeignKey("person.person_id"), primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": "employee",
    }
```

Both the `declarative table <orm_declarative_table>` and `imperative table <orm_imperative_table_configuration>` table configuration styles may be used with either the Declarative Base or decorator styles of Declarative mapping.

The decorator form of mapping is useful when combining a SQLAlchemy declarative mapping with other class instrumentation systems such as dataclasses_ and attrs_, though note that SQLAlchemy 2.0 now features dataclasses integration with Declarative Base classes as well.
