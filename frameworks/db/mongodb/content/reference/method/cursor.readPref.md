---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/cursor.readPref.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================================

# cursor.readPref() (mongosh method)

## Definition

### Parameters

:method:`~cursor.readPref()` does not support the `replica-set-read-preference-max-staleness` option for read preference.

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Examples

### Specify Read Preference Mode

The following operation uses the read preference `mode <cursor-readpref-mode>` to target the read to a secondary member.

```javascript
db.collection.find({ }).readPref( "secondary")
```

### Specify Read Preference Tag Set

To target secondaries with specific tags, include both the `mode <cursor-readpref-mode>` and the `tagSet <cursor-readpref-tagset>` array:

```javascript
db.collection.find({ }).readPref( 
   "secondary", 
   [ 
      { "datacenter": "B" },    // First, try matching by the datacenter tag
      { "region": "West"},      // If not found, then try matching by the region tag
      { }                       // If not found, then use the empty document to match all eligible members
   ]
)
```

During the secondary selection process, MongoDB tries to find secondary members with the `datacenter: "B"` tag first.

- If found, MongoDB limits the eligible secondaries to those with the
`datacenter: "B"` tag and ignores the remaining tags.

- If none are found, then, MongoDB tries to find secondary members with
the `"region": "West"` tag.

- If found, MongoDB limits the eligible secondaries to those with the
`"region": "West"` tag.

- If none are found, MongoDB uses any eligible secondaries.
See `read-pref-order-matching` for details.

> **Seealso:** `/tutorial/configure-replica-set-tag-sets`
