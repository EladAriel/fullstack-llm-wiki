---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/change-stream-pre-and-post-images-additional-information.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Pre- and post-images are not available for a `change stream event <change-stream-output>` if the images were:

- Not enabled on the collection at the time of a document update or
delete operation.

- Removed after the pre- and post-image retention time set in
`expireAfterSeconds`.

- The following example sets `expireAfterSeconds` to `100`
seconds on an entire cluster:

```javascript
    use admin
    db.runCommand( {
       setClusterParameter:
          { changeStreamOptions: {
             preAndPostImages: { expireAfterSeconds: 100 }
          } }
    } )

 .. note:: 

    The :dbcommand:`setClusterParameter` command is not supported in MongoDB 
    Atlas clusters. For information on Atlas support for all commands, see 
    :ref:`unsupported-commands`.

- The following example returns the current ``changeStreamOptions``
 settings, including ``expireAfterSeconds``:

 .. code-block:: javascript

    db.adminCommand( { getClusterParameter: "changeStreamOptions" } )

- Setting ``expireAfterSeconds`` to ``off`` uses the default retention
 policy: pre- and post-images are retained until the corresponding
 change stream events are removed from the :term:`oplog`.

- If a change stream event is removed from the oplog, then the
 corresponding pre- and post-images are also deleted regardless of
 the ``expireAfterSeconds`` pre- and post-image retention time.
```

Additional considerations:

- Enabling pre- and post-images consumes storage space and adds
processing time. Only enable pre- and post-images if you need them.

- Limit the change stream event size to less than 16 mebibytes. To limit
the event size, you can:

- Limit the document size to 8 megabytes. You can request pre- and
post-images simultaneously in the `change stream output <change-stream-output>` if other change stream event fields like `updateDescription` are not large.

- Request only post-images in the change stream output for documents
up to 16 mebibytes if other change stream event fields like `updateDescription` are not large.

- Request only pre-images in the change stream output for documents up
to 16 mebibytes if:

- document updates affect only a small fraction of the document
structure or content, and

- do not cause a `replace` change event. A `replace` event
always includes the post-image.

- To request a pre-image, you set `fullDocumentBeforeChange` to
`required` or `whenAvailable` in :method:`db.collection.watch()`. To request a post-image, you set `fullDocument` using the same method.

- Pre-images are written to the `config.system.preimages`
collection.

- The `config.system.preimages` collection may become large. To
limit the collection size, you can set `expireAfterSeconds` time for the pre-images as shown earlier.

- To monitor the size of `config.system.preimages`, connect to a
shard node on a sharded cluster or a :binary:`~bin.mongod` node on a replica set. Then, run the following commands:

```javascript
    use config
    db.system.preimages.totalSize()
    db.system.preimages.stats()

- Pre-images are removed asynchronously by a background process.
```

> **Important:** .. include:: /includes/downgrade-for-pre-and-post-images.rst

> **Seealso:** - For change stream events and output, see
  `change-stream-output`.
- To watch a collection for changes, see
  :method:`db.collection.watch`.
- For complete examples with the change stream output, see
  `db.collection.watch-change-streams-pre-and-post-images-example`.
