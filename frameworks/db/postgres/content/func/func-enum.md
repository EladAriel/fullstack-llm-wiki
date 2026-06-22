---
type: "Framework Learn Page"
framework: "postgres"
source_repo: "https://github.com/postgres/postgres.git"
source_branch: "master"
source_path: "doc/src/sgml/func/func-enum.sgml"
source_commit: "031904048aa22e7c70dc8e9c170e2743f9b0f090"
source_commit_short: "03190404"
source_commit_date: "2026-06-20T18:20:58+09:00"
generated_at: "2026-06-21T07:06:11Z"
---

## Enum Support Functions

For enum types (described in `datatype-enum`), there are several functions that allow cleaner programming without hard-coding particular values of an enum type. These are listed in `functions-enum-table`. The examples assume an enum type created as:

```
CREATE TYPE rainbow AS ENUM ('red', 'orange', 'yellow', 'green', 'blue', 'purple');
```

## Enum Support Functions

Function

Description

Example(s)

enum_first `enum_first` ( `anyenum` ) anyenum

Returns the first value of the input enum type.

`enum_first(null::rainbow)` red

enum_last `enum_last` ( `anyenum` ) anyenum

Returns the last value of the input enum type.

`enum_last(null::rainbow)` purple

enum_range `enum_range` ( `anyenum` ) anyarray

Returns all values of the input enum type in an ordered array.

`enum_range(null::rainbow)` {red,orange,yellow,zwspgreen,blue,purple}

`enum_range` ( `anyenum`, `anyenum` ) anyarray

Returns the range between the two given enum values, as an ordered array. The values must be from the same enum type. If the first parameter is null, the result will start with the first value of the enum type. If the second parameter is null, the result will end with the last value of the enum type.

`enum_range('orange'::rainbow, 'green'::rainbow)` {orange,yellow,green}

`enum_range(NULL, 'green'::rainbow)` {red,orange,zwspyellow,green}

`enum_range('orange'::rainbow, NULL)` {orange,yellow,green,zwspblue,purple}

Notice that except for the two-argument form of `enum_range`, these functions disregard the specific value passed to them; they care only about its declared data type. Either null or a specific value of the type can be passed, with the same result. It is more common to apply these functions to a table column or function argument than to a hardwired type name as used in the examples.
