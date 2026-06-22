---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.enableAutoMerger.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================================

# sh.enableAutoMerger() (mongosh method)

## Definition

.. versionadded:: 7.0

.. include:: /includes/enableAutoMerger.rst

`sh.enableAutoMerger()` is a :binary:`~bin.mongosh` helper method. It is effectively the same as running the :dbcommand:`configureCollectionBalancing` command with the `enableAutoMerger` field set to `true`.

.. include:: /includes/fact-mongosh-shell-method-alt.rst

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

```javascript
sh.enableAutoMerger( <namespace> )
```

## Method Field

.. include:: /includes/auto-merger-namespace-field.rst

## Behavior

.. include:: /includes/auto-merger-time-parameters.rst

## Example

The following example enables automatic chunk merges for `"testDatabase.myCollection"`. Run the example from :binary:`~bin.mongos`:

```javascript
sh.enableAutoMerger( "testDatabase.myCollection" )
```

## Learn More

- `automerger-concept`
- :method:`sh.disableAutoMerger()` method
- :method:`sh.startAutoMerger()` method
- :method:`sh.stopAutoMerger()` method
.. include:: /includes/auto-merger-learn-more.rst
