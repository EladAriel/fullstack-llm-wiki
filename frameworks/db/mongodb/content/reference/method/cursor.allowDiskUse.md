---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/cursor.allowDiskUse.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================================

# cursor.allowDiskUse() (mongosh method)

## Definition

See `sort-index-use` for more information on in-memory sort operations.

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Behavior

### Interaction with `allowDiskUseByDefault`

Starting in MongoDB 6.0, pipeline stages that require more than 100 megabytes of memory to execute write temporary files to disk by default.

> **Note:** Prior to MongoDB 6.0, `.allowDiskUse(false)` and
`.allowDiskUse(true)` have the same effect. In MongoDB 6.0, both
`mongosh` and the legacy `mongo` shell behave the following way:

If :parameter:`allowDiskUseByDefault` is `true` (this is the default):

- `.allowDiskUse()` has no additional effect
- `.allowDiskUse(true)` has no additional effect
- `.allowDiskUse(false)` prohibits the query from writing temporary
files to disk

If :parameter:`allowDiskUseByDefault` is `false`:

- `.allowDiskUse()` enables writing temporary files to disk
- `.allowDiskUse(true)` enables writing temporary files to disk
- `.allowDiskUse(false)` has no additional effect
### Supports Large Non-Indexed Sorts Only

:method:`cursor.allowDiskUse()` has no effect on sort operations answered using an index or non-indexed ("in-memory") sort operations which require less than 100 megabytes of memory. For more complete documentation on in-memory sorts and sort index use, see `sort-index-use`.

To check if MongoDB must perform an in-memory sort, append :method:`cursor.explain()` to the query and check the `explain results <explain-results>`. If the query plan contains a `SORT` stage, then MongoDB must perform an in-memory sort operation subject to the 100 megabyte memory limit.

## Example

Consider a collection `sensors with only the default index on id`. The collection contains documents similar to the following:

```json
{
  "sensor-name" : "TEMP-21425",
  "sensor-location" : "Unit 12",
  "reading" : {
    "timestamp" : Timestamp(1580247215, 1),
    "value" : 212,
    "unit" : "Fahrenheit"
  }
}
```

The following operation includes a :method:`cursor.sort()` on the field `reading.timestamp`. The operation also passes `false` to :method:`cursor.allowDiskUse()` to prohibit the query from writing temporary files to disk.

```javascript
db.sensors.find({"sensor-location" : "Unit 12"}).
  sort({"reading.timestamp" : 1}).
  allowDiskUse(false)
```

Since `reading.timestamp` is not included in an index, MongoDB must perform an in-memory sort operation to return results in the requested sort order. By specifying `cursor.allowDiskUse(false)`, MongoDB cannot process the sort operation if it requires more than 100 megabytes of system memory. If the operation requires more than 100 megabytes of system memory, MongoDB would return an error.
