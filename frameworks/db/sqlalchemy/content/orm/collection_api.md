---
type: "Framework Learn Page"
framework: "sqlalchemy"
source_repo: "https://github.com/sqlalchemy/sqlalchemy"
source_branch: "main"
source_path: "doc/build/orm/collection_api.rst"
source_commit: "ddf3b6589fd6ccb2affbaea5d4f400a8c1ad02d8"
source_commit_short: "ddf3b658"
source_commit_date: "2026-06-18T14:12:36-04:00"
generated_at: "2026-06-21T07:22:30Z"
---

========================================

# Collection Customization and API Details

The `_orm.relationship` function defines a linkage between two classes. When the linkage defines a one-to-many or many-to-many relationship, it's represented as a Python collection when objects are loaded and manipulated. This section presents additional information about collection configuration and techniques.

## Customizing Collection Access

Mapping a one-to-many or many-to-many relationship results in a collection of values accessible through an attribute on the parent instance.   The two common collection types for these are `list` and `set`, which in `Declarative <orm_declarative_styles_toplevel> mappings that use orm.Mapped is established by using the collection type within the orm.Mapped` container, as demonstrated in the `Parent.children` collection below where `list` is used:

```
from sqlalchemy import ForeignKey

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass

class Parent(Base):
    __tablename__ = "parent"

    parent_id: Mapped[int] = mapped_column(primary_key=True)

    # use a list
    children: Mapped[list["Child"]] = relationship()

class Child(Base):
    __tablename__ = "child"

    child_id: Mapped[int] = mapped_column(primary_key=True)
    parent_id: Mapped[int] = mapped_column(ForeignKey("parent.id"))
```

Or for a `set`, illustrated in the same `Parent.children` collection:

```
from sqlalchemy import ForeignKey

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass

class Parent(Base):
    __tablename__ = "parent"

    parent_id: Mapped[int] = mapped_column(primary_key=True)

    # use a set
    children: Mapped[set["Child"]] = relationship()

class Child(Base):
    __tablename__ = "child"

    child_id: Mapped[int] = mapped_column(primary_key=True)
    parent_id: Mapped[int] = mapped_column(ForeignKey("parent.id"))
```

When using mappings without the `_orm.Mapped` annotation, such as when using `imperative mappings <orm_imperative_mapping> or untyped Python code, as well as in a few special cases, the collection class for a orm.relationship can always be specified directly using the orm.relationship.collection_class` parameter:

```
# non-annotated mapping

class Parent(Base):
    __tablename__ = "parent"

    parent_id = mapped_column(Integer, primary_key=True)

    children = relationship("Child", collection_class=set)

class Child(Base):
    __tablename__ = "child"

    child_id = mapped_column(Integer, primary_key=True)
    parent_id = mapped_column(ForeignKey("parent.id"))
```

In the absence of `_orm.relationship.collection_class or orm.Mapped`, the default collection type is `list`.

Beyond `list` and `set` builtins, there is also support for two varieties of dictionary, described below at `orm_dictionary_collection`. There is also support for any arbitrary mutable sequence type can be set up as the target collection, with some additional configuration steps; this is described in the section `orm_custom_collection`.

### Dictionary Collections

A little extra detail is needed when using a dictionary as a collection. This because objects are always loaded from the database as lists, and a key-generation strategy must be available to populate the dictionary correctly.  The `.attribute_keyed_dict` function is by far the most common way to achieve a simple dictionary collection.  It produces a dictionary class that will apply a particular attribute of the mapped class as a key.   Below we map an `Item` class containing a dictionary of `Note` items keyed to the `Note.keyword` attribute. When using `.attribute_keyed_dict, the orm.Mapped annotation may be typed using the orm.KeyFuncDict` or just plain `dict as illustrated in the following example.   However, the orm.relationship.collection_class` parameter is required in this case so that the `.attribute_keyed_dict` may be appropriately parametrized:

