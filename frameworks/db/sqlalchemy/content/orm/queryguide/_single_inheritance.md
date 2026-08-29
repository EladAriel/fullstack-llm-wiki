---
type: "Framework Learn Page"
framework: "SQLAlchemy"
source_repo: "https://github.com/sqlalchemy/sqlalchemy"
source_branch: "main"
source_path: "doc/build/orm/queryguide/_single_inheritance.rst"
source_commit: "85cafd1a131fa8afeeeab23151940480b3fb0042"
source_commit_short: "85cafd1"
source_commit_date: "2026-08-28T20:17:49+00:00"
generated_at: "2026-08-29T09:39:27.728224Z"
---
:orphan:

# Setup for ORM Queryguide: Single Inheritance

This page illustrates the mappings and fixture data used by the
:ref:`single_inheritance` examples in the :doc:`inheritance` document of
the :ref:`queryguide_toplevel`.

**sourcecode:** python


    >>> from sqlalchemy import create_engine
    >>> from sqlalchemy import ForeignKey
    >>> from sqlalchemy.orm import DeclarativeBase
    >>> from sqlalchemy.orm import Mapped
    >>> from sqlalchemy.orm import mapped_column
    >>> from sqlalchemy.orm import relationship
    >>> from sqlalchemy.orm import Session
### >>>
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
### ...     }
    >>> engine = create_engine("sqlite://", echo=True)
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
