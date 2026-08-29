---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/vectorSearch.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.143636Z"
---
# $vectorSearch (aggregation stage)

**meta:** :description: Perform semantic searches on vector embeddings in Atlas clusters using the `$vectorSearch` aggregation stage.

.. default-domain:: mongodb

## Definition

**expression:** $vectorSearch

   ``$vectorSearch`` performs a semantic search on data in your Atlas
   cluster. 
   
   If you store vector embeddings on your Atlas cluster, you can
   seamlessly index the vector data along with your other collection
   data. You can use the :pipeline:`$vectorSearch` stage to pre-filter
   your data and perform semantic search against the indexed fields. 

   Your vector data must be less than or equal to 8192 dimensions in
   width.

## Compatibility

The ``$vectorSearch`` aggregation pipeline stage is available in the following 
environments:
   
- :atlas:`MongoDB Atlas </>` clusters running version 6.0.11 or later
- :ref:`MongoDB Enterprise <install-mdb-enterprise>` deployments running version 
  8.2 or later with the :ref:`{+k8s-op-short+} <k8s-operator>`
- :ref:`MongoDB Community <install-mdb-community-edition>` deployments running 
  version 8.2 or later 

To learn more, see :atlas:`{+avs+} 
</atlas-vector-search/vector-search-overview/>`. 

## Behavior

Starting in MongoDB 8.0, you can use a ``$vectorSearch`` stage in a
:pipeline:`$unionWith` stage. 

## Limitations

You cannot use a ``$vectorSearch`` stage in a :pipeline:`$facet`
stage or a :pipeline:`$lookup` stage. 

## Learn More

- To learn more about creating {+avs+} indexes, see
  :atlas:`Index Vector Embeddings
  </atlas-vector-search/vector-search-type/>`. 

- To learn more about :pipeline:`$vectorSearch` pipeline stage syntax
  and usage, see :atlas:`Vector Search Queries
  </atlas-vector-search/vector-search-stage/>`.  