---
type: "Framework Learn Page"
framework: "sqlalchemy"
source_repo: "https://github.com/sqlalchemy/sqlalchemy"
source_branch: "main"
source_path: "doc/build/orm/queryguide/_single_inheritance.rst"
source_commit: "ddf3b6589fd6ccb2affbaea5d4f400a8c1ad02d8"
source_commit_short: "ddf3b658"
source_commit_date: "2026-06-18T14:12:36-04:00"
generated_at: "2026-06-21T07:22:30Z"
---

:orphan:

=============================================

# Setup for ORM Queryguide: Single Inheritance

This page illustrates the mappings and fixture data used by the `single_inheritance` examples in the `inheritance` document of the `queryguide_toplevel`.

```python
 >>> from sqlalchemy import create_engine
 >>> from sqlalchemy import ForeignKey
 >>> from sqlalchemy.orm import DeclarativeBase
 >>> from sqlalchemy.orm import Mapped
 >>> from sqlalchemy.orm import mapped_column
 >>> from sqlalchemy.orm import relationship
 >>> from sqlalchemy.orm import Session
 >>>
 >>>
 >>> class Base(DeclarativeBase):
 ...     pass
 >>> class Employee(Base):
 ...     __tablename__ = "employee"
 ...     id: Mapped[int] = mapped_column(primary_key=True)
 ...     name: Mapped[str]
 ...     type: Mapped[str]
 ...
 ...     def __repr__(self):
 ...         return f"{self.__class__.__name__}({self.name!r})"
 ...
 ...     __mapper_args__ = {
 ...         "polymorphic_identity": "employee",
 ...         "polymorphic_on": "type",
 ...     }
 >>> class Manager(Employee):
 ...     manager_name: Mapped[str] = mapped_column(nullable=True)
 ...     __mapper_args__ = {
 ...         "polymorphic_identity": "manager",
 ...     }
 >>> class Engineer(Employee):
 ...     engineer_info: Mapped[str] = mapped_column(nullable=True)
 ...     __mapper_args__ = {
 ...         "polymorphic_identity": "engineer",
 ...     }
 >>>
 >>> engine = create_engine("sqlite://", echo=True)
 >>>
 >>> Base.metadata.create_all(engine)
 BEGIN ...

 >>> conn = engine.connect()
 >>> from sqlalchemy.orm import Session
 >>> session = Session(conn)
 >>> session.add_all(
 ...     [
 ...         Manager(
 ...             name="Mr. Krabs",
 ...             manager_name="Eugene H. Krabs",
 ...         ),
 ...         Engineer(name="SpongeBob", engineer_info="Krabby Patty Master"),
 ...         Engineer(
 ...             name="Squidward",
 ...             engineer_info="Senior Customer Engagement Engineer",
 ...         ),
 ...     ],
 ... )
 >>> session.commit()
 BEGIN ...
```
