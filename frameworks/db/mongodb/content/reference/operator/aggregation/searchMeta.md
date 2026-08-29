---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/searchMeta.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.204129Z"
---
# $searchMeta (aggregation stage)

**meta:** :description: Explore how `$searchMeta` returns metadata for {+fts+} queries using indexed fields in Atlas collections.

.. default-domain:: mongodb

``searchMeta`` returns different :ref:`types of metadata result 
<fts-metadata-results>` documents for {+fts+} queries on the field 
or fields in an Atlas collection. The fields must be covered by a 
:atlas:`{+fts+} </reference/atlas-search/index-definitions/>` 
index. See:

- :atlas:`Index Definitions
  </reference/atlas-search/index-definitions/>` to learn more about 
  creating and managing {+fts+} indexes.
- :atlas:`{+fts+} Aggregation Pipeline Stages
  </reference/atlas-search/query-syntax/>` to learn more about the 
  ``$searchMeta`` pipeline stage syntax, usage, and results.

**important:** The ``$searchMeta`` aggregation pipeline stage is available for 
   collections hosted on: 
   
   - :atlas:`MongoDB Atlas </>`.
   - :ref:`MongoDB Enterprise <install-mdb-enterprise>` deployments running 
     version 8.2 or later with the :ref:`{+k8s-op-short+} <k8s-operator>`.
   - :ref:`MongoDB Community <install-mdb-community-edition>` deployments 
     running version 8.2 or later.
    
   To learn more, see :atlas:`{+fts+} </atlas-search/>`.

