---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.startAutoMerger.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=====================================

# sh.startAutoMerger() (mongosh method)

## Definition

.. versionadded:: 7.0

.. include:: /includes/startAutoMerger.rst

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

```javascript
sh.startAutoMerger()
```

## Behavior

.. include:: /includes/auto-merger-time-parameters.rst

## Example

The following example enables the {+auto-merge-upper+}. Run the example from :binary:`~bin.mongos`:

```javascript
sh.startAutoMerger()
```

## Learn More

- `automerger-concept`
- :method:`sh.stopAutoMerger()` method
- :method:`sh.enableAutoMerger()` method
- :method:`sh.disableAutoMerger()` method
.. include:: /includes/auto-merger-learn-more.rst
