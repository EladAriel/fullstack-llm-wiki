---
type: "Framework Learn Page"
framework: "sqlalchemy"
source_repo: "https://github.com/sqlalchemy/sqlalchemy"
source_branch: "main"
source_path: "doc/build/orm/cascades.rst"
source_commit: "ddf3b6589fd6ccb2affbaea5d4f400a8c1ad02d8"
source_commit_short: "ddf3b658"
source_commit_date: "2026-06-18T14:12:36-04:00"
generated_at: "2026-06-21T07:22:30Z"
---

# Cascades

Mappers support the concept of configurable `cascade` behavior on `sqlalchemy.orm.relationship` constructs.  This refers to how operations performed on a "parent" object relative to a particular `.Session should be propagated to items referred to by that relationship (e.g. "child" objects), and is affected by the orm.relationship.cascade` option.

The default behavior of cascade is limited to cascades of the so-called `cascade_save_update` and `cascade_merge` settings. The typical "alternative" setting for cascade is to add the `cascade_delete` and `cascade_delete_orphan` options; these settings are appropriate for related objects which only exist as long as they are attached to their parent, and are otherwise deleted.

Cascade behavior is configured using the `_orm.relationship.cascade` option on `sqlalchemy.orm.relationship`:

```
class Order(Base):
    __tablename__ = "order"

    items = relationship("Item", cascade="all, delete-orphan")
    customer = relationship("User", cascade="save-update")
```

To set cascades on a backref, the same flag can be used with the `.sqlalchemy.orm.backref` function, which ultimately feeds its arguments back into `sqlalchemy.orm.relationship`:

```
class Item(Base):
    __tablename__ = "item"

    order = relationship(
        "Order", backref=backref("items", cascade="all, delete-orphan")
    )
```

The default value of `_orm.relationship.cascade` is `save-update, merge`. The typical alternative setting for this parameter is either `all` or more commonly `all, delete-orphan`.  The `all` symbol is a synonym for `save-update, merge, refresh-expire, expunge, delete`, and using it in conjunction with `delete-orphan` indicates that the child object should follow along with its parent in all cases, and be deleted once it is no longer associated with that parent.

> **Warning:** cascade setting which may not be desirable when using the
`asyncio_toplevel` extension, as it will expire related objects
more aggressively than is typically appropriate in an explicit IO context.
See the notes at `asyncio_orm_avoid_lazyloads` for further background.

The list of available values which can be specified for the `_orm.relationship.cascade` parameter are described in the following subsections.

## save-update

`save-update` cascade indicates that when an object is placed into a `.Session` via `.Session.add, all the objects associated with it via this orm.relationship` should also be added to that same `.Session`.  Suppose we have an object `user1` with two related objects `address1`, `address2`:

```
>>> user1 = User()
>>> address1, address2 = Address(), Address()
>>> user1.addresses = [address1, address2]
```

If we add `user1` to a `.Session`, it will also add `address1`, `address2` implicitly:

```
>>> sess = Session()
>>> sess.add(user1)
>>> address1 in sess
True
```

`save-update` cascade also affects attribute operations for objects that are already present in a `.Session`.  If we add a third object, `address3` to the `user1.addresses` collection, it becomes part of the state of that `.Session`:

```
>>> address3 = Address()
>>> user1.addresses.append(address3)
>>> address3 in sess
True
```

A `save-update` cascade can exhibit surprising behavior when removing an item from a collection or de-associating an object from a scalar attribute. In some cases, the orphaned objects may still be pulled into the ex-parent's `.Session`; this is so that the flush process may handle that related object appropriately. This case usually only arises if an object is removed from one `.Session` and added to another:

```
>>> user1 = sess1.scalars(select(User).filter_by(id=1)).first()
>>> address1 = user1.addresses[0]
>>> sess1.close()  # user1, address1 no longer associated with sess1
>>> user1.addresses.remove(address1)  # address1 no longer associated with user1
>>> sess2 = Session()
>>> sess2.add(user1)  # ... but it still gets added to the new session,
>>> address1 in sess2  # because it's still "pending" for flush
True
```

The `save-update` cascade is on by default, and is typically taken for granted; it simplifies code by allowing a single call to `.Session.add` to register an entire structure of objects within that `.Session` at once.   While it can be disabled, there is usually not a need to do so.

#### Behavior of save-update cascade with bi-directional relationships

The `save-update cascade takes place **uni-directionally** in the context of a bi-directional relationship, i.e. when using the orm.relationship.back_populates or orm.relationship.backref parameters to create two separate orm.relationship` objects which refer to each other.

