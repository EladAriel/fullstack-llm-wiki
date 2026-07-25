---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/planCacheListFilters.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=======================================

# planCacheListFilters (database command)

## Definition

### Query Settings

.. include:: /includes/persistent-query-settings-avoid-index-filters-intro.rst

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.runCommand( 
   { 
     planCacheListFilters: <collection> 
   } 
)
```

## Command Fields

The command has the following fields:

## Required Access

A user must have access that includes the :authaction:`planCacheIndexFilter` action.

## Output

The :dbcommand:`planCacheListFilters` command returns the document with the following form:

```none
{
   "filters" : [
      {
         "query" : <query>
         "sort" : <sort>,
         "projection" : <projection>,
         "collation" : <collation>,
         "indexes" : [
            <index1>,
            ...
         ]
      },
      ...
   ],
   "ok" : 1
}
```

> **Seealso:** - :dbcommand:`planCacheClearFilters`
- :dbcommand:`planCacheSetFilter`
