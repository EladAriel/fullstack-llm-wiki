---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/map-reduce.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========

# Map-Reduce

> **Note:** .. include:: /includes/fact-use-aggregation-not-map-reduce.rst

Map-reduce is a data processing paradigm for condensing large volumes of data into aggregated results. To perform map-reduce operations, MongoDB provides the :dbcommand:`mapReduce` database command.

Consider the following map-reduce operation:

.. include:: /images/map-reduce.rst

MongoDB applies the map phase to each input document (the documents in the collection that match the query condition). The map function emits key-value pairs. For keys that have multiple values, MongoDB applies the reduce phase, which collects and condenses the data, and then stores the results in a collection. The output of the reduce function can optionally pass through a finalize function to further process the results.

All map-reduce functions in MongoDB are JavaScript and run within the :binary:`~bin.mongod` process. Map-reduce operations take a single `collection` as input and can apply sorting and limiting before the map stage. :dbcommand:`mapReduce` can return results as a document or write them to a collection.

> **Note:** Map-reduce is unsupported for {+atlas+} Free and Flex clusters.

## Map-Reduce JavaScript Functions

Map-reduce operations use custom JavaScript functions to map values to a key. If a key has multiple values, the operation reduces them to a single object. A map function can emit multiple key-value pairs or none. An optional finalize function can make further modifications to the results.

## Map-Reduce Results

A map-reduce operation can write results to a collection or return them inline. If you write results to a collection, you can run subsequent map-reduce operations against the same input collection that replace, merge, or reduce new results with previous results. See :dbcommand:`mapReduce` and `incremental-map-reduce` for examples.

When returning results inline, the result documents must fit within the :limit:`BSON Document Size` limit of 16 mebibytes. For more limits and restrictions, see :dbcommand:`mapReduce`.

## Sharded Collections

MongoDB supports map-reduce operations on `sharded collections <sharding-background>`.

## Views

.. include:: /includes/extracts/views-unsupported-mapReduce.rst

## Contents

- Sharded Collections </core/map-reduce-sharded-collections>
- Concurrency </core/map-reduce-concurrency>
- Examples </tutorial/map-reduce-examples>
- Perform with Increments </tutorial/perform-incremental-map-reduce>
- Troubleshoot Map </tutorial/troubleshoot-map-function>
- Troubleshoot Reduce </tutorial/troubleshoot-reduce-function>
- Aggregation Pipeline </reference/map-reduce-to-aggregation-pipeline>
