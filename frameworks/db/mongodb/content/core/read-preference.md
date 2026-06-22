---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/read-preference.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============

# Read Preference

.. include:: /includes/introduction-read-preference.rst

Read preference consists of the `read preference mode <read-pref-modes-summary>` and optionally, a `tag set list <replica-set-read-preference-tag-sets>`, and the `maxStalenessSeconds <replica-set-read-preference-max-staleness>` option.

## Read Preference Modes

The following table summarizes the read preference modes:

.. include:: /includes/read-preference-modes-table.rst

For detailed description of the read preference modes, see `replica-set-read-preference-modes`.

> **Seealso:** - `replica-set-read-preference-tag-sets`
- `replica-set-read-preference-max-staleness`

## Behavior

- All read preference modes except :readmode:`primary` may return
stale data because `secondaries <secondary>` replicate operations from the primary in an asynchronous process. [#edge-cases-2-primaries]_ Ensure that your application can tolerate stale data if you choose to use a non-:readmode:`primary` mode.

- Read preference does not affect the visibility of data.
Clients can see the results of writes before they are acknowledged or have propagated to a majority of replica set members. For details, see `/core/read-isolation-consistency-recency`.

- Read preference does not affect
`causal consistency <causal-consistency>`. The `causal consistency guarantees <sessions>` provided by causally consistent sessions for read operations with :readconcern:`"majority"` read concern and write	operations with :writeconcern:`"majority"` write concern hold across all members of the MongoDB deployment.

.. include:: /includes/long-running-secondary-reads-may-terminate.rst

## Read Preference Modes

> **Seealso:** To learn about use cases for specific read preference settings,
see `read-preference-use-cases`.

## Configure Read Preference

When using a MongoDB driver, you can specify the read preference using the driver's read preference API. See the driver :driver:`API documentation </>`. You can also set the read preference when `connecting to the replica set or sharded cluster <connections-read-preference>`. For an example, see `connection string <connections-read-preference>`.

For a given read preference, the MongoDB drivers use the same `member selection logic <replica-set-read-preference-behavior-member-selection>`.

When using :binary:`~bin.mongosh`, see :method:`cursor.readPref()` and :method:`Mongo.setReadPref()`.

## Read Preference and Transactions

.. include:: /includes/extracts/transactions-read-pref.rst

## Additional Considerations

.. include:: /includes/merge-and-read-preference.rst

For :dbcommand:`mapReduce` operations, only "inline" :dbcommand:`mapReduce` operations that do not write data support read preference. Otherwise, :dbcommand:`mapReduce` operations run on the `primary` member.

.. include:: /includes/footnote-two-primaries-edge-cases.rst

## Contents

- Use Cases </core/read-preference-use-cases>
- Tag Sets </core/read-preference-tags>
- Configure Tag Sets </tutorial/configure-replica-set-tag-sets>
- maxStalenessSeconds </core/read-preference-staleness>
