---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/configure-replica-set-tag-sets.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================

# Configure Replica Set Tag Sets

A replica set member or members can be configured with :rsconf:`~members[n].tags`:

```javascript
{ "<tag1>": "<string1>", "<tag2>": "<string2>",... }
```

For read operations, you can specify a tag set in the `read preferences <replica-set-read-preference>` to help direct read operations to members that have specific tag(s).

For write operations, you can use the tags to create a custom `write concern <write-concern>`.

## Use Tag Sets in Read Preference

If a replica set member or members are associated with :rsconf:`~members[n].tags`, you can specify a tag set in the `read preference <read-preference>` to target those members. A tag set is an array of documents, where each document contains the tag and value pair(s). The specifications are tried in order until a match is found. Once found, that specification is used to find all eligible matching members.

> **Note:** You cannot specify a tag set when specifying read preference mode
:readmode:`primary`.

For example, a replica set has the following `replica set configuration <replica-set-configuration-document>` (some of the fields have been omitted for brevity):

```javascript
{
   "_id" : "rs0",
   "version" : 1,
   "protocolVersion" : Long(1),
   "writeConcernMajorityJournalDefault" : true,
   "members" : [
       { "_id" : 0, "host" : "mongodb0.example.net:27017", ...,  "tags": { }, ... },
       { "_id" : 1, "host" : "mongodb1.example.net:27017", ...,  "tags": { }, ... },
       { "_id" : 2, "host" : "mongodb2.example.net:27017", ...,  "tags": { }, ... }
   ],
   "settings" : {
      ...
   }
}
```

#. **Add tags to the members.**

Connect :binary:`~bin.mongosh` to the replica set and use :method:`rs.reconfig()` to add tags to the members:

```javascript
   conf = rs.conf();
   conf.members[0].tags = { "dc": "east", "usage": "production" };
   conf.members[1].tags = { "dc": "east", "usage": "reporting" };
   conf.members[2].tags = { "dc": "west", "usage": "production" };
   rs.reconfig(conf);
```

#. **Verify the replica set configuration.**

Run :method:`rs.conf()` to verify the replica set configuration (some of the fields have been omitted for brevity). The :method:`rs.conf()` returns a document similar to the following:

```javascript
   {
      "_id" : "rs0",
      "version" : 2,
      "protocolVersion" : Long(1),
      "writeConcernMajorityJournalDefault" : true,
      "members" : [
         {
             "_id" : 0,
             "host" : "mongodb0.example.net:27017",
             ...
             "tags" : {
                 "dc": "east",
                 "usage": "production"
             },
             ...
         },
         {
             "_id" : 1,
             "host" : "mongodb1.example.net:27017",
             ...
             "tags" : {
                 "dc": "east",
                 "usage": "reporting"
             },
             ...
          },
         {
             "_id" : 2,
             "host" : "mongodb2.example.net:27017",
             ...
             "tags" : {
                 "dc": "west",
                 "usage": "production"
             },
             ...
         }
      ],
      "settings" : {
         ...
      }
   }
```

#. **Specify tag sets in the read preference.**

To direct read operations to the secondaries tagged with a particular tag(s), in the :binary:`~mongo` shell connected to the replica set, you can use the :method:`~cursor.readPref()` method to specify the `read preference mode <read-pref-modes-summary>` and the `tag set <replica-set-read-preference-tag-sets>`. For example,

- To direct read operations to the secondary tagged with both
`"dc": "east"` and `"usage": "production"`, include the following tag set:

```javascript
     db.collection.find({}).readPref( "secondary", [ { "dc": "east", "usage": "production" } ] )

- To direct a read operation to the secondaries tagged with ``"dc":
  "east"``, and if not found, to secondaries tagged with 
  ``"usage": "production"``, include the following tag set:

  .. code-block:: javascript

     db.collection.find({}).readPref( "secondary", [ { "dc": "east"}, { "usage": "production" } ] )

.. seealso::

   :method:`Mongo.setReadPref()`
```

## Custom Multi-Datacenter Write Concerns

If a replica set member or members are associated with :rsconf:`~members[n].tags`, you can configure the replica set's :rsconf:`settings.getLastErrorModes` setting to create a custom write concern.

Given a five member replica set with members in two data centers:

1. a facility `VA` tagged `dc_va`
2. a facility `CA` tagged `dc_ca`
```javascript
{
   "_id" : "rs0",
   "version" : 1,
   "protocolVersion" : Long(1),
   "writeConcernMajorityJournalDefault" : true,
   "members" : [
       { "_id" : 0, "host" : "mongodb0.example.net:27017", ...,  "tags": { }, ... },
       { "_id" : 1, "host" : "mongodb1.example.net:27017", ...,  "tags": { }, ... },
       { "_id" : 2, "host" : "mongodb2.example.net:27017", ...,  "tags": { }, ... }
       { "_id" : 3, "host" : "mongodb3.example.net:27017", ...,  "tags": { }, ... }
       { "_id" : 4, "host" : "mongodb4.example.net:27017", ...,  "tags": { }, ... }
   ],
   "settings" : {
      ...
   }
}
```

#. **Add tags to the replica set members.**

Connect :binary:`~bin.mongosh` to the replica set and use :method:`rs.reconfig()` to add tags to the members:

```javascript
   conf = rs.conf();
   conf.members[0].tags = { "dc_va": "rack1"};
   conf.members[1].tags = { "dc_va": "rack2"};
   conf.members[2].tags = { "dc_ca": "rack1"};
   conf.members[3].tags = { "dc_ca": "rack2"};
   conf.members[4].tags = { "dc_va": "rack1"};
   rs.reconfig(conf);
```

#. **Create a custom write concern.**

In the replica set configuration, define a custom write concern in the :rsconf:`settings.getLastErrorModes` setting. For example, the following defines the custom write concern `MultipleDC` that requires the write to propagate to two members with different `dc_va` tag values and one member with any `dc_ca` tag value.

```javascript
   conf = rs.conf();
   conf.settings = { getLastErrorModes: { MultipleDC : { "dc_va": 2, "dc_ca": 1 } } };
   rs.reconfig(conf);

.. note::

   The ``MultipleDC`` write concern is not satisfied if the write
   propagates to two members with the same ``"dc_va"`` tag. For
   example, if the write has only propagated to ``members[0]`` and
   ``members[4]``, ``"dc_va": 2`` is not satisfied since they have
   the same tag value ``"rack1"``.
```

#. **Use the custom write concern.**

To use the custom write concern, pass in the write concern name to the `wc-w` in the write concern:

```javascript
   db.collection.insertOne(
      { id: "xyz", status: "A" },
      { writeConcern: { w: "MultipleDC", j: true } }
   )
```
