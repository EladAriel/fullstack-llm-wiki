---
type: "Framework Learn Page"
framework: "pymongo"
source_repo: "https://github.com/mongodb/mongo-python-driver"
source_branch: "master"
source_path: "doc/migrate-to-pymongo4.rst"
source_commit: "1215d2f467d91038cd97a06dc043b74cf3a3edf1"
source_commit_short: "1215d2f4"
source_commit_date: "2026-06-18T10:29:26-04:00"
generated_at: "2026-06-21T11:44:03Z"
---

:orphan:

# PyMongo 4 Migration Guide

PyMongo 4.0 brings a number of improvements as well as some backward breaking changes. This guide provides a roadmap for migrating an existing application from PyMongo 3.x to 4.x or writing libraries that will work with both PyMongo 3.x and 4.x.

## PyMongo 3

The first step in any successful migration involves upgrading to, or requiring, at least that latest version of PyMongo 3.x. If your project has a requirements.txt file, add the line "pymongo >= 3.12, < 4.0" until you have completely migrated to PyMongo 4. Most of the key new methods and options from PyMongo 4.0 are backported in PyMongo 3.12 making migration much easier.

> **Note:** to PyMongo 3.x by following the `PyMongo 3 Migration Guide
<https://pymongo.readthedocs.io/en/3.12.1/migrate-to-pymongo3.html>`_.

## Python 3.6+