```
from typing import Dict
from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import attribute_keyed_dict
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass

class Item(Base):
    __tablename__ = "item"

    id: Mapped[int] = mapped_column(primary_key=True)

    notes: Mapped[Dict[str, "Note"]] = relationship(
        collection_class=attribute_keyed_dict("keyword"),
        cascade="all, delete-orphan",
    )

class Note(Base):
    __tablename__ = "note"

    id: Mapped[int] = mapped_column(primary_key=True)
    item_id: Mapped[int] = mapped_column(ForeignKey("item.id"))
    keyword: Mapped[str]
    text: Mapped[Optional[str]]

    def __init__(self, keyword: str, text: str):
        self.keyword = keyword
        self.text = text
```

`Item.notes` is then a dictionary:

```
>>> item = Item()
>>> item.notes["a"] = Note("a", "atext")
>>> item.notes
{'a': <__main__.Note object at 0x2eaaf0>}
```

`.attribute_keyed_dict` will ensure that the `.keyword` attribute of each `Note` complies with the key in the dictionary.   Such as, when assigning to `Item.notes`, the dictionary key we supply must match that of the actual `Note` object:

```
item = Item()
item.notes = {
    "a": Note("a", "atext"),
    "b": Note("b", "btext"),
}
```

The attribute which `.attribute_keyed_dict` uses as a key does not need to be mapped at all!  Using a regular Python `@property` allows virtually any detail or combination of details about the object to be used as the key, as below when we establish it as a tuple of `Note.keyword` and the first ten letters of the `Note.text` field:

```
class Item(Base):
    __tablename__ = "item"

    id: Mapped[int] = mapped_column(primary_key=True)

    notes: Mapped[Dict[str, "Note"]] = relationship(
        collection_class=attribute_keyed_dict("note_key"),
        back_populates="item",
        cascade="all, delete-orphan",
    )

class Note(Base):
    __tablename__ = "note"

    id: Mapped[int] = mapped_column(primary_key=True)
    item_id: Mapped[int] = mapped_column(ForeignKey("item.id"))
    keyword: Mapped[str]
    text: Mapped[str]

    item: Mapped["Item"] = relationship(back_populates="notes")

    @property
    def note_key(self):
        return (self.keyword, self.text[0:10])

    def __init__(self, keyword: str, text: str):
        self.keyword = keyword
        self.text = text
```

Above we added a `Note.item relationship, with a bi-directional orm.relationship.back_populates` configuration. Assigning to this reverse relationship, the `Note` is added to the `Item.notes` dictionary and the key is generated for us automatically:

```
>>> item = Item()
>>> n1 = Note("a", "atext")
>>> n1.item = item
>>> item.notes
{('a', 'atext'): <__main__.Note object at 0x2eaaf0>}
```

Other built-in dictionary types include `.column_keyed_dict`, which is almost like `.attribute_keyed_dict except given the schema.Column` object directly:

```
from sqlalchemy.orm import column_keyed_dict

class Item(Base):
    __tablename__ = "item"

    id: Mapped[int] = mapped_column(primary_key=True)

    notes: Mapped[Dict[str, "Note"]] = relationship(
        collection_class=column_keyed_dict(Note.__table__.c.keyword),
        cascade="all, delete-orphan",
    )
```

as well as `.mapped_collection` which is passed any callable function. Note that it's usually easier to use `.attribute_keyed_dict` along with a `@property` as mentioned earlier:

```
from sqlalchemy.orm import mapped_collection

class Item(Base):
    __tablename__ = "item"

    id: Mapped[int] = mapped_column(primary_key=True)

    notes: Mapped[Dict[str, "Note"]] = relationship(
        collection_class=mapped_collection(lambda note: note.text[0:10]),
        cascade="all, delete-orphan",
    )
```

Dictionary mappings are often combined with the "Association Proxy" extension to produce streamlined dictionary views.  See `proxying_dictionaries` and `composite_association_proxy` for examples.

#### Dealing with Key Mutations and back-populating for Dictionary collections

When using `.attribute_keyed_dict`, the "key" for the dictionary is taken from an attribute on the target object.   **Changes to this key are not tracked**.  This means that the key must be assigned towards when it is first used, and if the key changes, the collection will not be mutated. A typical example where this might be an issue is when relying upon backrefs to populate an attribute mapped collection.  Given the following:

```
class A(Base):
    __tablename__ = "a"

    id: Mapped[int] = mapped_column(primary_key=True)

    bs: Mapped[Dict[str, "B"]] = relationship(
        collection_class=attribute_keyed_dict("data"),
        back_populates="a",
    )

class B(Base):
    __tablename__ = "b"

    id: Mapped[int] = mapped_column(primary_key=True)
    a_id: Mapped[int] = mapped_column(ForeignKey("a.id"))
    data: Mapped[str]

    a: Mapped["A"] = relationship(back_populates="bs")
```

Above, if we create a `B()` that refers to a specific `A()`, the back populates will then add the `B()` to the `A.bs` collection, however if the value of `B.data` is not set yet, the key will be `None`:

```
>>> a1 = A()
>>> b1 = B(a=a1)
>>> a1.bs
{None: <test3.B object at 0x7f7b1023ef70>}
```

Setting `b1.data` after the fact does not update the collection:

```
>>> b1.data = "the key"
>>> a1.bs
{None: <test3.B object at 0x7f7b1023ef70>}
```

This can also be seen if one attempts to set up `B()` in the constructor. The order of arguments changes the result:

```
>>> B(a=a1, data="the key")
<test3.B object at 0x7f7b10114280>
>>> a1.bs
{None: <test3.B object at 0x7f7b10114280>}
```

vs:

```
>>> B(data="the key", a=a1)
<test3.B object at 0x7f7b10114340>
>>> a1.bs
{'the key': <test3.B object at 0x7f7b10114340>}
```

If backrefs are being used in this way, ensure that attributes are populated in the correct order using an `__init__` method.

An event handler such as the following may also be used to track changes in the collection as well:

```
from sqlalchemy import event
from sqlalchemy.orm import attributes

@event.listens_for(B.data, "set")
def set_item(obj, value, previous, initiator):
    if obj.a is not None:
        previous = None if previous == attributes.NO_VALUE else previous
        obj.a.bs[value] = obj
        obj.a.bs.pop(previous)
```

## Custom Collection Implementations

You can use your own types for collections as well.  In simple cases, inheriting from `list` or `set`, adding custom behavior, is all that's needed. In other cases, special decorators are needed to tell SQLAlchemy more detail about how the collection operates.

Collections in SQLAlchemy are transparently instrumented. Instrumentation means that normal operations on the collection are tracked and result in changes being written to the database at flush time. Additionally, collection operations can fire events which indicate some secondary operation must take place. Examples of a secondary operation include saving the child item in the parent's `sqlalchemy.orm.session.Session` (i.e. the `save-update` cascade), as well as synchronizing the state of a bi-directional relationship (i.e. a `.backref`).

The collections package understands the basic interface of lists, sets and dicts and will automatically apply instrumentation to those built-in types and their subclasses. Object-derived types that implement a basic collection interface are detected and instrumented via duck-typing:

```python+sql
 class ListLike:
     def __init__(self):
         self.data = []

     def append(self, item):
         self.data.append(item)

     def remove(self, item):
         self.data.remove(item)

     def extend(self, items):
         self.data.extend(items)

     def __iter__(self):
         return iter(self.data)

     def foo(self):
         return "foo"
```

`append`, `remove`, and `extend` are known members of `list, and will be instrumented automatically. _iter__` is not a mutator method and won't be instrumented, and `foo` won't be either.

Duck-typing (i.e. guesswork) isn't rock-solid, of course, so you can be explicit about the interface you are implementing by providing an `__emulates__` class attribute:

```
class SetLike:
    __emulates__ = set

    def __init__(self):
        self.data = set()

    def append(self, item):
        self.data.add(item)

    def remove(self, item):
        self.data.remove(item)

    def __iter__(self):
        return iter(self.data)
```

This class looks similar to a Python `list` (i.e. "list-like") as it has an `append method, but the _emulates__` attribute forces it to be treated as a `set`. `remove` is known to be part of the set interface and will be instrumented.

But this class won't work quite yet: a little glue is needed to adapt it for use by SQLAlchemy. The ORM needs to know which methods to use to append, remove and iterate over members of the collection. When using a type like `list` or `set`, the appropriate methods are well-known and used automatically when present.  However the class above, which only roughly resembles a `set`, does not provide the expected `add` method, so we must indicate to the ORM the method that will instead take the place of the `add` method, in this case using a decorator `@collection.appender`; this is illustrated in the next section.

