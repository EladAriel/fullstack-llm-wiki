---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/lookup.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================

# $lookup (aggregation stage)

## Definition

## Compatibility

.. include:: /includes/fact-compatibility.rst

## Syntax

The :pipeline:`$lookup` stage syntax:

```none
{
   $lookup:
     {
       from: <collection to join>,
       localField: <field from the input documents>,
       foreignField: <field from the documents of the "from" collection>,
       let: { <var_1>: <expression>, …, <var_n>: <expression> },
       pipeline: [ <pipeline to run> ],
       as: <output array field>
     }
}
```

The :pipeline:`$lookup` accepts a document with these fields:

### Equality Match with a Single Join Condition

To perform an equality match between a field from the input documents with a field from the documents of the foreign collection, the :pipeline:`$lookup` stage has this syntax:

```none
{
   $lookup:
     {
       from: <collection to join>,
       localField: <field from the input documents>,
       foreignField: <field from the documents of the "from" collection>,
       pipeline: [ <pipeline to run> ],
       as: <output array field>
     }
}
```

> **Note:** In this example, `pipeline` is optional and runs after
the local and foreign equality stage.

The operation corresponds to this pseudo-SQL statement:

```sql
SELECT *, (
   SELECT ARRAY_AGG(*)
   FROM <collection to join>
   WHERE <foreignField> = <collection.localField>
) AS <output array field>
FROM collection;
```

> **Note:** The SQL statements on this page are included for comparison to the
MongoDB aggregation pipeline syntax. The SQL statements aren't
runnable.

For MongoDB examples, see these pages:

- `lookup-single-equality-example`
- `unwind-example`
- `lookup-mergeObjects`
### Join Conditions and Subqueries on a Foreign Collection

MongoDB supports:

- Executing a pipeline on a foreign collection.
- Multiple join conditions.
- Correlated and uncorrelated subqueries.
In MongoDB, an uncorrelated subquery means that every input document will return the same result. A correlated subquery is a `pipeline <lookup-subquery-pipeline>` in a :pipeline:`$lookup` stage that uses the local or `input` collection's fields to return results correlated to each incoming document.

> **Note:** .. include:: /includes/uncorrelated-subquery.rst

MongoDB correlated subqueries are comparable to SQL correlated subqueries, where the inner query references outer query values. An SQL uncorrelated subquery does not reference outer query values.

MongoDB 5.0 also supports `concise correlated subqueries <lookup-syntax-concise-correlated-subquery>`.

To perform correlated and uncorrelated subqueries with two collections, and perform other join conditions besides a single equality match, use this :pipeline:`$lookup` syntax:

```javascript
{
   $lookup:
      {
         from: <foreign collection>,
         let: { <var_1>: <expression>, …, <var_n>: <expression> },
         pipeline: [ <pipeline to run on foreign collection> ],
         as: <output array field>
      }
}
```

The operation corresponds to this pseudo-SQL statement:

```sql
SELECT *, <output array field>
FROM collection
WHERE <output array field> IN (
   SELECT <documents as determined from the pipeline>
   FROM <collection to join>
   WHERE <pipeline>
);
```

See the following examples:

- `lookup-multiple-joins`
- `lookup-uncorrelated-subquery`
### Correlated Subqueries Using Concise Syntax

.. versionadded:: 5.0

Starting in MongoDB 5.0, you can use a concise syntax for a correlated subquery. Correlated subqueries reference document fields from a foreign collection  and the "local" collection on which the :method:`~db.collection.aggregate()` method was run.

The following new concise syntax removes the requirement for an equality match on the foreign and local fields inside of an :query:`$expr` operator:

```javascript
{
   $lookup:
      {
         from: <foreign collection>,
         localField: <field from local collection's documents>,
         foreignField: <field from foreign collection's documents>,
         let: { <var_1>: <expression>, …, <var_n>: <expression> },
         pipeline: [ <pipeline to run> ],
         as: <output array field>
      }
}
```

The operation corresponds to this pseudo-SQL statement:

```sql
SELECT *, <output array field>
FROM localCollection
WHERE <output array field> IN (
   SELECT <documents as determined from the pipeline>
   FROM <foreignCollection>
   WHERE <foreignCollection.foreignField> = <localCollection.localField>
   AND <pipeline match condition>
);
```

See this example:

- `lookup-concise-correlated-subquery`
## Behavior

### Encrypted Collections

Starting in MongoDB 8.1, you can reference multiple encrypted collections in a :pipeline:`$lookup` stage. However, `$lookup` does not support:

- Using an encrypted field as the join field in the `localField` or
`foreignField`.

> **Note:**   For drivers using {+csfle+}, you can use an encrypted field as a join
  field only if you are performing a self-join operation.

- Using any field in an encrypted array. An array is considered as encrypted if
it contains any encrypted elements.

- For example, you can't use any field within the resulting
`as <lookup-subquery-as>` array of the `$lookup` operation, unless you're using {+csfle+} and :pipeline:`$unwind` the `as` field.

### Views and Collation

.. include:: /includes/extracts/views-collation-agg.rst

### Restrictions

You cannot include the :pipeline:`$out` or the :pipeline:`$merge` stage in the :pipeline:`$lookup` stage. That is, when specifying a `pipeline for the foreign collection <lookup-syntax-let-pipeline>`, you cannot include either stage in the `pipeline` field.

```javascript
{
   $lookup:
   {
      from: <collection to join>,
      let: { <var_1>: <expression>, …, <var_n>: <expression> },
      pipeline: [ <pipeline to execute on the foreign collection> ],  // Cannot include $out or $merge
      as: <output array field>
   }
}
```

### {+fts+} Support

Starting in MongoDB 6.0, you can specify the :atlas:`{+fts+} </atlas-search>` :pipeline:`$search` or :pipeline:`$searchMeta` stage in the `$lookup` pipeline to search collections on the Atlas cluster. The :pipeline:`$search` or the :pipeline:`$searchMeta` stage must be the first stage inside the `$lookup` pipeline.

For example, when you `lookup-syntax-let-pipeline` or run `lookup-syntax-concise-correlated-subquery`, you can specify :pipeline:`$search` or :pipeline:`$searchMeta` inside the pipeline as shown below:

To see an example of :pipeline:`$lookup` with :pipeline:`$search`, see the {+fts+} tutorial :atlas:`Run a {+fts+} $search Query Using $lookup </atlas-search/tutorial/lookup-with-search/>`.

### Sharded Collections

Starting in MongoDB 5.1, you can specify `sharded collections <sharding-sharded-cluster>` in the `from` parameter of :pipeline:`$lookup` stages.

Starting in MongoDB 8.0, you can use the `$lookup` stage within a transaction while targeting a sharded collection.

### |sbe-title|

.. include:: /includes/fact-sbe-lookup-overview.rst

For more information, see `agg-lookup-optimization-sbe`.

### Performance Considerations

`$lookup` performance depends on the type of operation performed. Refer to the following table for performance considerations for different `$lookup` operations.

For general performance strategies, see `Indexing Strategies <manual-indexing-strategies>` and `Query Optimization <read-operations-indexing>`.

## Examples