An object that's not associated with a `_orm.Session, when assigned to an attribute or collection on a parent object that is associated with a orm.Session, will be automatically added to that same orm.Session. However, the same operation in reverse will not have this effect; an object that's not associated with a orm.Session, upon which a child object that is associated with a orm.Session is assigned, will not result in an automatic addition of that parent object to the orm.Session`.  The overall subject of this behavior is known as "cascade backrefs", and represents a change in behavior that was standardized as of SQLAlchemy 2.0.

To illustrate, given a mapping of `Order` objects which relate bi-directionally to a series of `Item` objects via relationships `Order.items` and `Item.order`:

```
mapper_registry.map_imperatively(
    Order,
    order_table,
    properties={"items": relationship(Item, back_populates="order")},
)

mapper_registry.map_imperatively(
    Item,
    item_table,
    properties={"order": relationship(Order, back_populates="items")},
)
```

If an `Order is already associated with a orm.Session`, and an `Item` object is then created and appended to the `Order.items` collection of that `Order`, the `Item will be automatically cascaded into that same orm.Session`:

```
>>> o1 = Order()
>>> session.add(o1)
>>> o1 in session
True

>>> i1 = Item()
>>> o1.items.append(i1)
>>> o1 is i1.order
True
>>> i1 in session
True
```

Above, the bidirectional nature of `Order.items` and `Item.order` means that appending to `Order.items` also assigns to `Item.order`. At the same time, the `save-update` cascade allowed for the `Item object to be added to the same orm.Session` which the parent `Order` was already associated.

However, if the operation above is performed in the **reverse** direction, where `Item.order` is assigned rather than appending directly to `Order.item, the cascade operation into the orm.Session` will **not** take place automatically, even though the object assignments `Order.items` and `Item.order` will be in the same state as in the previous example:

```
>>> o1 = Order()
>>> session.add(o1)
>>> o1 in session
True

>>> i1 = Item()
>>> i1.order = o1
>>> i1 in order.items
True
>>> i1 in session
False
```

In the above case, after the `Item object is created and all the desired state is set upon it, it should then be added to the orm.Session` explicitly:

```
>>> session.add(i1)
```

In older versions of SQLAlchemy, the save-update cascade would occur bidirectionally in all cases. It was then made optional using an option known as `cascade_backrefs`. Finally, in SQLAlchemy 1.4 the old behavior was deprecated and the `cascade_backrefs` option was removed in SQLAlchemy 2.0. The rationale is that users generally do not find it intuitive that assigning to an attribute on an object, illustrated above as the assignment of `i1.order = o1`, would alter the persistence state of that object `i1 such that it's now pending within a orm.Session`, and there would frequently be subsequent issues where autoflush would prematurely flush the object and cause errors, in those cases where the given object was still being constructed and wasn't in a ready state to be flushed. The option to select between uni-directional and bi-directional behaviors was also removed, as this option created two slightly different ways of working, adding to the overall learning curve of the ORM as well as to the documentation and user support burden.

> **Seealso:**  `change_5150` - background on the change in behavior for
 "cascade backrefs"

## delete

The `delete` cascade indicates that when a "parent" object is marked for deletion, its related "child" objects should also be marked for deletion.   If for example we have a relationship `User.addresses` with `delete` cascade configured:

```
class User(Base):
    # ...

    addresses = relationship("Address", cascade="all, delete")
```

If using the above mapping, we have a `User` object and two related `Address` objects:

```
>>> user1 = sess1.scalars(select(User).filter_by(id=1)).first()
>>> address1, address2 = user1.addresses
```

If we mark `user1` for deletion, after the flush operation proceeds, `address1` and `address2` will also be deleted:

```pycon+sql
 >>> sess.delete(user1)
 >>> sess.commit()
 {execsql}DELETE FROM address WHERE address.id = ?
 ((1,), (2,))
 DELETE FROM user WHERE user.id = ?
 (1,)
 COMMIT
```

Alternatively, if our `User.addresses` relationship does not have `delete` cascade, SQLAlchemy's default behavior is to instead de-associate `address1` and `address2` from `user1` by setting their foreign key reference to `NULL`.  Using a mapping as follows:

```
class User(Base):
    # ...

    addresses = relationship("Address")
```

Upon deletion of a parent `User` object, the rows in `address` are not deleted, but are instead de-associated:

