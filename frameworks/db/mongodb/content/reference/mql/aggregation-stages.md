---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/mql/aggregation-stages.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================

# Aggregation Stages

In the :method:`db.collection.aggregate` and :method:`db.aggregate` methods, `pipeline <aggregation-pipeline>` stages appear in an array. Documents pass through the stages in sequence. In the Atlas UI, arrange pipeline stages with the `aggregation pipeline builder <atlas-ui-agg-pipeline>`.

## db.collection.aggregate() Stages

All stages except the :pipeline:`$out`, :pipeline:`$merge`, :pipeline:`$geoNear`, :pipeline:`$changeStream`, and :pipeline:`$changeStreamSplitLargeEvent` stages can appear multiple times in a pipeline.

.. include:: /includes/extracts/operators-toc-explanation.rst

```javascript
db.collection.aggregate( [ { <stage> }, ... ] )
```

.. include:: /includes/extracts/agg-stages-db.collection.aggregate.rst

To learn about expressions that you can use in pipeline stages, see `operator-ref-landing`.

## db.aggregate() Stages

MongoDB also provides the :method:`db.aggregate` method:

```javascript
db.aggregate( [ { <stage> }, ... ] )
```

.. include:: /includes/extracts/agg-stages-db.aggregate.rst

## Stages Available for Updates

Use the aggregation pipeline for updates in:

.. include:: /includes/table-update-with-aggregation-availability.rst

For updates, the pipeline supports these stages:

.. include:: /includes/list-update-agg-stages.rst

## Contents

- $addFields </reference/operator/aggregation/addFields>
- $bucket </reference/operator/aggregation/bucket>
- $bucketAuto </reference/operator/aggregation/bucketAuto>
- $changeStream </reference/operator/aggregation/changeStream>
- $changeStreamSplitLargeEvent </reference/operator/aggregation/changeStreamSplitLargeEvent>
- $collStats </reference/operator/aggregation/collStats>
- $count </reference/operator/aggregation/count>
- $currentOp </reference/operator/aggregation/currentOp>
- $densify </reference/operator/aggregation/densify>
- $documents </reference/operator/aggregation/documents>
- $facet </reference/operator/aggregation/facet>
- $fill </reference/operator/aggregation/fill>
- $geoNear </reference/operator/aggregation/geoNear>
- $graphLookup </reference/operator/aggregation/graphLookup>
- $group </reference/operator/aggregation/group>
- $indexStats </reference/operator/aggregation/indexStats>
- $limit </reference/operator/aggregation/limit>
- $listClusterCatalog </reference/operator/aggregation/listClusterCatalog>
- $listLocalSessions </reference/operator/aggregation/listLocalSessions>
- $listSampledQueries </reference/operator/aggregation/listSampledQueries>
- $listSearchIndexes </reference/operator/aggregation/listSearchIndexes>
- $listSessions </reference/operator/aggregation/listSessions>
- $lookup </reference/operator/aggregation/lookup>
- $match </reference/operator/aggregation/match>
- $merge </reference/operator/aggregation/merge>
- $out </reference/operator/aggregation/out>
- $planCacheStats </reference/operator/aggregation/planCacheStats>
- $project </reference/operator/aggregation/project>
- $querySettings </reference/operator/aggregation/querySettings>
- $queryStats </reference/operator/aggregation/queryStats>
- $rankFusion </reference/operator/aggregation/rankFusion>
- $redact </reference/operator/aggregation/redact>
- $replaceRoot </reference/operator/aggregation/replaceRoot>
- $replaceWith </reference/operator/aggregation/replaceWith>
- $sample </reference/operator/aggregation/sample>
- $score </reference/operator/aggregation/score>
- $scoreFusion </reference/operator/aggregation/scoreFusion>
- $search </reference/operator/aggregation/search>
- $searchMeta </reference/operator/aggregation/searchMeta>
- $set </reference/operator/aggregation/set>
- $setWindowFields </reference/operator/aggregation/setWindowFields>
- $shardedDataDistribution </reference/operator/aggregation/shardedDataDistribution>
- $skip </reference/operator/aggregation/skip>
- $sort </reference/operator/aggregation/sort>
- $sortByCount </reference/operator/aggregation/sortByCount>
- $unionWith </reference/operator/aggregation/unionWith>
- $unset </reference/operator/aggregation/unset>
- $unwind </reference/operator/aggregation/unwind>
- $vectorSearch </reference/operator/aggregation/vectorSearch>