### Annotating Custom Collections via Decorators

Decorators can be used to tag the individual methods the ORM needs to manage collections. Use them when your class doesn't quite meet the regular interface for its container type, or when you otherwise would like to use a different method to get the job done.

```python
 from sqlalchemy.orm.collections import collection

 class SetLike:
     __emulates__ = set

     def __init__(self):
         self.data = set()

     @collection.appender
     def append(self, item):
         self.data.add(item)

     def remove(self, item):
         self.data.remove(item)

     def __iter__(self):
         return iter(self.data)
```

And that's all that's needed to complete the example. SQLAlchemy will add instances via the `append` method. `remove and _iter__` are the default methods for sets and will be used for removing and iteration. Default methods can be changed as well:

```python+sql
 from sqlalchemy.orm.collections import collection

 class MyList(list):
     @collection.remover
     def zark(self, item):
         # do something special...
         ...

     @collection.iterator
     def hey_use_this_instead_for_iteration(self): ...
```

There is no requirement to be "list-like" or "set-like" at all. Collection classes can be any shape, so long as they have the append, remove and iterate interface marked for SQLAlchemy's use. Append and remove methods will be called with a mapped entity as the single argument, and iterator methods are called with no arguments and must return an iterator.

### Custom Dictionary-Based Collections

The `.KeyFuncDict` class can be used as a base class for your custom types or as a mix-in to quickly add `dict collection support to other classes. It uses a keying function to delegate to _setitem__ and _delitem__`:

```python+sql
 from sqlalchemy.orm.collections import KeyFuncDict

 class MyNodeMap(KeyFuncDict):
     """Holds 'Node' objects, keyed by the 'name' attribute."""

     def __init__(self, *args, **kw):
         super().__init__(keyfunc=lambda node: node.name)
         dict.__init__(self, *args, **kw)
```

When subclassing `.KeyFuncDict, user-defined versions of _setitem__() or _delitem__()` should be decorated with `.collection.internally_instrumented`, **if** they call down to those same methods on `.KeyFuncDict`.  This because the methods on `.KeyFuncDict` are already instrumented - calling them from within an already instrumented call can cause events to be fired off repeatedly, or inappropriately, leading to internal state corruption in rare cases:

```
from sqlalchemy.orm.collections import KeyFuncDict, collection

class MyKeyFuncDict(KeyFuncDict):
    """Use @internally_instrumented when your methods
    call down to already-instrumented methods.

    """

    @collection.internally_instrumented
    def __setitem__(self, key, value, _sa_initiator=None):
        # do something with key, value
        super(MyKeyFuncDict, self).__setitem__(key, value, _sa_initiator)

    @collection.internally_instrumented
    def __delitem__(self, key, _sa_initiator=None):
        # do something with key
        super(MyKeyFuncDict, self).__delitem__(key, _sa_initiator)
```

The ORM understands the `dict` interface just like lists and sets, and will automatically instrument all "dict-like" methods if you choose to subclass `dict` or provide dict-like collection behavior in a duck-typed class. You must decorate appender and remover methods, however- there are no compatible methods in the basic dictionary interface for SQLAlchemy to use by default. Iteration will go through `values()` unless otherwise decorated.

### Instrumentation and Custom Types

Many custom types and existing library classes can be used as a entity collection type as-is without further ado. However, it is important to note that the instrumentation process will modify the type, adding decorators around methods automatically.

The decorations are lightweight and no-op outside of relationships, but they do add unneeded overhead when triggered elsewhere. When using a library class as a collection, it can be good practice to use the "trivial subclass" trick to restrict the decorations to just your usage in relationships. For example:

```python+sql
 class MyAwesomeList(some.great.library.AwesomeList):
     pass

 # ... relationship(..., collection_class=MyAwesomeList)
```

The ORM uses this approach for built-ins, quietly substituting a trivial subclass when a `list`, `set` or `dict` is used directly.

## Collection API

## Collection Internals
