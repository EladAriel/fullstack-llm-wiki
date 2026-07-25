---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.disableAutoMerger.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=======================================

# sh.disableAutoMerger() (mongosh method)

## Definition

.. versionadded:: 7.0

.. include:: /includes/disableAutoMerger.rst

`sh.disableAutoMerger()` is a :binary:`~bin.mongosh` helper method. It is effectively the same as running the :dbcommand:`configureCollectionBalancing` command with the `enableAutoMerger` field set to `false`.

.. include:: /includes/fact-mongosh-shell-method-alt.rst

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

```javascript
sh.disableAutoMerger( <namespace> )
```

## Method Field

.. include:: /includes/auto-merger-namespace-field.rst

## Behavior

.. include:: /includes/auto-merger-stop.rst

## Example

The following example disables automatic chunk merges for `"testDatabase.myCollection"`. Run the example from :binary:`~bin.mongos`:

```javascript
sh.disableAutoMerger( "testDatabase.myCollection" )
```

## Learn More

- `automerger-concept`
- :method:`sh.startAutoMerger()` method
- :method:`sh.stopAutoMerger()` method
- :method:`sh.enableAutoMerger()` method
.. include:: /includes/auto-merger-learn-more.rst