PyMongo 4.0 drops support for Python 2.7, 3.4, and 3.5. Users who wish to upgrade to 4.x must first upgrade to Python 3.6.2+. Users upgrading from Python 2 should consult [Python 3](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/reference/upgrade/#upgrade-pymongo-versions).

## Enable Deprecation Warnings

`DeprecationWarning` is raised by most methods removed in PyMongo 4.0. Make sure you enable runtime warnings to see where deprecated functions and methods are being used in your application:

```
python -Wd <your application>
```

Warnings can also be changed to errors:

```
python -Wd -Werror <your application>
```

> **Note:** used. See Removed features with no migration path.

## MongoReplicaSetClient

Removed `pymongo.mongo_replica_set_client.MongoReplicaSetClient`. Since PyMongo 3.0, `MongoReplicaSetClient` has been identical to `pymongo.mongo_client.MongoClient`. Applications can simply replace `MongoReplicaSetClient` with `pymongo.mongo_client.MongoClient` and get the same behavior.

## MongoClient

`directConnection` defaults to False ......................................

`directConnection` URI option and keyword argument to `pymongo .mongo_client.MongoClient` defaults to `False` instead of `None`, allowing for the automatic discovery of replica sets. This means that if you want a direct connection to a single server you must pass `directConnection=True` as a URI option or keyword argument.

If you see any `pymongo.errors.ServerSelectionTimeoutError`'s after upgrading from PyMongo 3 to 4.x, you likely need to add `directConnection=True` when creating the client. Here are some example errors:

```
     pymongo.errors.ServerSelectionTimeoutError: mongo_node2: [Errno 8] nodename nor servname
     provided, or not known,mongo_node1:27017
```

```
     ServerSelectionTimeoutError: No servers match selector "Primary()", Timeout: 30s,
     Topology Description: ...
```

Additionally, the "isWritablePrimary" attribute of a hello command sent back by the server will always be True if `directConnection=False`:

```
>>> client.admin.command('hello')['isWritablePrimary']
True
```

The waitQueueMultiple parameter is removed ..........................................

Removed the `waitQueueMultiple` keyword argument to `pymongo.mongo_client.MongoClient` and removed `pymongo.errors.ExceededMaxWaiters`. Instead of using `waitQueueMultiple` to bound queuing, limit the size of the thread pool in your application.

The socketKeepAlive parameter is removed ..........................................

Removed the `socketKeepAlive` keyword argument to `pymongo.mongo_client.MongoClient`. PyMongo now always enables TCP keepalive. For more information see the [documentation](https://mongodb.com/docs/manual/faq/diagnostics/#does-tcp-keepalive-time-affect-mongodb-deployments-).

Renamed URI options ...................

Several deprecated URI options have been renamed to the standardized option names defined in the [URI options specification](https://github.com/mongodb/specifications/blob/master/source/uri-options/uri-options.md). The old option names and their renamed equivalents are summarized in the table below. Some renamed options have different semantics from the option being replaced as noted in the 'Migration Notes' column.

+--------------------+-------------------------------+--------------------------------------------------------+ | Old URI Option     | Renamed URI Option            | Migration Notes                                        | +====================+===============================+========================================================+ | ssl_pem_passphrase | tlsCertificateKeyFilePassword | -                                                      | +--------------------+-------------------------------+--------------------------------------------------------+ | ssl_ca_certs       | tlsCAFile                     | -                                                      | +--------------------+-------------------------------+--------------------------------------------------------+ | ssl_crlfile        | tlsCRLFile                    | -                                                      | +--------------------+-------------------------------+--------------------------------------------------------+ | ssl_match_hostname | tlsAllowInvalidHostnames      | `ssl_match_hostname=True` is equivalent to           | |                    |                               | `tlsAllowInvalidHostnames=False` and vice-versa.     | +--------------------+-------------------------------+--------------------------------------------------------+ | ssl_cert_reqs      | tlsAllowInvalidCertificates   | Instead of `ssl.CERT_NONE`, `ssl.CERT_OPTIONAL`    | |                    |                               | and `ssl.CERT_REQUIRED`, the new option expects      | |                    |                               | a boolean value - `True` is equivalent to            | |                    |                               | `ssl.CERT_NONE`, while `False` is equivalent to    | |                    |                               | `ssl.CERT_REQUIRED`.                                 | +--------------------+-------------------------------+--------------------------------------------------------+ | ssl_certfile       | tlsCertificateKeyFile         | Instead of using `ssl_certfile` and `ssl_keyfile`  | |                    |                               | to specify the certificate and private key files       | +--------------------+                               | respectively,  use `tlsCertificateKeyFile` to pass   | | ssl_keyfile        |                               | a single file containing both the client certificate   | |                    |                               | and the private key.                                   | +--------------------+-------------------------------+--------------------------------------------------------+ | j                  | journal                       | -                                                      | +--------------------+-------------------------------+--------------------------------------------------------+ | wtimeout           | wTimeoutMS                    | -                                                      | +--------------------+-------------------------------+--------------------------------------------------------+

MongoClient.fsync is removed ............................

Removed `pymongo.mongo_client.MongoClient.fsync`. Run the fsync command directly with `pymongo.database.Database.command` instead. For example:

```
client.admin.command('fsync', lock=True)
```

MongoClient.unlock is removed .............................

Removed `pymongo.mongo_client.MongoClient.unlock`. Run the fsyncUnlock command directly with `pymongo.database.Database.command` instead. For example:

```
 client.admin.command('fsyncUnlock')
```

MongoClient.is_locked is removed ................................

Removed `pymongo.mongo_client.MongoClient.is_locked`. Run the currentOp command directly with `pymongo.database.Database.command` instead. For example:

```
is_locked = client.admin.command('currentOp').get('fsyncLock')
```

MongoClient.database_names is removed .....................................

Removed `pymongo.mongo_client.MongoClient.database_names`. Use `pymongo.mongo_client.MongoClient.list_database_names` instead. Code like this:

```
names = client.database_names()
```

can be changed to this:

```
names = client.list_database_names()
```

MongoClient.max_bson_size/max_message_size/max_write_batch_size are removed ...........................................................................

Removed `pymongo.mongo_client.MongoClient.max_bson_size`, `pymongo.mongo_client.MongoClient.max_message_size`, and `pymongo.mongo_client.MongoClient.max_write_batch_size`. These helpers were incorrect when in `loadBalanced=true mode` and ambiguous in clusters with mixed versions. Use the hello command to get the authoritative value from the remote server instead. Code like this:

```
max_bson_size = client.max_bson_size
max_message_size = client.max_message_size
max_write_batch_size = client.max_write_batch_size
```

can be changed to this:

```
doc = client.admin.command('hello')
max_bson_size = doc['maxBsonObjectSize']
max_message_size = doc['maxMessageSizeBytes']
max_write_batch_size = doc['maxWriteBatchSize']
```

MongoClient.event_listeners and other configuration option helpers are removed ..............................................................................

The following client configuration option helpers are removed:

- `pymongo.mongo_client.MongoClient.event_listeners`.
- `pymongo.mongo_client.MongoClient.max_pool_size`.
- `pymongo.mongo_client.MongoClient.max_idle_time_ms`.
- `pymongo.mongo_client.MongoClient.local_threshold_ms`.
- `pymongo.mongo_client.MongoClient.server_selection_timeout`.
- `pymongo.mongo_client.MongoClient.retry_writes`.
- `pymongo.mongo_client.MongoClient.retry_reads`.
These helpers have been replaced by `pymongo.mongo_client.MongoClient.options`. Code like this:

```
client.event_listeners
client.local_threshold_ms
client.server_selection_timeout
client.max_pool_size
client.min_pool_size
client.max_idle_time_ms
```

can be changed to this:

```
client.options.event_listeners
client.options.local_threshold_ms
client.options.server_selection_timeout
client.options.pool_options.max_pool_size
client.options.pool_options.min_pool_size
client.options.pool_options.max_idle_time_seconds
```

`tz_aware` defaults to `False` ..................................

The `tz_aware` argument to `bson.json_util.JSONOptions` now defaults to `False` instead of `True`. `bson.json_util.loads` now decodes datetime as naive by default:

```
>>> from bson import json_util
>>> s = '{"dt": {"$date": "2022-05-09T17:54:00Z"}}'
>>> json_util.loads(s)
{'dt': datetime.datetime(2022, 5, 9, 17, 54)}
```

To retain the PyMongo 3 behavior set `tz_aware=True`, for example:

```
>>> from bson import json_util
>>> opts = json_util.JSONOptions(tz_aware=True)
>>> s = '{"dt": {"$date": "2022-05-09T17:54:00Z"}}'
>>> json_util.loads(s, json_options=opts)
{'dt': datetime.datetime(2022, 5, 9, 17, 54, tzinfo=<bson.tz_util.FixedOffset object at 0x7fd1ebc1add0>)}
```

This change was made to match the default behavior of `bson.codec_options.CodecOptions` and `bson.decode`.

MongoClient cannot execute operations after `close()` .......................................................

`pymongo.mongo_client.MongoClient` cannot execute any operations after being closed. The previous behavior would simply reconnect. However, now you must create a new instance.

MongoClient raises exception when given more than one URI .........................................................

`pymongo.mongo_client.MongoClient` now raises a `pymongo.errors.ConfigurationError` when more than one URI is passed into the `hosts` argument.

MongoClient raises exception when given unescaped percent sign in login info ............................................................................

`pymongo.mongo_client.MongoClient` now raises an `pymongo.errors.InvalidURI` exception when it encounters unescaped percent signs in username and password.

## Database

Database.authenticate and Database.logout are removed .....................................................

Removed `pymongo.database.Database.authenticate` and `pymongo.database.Database.logout`. Authenticating multiple users on the same client conflicts with support for logical sessions in MongoDB 3.6+. To authenticate as multiple users, create multiple instances of `pymongo.mongo_client.MongoClient`. Code like this:

```
client = MongoClient()
client.admin.authenticate('user1', 'pass1')
client.admin.authenticate('user2', 'pass2')
```

can be changed to this:

```
client1 = MongoClient(username='user1', password='pass1')
client2 = MongoClient(username='user2', password='pass2')
```

Alternatively, create a single user that contains all the authentication privileges required by your application.

Database.collection_names is removed ....................................

Removed `pymongo.database.Database.collection_names`. Use `pymongo.database.Database.list_collection_names` instead. Code like this:

```
names = client.db.collection_names()
non_system_names = client.db.collection_names(include_system_collections=False)
```

can be changed to this:

```
names = client.db.list_collection_names()
non_system_names = client.db.list_collection_names(filter={"name": {"$regex": "^(?!system\\.)"}})
```

Database.current_op is removed ..............................

Removed `pymongo.database.Database.current_op`. Use `pymongo.database.Database.aggregate` instead with the $currentOp aggregation pipeline stage. Code like this:

```
ops = client.admin.current_op()['inprog']
```

can be changed to this:

```
ops = list(client.admin.aggregate([{'$currentOp': {}}]))
```

Database.add_user is removed ............................

Removed `pymongo.database.Database.add_user`  which was deprecated in PyMongo 3.6. Use the createUser command or updateUser command instead. To create a user:

```
db.command("createUser", "admin", pwd="password", roles=["dbAdmin"])
```

To create a read-only user:

```
db.command("createUser", "user", pwd="password", roles=["read"])
```

To change a password:

```
db.command("updateUser", "user", pwd="newpassword")
```

Or change roles:

```
db.command("updateUser", "user", roles=["readWrite"])
```

Database.remove_user is removed ...............................

Removed `pymongo.database.Database.remove_user` which was deprecated in PyMongo 3.6. Use the dropUser command instead:

```
db.command("dropUser", "user")
```

Database.profiling_level is removed ...................................

Removed `pymongo.database.Database.profiling_level` which was deprecated in PyMongo 3.12. Use the profile command instead. Code like this:

```
level = db.profiling_level()
```

Can be changed to this:

```
profile = db.command('profile', -1)
level = profile['was']
```

Database.set_profiling_level is removed .......................................

Removed `pymongo.database.Database.set_profiling_level` which was deprecated in PyMongo 3.12. Use the profile command instead. Code like this:

```
db.set_profiling_level(pymongo.ALL, filter={'op': 'query'})
```

Can be changed to this:

```
res = db.command('profile', 2, filter={'op': 'query'})
```

Database.profiling_info is removed ..................................

Removed `pymongo.database.Database.profiling_info` which was deprecated in PyMongo 3.12. Query the 'system.profile' collection instead. Code like this:

```
profiling_info = db.profiling_info()
```

Can be changed to this:

```
profiling_info = list(db['system.profile'].find())
```

Database.__bool__ raises NotImplementedError ............................................ `pymongo.database.Database` now raises an error upon evaluating as a Boolean. Code like this:

```
if database:
```

Can be changed to this:

```
if database is not None:
```

You must now explicitly compare with None.

## Collection

The useCursor option for Collection.aggregate is removed ........................................................

Removed the `useCursor` option for `pymongo.collection.Collection.aggregate` which was deprecated in PyMongo 3.6. The option was only necessary when upgrading from MongoDB 2.4 to MongoDB 2.6.

Collection.insert is removed ............................

Removed `pymongo.collection.Collection.insert`. Use `pymongo.collection.Collection.insert_one` or `pymongo.collection.Collection.insert_many` instead.

Code like this:

```
collection.insert({'doc': 1})
collection.insert([{'doc': 2}, {'doc': 3}])
```

Can be changed to this:

```
collection.insert_one({'my': 'document'})
collection.insert_many([{'doc': 2}, {'doc': 3}])
```

Collection.save is removed ..........................

Removed `pymongo.collection.Collection.save`. Applications will get better performance using `pymongo.collection.Collection.insert_one` to insert a new document and `pymongo.collection.Collection.update_one` to update an existing document. Code like this:

```
doc = collection.find_one({"_id": "some id"})
doc["some field"] = <some value>
db.collection.save(doc)
```

Can be changed to this:

```
result = collection.update_one({"_id": "some id"}, {"$set": {"some field": <some value>}})
```

If performance is not a concern and refactoring is untenable, `save` can be implemented like so:

```
def save(doc):
  if '_id' in doc:
      collection.replace_one({'_id': doc['_id']}, doc, upsert=True)
      return doc['_id']
  else:
      res = collection.insert_one(doc)
      return res.inserted_id
```

Collection.update is removed ............................

Removed `pymongo.collection.Collection.update`. Use `pymongo.collection.Collection.update_one` to update a single document or `pymongo.collection.Collection.update_many` to update multiple documents. Code like this:

```
collection.update({}, {'$set': {'a': 1}})
collection.update({}, {'$set': {'b': 1}}, multi=True)
```

Can be changed to this:

```
collection.update_one({}, {'$set': {'a': 1}})
collection.update_many({}, {'$set': {'b': 1}})
```

Collection.remove is removed ............................

Removed `pymongo.collection.Collection.remove`. Use `pymongo.collection.Collection.delete_one` to delete a single document or `pymongo.collection.Collection.delete_many` to delete multiple documents. Code like this:

```
collection.remove({'a': 1}, multi=False)
collection.remove({'b': 1})
```

Can be changed to this:

```
collection.delete_one({'a': 1})
collection.delete_many({'b': 1})
```

Collection.find_and_modify is removed .....................................

Removed `pymongo.collection.Collection.find_and_modify`. Use `pymongo.collection.Collection.find_one_and_update`, `pymongo.collection.Collection.find_one_and_replace`, or `pymongo.collection.Collection.find_one_and_delete` instead. Code like this:

```
updated_doc = collection.find_and_modify({'a': 1}, {'$set': {'b': 1}})
replaced_doc = collection.find_and_modify({'b': 1}, {'c': 1})
deleted_doc = collection.find_and_modify({'c': 1}, remove=True)
```

Can be changed to this:

```
updated_doc = collection.find_one_and_update({'a': 1}, {'$set': {'b': 1}})
replaced_doc = collection.find_one_and_replace({'b': 1}, {'c': 1})
deleted_doc = collection.find_one_and_delete({'c': 1})
```

Collection.count and Cursor.count is removed ............................................

Removed `pymongo.collection.Collection.count` and `pymongo.cursor.Cursor.count`. Use `pymongo.collection.Collection.count_documents` or `pymongo.collection.Collection.estimated_document_count` instead. Code like this:

```
ntotal = collection.count({})
nmatched = collection.count({'price': {'$gte': 10}})
# Or via the Cursor.count api:
ntotal = collection.find({}).count()
nmatched = collection.find({'price': {'$gte': 10}}).count()
```

Can be changed to this:

```
ntotal = collection.estimated_document_count()
nmatched = collection.count_documents({'price': {'$gte': 10}})
```

> **Note:** the following query operators must be replaced:
+-------------+--------------------------------------------------------------+
| Operator    | Replacement                                                  |
+=============+==============================================================+
| $where      | $expr                                                     |
+-------------+--------------------------------------------------------------+
| $near       | $geoWithin with $center; i.e.                          |
|             | `{'$geoWithin': {'$center': [[<x>,<y>], <radius>]}}`       |
+-------------+--------------------------------------------------------------+
| $nearSphere | $geoWithin with $centerSphere; i.e.                    |
|             | `{'$geoWithin': {'$centerSphere': [[<x>,<y>], <radius>]}}` |
+-------------+--------------------------------------------------------------+

Collection.initialize_ordered_bulk_op and initialize_unordered_bulk_op is removed .................................................................................

Removed `pymongo.collection.Collection.initialize_ordered_bulk_op` and `pymongo.bulk.BulkOperationBuilder`. Use `pymongo.collection.Collection.bulk_write` instead. Code like this:

```
batch = coll.initialize_ordered_bulk_op()
batch.insert({'a': 1})
batch.find({'a': 1}).update_one({'$set': {'b': 1}})
batch.find({'a': 2}).upsert().replace_one({'b': 2})
batch.find({'a': 3}).remove()
result = batch.execute()
```

Can be changed to this:

```
coll.bulk_write([
  InsertOne({'a': 1}),
  UpdateOne({'a': 1}, {'$set': {'b': 1}}),
  ReplaceOne({'a': 2}, {'b': 2}, upsert=True),
  DeleteOne({'a': 3}),
])
```

Collection.initialize_unordered_bulk_op is removed ..................................................

Removed `pymongo.collection.Collection.initialize_unordered_bulk_op`. Use `pymongo.collection.Collection.bulk_write` instead. Code like this:

```
batch = coll.initialize_unordered_bulk_op()
batch.insert({'a': 1})
batch.find({'a': 1}).update_one({'$set': {'b': 1}})
batch.find({'a': 2}).upsert().replace_one({'b': 2})
batch.find({'a': 3}).remove()
result = batch.execute()
```

Can be changed to this:

```
coll.bulk_write([
  InsertOne({'a': 1}),
  UpdateOne({'a': 1}, {'$set': {'b': 1}}),
  ReplaceOne({'a': 2}, {'b': 2}, upsert=True),
  DeleteOne({'a': 3}),
], ordered=False)
```

Collection.group is removed ...........................

Removed `pymongo.collection.Collection.group`. This method was deprecated in PyMongo 3.5. MongoDB 4.2 removed the group command. Use `pymongo.collection.Collection.aggregate` with the `$group` stage instead.

Collection.map_reduce and Collection.inline_map_reduce are removed ..................................................................

Removed `pymongo.collection.Collection.map_reduce` and `pymongo.collection.Collection.inline_map_reduce`. Migrate to `pymongo.collection.Collection.aggregate` or run the mapReduce command directly with `pymongo.database.Database.command` instead. For more guidance on this migration see:

- https://mongodb.com/docs/manual/reference/map-reduce-to-aggregation-pipeline/
- https://mongodb.com/docs/manual/reference/aggregation-commands-comparison/
Collection.ensure_index is removed ..................................

Removed `pymongo.collection.Collection.ensure_index`. Use `pymongo.collection.Collection.create_index` or `pymongo.collection.Collection.create_indexes` instead. Note that `ensure_index` maintained an in memory cache of recently created indexes whereas the newer methods do not. Applications should avoid frequent calls to `pymongo.collection.Collection.create_index` or `pymongo.collection.Collection.create_indexes`. Code like this:

```
def persist(self, document):
  collection.ensure_index('a', unique=True)
  collection.insert_one(document)
```

Can be changed to this:

```
def persist(self, document):
  if not self.created_index:
      collection.create_index('a', unique=True)
      self.created_index = True
  collection.insert_one(document)
```

Collection.reindex is removed .............................

Removed `pymongo.collection.Collection.reindex`. Run the reIndex command directly instead. Code like this:

```
>>> result = database.my_collection.reindex()
```

can be changed to this:

```
>>> result = database.command('reIndex', 'my_collection')
```

The modifiers parameter is removed ..................................

Removed the `modifiers` parameter from `pymongo.collection.Collection.find`, `pymongo.collection.Collection.find_one`, `pymongo.collection.Collection.find_raw_batches`, and `pymongo.cursor.Cursor`. Pass the options directly to the method instead. Code like this:

```
cursor = coll.find({}, modifiers={
  "$comment": "comment",
  "$hint": {"_id": 1},
  "$min": {"_id": 0},
  "$max": {"_id": 6},
  "$maxTimeMS": 6000,
  "$returnKey": False,
  "$showDiskLoc": False,
})
```

can be changed to this:

```
cursor = coll.find(
  {},
  comment="comment",
  hint={"_id": 1},
  min={"_id": 0},
  max={"_id": 6},
  max_time_ms=6000,
  return_key=False,
  show_record_id=False,
)
```

The hint parameter is required with min/max ...........................................

The `hint` option is now required when using `min` or `max` queries with `pymongo.collection.Collection.find` to ensure the query utilizes the correct index. For example, code like this:

```
cursor = coll.find({}, min={'x', min_value})
```

can be changed to this:

```
cursor = coll.find({}, min={'x', min_value}, hint=[('x', ASCENDING)])
```

Collection.__bool__ raises NotImplementedError .............................................. `pymongo.collection.Collection` now raises an error upon evaluating as a Boolean. Code like this:

```
if collection:
```

Can be changed to this:

```
if collection is not None:
```

You must now explicitly compare with None.

Collection.find returns entire document with empty projection ............................................................. Empty projections (eg {} or []) for `pymongo.collection.Collection.find`, and `pymongo.collection.Collection.find_one` are passed to the server as-is rather than the previous behavior which substituted in a projection of `{"_id": 1}`. This means that an empty projection will now return the entire document, not just the `"_id"` field. To ensure that behavior remains consistent, code like this:

```
coll.find({}, projection={})
```

Can be changed to this:

```
coll.find({}, projection={"_id":1})
```

## SONManipulator is removed

Removed `pymongo.son_manipulator`, `pymongo.son_manipulator.SONManipulator`, `pymongo.son_manipulator.ObjectIdInjector`, `pymongo.son_manipulator.ObjectIdShuffler`, `pymongo.son_manipulator.AutoReference`, `pymongo.son_manipulator.NamespaceInjector`, `pymongo.database.Database.add_son_manipulator`, `pymongo.database.Database.outgoing_copying_manipulators`, `pymongo.database.Database.outgoing_manipulators`, `pymongo.database.Database.incoming_copying_manipulators`, and `pymongo.database.Database.incoming_manipulators`.

Removed the `manipulate` parameter from `pymongo.collection.Collection.find`, `pymongo.collection.Collection.find_one`, and `pymongo.cursor.Cursor`.

The `pymongo.son_manipulator.SONManipulator` API has limitations as a technique for transforming your data and was deprecated in PyMongo 3.0. Instead, it is more flexible and straightforward to transform outgoing documents in your own code before passing them to PyMongo, and transform incoming documents after receiving them from PyMongo.

Alternatively, if your application uses the `SONManipulator` API to convert custom types to BSON, the `bson.codec_options.TypeCodec` and `bson.codec_options.TypeRegistry` APIs may be a suitable alternative. For more information, see [Custom Types](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/data-formats/custom-types/type-codecs/#encode-data-with-type-codecs).

## `SON().items()` now returns `dict_items` object.

`bson.son.SON.items` now returns a `dict_items` object rather than a list.

## `SON().iteritems()` removed.

`SON.iteritems()` now removed. Code that looks like this:

```
for k, v in son.iteritems():
```

Can now be replaced by code that looks like:

```
for k, v in son.items():
```

## IsMaster is removed

Removed `pymongo.ismaster.IsMaster`. Use `pymongo.hello.Hello` instead.

## NotMasterError is removed

Removed `pymongo.errors.NotMasterError`. Use `pymongo.errors.NotPrimaryError` instead.

## CertificateError is removed

Removed `pymongo.errors.CertificateError`. Since PyMongo 3.0 this error is handled internally and is never raised to the application.

## pymongo.GEOHAYSTACK is removed

Removed `pymongo.GEOHAYSTACK`. Replace with "geoHaystack" or create a 2d index and use $geoNear or $geoWithin instead.

## UUIDLegacy is removed

Removed `bson.binary.UUIDLegacy`. Use `bson.binary.Binary.from_uuid` instead.  Code like this:

```
uu = uuid.uuid4()
uuid_legacy = UUIDLegacy(uu)
```

can be changed to this:

```
uu = uuid.uuid4()
uuid_legacy = Binary.from_uuid(uu, PYTHON_LEGACY)
```

## Default JSONMode changed from LEGACY to RELAXED

Changed the default JSON encoding representation from legacy to relaxed. The json_mode parameter for :const:`bson.json_util.dumps` now defaults to :const:`~bson.json_util.RELAXED_JSON_OPTIONS`.

## GridFS changes

disable_md5 parameter is removed ................................

Removed the `disable_md5` option for `gridfs.GridFSBucket` and `gridfs.GridFS`. GridFS no longer generates checksums. Applications that desire a file digest should implement it outside GridFS and store it with other file metadata. For example:

```
import hashlib
my_db = MongoClient().test
fs = GridFSBucket(my_db)
with fs.open_upload_stream("test_file") as grid_in:
  file_data = b'...'
  sha356 = hashlib.sha256(file_data).hexdigest()
  grid_in.write(file_data)
  grid_in.sha356 = sha356  # Set the custom 'sha356' field
```

Note that for large files, the checksum may need to be computed in chunks to avoid the excessive memory needed to load the entire file at once.

## Removed features with no migration path

cursor_manager support is removed .................................

Removed `pymongo.cursor_manager.CursorManager`, `pymongo.cursor_manager`, and `pymongo.mongo_client.MongoClient.set_cursor_manager`.

MongoClient.close_cursor is removed ...................................

Removed `pymongo.mongo_client.MongoClient.close_cursor` and `pymongo.mongo_client.MongoClient.kill_cursors`. Instead, close cursors with `pymongo.cursor.Cursor.close` or `pymongo.command_cursor.CommandCursor.close`.

Database.eval, Database.system_js, and SystemJS are removed ...........................................................

Removed `pymongo.database.Database.eval`, `pymongo.database.Database.system_js` and `pymongo.database.SystemJS`. The eval command was deprecated in MongoDB 3.0 and removed in MongoDB 4.2. There is no replacement for eval with MongoDB 4.2+.

However, on MongoDB <= 4.0, code like this:

```
>>> result = database.eval('function (x) {return x;}', 3)
```

can be changed to this:

```
>>> from bson.code import Code
>>> result = database.command('eval', Code('function (x) {return x;}'), args=[3]).get('retval')
```

Database.error, Database.last_status, Database.previous_error, and Database.reset_error_history are removed ...........................................................................................................

Removed `pymongo.database.Database.error`, `pymongo.database.Database.last_status`, `pymongo.database.Database.previous_error`, and `pymongo.database.Database.reset_error_history`. These methods are obsolete: all MongoDB write operations use an acknowledged write concern and report their errors by default. These methods were deprecated in PyMongo 2.8.

Collection.parallel_scan is removed ...................................

Removed `pymongo.collection.Collection.parallel_scan`. MongoDB 4.2 removed the parallelCollectionScan command.  There is no replacement.

pymongo.message helpers are removed ...................................

Removed `pymongo.message.delete`, `pymongo.message.get_more`, `pymongo.message.insert`, `pymongo.message.kill_cursors`, `pymongo.message.query`, and `pymongo.message.update`.

Name is a required argument for pymongo.driver_info.DriverInfo ..............................................................

`name` is now a required argument for the `pymongo.driver_info.DriverInfo` class.

DBRef BSON/JSON decoding behavior .................................

Changed the BSON and JSON decoding behavior of `bson.dbref.DBRef` to match the behavior outlined in the DBRef specification version 1.0. Specifically, PyMongo now only decodes a subdocument into a `bson.dbref.DBRef` if and only if, it contains both `$ref` and `$id` fields and the `$ref`, `$id`, and `$db` fields are of the correct type. Otherwise the document is returned as normal. Previously, any subdocument containing a `$ref` field would be decoded as a `bson.dbref.DBRef`.

Encoding a UUID raises an error by default ..........................................

The default `uuid_representation` for `bson.codec_options.CodecOptions`, `bson.json_util.JSONOptions`, and `pymongo.mongo_client.MongoClient` has been changed from `bson.binary.UuidRepresentation.PYTHON_LEGACY` to `bson.binary.UuidRepresentation.UNSPECIFIED`. Attempting to encode a `uuid.UUID` instance to BSON or JSON now produces an error by default. If you were using UUIDs previously, you will need to set your `uuid_representation` to `bson.binary.UuidRepresentation.PYTHON_LEGACY` to avoid data corruption. If you do not have UUIDs, then you should set `bson.binary.UuidRepresentation.STANDARD`. If you do not explicitly set a value, you will receive an error like this when attempting to encode a `uuid.UUID`:

```
ValueError: cannot encode native uuid.UUID with UuidRepresentation.UNSPECIFIED. UUIDs can be manually converted...
```

See [Handling UUIDs](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/data-formats/uuid/#universally-unique-ids--uuids-) for details.

Additional BSON classes implement `__slots__` ...............................................

`bson.int64.Int64`, `bson.min_key.MinKey`, `bson.max_key.MaxKey`, `bson.timestamp.Timestamp`, `bson.regex.Regex`, and `bson.dbref.DBRef now implement _slots__` to reduce memory usage. This means that their attributes are fixed, and new attributes cannot be added to the object at runtime.
