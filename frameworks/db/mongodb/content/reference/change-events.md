---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/change-events.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

====================

# Change Stream Events

Change streams watch collections, databases, or deployments for changes.

When a change occurs on a watched resource, the change stream returns a change event notification document, with information on the operation and the changes it makes.

## Operation Types

> **Note:** The server might return update operations as replace events when
the replace representation is more concise. If you listen for
update operations, also listen for replace operations.

## Resume Token

Each change event includes an `_id` field, which is a `BSON` object that serves as an identifier for the change stream event. For an example of resuming a change stream by `resumeToken`, see `change-stream-resume`.

## Expanded Events

.. versionadded:: 6.0

Change streams support data definition language (DDL) event notifications, such as `createIndexes <change-event-createIndexes>` and `dropIndexes <change-event-dropIndexes>`. To include expanded events, open a change stream cursor with the `showExpandedEvents` option.

For example:

## Contents

- create </reference/change-events/create>
- createIndexes </reference/change-events/createIndexes>
- delete </reference/change-events/delete>
- drop </reference/change-events/drop>
- dropDatabase </reference/change-events/dropDatabase>
- dropIndexes </reference/change-events/dropIndexes>
- insert </reference/change-events/insert>
- invalidate </reference/change-events/invalidate>
- modify </reference/change-events/modify>
- refineCollectionShardKey </reference/change-events/refineCollectionShardKey>
- rename </reference/change-events/rename>
- replace </reference/change-events/replace>
- reshardCollection </reference/change-events/reshardCollection>
- shardCollection </reference/change-events/shardCollection>
- update </reference/change-events/update>
