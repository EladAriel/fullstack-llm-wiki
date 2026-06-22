---
type: "Framework Learn Page"
framework: "sqlalchemy"
source_repo: "https://github.com/sqlalchemy/sqlalchemy"
source_branch: "main"
source_path: "doc/build/orm/events.rst"
source_commit: "ddf3b6589fd6ccb2affbaea5d4f400a8c1ad02d8"
source_commit_short: "ddf3b658"
source_commit_date: "2026-06-18T14:12:36-04:00"
generated_at: "2026-06-21T07:22:30Z"
---

# ORM Events

The ORM includes a wide variety of hooks available for subscription.

For an introduction to the most commonly used ORM events, see the section `session_events_toplevel`.   The event system in general is discussed at `event_toplevel`.  Non-ORM events such as those regarding connections and low-level statement execution are described in `core_event_toplevel`.

## Session Events

The most basic event hooks are available at the level of the ORM `_orm.Session` object.   The types of things that are intercepted here include:

- **Persistence Operations** - the ORM flush process that sends changes to the
database can be extended using events that fire off at different parts of the flush, to augment or modify the data being sent to the database or to allow other things to happen when persistence occurs.   Read more about persistence events at `session_persistence_events`.

- **Object lifecycle events** - hooks when objects are added, persisted,
deleted from sessions.   Read more about these at `session_lifecycle_events`.

- **Execution Events** - Part of the `2.0 style` execution model, all
SELECT statements against ORM entities emitted, as well as bulk UPDATE and DELETE statements outside of the flush process, are intercepted from the `_orm.Session.execute method using the orm.SessionEvents.do_orm_execute` method.  Read more about this event at `session_execute_events`.

Be sure to read the `session_events_toplevel` chapter for context on these events.

## Mapper Events

Mapper event hooks encompass things that happen as related to individual or multiple `_orm.Mapper objects, which are the central configurational object that maps a user-defined class to a schema.Table object. Types of things which occur at the orm.Mapper` level include:

- **Per-object persistence operations** - the most popular mapper hooks are the
unit-of-work hooks such as `_orm.MapperEvents.before_insert, orm.MapperEvents.after_update, etc.  These events are contrasted to the more coarse grained session-level events such as orm.SessionEvents.before_flush in that they occur within the flush process on a per-object basis; while finer grained activity on an object is more straightforward, availability of orm.Session` features is limited.

- **Mapper configuration events** - the other major class of mapper hooks are
those which occur as a class is mapped, as a mapper is finalized, and when sets of mappers are configured to refer to each other.  These events include `_orm.MapperEvents.instrument_class, orm.MapperEvents.before_mapper_configured and orm.MapperEvents.mapper_configured at the individual orm.Mapper level, and  orm.MapperEvents.before_configured and orm.MapperEvents.after_configured at the level of collections of orm.Mapper` objects.

## Registry Events

Registry event hooks indicate things happening in reference to a particular `_orm.registry.   These include configurational events orm.RegistryEvents.before_configured and orm.RegistryEvents.after_configured, as well as a hook to customize type resolution orm.RegistryEvents.resolve_type_annotation`.

## Instance Events

Instance events are focused on the construction of ORM mapped instances, including when they are instantiated as `transient` objects, when they are loaded from the database and become `persistent` objects, as well as when database refresh or expiration operations occur on the object.

## Attribute Events

Attribute events are triggered as things occur on individual attributes of ORM mapped objects.  These events form the basis for things like `custom validation functions <simple_validators>` as well as `backref handlers <relationships_backref>`.

> **Seealso:** `mapping_attributes_toplevel`

## Query Events

## Instrumentation Events
