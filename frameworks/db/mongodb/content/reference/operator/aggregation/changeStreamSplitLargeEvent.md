---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/changeStreamSplitLargeEvent.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

================================================

# $changeStreamSplitLargeEvent (aggregation stage)

## Definition

New in MongoDB 7.0 (and 6.0.9).

If a `change stream <changeStreams>` has large events that exceed 16 MB, a `BSONObjectTooLarge` exception is returned. Starting in MongoDB 7.0 (and 6.0.9), you can use a `$changeStreamSplitLargeEvent` stage to split the events into smaller fragments.

You should only use `$changeStreamSplitLargeEvent` when strictly necessary. For example, if your application requires full document pre- or post-images, and generates large events that exceed 16 MB, use `$changeStreamSplitLargeEvent`.

Before you decide to use `$changeStreamSplitLargeEvent`, you should first try to reduce the change event size. For example:

- Don't request document pre- or post-images unless your application
requires them. This generates `fullDocument` and `fullDocumentBeforeChange` fields in more cases, which are typically the largest objects in a change event.

- Use a :pipeline:`$project` stage to include only the fields necessary
for your application. This reduces the change event size and avoids the additional time to split large events into fragments. This allows more change events to be returned in each batch.

You can only have one `$changeStreamSplitLargeEvent` stage in your pipeline, and it must be the last stage. You can only use `$changeStreamSplitLargeEvent` in a `$changeStream` pipeline.

`$changeStreamSplitLargeEvent` syntax:

```javascript
{
  $changeStreamSplitLargeEvent: {}
}
```

## Behavior

`$changeStreamSplitLargeEvent` splits events that exceed 16 MB into fragments and returns the fragments sequentially using the change stream cursor.

The fragments are split so that the maximum number of fields are returned in the first fragment. This ensures the event context is returned as quickly as possible.

When the change event is split, only the size of top-level fields are used. `$changeStreamSplitLargeEvent` does not recursively process or split subdocuments. For example, if you use a `$project` stage to create a change event with a single field that is 20 MB in size, the event is not split and the stage returns an error.

Each fragment has a resume token. A stream that is resumed using a fragment's token will either:

- Begin a new stream from the subsequent fragment.
- Start at the next event if resuming from the final fragment in the
sequence.

Each fragment for an event includes a `splitEvent` document:

```javascript
splitEvent: {
   fragment: <int>,
   of: <int>
}
```

The following table describes the fields.

## Examples

## Learn More

For more information on change stream notifications, see `Change Events <change-events>`.

To learn more about related pipeline stages, see the :pipeline:`$changeStream` guide.