```pycon+sql
 >>> sess.delete(user1)
 >>> sess.commit()
 {execsql}UPDATE address SET user_id=? WHERE address.id = ?
 (None, 1)
 UPDATE address SET user_id=? WHERE address.id = ?
 (None, 2)
 DELETE FROM user WHERE user.id = ?
 (1,)
 COMMIT
```

`cascade_delete` cascade on one-to-many relationships is often combined with `cascade_delete_orphan` cascade, which will emit a DELETE for the related row if the "child" object is deassociated from the parent.  The combination of `delete` and `delete-orphan` cascade covers both situations where SQLAlchemy has to decide between setting a foreign key column to NULL versus deleting the row entirely.

The feature by default works completely independently of database-configured `FOREIGN KEY` constraints that may themselves configure `CASCADE` behavior. In order to integrate more efficiently with this configuration, additional directives described at `passive_deletes` should be used.

> **Warning:** **only** to the use of the `_orm.Session.delete` method to mark
individual ORM instances for deletion within the `unit of work` process.
It does **not** apply to "bulk" deletes, which would be emitted using
the `_sql.delete` construct as illustrated at
`orm_queryguide_update_delete_where`.   See
`orm_queryguide_update_delete_caveats` for additional background.

> **Seealso:**  `passive_deletes`
 `cascade_delete_many_to_many`
 `cascade_delete_orphan`

#### Using delete cascade with many-to-many relationships

The `cascade="all, delete" option works equally well with a many-to-many relationship, one that uses orm.relationship.secondary` to indicate an association table.   When a parent object is deleted, and therefore de-associated with its related objects, the unit of work process will normally delete rows from the association table, but leave the related objects intact. When combined with `cascade="all, delete"`, additional `DELETE` statements will take place for the child rows themselves.

The following example adapts that of `relationships_many_to_many` to illustrate the `cascade="all, delete"` setting on **one** side of the association:

```
association_table = Table(
    "association",
    Base.metadata,
    Column("left_id", Integer, ForeignKey("left.id")),
    Column("right_id", Integer, ForeignKey("right.id")),
)

class Parent(Base):
    __tablename__ = "left"
    id = mapped_column(Integer, primary_key=True)
    children = relationship(
        "Child",
        secondary=association_table,
        back_populates="parents",
        cascade="all, delete",
    )

class Child(Base):
    __tablename__ = "right"
    id = mapped_column(Integer, primary_key=True)
    parents = relationship(
        "Parent",
        secondary=association_table,
        back_populates="children",
    )
```

Above, when a `Parent object is marked for deletion using orm.Session.delete`, the flush process will as usual delete the associated rows from the `association` table, however per cascade rules it will also delete all related `Child` rows.

> **Warning:**  If the above `cascade="all, delete"` setting were configured on **both**
 relationships, then the cascade action would continue cascading through all
 `Parent` and `Child` objects, loading each `children` and `parents`
 collection encountered and deleting everything that's connected.   It is
 typically not desirable for "delete" cascade to be configured
 bidirectionally.

> **Seealso:** `relationships_many_to_many_deletion`
`passive_deletes_many_to_many`

#### Using foreign key ON DELETE cascade with ORM relationships

The behavior of SQLAlchemy's "delete" cascade overlaps with the `ON DELETE` feature of a database `FOREIGN KEY` constraint. SQLAlchemy allows configuration of these schema-level `DDL behaviors using the schema.ForeignKey and schema.ForeignKeyConstraint constructs; usage of these objects in conjunction with schema.Table` metadata is described at `on_update_on_delete`.

In order to use `ON DELETE foreign key cascades in conjunction with orm.relationship, it's important to note first and foremost that the orm.relationship.cascade` setting must still be configured to match the desired "delete" or "set null" behavior (using `delete` cascade or leaving it omitted), so that whether the ORM or the database level constraints will handle the task of actually modifying the data in the database, the ORM will still be able to appropriately track the state of locally present objects that may be affected.

There is then an additional option on `_orm.relationship which indicates the degree to which the ORM should try to run DELETE/UPDATE operations on related rows itself, vs. how much it should rely upon expecting the database-side FOREIGN KEY constraint cascade to handle the task; this is the orm.relationship.passive_deletes` parameter and it accepts options `False` (the default), `True` and `"all"`.

The most typical example is that where child rows are to be deleted when parent rows are deleted, and that `ON DELETE CASCADE` is configured on the relevant `FOREIGN KEY` constraint as well:

```
class Parent(Base):
    __tablename__ = "parent"
    id = mapped_column(Integer, primary_key=True)
    children = relationship(
        "Child",
        back_populates="parent",
        cascade="all, delete",
        passive_deletes=True,
    )

class Child(Base):
    __tablename__ = "child"
    id = mapped_column(Integer, primary_key=True)
    parent_id = mapped_column(Integer, ForeignKey("parent.id", ondelete="CASCADE"))
    parent = relationship("Parent", back_populates="children")
```

The behavior of the above configuration when a parent row is deleted is as follows:

1. The application calls `session.delete(my_parent)`, where `my_parent`
is an instance of `Parent`.

2. When the `_orm.Session` next flushes changes to the database,
all of the **currently loaded** items within the `my_parent.children` collection are deleted by the ORM, meaning a `DELETE` statement is emitted for each record.

3. If the `my_parent.children` collection is **unloaded**, then no `DELETE`
statements are emitted.   If the `_orm.relationship.passive_deletes flag were **not** set on this orm.relationship`, then a `SELECT` statement for unloaded `Child` objects would have been emitted.

4. A `DELETE` statement is then emitted for the `my_parent` row itself.
5. The database-level `ON DELETE CASCADE` setting ensures that all rows in
`child` which refer to the affected row in `parent` are also deleted.

6. The `Parent` instance referred to by `my_parent`, as well as all
instances of `Child` that were related to this object and were **loaded** (i.e. step 2 above took place), are de-associated from the `._orm.Session`.

> **Note:**  To use "ON DELETE CASCADE", the underlying database engine must
 support `FOREIGN KEY` constraints and they must be enforcing:
 * When using MySQL, an appropriate storage engine must be
   selected.  See `mysql_storage_engines` for details.
 * When using SQLite, foreign key support must be enabled explicitly.
   See `sqlite_foreign_keys` for details.

#### Using foreign key ON DELETE with many-to-many relationships

As described at `cascade_delete_many_to_many`, "delete" cascade works for many-to-many relationships as well.  To make use of `ON DELETE CASCADE` foreign keys in conjunction with many to many, `FOREIGN KEY` directives are configured on the association table.   These directives can handle the task of automatically deleting from the association table, but cannot accommodate the automatic deletion of the related objects themselves.

In this case, the `_orm.relationship.passive_deletes` directive can save us some additional `SELECT` statements during a delete operation but there are still some collections that the ORM will continue to load, in order to locate affected child objects and handle them correctly.

> **Note:** Hypothetical optimizations to this could include a single `DELETE`
statement against all parent-associated rows of the association table at
once, then use `RETURNING` to locate affected related child rows, however
this is not currently part of the ORM unit of work implementation.

In this configuration, we configure `ON DELETE CASCADE` on both foreign key constraints of the association table.  We configure `cascade="all, delete"` on the parent->child side of the relationship, and we can then configure `passive_deletes=True` on the **other** side of the bidirectional relationship as illustrated below:

```
association_table = Table(
    "association",
    Base.metadata,
    Column("left_id", Integer, ForeignKey("left.id", ondelete="CASCADE")),
    Column("right_id", Integer, ForeignKey("right.id", ondelete="CASCADE")),
)

class Parent(Base):
    __tablename__ = "left"
    id = mapped_column(Integer, primary_key=True)
    children = relationship(
        "Child",
        secondary=association_table,
        back_populates="parents",
        cascade="all, delete",
    )

class Child(Base):
    __tablename__ = "right"
    id = mapped_column(Integer, primary_key=True)
    parents = relationship(
        "Parent",
        secondary=association_table,
        back_populates="children",
        passive_deletes=True,
    )
```

Using the above configuration, the deletion of a `Parent` object proceeds as follows:

1. A `Parent` object is marked for deletion using
`_orm.Session.delete`.

2. When the flush occurs, if the `Parent.children` collection is not loaded,
the ORM will first emit a SELECT statement in order to load the `Child` objects that correspond to `Parent.children`.

3. It will then then emit `DELETE` statements for the rows in `association`
which correspond to that parent row.

4. for each `Child` object affected by this immediate deletion, because
`passive_deletes=True` is configured, the unit of work will not need to try to emit SELECT statements for each `Child.parents` collection as it is assumed the corresponding rows in `association` will be deleted.

5. `DELETE` statements are then emitted for each `Child` object that was
loaded from `Parent.children`.

## delete-orphan

`delete-orphan` cascade adds behavior to the `delete` cascade, such that a child object will be marked for deletion when it is de-associated from the parent, not just when the parent is marked for deletion.   This is a common feature when dealing with a related object that is "owned" by its parent, with a NOT NULL foreign key, so that removal of the item from the parent collection results in its deletion.

