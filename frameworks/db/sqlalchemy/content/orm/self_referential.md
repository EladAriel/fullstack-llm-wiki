---
type: "Framework Learn Page"
framework: "sqlalchemy"
source_repo: "https://github.com/sqlalchemy/sqlalchemy"
source_branch: "main"
source_path: "doc/build/orm/self_referential.rst"
source_commit: "ddf3b6589fd6ccb2affbaea5d4f400a8c1ad02d8"
source_commit_short: "ddf3b658"
source_commit_date: "2026-06-18T14:12:36-04:00"
generated_at: "2026-06-21T07:22:30Z"
---

## Adjacency List Relationships

The **adjacency list** pattern is a common relational pattern whereby a table contains a foreign key reference to itself, in other words is a **self referential relationship**. This is the most common way to represent hierarchical data in flat tables.  Other methods include **nested sets**, sometimes called "modified preorder", as well as **materialized path**.  Despite the appeal that modified preorder has when evaluated for its fluency within SQL queries, the adjacency list model is probably the most appropriate pattern for the large majority of hierarchical storage needs, for reasons of concurrency, reduced complexity, and that modified preorder has little advantage over an application which can fully load subtrees into the application space.

> **Seealso:**  This section details the single-table version of a self-referential
 relationship. For a self-referential relationship that uses a second table
 as an association table, see the section
 `self_referential_many_to_many`.

In this example, we'll work with a single mapped class called `Node`, representing a tree structure:

```
class Node(Base):
    __tablename__ = "node"
    id = mapped_column(Integer, primary_key=True)
    parent_id = mapped_column(Integer, ForeignKey("node.id"))
    data = mapped_column(String(50))
    children = relationship("Node")
```

With this structure, a graph such as the following:

```text
 root --+---> child1
        +---> child2 --+--> subchild1
        |              +--> subchild2
        +---> child3
```

Would be represented with data such as:

```text
 id       parent_id     data
 ---      -------       ----
 1        NULL          root
 2        1             child1
 3        1             child2
 4        3             subchild1
 5        3             subchild2
 6        1             child3
```

The `_orm.relationship configuration here works in the same way as a "normal" one-to-many relationship, with the exception that the "direction", i.e. whether the relationship is one-to-many or many-to-one, is assumed by default to be one-to-many.   To establish the relationship as many-to-one, an extra directive is added known as orm.relationship.remote_side, which is a schema.Column or collection of schema.Column` objects that indicate those which should be considered to be "remote":

```
class Node(Base):
    __tablename__ = "node"
    id = mapped_column(Integer, primary_key=True)
    parent_id = mapped_column(Integer, ForeignKey("node.id"))
    data = mapped_column(String(50))
    parent = relationship("Node", remote_side=[id])
```

Where above, the `id column is applied as the orm.relationship.remote_side` of the `parent orm.relationship`, thus establishing `parent_id` as the "local" side, and the relationship then behaves as a many-to-one.

As always, both directions can be combined into a bidirectional relationship using two `_orm.relationship constructs linked by orm.relationship.back_populates`:

```
class Node(Base):
    __tablename__ = "node"
    id = mapped_column(Integer, primary_key=True)
    parent_id = mapped_column(Integer, ForeignKey("node.id"))
    data = mapped_column(String(50))
    children = relationship("Node", back_populates="parent")
    parent = relationship("Node", back_populates="children", remote_side=[id])
```

> **Seealso:**  `examples_adjacencylist` - working example, updated for SQLAlchemy 2.0

### Composite Adjacency Lists

A sub-category of the adjacency list relationship is the rare case where a particular column is present on both the "local" and "remote" side of the join condition.  An example is the `Folder` class below; using a composite primary key, the `account_id` column refers to itself, to indicate sub folders which are within the same account as that of the parent; while `folder_id` refers to a specific folder within that account:

```
class Folder(Base):
    __tablename__ = "folder"
    __table_args__ = (
        ForeignKeyConstraint(
            ["account_id", "parent_id"], ["folder.account_id", "folder.folder_id"]
        ),
    )

    account_id = mapped_column(Integer, primary_key=True)
    folder_id = mapped_column(Integer, primary_key=True)
    parent_id = mapped_column(Integer)
    name = mapped_column(String)

    parent_folder = relationship(
        "Folder", back_populates="child_folders", remote_side=[account_id, folder_id]
    )

    child_folders = relationship("Folder", back_populates="parent_folder")
```

Above, we pass `account_id into the orm.relationship.remote_side list. orm.relationship` recognizes that the `account_id` column here is on both sides, and aligns the "remote" column along with the `folder_id` column, which it recognizes as uniquely present on the "remote" side.

### Self-Referential Query Strategies

Querying of self-referential structures works like any other query:

```
# get all nodes named 'child2'
session.scalars(select(Node).where(Node.data == "child2"))
```

However extra care is needed when attempting to join along the foreign key from one level of the tree to the next.  In SQL, a join from a table to itself requires that at least one side of the expression be "aliased" so that it can be unambiguously referred to.

Recall from `orm_queryguide_orm_aliases in the ORM tutorial that the orm.aliased` construct is normally used to provide an "alias" of an ORM entity.  Joining from `Node` to itself using this technique looks like:

```python+sql
 from sqlalchemy.orm import aliased

 nodealias = aliased(Node)
 session.scalars(
     select(Node)
     .where(Node.data == "subchild1")
     .join(Node.parent.of_type(nodealias))
     .where(nodealias.data == "child2")
 ).all()
 {execsql}SELECT node.id AS node_id,
         node.parent_id AS node_parent_id,
         node.data AS node_data
 FROM node JOIN node AS node_1
     ON node.parent_id = node_1.id
 WHERE node.data = ?
     AND node_1.data = ?
 ['subchild1', 'child2']
```

### Configuring Self-Referential Eager Loading

Eager loading of relationships occurs using joins or outerjoins from parent to child table during a normal query operation, such that the parent and its immediate child collection or reference can be populated from a single SQL statement, or a second statement for all immediate child collections. SQLAlchemy's joined and subquery eager loading use aliased tables in all cases when joining to related items, so are compatible with self-referential joining. However, to use eager loading with a self-referential relationship, SQLAlchemy needs to be told how many levels deep it should join and/or query; otherwise the eager load will not take place at all. This depth setting is configured via `.relationships.join_depth`:

```python+sql
 class Node(Base):
     __tablename__ = "node"
     id = mapped_column(Integer, primary_key=True)
     parent_id = mapped_column(Integer, ForeignKey("node.id"))
     data = mapped_column(String(50))
     children = relationship("Node", lazy="joined", join_depth=2)

 session.scalars(select(Node)).all()
 {execsql}SELECT node_1.id AS node_1_id,
         node_1.parent_id AS node_1_parent_id,
         node_1.data AS node_1_data,
         node_2.id AS node_2_id,
         node_2.parent_id AS node_2_parent_id,
         node_2.data AS node_2_data,
         node.id AS node_id,
         node.parent_id AS node_parent_id,
         node.data AS node_data
 FROM node
     LEFT OUTER JOIN node AS node_2
         ON node.id = node_2.parent_id
     LEFT OUTER JOIN node AS node_1
         ON node_2.id = node_1.parent_id
 []
```
