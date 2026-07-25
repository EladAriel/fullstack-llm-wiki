---
type: "Framework Learn Page"
framework: "sqlalchemy"
source_repo: "https://github.com/sqlalchemy/sqlalchemy"
source_branch: "main"
source_path: "doc/build/core/inspection.rst"
source_commit: "aa1a5575358d3aa14953b04dced02f4763fed2e7"
source_commit_short: "aa1a5575"
source_commit_date: "2026-07-23T18:02:59Z"
generated_at: "2026-07-25T11:50:45Z"
---

# Runtime Inspection API

## Available Inspection Targets

Below is a listing of many of the most common inspection targets.

- `.Connectable (i.e. engine.Engine`,
`_engine.Connection) - returns an reflection.Inspector` object.

- `_expression.ClauseElement` - all SQL expression components, including
`_schema.Table, schema.Column, serve as their own inspection objects, meaning any of these objects passed to sa.inspect` return themselves.

- `object` - an object given will be checked by the ORM for a mapping -
if so, an `.InstanceState` is returned representing the mapped state of the object.  The `.InstanceState` also provides access to per attribute state via the `.AttributeState` interface as well as the per-flush "history" of any attribute via the `.History` object.

> **Seealso:**    `orm_mapper_inspection_instancestate`

- `type` (i.e. a class) - a class given will be checked by the ORM for a
mapping - if so, a `_orm.Mapper` for that class is returned.

> **Seealso:**    `orm_mapper_inspection_mapper`

- mapped attribute - passing a mapped attribute to `_sa.inspect`, such
as `inspect(MyClass.some_attribute)`, returns a `.QueryableAttribute` object, which is the `descriptor` associated with a mapped class. This descriptor refers to a `.MapperProperty`, which is usually an instance of `.ColumnProperty` or `.RelationshipProperty`, via its `.QueryableAttribute.property` attribute.

- `.AliasedClass` - returns an `.AliasedInsp` object.