`delete-orphan cascade implies that each child object can only have one parent at a time, and in the **vast majority of cases is configured only on a one-to-many relationship.**   For the much less common case of setting it on a many-to-one or many-to-many relationship, the "many" side can be forced to allow only a single object at a time by configuring the orm.relationship.single_parent` argument, which establishes Python-side validation that ensures the object is associated with only one parent at a time, however this greatly limits the functionality of the "many" relationship and is usually not what's desired.

> **Seealso:** `error_bbf0` - background on a common error scenario involving delete-orphan
cascade.

## merge

`merge` cascade indicates that the `.Session.merge` operation should be propagated from a parent that's the subject of the `.Session.merge` call down to referred objects. This cascade is also on by default.

## refresh-expire

`refresh-expire` is an uncommon option, indicating that the `.Session.expire` operation should be propagated from a parent down to referred objects.   When using `.Session.refresh`, the referred objects are expired only, but not actually refreshed.

## expunge

`expunge` cascade indicates that when the parent object is removed from the `.Session` using `.Session.expunge`, the operation should be propagated down to referred objects.

## Notes on Delete - Deleting Objects Referenced from Collections and Scalar Relationships

The ORM in general never modifies the contents of a collection or scalar relationship during the flush process.  This means, if your class has a `_orm.relationship` that refers to a collection of objects, or a reference to a single object such as many-to-one, the contents of this attribute will not be modified when the flush process occurs.  Instead, it is expected that the `.Session` would eventually be expired, either through the expire-on-commit behavior of `.Session.commit` or through explicit use of `.Session.expire`. At that point, any referenced object or collection associated with that `.Session` will be cleared and will re-load itself upon next access.

A common confusion that arises regarding this behavior involves the use of the `.Session.delete` method.   When `.Session.delete` is invoked upon an object and the `.Session is flushed, the row is deleted from the database.  Rows that refer to the target row via  foreign key, assuming they are tracked using a orm.relationship` between the two mapped object types, will also see their foreign key attributes UPDATED to null, or if delete cascade is set up, the related rows will be deleted as well. However, even though rows related to the deleted object might be themselves modified as well, **no changes occur to relationship-bound collections or object references on the objects** involved in the operation within the scope of the flush itself.   This means if the object was a member of a related collection, it will still be present on the Python side until that collection is expired.  Similarly, if the object were referenced via many-to-one or one-to-one from another object, that reference will remain present on that object until the object is expired as well.

Below, we illustrate that after an `Address` object is marked for deletion, it's still present in the collection associated with the parent `User`, even after a flush:

```
>>> address = user.addresses[1]
>>> session.delete(address)
>>> session.flush()
>>> address in user.addresses
True
```

When the above session is committed, all attributes are expired.  The next access of `user.addresses` will re-load the collection, revealing the desired state:

```
>>> session.commit()
>>> address in user.addresses
False
```

There is a recipe for intercepting `.Session.delete` and invoking this expiration automatically; see [ExpireRelationshipOnFKChange](https://www.sqlalchemy.org/trac/wiki/UsageRecipes/ExpireRelationshipOnFKChange) for this.  However, the usual practice of deleting items within collections is to forego the usage of `.Session.delete` directly, and instead use cascade behavior to automatically invoke the deletion as a result of removing the object from the parent collection.  The `delete-orphan` cascade accomplishes this, as illustrated in the example below:

```
class User(Base):
    __tablename__ = "user"

    # ...

    addresses = relationship("Address", cascade="all, delete-orphan")

# ...

del user.addresses[1]
session.flush()
```

Where above, upon removing the `Address` object from the `User.addresses` collection, the `delete-orphan` cascade has the effect of marking the `Address` object for deletion in the same way as passing it to `.Session.delete`.

The `delete-orphan` cascade can also be applied to a many-to-one or one-to-one relationship, so that when an object is de-associated from its parent, it is also automatically marked for deletion.   Using `delete-orphan cascade on a many-to-one or one-to-one requires an additional flag orm.relationship.single_parent` which invokes an assertion that this related object is not to shared with any other parent simultaneously:

```
class User(Base):
    # ...

    preference = relationship(
        "Preference", cascade="all, delete-orphan", single_parent=True
    )
```

Above, if a hypothetical `Preference` object is removed from a `User`, it will be deleted on flush:

```
some_user.preference = None
session.flush()  # will delete the Preference object
```

> **Seealso:**  `unitofwork_cascades` for detail on cascades.
