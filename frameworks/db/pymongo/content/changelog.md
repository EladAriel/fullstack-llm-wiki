---
type: "Framework Learn Page"
framework: "pymongo"
source_repo: "https://github.com/mongodb/mongo-python-driver"
source_branch: "master"
source_path: "doc/changelog.rst"
source_commit: "1215d2f467d91038cd97a06dc043b74cf3a3edf1"
source_commit_short: "1215d2f4"
source_commit_date: "2026-06-18T10:29:26-04:00"
generated_at: "2026-06-21T11:44:03Z"
---

# Changelog

## Changes in Version 4.18.0

- Improved TLS connection performance by reusing TLS sessions across connections
to the same server, avoiding a full handshake on each new connection. Session resumption is supported on all Python versions for synchronous clients and on Python 3.11+ for async clients.

## Changes in Version 4.17.0 (2026/04/20)

PyMongo 4.17 brings a number of changes including:

- `has_key`, `iterkeys` and `itervalues` in `bson.son.SON` have
been deprecated and will be removed in PyMongo 5.0. These methods were deprecated in favor of the standard dictionary containment operator `in` and the `keys()` and `values()` methods, respectively.

- Added the `pymongo.asynchronous.client_session.AsyncClientSession.bind` and `pymongo.client_session.ClientSession.bind` methods
that allow users to bind a session to all database operations within the scope of a context manager instead of having to explicitly pass the session to each individual operation. See the [Transactions docs](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/crud/transactions/#methods) for examples and more information.

- Added support for MongoDB's Intelligent Workload Management (IWM) and ingress connection rate limiting features.
The driver now gracefully handles write-blocking scenarios and optimizes connection establishment during high-load conditions to maintain application availability. See the [IWM](https://www.mongodb.com/docs/atlas/production-notes) or [Overload Errors](https://www.mongodb.com/docs/atlas/overload-errors/?interface=driver&language=python) docs for more information.

## Changes in Version 4.16.0 (2026/01/07)

PyMongo 4.16 brings a number of changes including:

- Removed invalid documents from `bson.errors.InvalidDocument` error messages as
doing so may leak sensitive user data. Instead, invalid documents are stored in `bson.errors.InvalidDocument.document`.

- PyMongo now requires `dnspython>=2.6.1`, since `dnspython` 1.0 is no longer maintained.
The minimum version is `2.6.1` to account for [CVE-2023-29483](https://www.cve.org/CVERecord?id=CVE-2023-29483).

- Removed support for Eventlet.
Eventlet is actively being sunset by its maintainers and has compatibility issues with PyMongo's dnspython dependency.

- Use Zstandard support from the standard library for Python 3.14+, and use `backports.zstd` for older versions.
- Fixed return type annotation for `find_one_and_*` methods on `pymongo.asynchronous.collection.AsyncCollection`
and `pymongo.synchronous.collection.Collection` to include `None`.

- Added support for NumPy 1D-arrays in `bson.binary.BinaryVector`.
- Prevented `pymongo.encryption.ClientEncryption` from loading the crypt
shared library to fix "MongoCryptError: An existing crypt_shared library is loaded by the application" unless the linked library search path is set.

## Changes in Version 4.15.5 (2025/12/02)

Version 4.15.5 is a bug fix release.

- Fixed a bug that could cause `AutoReconnect("connection pool paused")` errors when cursors fetched more documents from the database after SDAM heartbeat failures.
## Changes in Version 4.15.4 (2025/10/21)

Version 4.15.4 is a bug fix release.

- Relaxed the callback type of `pymongo.asynchronous.client_session.AsyncClientSession.with_transaction` to allow the broader Awaitable type rather than only Coroutine objects.
- Added the missing Python 3.14 trove classifier to the package metadata.
Issues Resolved ...............

See the PyMongo 4.15.4 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 4.15.3 (2025/10/07)

Version 4.15.3 is a bug fix release.

- Fixed a memory leak when raising `bson.errors.InvalidDocument` with C extensions.
- Fixed the return type of the  `pymongo.asynchronous.collection.AsyncCollection.distinct`,
`pymongo.synchronous.collection.Collection.distinct`, `pymongo.asynchronous.cursor.AsyncCursor.distinct`, and `pymongo.asynchronous.cursor.AsyncCursor.distinct` methods.

Issues Resolved ...............

See the PyMongo 4.15.3 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 4.15.2 (2025/10/01)

Version 4.15.2 is a bug fix release.

- Add wheels for Python 3.14 and 3.14t that were missing from 4.15.0 release. Drop the 3.13t wheel.
Issues Resolved ...............

See the PyMongo 4.15.2 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 4.15.1 (2025/09/16)

Version 4.15.1 is a bug fix release.

- Fixed a bug in `pymongo.synchronous.encryption.ClientEncryption.encrypt`
and `pymongo.asynchronous.encryption.AsyncClientEncryption.encrypt` that would cause a `TypeError` when using `pymongocrypt<1.16` by passing an unsupported `type_opts` parameter even if Queryable Encryption text queries beta was not used.

- Fixed a bug in `AsyncMongoClient` that caused a `ServerSelectionTimeoutError`
when used with `uvicorn`, `FastAPI`, or `uvloop`.

Issues Resolved ...............

See the PyMongo 4.15.1 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 4.15.0 (2025/09/10)

PyMongo 4.15 brings a number of changes including:

- Added `pymongo.encryption_options.TextOpts`,
`pymongo.encryption.Algorithm.TEXTPREVIEW`, `pymongo.encryption.QueryType.PREFIXPREVIEW`, `pymongo.encryption.QueryType.SUFFIXPREVIEW`, `pymongo.encryption.QueryType.SUBSTRINGPREVIEW`, as part of the experimental Queryable Encryption text queries beta. `pymongocrypt>=1.16` is required for text query support.

- Added `bson.decimal128.DecimalEncoder` and
`bson.decimal128.DecimalDecoder` to support encoding and decoding of BSON Decimal128 values to decimal.Decimal values using the TypeRegistry API.

- Added support for Windows `arm64` wheels.
## Changes in Version 4.14.1 (2025/08/19)

Version 4.14.1 is a bug fix release.

- Fixed a bug in `MongoClient.append_metadata()` and
`AsyncMongoClient.append_metadata()` that allowed duplicate `DriverInfo.name` to be appended to the metadata.

Issues Resolved ...............

See the PyMongo 4.14.1 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 4.14.0 (2025/08/06)

> **Warning:** MongoDB 4.2+.

PyMongo 4.14 brings a number of changes including:

- Dropped support for MongoDB 4.0.
- Added preliminary support for Python 3.14 and 3.14 with free-threading. We do
not yet support the following with Python 3.14:

- Subinterpreters (`concurrent.interpreters`)
- Free-threading with Encryption
- mod_wsgi
- Removed experimental support for free-threading support in Python 3.13.
- Added `bson.codec_options.TypeRegistry.codecs` and
`bson.codec_options.TypeRegistry.fallback_encoder` properties to allow users to directly access the type codecs and fallback encoder for a given `bson.codec_options.TypeRegistry`.

- Added
`pymongo.asynchronous.mongo_client.AsyncMongoClient.append_metadata` and `pymongo.mongo_client.MongoClient.append_metadata` to allow instantiated MongoClients to send client metadata on-demand

- Improved performance of selecting a server with the Primary selector.
- Introduces a minor breaking change. When encoding
`bson.binary.BinaryVector`, a `ValueError` will be raised if the 'padding' metadata field is < 0 or > 7, or non-zero for any type other than PACKED_BIT.

- Changed `pymongo.uri_parser.parse_uri`'s `options` return value to be
type `dict instead of CaseInsensitiveDictionary`.

Issues Resolved ...............

See the PyMongo 4.14 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 4.13.2 (2025/06/17)

Version 4.13.2 is a bug fix release.

- Fixed a bug where `AsyncMongoClient` would block the event loop while creating new connections,
potentially significantly increasing latency for ongoing operations.

Issues Resolved ...............

See the PyMongo 4.13.2 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 4.13.1 (2025/06/10)

Version 4.13.1 is a bug fix release.

- Fixed a bug that could raise `ServerSelectionTimeoutError` when using timeouts with `AsyncMongoClient`.
- Fixed a bug that could raise `NetworkTimeout` errors on Windows.
Issues Resolved ...............

See the PyMongo 4.13.1 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 4.13.0 (2025/05/14)

PyMongo 4.13 brings a number of changes including:

- The asynchronous API is now stable and no longer in beta.
See the `pymongo.asynchronous` docs or the [migration guide](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/reference/migration/) for more information.

- Fixed a bug where `pymongo.write_concern.WriteConcern` repr was not eval-able
when using `w="majority"`.

- When padding is set, ignored bits in a BSON BinaryVector of PACKED_BIT dtype should be set to zero.
When encoding, this is enforced and is a breaking change. It is not yet enforced when decoding, so reading from the database will not fail, however a warning will be triggered. From PyMongo 5.0, this rule will be enforced for both encoding and decoding.

Issues Resolved ...............

See the PyMongo 4.13 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 4.12.1 (2025/04/29)

Version 4.12.1 is a bug fix release.

- Fixed a bug that could raise `UnboundLocalError` when creating asynchronous connections over SSL.
- Fixed a bug causing SRV hostname validation to fail when resolver and resolved hostnames are identical with three domain levels.
- Fixed a bug that caused direct use of `pymongo.uri_parser` to raise an `AttributeError`.
- Fixed a bug where clients created with connect=False and a "mongodb+srv://" connection string
could cause public `pymongo.MongoClient` and `pymongo.AsyncMongoClient` attributes (topology_description, nodes, address, primary, secondaries, arbiters) to incorrectly return a Database, leading to type errors such as: "NotImplementedError: Database objects do not implement truth value testing or bool()".

- Removed Eventlet testing against Python versions newer than 3.9 since
Eventlet is actively being sunset by its maintainers and has compatibility issues with PyMongo's dnspython dependency.

- Fixed a bug where MongoDB cluster topology changes could cause asynchronous operations to take much longer to complete
due to holding the Topology lock while closing stale connections.

- Fixed a bug that would cause AsyncMongoClient to attempt to use PyOpenSSL when available, resulting in errors such as
"pymongo.errors.ServerSelectionTimeoutError: 'SSLContext' object has no attribute 'wrap_bio'".

Issues Resolved ...............

See the PyMongo 4.12.1 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 4.12.0 (2025/04/08)

> **Warning:** PyMongo 4.12 will be the last release to support MongoDB 4.0.

PyMongo 4.12 brings a number of changes including:

- Support for configuring DEK cache lifetime via the `key_expiration_ms` argument to
`pymongo.encryption_options.AutoEncryptionOpts`.

- Support for $lookup in CSFLE and QE supported on MongoDB 8.1+.
- pymongocrypt>=1.13 is now required for [In-Use Encryption](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/security/in-use-encryption/#in-use-encryption) support.
- Added `gridfs.asynchronous.grid_file.AsyncGridFSBucket.rename_by_name` and `gridfs.grid_file.GridFSBucket.rename_by_name`
for more performant renaming of a file with multiple revisions.

- Added `gridfs.asynchronous.grid_file.AsyncGridFSBucket.delete_by_name` and `gridfs.grid_file.GridFSBucket.delete_by_name`
for more performant deletion of a file with multiple revisions.

- AsyncMongoClient no longer performs DNS resolution for "mongodb+srv://" connection strings on creation.
To avoid blocking the asyncio loop, the resolution is now deferred until the client is first connected.

- Added index hinting support to the
`pymongo.asynchronous.collection.AsyncCollection.distinct` and `pymongo.collection.Collection.distinct` commands.

- Deprecated the `hedge` parameter for
`pymongo.read_preferences.PrimaryPreferred`, `pymongo.read_preferences.Secondary`, `pymongo.read_preferences.SecondaryPreferred`, `pymongo.read_preferences.Nearest`. Support for `hedge` will be removed in PyMongo 5.0.

- Removed PyOpenSSL support from the asynchronous API due to limitations of the CPython asyncio.Protocol SSL implementation.
- Allow valid SRV hostnames with less than 3 parts.
Issues Resolved ...............

See the PyMongo 4.12 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 4.11.2 (2025/03/05)

Version 4.11.2 is a bug fix release.

- Fixed a bug where `pymongo.database.Database.command` would fail when attempting to run the bulkWrite command.
Issues Resolved ...............

See the PyMongo 4.11.2 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 4.11.1 (2025/02/10)

- Fixed support for prebuilt `ppc64le` and `s390x` wheels.
## Changes in Version 4.11.0 (2025/01/28)

> **Warning:**

> **Warning:** Driver support for MongoDB 3.6 reached end of life in April 2024.

> **Warning:** A future minor release of PyMongo will raise the minimum supported MongoDB Server version from 4.0 to 4.2.
This is in accordance with [MongoDB Software Lifecycle Schedules](https://www.mongodb.com/legal/support-policy/lifecycles).
**Support for MongoDB Server 4.0 will be dropped in a future release!**

> **Warning:**

PyMongo 4.11 brings a number of changes including:

- Dropped support for Python 3.8 and PyPy 3.9.
- Dropped support for MongoDB 3.6.
- Dropped support for the MONGODB-CR authenticate mechanism, which is no longer supported by MongoDB 4.0+.
- pymongocrypt>=1.12 is now required for [In-Use Encryption](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/security/in-use-encryption/#in-use-encryption) support.
- Added support for free-threaded Python with the GIL disabled. For more information see:
[Free-threaded CPython](https://docs.python.org/3.13/whatsnew/3.13.html#whatsnew313-free-threaded-cpython). We do not yet support free-threaded Python on Windows (PYTHON-5027) or with In-Use Encryption (PYTHON-5024).

- `pymongo.asynchronous.mongo_client.AsyncMongoClient.address` and
`pymongo.mongo_client.MongoClient.address` now correctly block when called on unconnected clients until either connection succeeds or a server selection timeout error is raised.

- Added `repr` support to `pymongo.operations.IndexModel`.
- Added `repr` support to `pymongo.operations.SearchIndexModel`.
- Added `sort` parameter to
`pymongo.collection.Collection.update_one`, `pymongo.collection.Collection.replace_one`, `pymongo.operations.UpdateOne`, and `pymongo.operations.UpdateMany`,

- `pymongo.mongo_client.MongoClient.bulk_write` and
`pymongo.asynchronous.mongo_client.AsyncMongoClient.bulk_write` now throw an error when `ordered=True` or `verboseResults=True` are used with unacknowledged writes. These are unavoidable breaking changes.

- Fixed a bug in :const:`bson.json_util.dumps` where a `bson.datetime_ms.DatetimeMS` would
be incorrectly encoded as `'{"$date": "X"}'` instead of `'{"$date": X}'` when using the legacy MongoDB Extended JSON datetime representation.

- Fixed a bug where :const:`bson.json_util.loads` would raise an IndexError when parsing an invalid
`"$date"` instead of a ValueError.

Issues Resolved ...............

See the PyMongo 4.11 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 4.10.1 (2024/10/01)

Version 4.10.1 is a bug fix release.

- Fixed a bug where `pymongo.results.UpdateResult.did_upsert` would raise a `TypeError`.
- Fixed Binary BSON subtype (9) support on big-endian operating systems (such as zSeries).
Issues Resolved ...............

See the PyMongo 4.10.1 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 4.10.0 (2024/09/30)

- Added provisional **(BETA)** support for a new Binary BSON subtype (9) used for efficient storage and retrieval of vectors:
densely packed arrays of numbers, all of the same type. This includes new methods `bson.binary.Binary.from_vector` and `bson.binary.Binary.as_vector`.

- Added C extension use to client metadata, for example: `{"driver": {"name": "PyMongo|c", "version": "4.10.0"}, ...}`
- Fixed a bug where `pymongo.asynchronous.mongo_client.AsyncMongoClient` could deadlock.
- Fixed a bug where PyMongo could fail to import on Windows if `asyncio` is misconfigured.
Issues Resolved ...............

See the PyMongo 4.10 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 4.9.2 (2024/10/02)

- Fixed a bug where `pymongo.asynchronous.mongo_client.AsyncMongoClient` could deadlock.
- Fixed a bug where PyMongo could fail to import on Windows if `asyncio` is misconfigured.
- Fixed a bug where `pymongo.results.UpdateResult.did_upsert` would raise a `TypeError`.
Issues Resolved ...............

See the PyMongo 4.9.2 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 4.9.1 (2024/09/18)

- Add missing documentation about the fact the async API is in beta state.
Issues Resolved ...............

See the PyMongo 4.9.1 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 4.9 (2024/09/18)

> **Warning:** PyMongo 4.9 will be the last release to support MongoDB 3.6.

> **Warning:** As a result, versions of Motor older than 3.6 are not compatible with PyMongo 4.9.
Existing users of these versions must either upgrade to Motor 3.6 and PyMongo 4.9,
or cap their PyMongo version to `< 4.9`.
Any applications that use private APIs may also break as a result of these internal changes.

PyMongo 4.9 brings a number of improvements including:

- Added support for MongoDB 8.0.
- Added support for Python 3.13.
- A new beta asynchronous API with full asyncio support.
This new asynchronous API is a work-in-progress that may change during the beta period before the full release.

- Added support for In-Use Encryption range queries with MongoDB 8.0.
Added `pymongo.encryption.Algorithm.RANGE`. `sparsity` and `trim_factor` are now optional in `pymongo.encryption_options.RangeOpts`.

- Added support for the "delegated" option for the KMIP `master_key` in
`pymongo.encryption.ClientEncryption.create_data_key`.

- pymongocrypt>=1.10 is now required for [In-Use Encryption](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/security/in-use-encryption/#in-use-encryption) support.
- Added `pymongo.cursor.Cursor.to_list` to `pymongo.cursor.Cursor`,
`pymongo.command_cursor.CommandCursor`, `pymongo.asynchronous.cursor.AsyncCursor`, and `pymongo.asynchronous.command_cursor.AsyncCommandCursor` as an asynchronous-friendly alternative to `list(cursor)`.

- Added `pymongo.mongo_client.MongoClient.bulk_write` to `pymongo.mongo_client.MongoClient`
and `pymongo.asynchronous.mongo_client.AsyncMongoClient`, enabling users to perform insert, update, and delete operations against mixed namespaces in a minimized number of round trips. Please see [Client Bulk Write](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/crud/bulk-write/#client-bulk-write-example) for more information.

- Added support for the `namespace` parameter to the
`pymongo.operations.InsertOne`, `pymongo.operations.ReplaceOne`, `pymongo.operations.UpdateOne`, `pymongo.operations.UpdateMany`, `pymongo.operations.DeleteOne`, and `pymongo.operations.DeleteMany` operations, so they can be used in the new `pymongo.mongo_client.MongoClient.bulk_write`.

- Added `repr` support to `bson.tz_util.FixedOffset`.
- Fixed a bug where PyMongo would raise `InvalidBSON: unhashable type: 'tzfile'`
when using `bson.codec_options.DatetimeConversion.DATETIME_CLAMP` or `bson.codec_options.DatetimeConversion.DATETIME_AUTO` with a timezone from dateutil.

- Fixed a bug where PyMongo would raise `InvalidBSON: date value out of range`
when using `bson.codec_options.DatetimeConversion.DATETIME_CLAMP` or `bson.codec_options.DatetimeConversion.DATETIME_AUTO` with a non-UTC timezone.

- Added a warning to unclosed MongoClient instances
telling users to explicitly close clients when finished with them to avoid leaking resources. For example:

```
 sys:1: ResourceWarning: Unclosed MongoClient opened at:
     File "/Users/<user>/my_file.py", line 8, in <module>``
         client = MongoClient()
 Call MongoClient.close() to safely shut down your client and free up resources.
```

- The default value for `connect` in `MongoClient` is changed to `False` when running on
unction-as-a-service (FaaS) like AWS Lambda, Google Cloud Functions, and Microsoft Azure Functions. On some FaaS systems, there is a `fork()` operation at function startup.  By delaying the connection to the first operation, we avoid a deadlock.  See [multiple forks](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/connect/mongoclient/#multiple-forks) for more information.

Issues Resolved ...............

See the PyMongo 4.9 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 4.8.0 (2024/06/26)

> **Warning:**

PyMongo 4.8 brings a number of improvements including:

- The handshake metadata for "os.name" on Windows has been simplified to "Windows" to improve import time.
- The repr of `bson.binary.Binary` is now redacted when the subtype is SENSITIVE_SUBTYPE(8).
- Secure Software Development Life Cycle automation for release process.
GitHub Releases now include a Software Bill of Materials, and signature files corresponding to the distribution files released on PyPI.

- Fixed a bug in change streams where both `startAtOperationTime` and `resumeToken`
could be added to a retry attempt, which caused the retry to fail.

- Fallback to stdlib `ssl` module when `pyopenssl` import fails with AttributeError.
- Improved performance of MongoClient operations, especially when many operations are being run concurrently.
Unavoidable breaking changes ............................

- Since we are now using `hatch` as our build backend, we no longer have a usable `setup.py` file
and require installation using `pip`.  Attempts to invoke the `setup.py` file will raise an exception. Additionally, `pip` >= 21.3 is now required for editable installs.

- We no longer support the `srv` extra, since `dnspython` is included as a dependency in PyMongo 4.7+.
Instead of `pip install pymongo[srv]`, use `pip install pymongo`.

- We no longer support the `tls` extra, which was only valid for Python 2.
Instead of `pip install pymongo[tls]`, use `pip install pymongo`.

Issues Resolved ...............

See the PyMongo 4.8 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 4.7.3 (2024/06/04)

Version 4.7.3 has further fixes for lazily loading modules.

- Use deferred imports instead of importlib lazy module loading.
- Improve import time on Windows.
- Reduce verbosity of "Waiting for suitable server to become available" log message from info to debug.
Issues Resolved ...............

See the PyMongo 4.7.3 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 4.7.2 (2024/05/07)

Version 4.7.2 fixes a bug introduced in 4.7.0:

- Fixed a bug where PyMongo could not be used with the Nuitka compiler.
Issues Resolved ...............

See the PyMongo 4.7.2 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 4.7.1 (2024/04/30)

Version 4.7.1 fixes a bug introduced in 4.7.0:

- Fixed a bug where PyMongo would cause an `AttributeError` if `dns.resolver` was imported and referenced
after PyMongo was imported.

- Clarified the behavior of the `TOKEN_RESOURCE` auth mechanism property for `MONGODB-OIDC`.
Issues Resolved ...............

See the PyMongo 4.7.1 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 4.7.0 (2024/04/24)

PyMongo 4.7 brings a number of improvements including:

- Added support for `MONGODB-OIDC` authentication.  The MONGODB-OIDC mechanism authenticates
using an OpenID Connect (OIDC) access token. The driver supports OIDC for workload identity, defined as an identity you assign to a software workload (such as an application, service, script, or container) to authenticate and access other services and resources. Please see [Authentication](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/security/authentication/#authentication-mechanisms) for more information.

- Added support for Python's [native logging library](https://docs.python.org/3/howto/logging.html),
enabling developers to customize the verbosity of log messages for their applications. Please see [Logging](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/monitoring-and-logging/logging/#logging) for more information.

- Significantly improved the performance of encoding BSON documents to JSON.
- Added support for named KMS providers for client side field level encryption.
Previously supported KMS providers were only: aws, azure, gcp, kmip, and local. The KMS provider is now expanded to support name suffixes (e.g. local:myname). Named KMS providers enables more than one of each KMS provider type to be configured. See the docstring for `pymongo.encryption_options.AutoEncryptionOpts`. Note that named KMS providers requires pymongocrypt >=1.9 and libmongocrypt >=1.9.

- Added the `pymongo.hello.Hello.connection_id`,
`pymongo.monitoring.CommandStartedEvent.server_connection_id`, `pymongo.monitoring.CommandSucceededEvent.server_connection_id`, and `pymongo.monitoring.CommandFailedEvent.server_connection_id` properties.

- Fixed a bug where inflating a `bson.raw_bson.RawBSONDocument` containing a `bson.code.Code` would cause an error.
- `pymongo.encryption.ClientEncryption.encrypt` and
`pymongo.encryption.ClientEncryption.encrypt_expression` now allow `key_id` to be passed in as a `uuid.UUID`.

- Fixed a bug where `bson.int64.Int64` instances could not always be encoded by orjson. The following now
works:

```
>>> import orjson
>>> from bson import json_util
>>> orjson.dumps({'a': Int64(1)}, default=json_util.default, option=orjson.OPT_PASSTHROUGH_SUBCLASS)
```

- Fixed a bug appearing in Python 3.12 where "RuntimeError: can't create new thread at interpreter shutdown"
could be written to stderr when a MongoClient's thread starts as the python interpreter is shutting down.

- Added a warning when connecting to DocumentDB and CosmosDB clusters.
For more information regarding feature compatibility and support please visit [mongodb.com/supportability/documentdb](https://mongodb.com/supportability/documentdb) and [mongodb.com/supportability/cosmosdb](https://mongodb.com/supportability/cosmosdb).

- Added the `pymongo.monitoring.ConnectionCheckedOutEvent.duration`,
`pymongo.monitoring.ConnectionCheckOutFailedEvent.duration`, and `pymongo.monitoring.ConnectionReadyEvent.duration` properties.

- Added the `type` and `kwargs` arguments to `pymongo.operations.SearchIndexModel` to enable
creating vector search indexes in MongoDB Atlas.

- Fixed a bug where `read_concern` and `write_concern` were improperly added to
`pymongo.collection.Collection.list_search_indexes` queries.

- Deprecated `pymongo.write_concern.WriteConcern.wtimeout` and `pymongo.mongo_client.MongoClient.wTimeoutMS`.
Use `pymongo.timeout` instead.

> **Warning:** [CVE-2023-29483](https://www.cve.org/CVERecord?id=CVE-2023-29483).  We do not explicitly require
that version, but we strongly recommend that you install at least that version in your environment.

Unavoidable breaking changes ............................

- Replaced usage of `bson.son.SON` on all internal classes and commands to dict,
`options.pool_options.metadata` is now of type `dict` as opposed to `bson.son.SON`. Here's some examples of how this changes expected output as well as how to convert from `dict` to `bson.son.SON`:

```
# Before
>>> from pymongo import MongoClient
>>> client = MongoClient()
>>> client.options.pool_options.metadata
SON([('driver', SON([('name', 'PyMongo'), ('version', '4.7.0.dev0')])), ('os', SON([('type', 'Darwin'), ('name', 'Darwin'), ('architecture', 'arm64'), ('version', '14.3')])), ('platform', 'CPython 3.11.6.final.0')])

# After
>>> client.options.pool_options.metadata
{'driver': {'name': 'PyMongo', 'version': '4.7.0.dev0'}, 'os': {'type': 'Darwin', 'name': 'Darwin', 'architecture': 'arm64', 'version': '14.3'}, 'platform': 'CPython 3.11.6.final.0'}

# To convert from dict to SON
# This will only convert the first layer of the dictionary
>>> data_as_dict = client.options.pool_options.metadata
>>> SON(data_as_dict)
SON([('driver', {'name': 'PyMongo', 'version': '4.7.0.dev0'}), ('os', {'type': 'Darwin', 'name': 'Darwin', 'architecture': 'arm64', 'version': '14.3'}), ('platform', 'CPython 3.11.6.final.0')])

# To convert from dict to SON on a nested dictionary
>>> def dict_to_SON(data_as_dict: dict[Any, Any]):
...     data_as_SON = SON()
...     for key, value in data_as_dict.items():
...         data_as_SON[key] = dict_to_SON(value) if isinstance(value, dict) else value
...     return data_as_SON
>>>
>>> dict_to_SON(data_as_dict)
SON([('driver', SON([('name', 'PyMongo'), ('version', '4.7.0.dev0')])), ('os', SON([('type', 'Darwin'), ('name', 'Darwin'), ('architecture', 'arm64'), ('version', '14.3')])), ('platform', 'CPython 3.11.6.final.0')])
```

- PyMongo now uses [lazy imports](https://docs.python.org/3/library/importlib.html#implementing-lazy-imports) for external dependencies.
If you are relying on any kind of monkey-patching of the standard library, you may need to explicitly import those external libraries in addition to `pymongo` before applying the patch.  Note that we test with `gevent` and `eventlet` patching, and those continue to work.

- The "aws" extra now requires minimum version of `1.1.0` for `pymongo_auth_aws`.
## Changes in Version 4.6.3 (2024/03/27)

PyMongo 4.6.3 fixes the following bug:

- Fixed a potential memory access violation when decoding invalid bson.
Issues Resolved ...............

See the PyMongo 4.6.3 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 4.6.2 (2024/02/21)

PyMongo 4.6.2 fixes the following bug:

- Fixed a bug appearing in Python 3.12 where "RuntimeError: can't create new thread at interpreter shutdown"
could be written to stderr when a MongoClient's thread starts as the python interpreter is shutting down.

Issues Resolved ...............

See the PyMongo 4.6.2 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 4.6.1 (2023/11/29)

PyMongo 4.6.1 fixes the following bug:

- Ensure retryable read `OperationFailure` errors re-raise exception when 0 or NoneType error code is provided.
Issues Resolved ...............

See the PyMongo 4.6.1 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 4.6.0 (2023/11/01)

PyMongo 4.6 brings a number of improvements including:

- Added the `serverMonitoringMode` URI and keyword argument to `pymongo.mongo_client.MongoClient`.
- Improved client performance and reduced connection requirements in Function-as-a-service (FaaS)
environments like AWS Lambda, Google Cloud Functions, and Microsoft Azure Functions.

- Added the `pymongo.monitoring.CommandSucceededEvent.database_name` property.
- Added the `pymongo.monitoring.CommandFailedEvent.database_name` property.
- Allow passing a `dict` to sort/create_index/hint.
- Added `repr` support to the write result classes:
`pymongo.results.BulkWriteResult`, `pymongo.results.DeleteResult`, `pymongo.results.InsertManyResult`, `pymongo.results.InsertOneResult`, `pymongo.results.UpdateResult`, and `pymongo.encryption.RewrapManyDataKeyResult`. For example:

>>> client.t.t.insert_one({}) InsertOneResult(ObjectId('65319acdd55bb3a27ab5502b'), acknowledged=True) >>> client.t.t.insert_many([{} for _ in range(3)]) InsertManyResult([ObjectId('6532f85e826f2b6125d6ce39'), ObjectId('6532f85e826f2b6125d6ce3a'), ObjectId('6532f85e826f2b6125d6ce3b')], acknowledged=True)

- `pymongo.uri_parser.parse_uri` now considers the delimiting slash (`/`)
between hosts and connection options optional. For example, "mongodb://example.com?tls=true" is now a valid URI.

- Fixed a bug where PyMongo would incorrectly promote all cursors to exhaust cursors
when connected to load balanced MongoDB clusters or Serverless clusters.

- Added the [network compression](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/connect/connection-options/network-compression/#compress-network-traffic) documentation page.
- Added more timeout information to network errors.
Issues Resolved ...............

See the PyMongo 4.6 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 4.5.0 (2023/08/22)

PyMongo 4.5 brings a number of improvements including:

- Added new helper methods for Atlas Search Index (requires MongoDB Server 7.0+):
`pymongo.collection.Collection.list_search_indexes`, `pymongo.collection.Collection.create_search_index`, `pymongo.collection.Collection.create_search_indexes`, `pymongo.collection.Collection.drop_search_index`, `pymongo.collection.Collection.update_search_index`

- Added `pymongo.database.Database.cursor_command`
and `pymongo.command_cursor.CommandCursor.try_next` to support executing an arbitrary command that returns a cursor.

- `cryptography` 2.5 or later is now required for [OCSP](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/security/tls/#ocsp) support.
- Improved bson encoding and decoding performance by up to 134%(PYTHON-3729, PYTHON-3797, PYTHON-3816, PYTHON-3817, PYTHON-3820, PYTHON-3824, and PYTHON-3846).
> **Warning:** must upgrade to PyPy3.8+.

Issues Resolved ...............

See the PyMongo 4.5 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 4.4.1 (2023/07/13)

Version 4.4.1 fixes the following bugs:

- Fixed a bug where pymongo would raise a `ConfigurationError: Invalid SRV host`
error when connecting to a "mongodb+srv://" URI that included capital letters in the SRV hosts returned from DNS. (PYTHON-3800).

- Fixed a minor reference counting bug in the C extension (PYTHON-3798).
Issues Resolved ...............

See the PyMongo 4.4.1 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 4.4.0 (2023/06/21)

PyMongo 4.4 brings a number of improvements including:

- Added support for MongoDB 7.0.
- Added support for Python 3.11.
- Added support for passing a list containing (key, direction) pairs
or keys to `pymongo.collection.Collection.create_index`.

- Improved bson encoding performance (PYTHON-3717 and PYTHON-3718).
- Improved support for Pyright to improve typing support for IDEs like Visual Studio Code
or Visual Studio.

- Improved support for type-checking with MyPy "strict" mode (`--strict`).
- Added `pymongo.encryption.ClientEncryption.create_encrypted_collection`,
`pymongo.errors.EncryptedCollectionError`, `pymongo.encryption.ClientEncryption.encrypt_expression`, `pymongo.encryption_options.RangeOpts`, and `pymongo.encryption.Algorithm.RANGEPREVIEW` as part of the experimental Queryable Encryption beta.

- pymongocrypt 1.6.0 or later is now required for [In-Use Encryption](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/security/in-use-encryption/#in-use-encryption) support. MongoDB
Server 7.0 introduced a backwards breaking change to the QE protocol. Users taking advantage of the Queryable Encryption beta must now upgrade to MongoDB 7.0+ and PyMongo 4.4+.

- Previously, PyMongo's docs recommended using `datetime.datetime.utcnow` and
`datetime.datetime.utcfromtimestamp`. utcnow and utcfromtimestamp are deprecated in Python 3.12, for reasons explained in this Github issue. Instead, users should use `datetime.datetime.now(tz=timezone.utc)` and `datetime.datetime.fromtimestamp(tz=timezone.utc)` instead.

Issues Resolved ...............

See the PyMongo 4.4 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 4.3.3 (2022/11/17)

Version 4.3.3 documents support for the following:

- [CSFLE on-demand credentials](https://www.mongodb.com/docs/v7.0/core/csfle/tutorials/aws/aws-automatic/?interface=driver&language=python#use-automatic-client-side-field-level-encryption-with-aws) for cloud KMS providers.
- Authentication support for [EKS Clusters](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/security/authentication/aws-iam/#assumerolewithwebidentity).
- Added the [timeout](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/connect/connection-options/csot/#limit-server-execution-time) example page to improve the documentation
for `pymongo.timeout`.

Bug Fixes .........

- Fixed a performance regression in `gridfs.GridFSBucket.download_to_stream`
and `gridfs.GridFSBucket.download_to_stream_by_name` by reading in chunks instead of line by line (PYTHON-3502).

- Improved performance of `gridfs.grid_file.GridOut.read` and
`gridfs.grid_file.GridOut.readline` (PYTHON-3508).

Issues Resolved ...............

See the PyMongo 4.3.3 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 4.3.2 (2022/10/18)

Note: We withheld uploading tags 4.3.0 and 4.3.1 to PyPI due to a version handling error and a necessary documentation update.

[dnspython](https://pypi.python.org/pypi/dnspython) is now a required dependency. This change makes PyMongo easier to install for use with "mongodb+srv://" connection strings and [MongoDB Atlas](https://www.mongodb.com/cloud).

PyMongo 4.3 brings a number of improvements including:

- Added support for decoding BSON datetimes outside of the range supported
by Python's `datetime.datetime` builtin. See [handling out of range datetimes](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/data-formats/dates-and-times/#handling-out-of-range-datetimes) for examples, as well as `bson.datetime_ms.DatetimeMS`, `bson.codec_options.DatetimeConversion`, and `bson.codec_options.CodecOptions`'s `datetime_conversion` parameter for more details (PYTHON-1824).

- PyMongo now resets its locks and other shared state in the child process
after a `os.fork` to reduce the frequency of deadlocks. Note that deadlocks are still possible because libraries that PyMongo depends like OpenSSL cannot be made fork() safe in multithreaded applications. (PYTHON-2484). For more info see [multiple forks](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/connect/mongoclient/#multiple-forks).

- When used with MongoDB 6.0+, `pymongo.change_stream.ChangeStream` s
now allow for new types of events (such as DDL and C2C replication events) to be recorded with the new parameter `show_expanded_events` that can be passed to methods such as `pymongo.collection.Collection.watch`.

- PyMongo now internally caches AWS credentials that it fetches from AWS
endpoints, to avoid rate limitations.  The cache is cleared when the credentials expire or an error is encountered.

- When using the `MONGODB-AWS` authentication mechanism with the
`aws` extra, the behavior of credential fetching has changed with `pymongo_auth_aws>=1.1.0`.  Please see [Authentication](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/security/authentication/#authentication-mechanisms) for more information.

Bug fixes .........

- Fixed a bug where  `pymongo.change_stream.ChangeStream`
would allow an app to retry calling `next()` or `try_next()` even after non-resumable errors (PYTHON-3389).

- Fixed a bug where the client could be unable to discover the new primary
after a simultaneous replica set election and reconfig (PYTHON-2970).

Issues Resolved ...............

See the PyMongo 4.3 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 4.2.0 (2022/07/20)

> **Warning:**

PyMongo 4.2 brings a number of improvements including:

- Support for MongoDB 6.0.
- Support for the Queryable Encryption beta with MongoDB 6.0. Note that backwards-breaking
changes may be made before the final release.  See [automatic queryable client-side encryption](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/security/in-use-encryption/#queryable-encryption) for example usage.

- Provisional (beta) support for `pymongo.timeout` to apply a single timeout
to an entire block of pymongo operations. See [timeout](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/connect/connection-options/csot/#limit-server-execution-time) for examples.

- Added the `timeoutMS` URI and keyword argument to `pymongo.mongo_client.MongoClient`.
- Added the `pymongo.errors.PyMongoError.timeout` property which is `True` when
the error was caused by a timeout.

- Added the `check_exists` argument to `pymongo.database.Database.create_collection`
that when True (the default)  runs an additional `listCollections` command to verify that the collection does not exist already.

- Added the following key management APIs to `pymongo.encryption.ClientEncryption`:
- `pymongo.encryption.ClientEncryption.get_key`
- `pymongo.encryption.ClientEncryption.get_keys`
- `pymongo.encryption.ClientEncryption.delete_key`
- `pymongo.encryption.ClientEncryption.add_key_alt_name`
- `pymongo.encryption.ClientEncryption.get_key_by_alt_name`
- `pymongo.encryption.ClientEncryption.remove_key_alt_name`
- `pymongo.encryption.ClientEncryption.rewrap_many_data_key`
- `pymongo.encryption.RewrapManyDataKeyResult`
- Support for the `crypt_shared` library to replace `mongocryptd` using the new
`crypt_shared_lib_path` and `crypt_shared_lib_required` arguments to `pymongo.encryption_options.AutoEncryptionOpts`.

Bug fixes .........

- Fixed a bug where `pymongo.collection.Collection.estimated_document_count`
would fail with a "CommandNotSupportedOnView" error on views (PYTHON-2885).

- Fixed a bug where invalid UTF-8 strings could be passed as patterns for `bson.regex.Regex`
objects. `bson.encode` now correctly raises `bson.errors.InvalidStringData` (PYTHON-3048).

- Fixed a bug that caused `AutoReconnect("connection pool paused")` errors in the child
process after fork (PYTHON-3257).

- Fixed a bug where  `pymongo.collection.Collection.count_documents` and
`pymongo.collection.Collection.distinct` would fail in a transaction with `directConnection=True` (PYTHON-3333).

- GridFS no longer uploads an incomplete files collection document after encountering an
error in the middle of an upload fork. This results in fewer `gridfs.errors.CorruptGridFile` errors (PYTHON-1552).

- Renamed PyMongo's internal C extension methods to avoid crashing due to name conflicts
with mpi4py and other shared libraries (PYTHON-2110).

- Fixed tight CPU loop for network I/O when using PyOpenSSL (PYTHON-3187).
Unavoidable breaking changes ............................

- pymongocrypt 1.3.0 or later is now required for client side field level
encryption support.

- `pymongo.collection.Collection.estimated_document_count` now always uses
the count command. Due to an oversight in versions 5.0.0-5.0.8 of MongoDB, the count command was not included in V1 of the [Stable API](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/connect/connection-options/stable-api/#stable-api). Users of the Stable API with estimated_document_count are recommended to upgrade their server version to 5.0.9+ or set `pymongo.server_api.ServerApi.strict` to `False` to avoid encountering errors (PYTHON-3167).

- Removed generic typing from `pymongo.client_session.ClientSession` to improve
support for Pyright (PYTHON-3283).

- Added `__all__` to the bson, pymongo, and gridfs packages. This could be a breaking
change for apps that relied on `from bson import * to import APIs not present in _all__` (PYTHON-3311).

Issues Resolved ...............

See the PyMongo 4.2 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 4.1.1 (2022/04/13)

Version 4.1.1 fixes a number of bugs:

- Fixed a memory leak bug when calling `bson.decode_all` without a
`codec_options` argument (PYTHON-3222).

- Fixed a bug where `bson.decode_all` did not accept `codec_options`
as a keyword argument (PYTHON-3222).

- Fixed an oversight where type markers (py.typed files) were not included
in our release distributions (PYTHON-3214).

- Fixed a bug where pymongo would raise a "NameError: name sys is not defined"
exception when attempting to parse a "mongodb+srv://" URI when the dnspython dependency was not installed (PYTHON-3198).

Issues Resolved ...............

See the PyMongo 4.1.1 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 4.1 (2021/12/07)

> **Warning:**

PyMongo 4.1 brings a number of improvements including:

- Type Hinting support (formerly provided by pymongo-stubs).  See [Type Hints](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/run-command/#type-hints) for more information.
- Added support for the `comment` parameter to all helpers. For example see
`pymongo.collection.Collection.insert_one`.

- Added support for the `let` parameter to
`pymongo.collection.Collection.update_one`, `pymongo.collection.Collection.update_many`, `pymongo.collection.Collection.delete_one`, `pymongo.collection.Collection.delete_many`, `pymongo.collection.Collection.replace_one`, `pymongo.collection.Collection.aggregate`, `pymongo.collection.Collection.find_one_and_delete`, `pymongo.collection.Collection.find_one_and_replace`, `pymongo.collection.Collection.find_one_and_update`, `pymongo.collection.Collection.find`, `pymongo.collection.Collection.find_one`, and `pymongo.collection.Collection.bulk_write`. `let` is a map of parameter names and values. Parameters can then be accessed as variables in an aggregate expression context.

- `pymongo.collection.Collection.aggregate` now supports
$merge and $out executing on secondaries on MongoDB >=5.0. aggregate() now always obeys the collection's `read_preference` on MongoDB >= 5.0.

- `gridfs.grid_file.GridOut.seek` now returns the new position in the file, to
conform to the behavior of `io.IOBase.seek`.

- Improved reuse of implicit sessions (PYTHON-2956).
Bug fixes .........

- Fixed bug that would cause SDAM heartbeat timeouts and connection churn on
AWS Lambda and other FaaS environments (PYTHON-3186).

- Fixed bug where `pymongo.mongo_client.MongoClient`,
`pymongo.database.Database`, and `pymongo.collection.Collection` mistakenly implemented `typing.Iterable` (PYTHON-3084).

Issues Resolved ...............

See the PyMongo 4.1 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 4.0.2 (2022/03/03)

- No changes
## Changes in Version 4.0.1 (2021/12/07)

- No changes
## Changes in Version 4.0 (2021/11/29)

> **Warning:**

> **Warning:**

> **Warning:** keyword argument to `pymongo.mongo_client.MongoClient`
to `False` instead of `None`, allowing for the automatic
discovery of replica sets. This means that if you
want a direct connection to a single server you must pass
`directConnection=True` as a URI option or keyword argument.
For more details, see the relevant section of the PyMongo 4.x migration
guide: `pymongo4-migration-direct-connection`.

PyMongo 4.0 brings a number of improvements as well as some backward breaking changes. For example, all APIs deprecated in PyMongo 3.X have been removed. Be sure to read the changes listed below and the `migrate-to-pymongo4` before upgrading from PyMongo 3.x.

Breaking Changes in 4.0 .......................

- Removed support for Python 2.7, 3.4, and 3.5. Python 3.6.2+ is now required.
- The default uuid_representation for `bson.codec_options.CodecOptions`,
`bson.json_util.JSONOptions`, and `pymongo.mongo_client.MongoClient` has been changed from `bson.binary.UuidRepresentation.PYTHON_LEGACY` to `bson.binary.UuidRepresentation.UNSPECIFIED`. Attempting to encode a `uuid.UUID` instance to BSON or JSON now produces an error by default. See [UUID representations](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/data-formats/uuid/#universally-unique-ids--uuids-) for details.

- Removed the `waitQueueMultiple` keyword argument to
`pymongo.mongo_client.MongoClient` and removed `pymongo.errors.ExceededMaxWaiters`.

- Removed the `socketKeepAlive` keyword argument to
`pymongo.mongo_client.MongoClient`.

- Removed `pymongo.mongo_client.MongoClient.fsync`,
`pymongo.mongo_client.MongoClient.unlock`, and `pymongo.mongo_client.MongoClient.is_locked`.

- Removed `pymongo.mongo_client.MongoClient.database_names`.
- Removed `pymongo.mongo_client.MongoClient.max_bson_size`.
- Removed `pymongo.mongo_client.MongoClient.max_message_size`.
- Removed `pymongo.mongo_client.MongoClient.max_write_batch_size`.
- Removed `pymongo.mongo_client.MongoClient.event_listeners`.
- Removed `pymongo.mongo_client.MongoClient.max_pool_size`.
- Removed `pymongo.mongo_client.MongoClient.max_idle_time_ms`.
- Removed `pymongo.mongo_client.MongoClient.local_threshold_ms`.
- Removed `pymongo.mongo_client.MongoClient.server_selection_timeout`.
- Removed `pymongo.mongo_client.MongoClient.retry_writes`.
- Removed `pymongo.mongo_client.MongoClient.retry_reads`.
- Removed `pymongo.database.Database.eval`,
`pymongo.database.Database.system_js` and `pymongo.database.SystemJS`.

- Removed `pymongo.database.Database.collection_names`.
- Removed `pymongo.database.Database.current_op`.
- Removed `pymongo.database.Database.authenticate` and
`pymongo.database.Database.logout`.

- Removed `pymongo.database.Database.error`,
`pymongo.database.Database.last_status`, `pymongo.database.Database.previous_error`, `pymongo.database.Database.reset_error_history`.

- Removed `pymongo.database.Database.add_user` and
`pymongo.database.Database.remove_user`.

- Removed support for database profiler helpers
`pymongo.database.Database.profiling_level`, `pymongo.database.Database.set_profiling_level`, and `pymongo.database.Database.profiling_info`. Instead, users should run the profile command with the `pymongo.database.Database.command` helper directly.

- Removed `pymongo.OFF`, `pymongo.SLOW_ONLY`, and
`pymongo.ALL`.

- Removed `pymongo.collection.Collection.parallel_scan`.
- Removed `pymongo.collection.Collection.ensure_index`.
- Removed `pymongo.collection.Collection.reindex`.
- Removed `pymongo.collection.Collection.save`.
- Removed `pymongo.collection.Collection.insert`.
- Removed `pymongo.collection.Collection.update`.
- Removed `pymongo.collection.Collection.remove`.
- Removed `pymongo.collection.Collection.find_and_modify`.
- Removed `pymongo.collection.Collection.count`.
- Removed `pymongo.collection.Collection.initialize_ordered_bulk_op`,
`pymongo.collection.Collection.initialize_unordered_bulk_op`, and `pymongo.bulk.BulkOperationBuilder`. Use `pymongo.collection.Collection.bulk_write` instead.

- Removed `pymongo.collection.Collection.group`.
- Removed `pymongo.collection.Collection.map_reduce` and
`pymongo.collection.Collection.inline_map_reduce`.

- Removed the `useCursor` option for
`pymongo.collection.Collection.aggregate`.

- Removed `pymongo.mongo_client.MongoClient.close_cursor`. Use
`pymongo.cursor.Cursor.close` instead.

- Removed `pymongo.mongo_client.MongoClient.kill_cursors`.
- Removed `pymongo.cursor_manager.CursorManager` and
`pymongo.cursor_manager`.

- Removed `pymongo.mongo_client.MongoClient.set_cursor_manager`.
- Removed `pymongo.cursor.Cursor.count`.
- Removed `pymongo.thread_util`.
- Removed `pymongo.mongo_replica_set_client.MongoReplicaSetClient`.
- Removed `pymongo.ismaster.IsMaster`.
Use `pymongo.hello.Hello` instead.

- Removed `pymongo.son_manipulator`,
`pymongo.son_manipulator.SONManipulator`, `pymongo.son_manipulator.ObjectIdInjector`, `pymongo.son_manipulator.ObjectIdShuffler`, `pymongo.son_manipulator.AutoReference`, `pymongo.son_manipulator.NamespaceInjector`, `pymongo.database.Database.add_son_manipulator`, `pymongo.database.Database.outgoing_copying_manipulators`, `pymongo.database.Database.outgoing_manipulators`, `pymongo.database.Database.incoming_copying_manipulators`, and `pymongo.database.Database.incoming_manipulators`.

- Removed the `manipulate` and `modifiers` parameters from
`pymongo.collection.Collection.find`, `pymongo.collection.Collection.find_one`, `pymongo.collection.Collection.find_raw_batches`, and `pymongo.cursor.Cursor`.

- Removed `pymongo.message.delete`, `pymongo.message.get_more`,
`pymongo.message.insert`, `pymongo.message.kill_cursors`, `pymongo.message.query`, and `pymongo.message.update`.

- Removed `pymongo.errors.NotMasterError`.
Use `pymongo.errors.NotPrimaryError` instead.

- Removed `pymongo.errors.CertificateError`.
- Removed `pymongo.GEOHAYSTACK`.
- Removed `bson.binary.UUIDLegacy`.
- Removed :const:`bson.json_util.STRICT_JSON_OPTIONS`. Use
:const:`~bson.json_util.RELAXED_JSON_OPTIONS` or :const:`~bson.json_util.CANONICAL_JSON_OPTIONS` instead.

- Changed the default JSON encoding representation from legacy to relaxed.
The json_mode parameter for :const:`bson.json_util.dumps` now defaults to :const:`~bson.json_util.RELAXED_JSON_OPTIONS`.

- Changed the BSON and JSON decoding behavior of `bson.dbref.DBRef`
to match the behavior outlined in the DBRef specification version 1.0. Specifically, PyMongo now only decodes a subdocument into a `bson.dbref.DBRef` if and only if, it contains both `$ref` and `$id` fields and the `$ref`, `$id`, and `$db` fields are of the correct type. Otherwise the document is returned as normal. Previously, any subdocument containing a `$ref` field would be decoded as a `bson.dbref.DBRef`.

- The "tls" install extra is no longer necessary or supported and will be
ignored by pip.

- The `tz_aware` argument to `bson.json_util.JSONOptions`
now defaults to `False` instead of `True`. `bson.json_util.loads` now decodes datetime as naive by default. See `tz_aware_default_change` for more info.

- `directConnection` URI option and keyword argument to `pymongo.mongo_client.MongoClient`
defaults to `False` instead of `None`, allowing for the automatic discovery of replica sets. This means that if you want a direct connection to a single server you must pass `directConnection=True` as a URI option or keyword argument.

- The `hint` option is now required when using `min` or `max` queries
with `pymongo.collection.Collection.find`.

- `name` is now a required argument for the `pymongo.driver_info.DriverInfo` class.
- When providing a "mongodb+srv://" URI to
`pymongo.mongo_client.MongoClient` constructor you can now use the `srvServiceName` URI option to specify your own SRV service name.

- `bson.son.SON.items` now returns a `dict_items` object rather
than a list.

- Removed `bson.son.SON.iteritems`.
- `pymongo.collection.Collection` and `pymongo.database.Database`
now raises an error upon evaluating as a Boolean, please use the syntax `if collection is not None:` or `if database is not None:` as opposed to the previous syntax which was simply `if collection:` or `if database:`. You must now explicitly compare with None.

- `pymongo.mongo_client.MongoClient` cannot execute any operations
after being closed. The previous behavior would simply reconnect. However, now you must create a new instance.

- Classes `bson.int64.Int64`, `bson.min_key.MinKey`,
`bson.max_key.MaxKey`, `bson.timestamp.Timestamp`, `bson.regex.Regex`, and `bson.dbref.DBRef all implement _slots__` now. This means that their attributes are fixed, and new attributes cannot be added to them at runtime.

- Empty projections (eg {} or []) for
`pymongo.collection.Collection.find`, and `pymongo.collection.Collection.find_one` are passed to the server as-is rather than the previous behavior which substituted in a projection of `{"_id": 1}`. This means that an empty projection will now return the entire document, not just the `"_id"` field.

- `pymongo.mongo_client.MongoClient` now raises a
`pymongo.errors.ConfigurationError` when more than one URI is passed into the `hosts` argument.

- `pymongo.mongo_client.MongoClient`` now raises an
`pymongo.errors.InvalidURI` exception when it encounters unescaped percent signs in username and password when parsing MongoDB URIs.

- Comparing two `pymongo.mongo_client.MongoClient` instances now
uses a set of immutable properties rather than `pymongo.mongo_client.MongoClient.address` which can change.

- Removed the `disable_md5` parameter for `gridfs.GridFSBucket` and
`gridfs.GridFS`. See `removed-gridfs-checksum` for details.

- pymongocrypt 1.2.0 or later is now required for client side field level
encryption support.

Notable improvements ....................

- Enhanced connection pooling to create connections more efficiently and
avoid connection storms.

- Added the `maxConnecting` URI and
`pymongo.mongo_client.MongoClient` keyword argument.

- `pymongo.mongo_client.MongoClient` now accepts a URI and keyword
argument `srvMaxHosts` that limits the number of mongos-like hosts a client will connect to. More specifically, when a mongodb+srv:// connection string resolves to more than `srvMaxHosts` number of hosts, the client will randomly choose a `srvMaxHosts` sized subset of hosts.

- Added `pymongo.mongo_client.MongoClient.options` for read-only access
to a client's configuration options.

- Support for the "kmip" KMS provider for client side field level encryption.
See the docstring for `pymongo.encryption_options.AutoEncryptionOpts` and `pymongo.encryption`.

Issues Resolved ...............

See the PyMongo 4.0 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 3.13.0 (2022/11/01)

Version 3.13 provides an upgrade path to PyMongo 4.x. Most of the API changes from PyMongo 4.0 have been backported in a backward compatible way, allowing applications to be written against PyMongo >= 3.13, rather then PyMongo 3.x or PyMongo 4.x. See the PyMongo 4 Migration Guide for detailed examples.

Notable improvements ....................

- Added `pymongo.mongo_client.MongoClient.options` for read-only access
to a client's configuration options.

Issues Resolved ...............

PyMongo 3.13 drops support for Python 3.4.

Bug fixes .........

- Fixed a memory leak bug when calling `bson.decode_all` without a
`codec_options` argument (PYTHON-3222).

- Fixed a bug where `bson.decode_all` did not accept `codec_options`
as a keyword argument (PYTHON-3222).

Deprecations ............

- Deprecated `pymongo.collection.Collection.map_reduce` and
`pymongo.collection.Collection.inline_map_reduce`. Use `pymongo.collection.Collection.aggregate` instead.

- Deprecated `pymongo.mongo_client.MongoClient.event_listeners`.
Use `pymongo.mongo_client.options.event_listeners` instead.

- Deprecated `pymongo.mongo_client.MongoClient.max_pool_size`.
Use `pymongo.mongo_client.options.pool_options.max_pool_size` instead.

- Deprecated `pymongo.mongo_client.MongoClient.max_idle_time_ms`.
Use `pymongo.mongo_client.options.pool_options.max_idle_time_seconds` instead.

- Deprecated `pymongo.mongo_client.MongoClient.local_threshold_ms`.
Use `pymongo.mongo_client.options.local_threshold_ms` instead.

- Deprecated `pymongo.mongo_client.MongoClient.server_selection_timeout`.
Use `pymongo.mongo_client.options.server_selection_timeout` instead.

- Deprecated `pymongo.mongo_client.MongoClient.retry_writes`.
Use `pymongo.mongo_client.options.retry_writes` instead.

- Deprecated `pymongo.mongo_client.MongoClient.retry_reads`.
Use `pymongo.mongo_client.options.retry_reads` instead.

- Deprecated `pymongo.mongo_client.MongoClient.max_bson_size`,
`pymongo.mongo_client.MongoClient.max_message_size`, and `pymongo.mongo_client.MongoClient.max_write_batch_size`. These helpers were incorrect when in `loadBalanced=true mode` and ambiguous in clusters with mixed versions. Use the hello command to get the authoritative value from the remote server instead. Code like this:

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

See the PyMongo 3.13.0 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 3.12.3 (2021/12/07)

Issues Resolved ...............

Version 3.12.3 fixes a bug that prevented `bson.json_util.loads` from decoding a document with a non-string "$regex" field (PYTHON-3028).

See the PyMongo 3.12.3 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 3.12.2 (2021/11/29)

Issues Resolved ...............

Version 3.12.2 fixes a number of bugs:

- Fixed a bug that prevented PyMongo from retrying bulk writes
after a `writeConcernError` on MongoDB 4.4+ (PYTHON-2984).

- Fixed a bug that could cause the driver to hang during automatic
client side field level encryption (PYTHON-3017).

See the PyMongo 3.12.2 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 3.12.1 (2021/10/19)

Issues Resolved ...............

Version 3.12.1 fixes a number of bugs:

- Fixed a bug that caused a multi-document transaction to fail when the first
operation was large bulk write (>48MB) that required splitting a batched write command (PYTHON-2915).

- Fixed a bug that caused the `tlsDisableOCSPEndpointCheck` URI option to
be applied incorrectly (PYTHON-2866).

See the PyMongo 3.12.1 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 3.12.0 (2021/07/13)

> **Warning:** These Python versions will not be supported by PyMongo 4.

> **Warning:** dots ('.') or start with dollar signs ('$').

- pymongocrypt 1.1.0 or later is now required for client side field level
encryption support.

- Iterating over `gridfs.grid_file.GridOut` now moves through
the file line by line instead of chunk by chunk, and does not restart at the top for subsequent iterations on the same object. Call `seek(0)` to reset the iterator.

Notable improvements ....................

- Added support for MongoDB 5.0.
- Support for MongoDB Stable API, see `pymongo.server_api.ServerApi`.
- Support for snapshot reads on secondaries (see [snapshot reads](https://www.mongodb.com/docs/manual/reference/read-concern-snapshot/#read-concern--snapshot-)).
- Support for Azure and GCP KMS providers for client side field level
encryption. See the docstring for `pymongo.mongo_client.MongoClient`, `pymongo.encryption_options.AutoEncryptionOpts`, and `pymongo.encryption`.

- Support AWS authentication with temporary credentials when connecting to KMS
in client side field level encryption.

- Support for connecting to load balanced MongoDB clusters via the new
`loadBalanced` URI option.

- Support for creating timeseries collections via the `timeseries` and
`expireAfterSeconds` arguments to `pymongo.database.Database.create_collection`.

- Added `pymongo.mongo_client.MongoClient.topology_description`.
- Added hash support to `pymongo.mongo_client.MongoClient`,
`pymongo.database.Database` and `pymongo.collection.Collection` (PYTHON-2466).

- Improved the error message returned by
`pymongo.collection.Collection.insert_many` when supplied with an argument of incorrect type (PYTHON-1690).

- Added session and read concern support to
`pymongo.collection.Collection.find_raw_batches` and `pymongo.collection.Collection.aggregate_raw_batches`.

Bug fixes .........

- Fixed a bug that could cause the driver to deadlock during automatic
client side field level encryption (PYTHON-2472).

- Fixed a potential deadlock when garbage collecting an unclosed exhaust
`pymongo.cursor.Cursor`.

- Fixed an bug where using gevent.Timeout to timeout an operation could
lead to a deadlock.

- Fixed the following bug with Atlas Data Lake. When closing cursors,
pymongo now sends killCursors with the namespace returned the cursor's initial command response.

- Fixed a bug in `pymongo.cursor.RawBatchCursor` that caused it to
return an empty bytestring when the cursor contained no results. It now raises `StopIteration` instead.

Deprecations ............

- Deprecated support for Python 2.7, 3.4 and 3.5.
- Deprecated support for database profiler helpers
`pymongo.database.Database.profiling_level`, `pymongo.database.Database.set_profiling_level`, and `pymongo.database.Database.profiling_info`. Instead, users should run the profile command with the `pymongo.database.Database.command` helper directly.

- Deprecated `pymongo.errors.NotMasterError`. Users should
use `pymongo.errors.NotPrimaryError` instead.

- Deprecated `pymongo.ismaster.IsMaster` and `pymongo.ismaster`
which will be removed in PyMongo 4.0 and are replaced by `pymongo.hello.Hello` and `pymongo.hello` which provide the same API.

- Deprecated the `pymongo.messeage` module.
- Deprecated the `ssl_keyfile` and `ssl_certfile` URI options in favor
of `tlsCertificateKeyFile` (see [TLS](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/security/tls/#configure-transport-layer-security--tls-)).

Issues Resolved ...............

See the PyMongo 3.12.0 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 3.11.3 (2021/02/02)

Issues Resolved ...............

Version 3.11.3 fixes a bug that prevented PyMongo from retrying writes after a `writeConcernError` on MongoDB 4.4+ (PYTHON-2452)

See the PyMongo 3.11.3 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 3.11.2 (2020/12/02)

Issues Resolved ...............

Version 3.11.2 includes a number of bugfixes. Highlights include:

- Fixed a memory leak caused by failing SDAM monitor checks on Python 3 (PYTHON-2433).
- Fixed a regression that changed the string representation of
`pymongo.errors.BulkWriteError` (PYTHON-2438).

- Fixed a bug that made it impossible to use
`bson.codec_options.CodecOptions.with_options` and `bson.json_util.JSONOptions.with_options` on some early versions of Python 3.4 and Python 3.5 due to a bug in the standard library implementation of `collections.namedtuple._asdict` (PYTHON-2440).

- Fixed a bug that resulted in a `TypeError` exception when a PyOpenSSL
socket was configured with a timeout of `None` (PYTHON-2443).

See the PyMongo 3.11.2 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 3.11.1 (2020/11/17)

Version 3.11.1 adds support for Python 3.9 and includes a number of bugfixes. Highlights include:

- Support for Python 3.9.
- Initial support for Azure and GCP KMS providers for client side field level
encryption is in beta. See the docstring for `pymongo.mongo_client.MongoClient`, `pymongo.encryption_options.AutoEncryptionOpts`, and `pymongo.encryption`. **Note: Backwards-breaking changes may be made before the final release.**

- Fixed a bug where the `bson.json_util.JSONOptions` API did not match
the `bson.codec_options.CodecOptions` API due to the absence of a `bson.json_util.JSONOptions.with_options` method. This method has now been added.

- Fixed a bug which made it impossible to serialize
`pymongo.errors.BulkWriteError` instances using `pickle`.

- Fixed a bug wherein PyMongo did not always discard an implicit session after
encountering a network error.

- Fixed a bug where connections created in the background were not
authenticated.

- Fixed a memory leak in the `bson` module when using a
`bson.codec_options.TypeRegistry`.

Issues Resolved ...............

See the PyMongo 3.11.1 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 3.11.0 (2020/07/30)

Version 3.11 adds support for MongoDB 4.4 and includes a number of bug fixes. Highlights include:

- Support for [OCSP](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/security/tls/#ocsp) (Online Certificate Status Protocol).
- Support for [PyOpenSSL](https://pypi.org/project/pyOpenSSL/) as an
alternative TLS implementation. PyOpenSSL is required for [OCSP](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/security/tls/#ocsp) support. It will also be installed when using the "tls" extra if the version of Python in use is older than 2.7.9.

- Support for the [MONGODB-AWS](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/security/authentication/aws-iam/#aws-identity-and-access-management) authentication mechanism.
- Support for the `directConnection` URI option and kwarg to
`pymongo.mongo_client.MongoClient`.

- Support for speculative authentication attempts in connection handshakes
which reduces the number of network roundtrips needed to authenticate new connections on MongoDB 4.4+.

- Support for creating collections in multi-document transactions with
`pymongo.database.Database.create_collection` on MongoDB 4.4+.

- Added index hinting support to the
`pymongo.collection.Collection.replace_one`, `pymongo.collection.Collection.update_one`, `pymongo.collection.Collection.update_many`, `pymongo.collection.Collection.find_one_and_replace`, `pymongo.collection.Collection.find_one_and_update`, `pymongo.collection.Collection.delete_one`, `pymongo.collection.Collection.delete_many`, and `pymongo.collection.Collection.find_one_and_delete` commands.

- Added index hinting support to the
`pymongo.operations.ReplaceOne`, `pymongo.operations.UpdateOne`, `pymongo.operations.UpdateMany`, `pymongo.operations.DeleteOne`, and `pymongo.operations.DeleteMany` bulk operations.

- Added support for `bson.binary.UuidRepresentation.UNSPECIFIED` and
`MongoClient(uuidRepresentation='unspecified')` which will become the default UUID representation starting in PyMongo 4.0. See [UUID representations](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/data-formats/uuid/#universally-unique-ids--uuids-) for details.

- New methods `bson.binary.Binary.from_uuid` and
`bson.binary.Binary.as_uuid`.

- Added the `background` parameter to
`pymongo.database.Database.validate_collection`. For a description of this parameter see the MongoDB documentation for the validate command.

- Added the `allow_disk_use` parameters to
`pymongo.collection.Collection.find`.

- Added the `hedge` parameter to
`pymongo.read_preferences.PrimaryPreferred`, `pymongo.read_preferences.Secondary`, `pymongo.read_preferences.SecondaryPreferred`, `pymongo.read_preferences.Nearest` to support disabling (or explicitly enabling) hedged reads in MongoDB 4.4+.

- Fixed a bug in change streams that could cause PyMongo to miss some change
documents when resuming a stream that was started without a resume token and whose first batch did not contain any change documents.

- Fixed an bug where using gevent.Timeout to timeout an operation could
lead to a deadlock.

Deprecations:

- Deprecated the `oplog_replay` parameter to
`pymongo.collection.Collection.find`. Starting in MongoDB 4.4, the server optimizes queries against the oplog collection without requiring the user to set this flag.

- Deprecated `pymongo.collection.Collection.reindex`. Use
`pymongo.database.Database.command` to run the `reIndex` command instead.

- Deprecated `pymongo.mongo_client.MongoClient.fsync`. Use
`pymongo.database.Database.command` to run the `fsync` command instead.

- Deprecated `pymongo.mongo_client.MongoClient.unlock`. Use
`pymongo.database.Database.command` to run the `fsyncUnlock` command instead. See the documentation for more information.

- Deprecated `pymongo.mongo_client.MongoClient.is_locked`. Use
`pymongo.database.Database.command` to run the `currentOp` command instead. See the documentation for more information.

- Deprecated `bson.binary.UUIDLegacy`. Use
`bson.binary.Binary.from_uuid` instead.

Unavoidable breaking changes:

- `gridfs.GridFSBucket` and `gridfs.GridFS` do not support
multi-document transactions. Running a GridFS operation in a transaction now always raises the following error: `InvalidOperation: GridFS does not support multi-document transactions`

Issues Resolved ...............

See the PyMongo 3.11.0 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 3.10.1 (2020/01/07)

Version 3.10.1 fixes the following issues discovered since the release of 3.10.0:

- Fix a TypeError logged to stderr that could be triggered during server
maintenance or during `pymongo.mongo_client.MongoClient.close`.

- Avoid creating new connections during
`pymongo.mongo_client.MongoClient.close`.

Issues Resolved ...............

See the PyMongo 3.10.1 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 3.10.0 (2019/12/10)

Version 3.10 includes a number of improvements and bug fixes. Highlights include:

- Support for Client-Side Field Level Encryption with MongoDB 4.2. See
[Client-Side Field Level Encryption](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/security/in-use-encryption/#client-side-field-level-encryption) for examples.

- Support for Python 3.8.
- Added `pymongo.client_session.ClientSession.in_transaction`.
- Do not hold the Topology lock while creating connections in a MongoClient's
background thread. This change fixes a bug where application operations would block while the background thread ensures that all server pools have minPoolSize connections.

- Fix a UnicodeDecodeError bug when coercing a PyMongoError with a non-ascii
error message to unicode on Python 2.

- Fix an edge case bug where PyMongo could exceed the server's
maxMessageSizeBytes when generating a compressed bulk write command.

Issues Resolved ...............

See the PyMongo 3.10 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 3.9.0 (2019/08/13)

Version 3.9 adds support for MongoDB 4.2. Highlights include:

- Support for MongoDB 4.2 sharded transactions. Sharded transactions have
the same API as replica set transactions. See [Transactions](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/crud/transactions/#transactions).

- New method `pymongo.client_session.ClientSession.with_transaction` to
support conveniently running a transaction in a session with automatic retries and at-most-once semantics.

- Initial support for client side field level encryption. See the docstring for
`pymongo.mongo_client.MongoClient`, `pymongo.encryption_options.AutoEncryptionOpts`, and `pymongo.encryption` for details. **Note: Support for client side encryption is in beta. Backwards-breaking changes may be made before the final release.**

- Added the `max_commit_time_ms` parameter to
`pymongo.client_session.ClientSession.start_transaction`.

- Implement the URI options specification in the
`pymongo.mongo_client.MongoClient` constructor. Consequently, there are a number of changes in connection options:

- The `tlsInsecure` option has been added.
- The `tls` option has been added. The older `ssl` option has been retained
as an alias to the new `tls` option.

- `wTimeout` has been deprecated in favor of `wTimeoutMS`.
- `wTimeoutMS` now overrides `wTimeout` if the user provides both.
- `j` has been deprecated in favor of `journal`.
- `journal` now overrides `j` if the user provides both.
- `ssl_cert_reqs` has been deprecated in favor of `tlsAllowInvalidCertificates`.
Instead of `ssl.CERT_NONE`, `ssl.CERT_OPTIONAL` and `ssl.CERT_REQUIRED`, the new option expects a boolean value - `True` is equivalent to `ssl.CERT_NONE`, while `False` is equivalent to `ssl.CERT_REQUIRED`.

- `ssl_match_hostname` has been deprecated in favor of `tlsAllowInvalidHostnames`.
- `ssl_ca_certs` has been deprecated in favor of `tlsCAFile`.
- `ssl_certfile` has been deprecated in favor of `tlsCertificateKeyFile`.
- `ssl_pem_passphrase` has been deprecated in favor of `tlsCertificateKeyFilePassword`.
- `waitQueueMultiple` has been deprecated without replacement. This option
was a poor solution for putting an upper bound on queuing since it didn't affect queuing in other parts of the driver.

- The `retryWrites` URI option now defaults to `True`. Supported write
operations that fail with a retryable error will automatically be retried one time, with at-most-once semantics.

- Support for retryable reads and the `retryReads` URI option which is
enabled by default. See the `pymongo.mongo_client.MongoClient` documentation for details. Now that supported operations are retried automatically and transparently, users should consider adjusting any custom retry logic to prevent an application from inadvertently retrying for too long.

- Support zstandard for wire protocol compression.
- Support for periodically polling DNS SRV records to update the mongos proxy
list without having to change client configuration.

- New method `pymongo.database.Database.aggregate` to support running
database level aggregations.

- Support for publishing Connection Monitoring and Pooling events via the new
`pymongo.monitoring.ConnectionPoolListener` class. See `pymongo.monitoring` for an example.

- `pymongo.collection.Collection.aggregate` and
`pymongo.database.Database.aggregate` now support the `$merge` pipeline stage and use read preference `pymongo.read_preferences.ReadPreference.PRIMARY` if the `$out` or `$merge` pipeline stages are used.

- Support for specifying a pipeline or document in
`pymongo.collection.Collection.update_one`, `pymongo.collection.Collection.update_many`, `pymongo.collection.Collection.find_one_and_update`, `pymongo.operations.UpdateOne`, and `pymongo.operations.UpdateMany`.

- New BSON utility functions `bson.encode` and `bson.decode`
- `bson.binary.Binary` now supports any bytes-like type that implements
the buffer protocol.

- Resume tokens can now be accessed from a `ChangeStream` cursor using the
`pymongo.change_stream.ChangeStream.resume_token` attribute.

- Connections now survive primary step-down when using MongoDB 4.2+.
Applications should expect less socket connection turnover during replica set elections.

Unavoidable breaking changes:

- Applications that use MongoDB with the MMAPv1 storage engine must now
explicitly disable retryable writes via the connection string (e.g. `MongoClient("mongodb://my.mongodb.cluster/db?retryWrites=false")`) or the `pymongo.mongo_client.MongoClient` constructor's keyword argument (e.g. `MongoClient("mongodb://my.mongodb.cluster/db", retryWrites=False)`) to avoid running into `pymongo.errors.OperationFailure` exceptions during write operations. The MMAPv1 storage engine is deprecated and does not support retryable writes which are now turned on by default.

- In order to ensure that the `connectTimeoutMS` URI option is honored when
connecting to clusters with a `mongodb+srv://` connection string, the minimum required version of the optional `dnspython` dependency has been bumped to 1.16.0. This is a breaking change for applications that use PyMongo's SRV support with a version of `dnspython` older than 1.16.0.

Issues Resolved ...............

See the PyMongo 3.9 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 3.8.0 (2019/04/22)

> **Warning:** Python 2.7 or newer from Red Hat Software Collections.
CentOS 6 users should install Python 2.7 or newer from `SCL
<https://wiki.centos.org/AdditionalResources/Repositories/SCL>`_

> **Warning:** must upgrade to PyPy3.5+.

- `bson.objectid.ObjectId` now implements the `ObjectID specification
version 0.2 <https://github.com/mongodb/specifications/blob/master/source/bson-objectid/objectid.md>`_.

- For better performance and to better follow the GridFS spec,
`gridfs.grid_file.GridOut` now uses a single cursor to read all the chunks in the file. Previously, each chunk in the file was queried individually using `pymongo.collection.Collection.find_one`.

- `gridfs.grid_file.GridOut.read` now only checks for extra chunks after
reading the entire file. Previously, this method would check for extra chunks on every call.

- `pymongo.database.Database.current_op` now always uses the
`Database`'s  `pymongo.database.Database.codec_options` when decoding the command response. Previously the codec_options was only used when the MongoDB server version was <= 3.0.

- Undeprecated `pymongo.mongo_client.MongoClient.get_default_database`
and added the `default` parameter.

- TLS Renegotiation is now disabled when possible.
- Custom types can now be directly encoded to, and decoded from MongoDB using
the `bson.codec_options.TypeCodec` and `bson.codec_options.TypeRegistry` APIs. For more information, see [Custom Types](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/data-formats/custom-types/type-codecs/#encode-data-with-type-codecs).

- Attempting a multi-document transaction on a sharded cluster now raises a
`pymongo.errors.ConfigurationError`.

- `pymongo.cursor.Cursor.distinct` and
`pymongo.cursor.Cursor.count` now send the Cursor's `pymongo.cursor.Cursor.comment` as the "comment" top-level command option instead of "$comment". Also, note that "comment" must be a string.

- Add the `filter` parameter to
`pymongo.database.Database.list_collection_names`.

- Changes can now be requested from a `ChangeStream` cursor without blocking
indefinitely using the new `pymongo.change_stream.ChangeStream.try_next` method.

- Fixed a reference leak bug when splitting a batched write command based on
maxWriteBatchSize or the max message size.

- Deprecated running find queries that set `pymongo.cursor.Cursor.min`
and/or `pymongo.cursor.Cursor.max` but do not also set a `pymongo.cursor.Cursor.hint` of which index to use. The find command is expected to require a `pymongo.cursor.Cursor.hint` when using min/max starting in MongoDB 4.2.

- Documented support for the uuidRepresentation URI option, which has been
supported since PyMongo 2.7. Valid values are `pythonLegacy` (the default), `javaLegacy`, `csharpLegacy` and `standard`. New applications should consider setting this to `standard` for cross language compatibility.

- `bson.raw_bson.RawBSONDocument` now validates that the `bson_bytes`
passed in represent a single bson document. Earlier versions would mistakenly accept multiple bson documents.

- Iterating over a `bson.raw_bson.RawBSONDocument` now maintains the
same field order of the underlying raw BSON document.

- Applications can now register a custom server selector. For more information
see [Customize Server Selection](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/connect/connection-options/server-selection/#customize-server-selection).

- The connection pool now implements a LIFO policy.
Unavoidable breaking changes:

- In order to follow the ObjectID Spec version 0.2, an ObjectId's 3-byte
machine identifier and 2-byte process id have been replaced with a single 5-byte random value generated per process. This is a breaking change for any application that attempts to interpret those bytes.

Issues Resolved ...............

See the PyMongo 3.8 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 3.7.2 (2018/10/10)

Version 3.7.2 fixes a few issues discovered since the release of 3.7.1.

- Fixed a bug in retryable writes where a previous command's "txnNumber"
field could be sent leading to incorrect results.

- Fixed a memory leak of a few bytes on some insert, update, or delete
commands when running against MongoDB 3.6+.

- Fixed a bug that caused `pymongo.collection.Collection.ensure_index`
to only cache a single index per database.

- Updated the documentation examples to use
`pymongo.collection.Collection.count_documents` instead of `pymongo.collection.Collection.count` and `pymongo.cursor.Cursor.count`.

Issues Resolved ...............

See the PyMongo 3.7.2 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 3.7.1 (2018/07/16)

Version 3.7.1 fixes a few issues discovered since the release of 3.7.0.

- Calling `pymongo.database.Database.authenticate` more than once
with the same credentials results in OperationFailure.

- Authentication fails when SCRAM-SHA-1 is used to authenticate users with
only MONGODB-CR credentials.

- A millisecond rounding problem when decoding datetimes in the pure Python
BSON decoder on 32 bit systems and AWS lambda.

Issues Resolved ...............

See the PyMongo 3.7.1 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 3.7.0 (2018/06/26)

Version 3.7 adds support for MongoDB 4.0. Highlights include:

- Support for single replica set multi-document ACID transactions.
See [transactions](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/crud/transactions/#transactions).

- Support for wire protocol compression via the new `compressors` URI and keyword argument to
`pymongo.mongo_client.MongoClient`. See [network compression](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/connect/connection-options/network-compression/#compress-network-traffic) for details.

- Support for Python 3.7.
- New count methods, `pymongo.collection.Collection.count_documents`
and `pymongo.collection.Collection.estimated_document_count`. `pymongo.collection.Collection.count_documents` is always accurate when used with MongoDB 3.6+, or when used with older standalone or replica set deployments. With older sharded clusters is it always accurate when used with Primary read preference. It can also be used in a transaction, unlike the now deprecated `pymongo.collection.Collection.count` and `pymongo.cursor.Cursor.count` methods.

- Support for watching changes on all collections in a database using the
new `pymongo.database.Database.watch` method.

- Support for watching changes on all collections in all databases using the
new `pymongo.mongo_client.MongoClient.watch` method.

- Support for watching changes starting at a user provided timestamp using the
new `start_at_operation_time` parameter for the `watch()` helpers.

- Better support for using PyMongo in a FIPS 140-2 environment. Specifically,
the following features and changes allow PyMongo to function when MD5 support is disabled in OpenSSL by the FIPS Object Module:

- Support for the [SCRAM-SHA-256](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/security/authentication/scram/#scram)
authentication mechanism. The [GSSAPI](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/security/authentication/kerberos/#kerberos--gssapi-), [PLAIN](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/security/authentication/ldap/#overview), and [MONGODB-X509](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/security/authentication/x509/#x.509) mechanisms can also be used to avoid issues with OpenSSL in FIPS environments.

- MD5 checksums are now optional in GridFS. See the `disable_md5` option
of `gridfs.GridFS` and `gridfs.GridFSBucket`.

- `bson.objectid.ObjectId` machine bytes are now hashed using
[FNV-1a](https://en.wikipedia.org/wiki/Fowler-Noll-Vo_hash_function) instead of MD5.

- The `pymongo.database.Database.list_collection_names` and
`pymongo.database.Database.collection_names` methods use the nameOnly option when supported by MongoDB.

- The `pymongo.collection.Collection.watch` method now returns an
instance of the `pymongo.change_stream.CollectionChangeStream` class which is a subclass of `pymongo.change_stream.ChangeStream`.

- SCRAM client and server keys are cached for improved performance, following
[RFC 5802](https://tools.ietf.org/html/rfc5802).

- If not specified, the authSource for the [PLAIN](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/security/authentication/ldap/#overview)
authentication mechanism defaults to $external.

- wtimeoutMS is once again supported as a URI option.
- When using unacknowledged write concern and connected to MongoDB server
version 3.6 or greater, the `bypass_document_validation` option is now supported in the following write helpers: `pymongo.collection.Collection.insert_one`, `pymongo.collection.Collection.replace_one`, `pymongo.collection.Collection.update_one`, `pymongo.collection.Collection.update_many`.

Deprecations:

- Deprecated `pymongo.collection.Collection.count` and
`pymongo.cursor.Cursor.count`. These two methods use the `count` command and [may or may not be accurate](https://mongodb.com/docs/manual/reference/command/count/#behavior), depending on the options used and connected MongoDB topology. Use `pymongo.collection.Collection.count_documents` instead.

- Deprecated the snapshot option of `pymongo.collection.Collection.find`
and `pymongo.collection.Collection.find_one`. The option was deprecated in MongoDB 3.6 and removed in MongoDB 4.0.

- Deprecated the max_scan option of `pymongo.collection.Collection.find`
and `pymongo.collection.Collection.find_one`. The option was deprecated in MongoDB 4.0. Use `maxTimeMS` instead.

- Deprecated `pymongo.mongo_client.MongoClient.close_cursor`. Use
`pymongo.cursor.Cursor.close` instead.

- Deprecated `pymongo.mongo_client.MongoClient.database_names`. Use
`pymongo.mongo_client.MongoClient.list_database_names` instead.

- Deprecated `pymongo.database.Database.collection_names`. Use
`pymongo.database.Database.list_collection_names` instead.

- Deprecated `pymongo.collection.Collection.parallel_scan`. MongoDB 4.2
will remove the parallelCollectionScan command.

Unavoidable breaking changes:

- Commands that fail with server error codes 10107, 13435, 13436, 11600,
11602, 189, 91 (NotMaster, NotMasterNoSlaveOk, NotMasterOrSecondary, InterruptedAtShutdown, InterruptedDueToReplStateChange, PrimarySteppedDown, ShutdownInProgress respectively) now always raise `pymongo.errors.NotMasterError` instead of `pymongo.errors.OperationFailure`.

- `pymongo.collection.Collection.parallel_scan` no longer uses an
implicit session. Explicit sessions are still supported.

- Unacknowledged writes (`w=0`) with an explicit `session` parameter now
raise a client side error. Since PyMongo does not wait for a response for an unacknowledged write, two unacknowledged writes run serially by the client may be executed simultaneously on the server. However, the server requires a single session must not be used simultaneously by more than one operation. Therefore explicit sessions cannot support unacknowledged writes. Unacknowledged writes without a `session` parameter are still supported.

Issues Resolved ...............

See the PyMongo 3.7 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 3.6.1 (2018/03/01)

Version 3.6.1 fixes bugs reported since the release of 3.6.0:

- Fix regression in PyMongo 3.5.0 that causes idle sockets to be closed almost
instantly when `maxIdleTimeMS` is set. Idle sockets are now closed after `maxIdleTimeMS` milliseconds.

- `pymongo.mongo_client.MongoClient.max_idle_time_ms` now returns
milliseconds instead of seconds.

- Properly import and use the
[monotonic](https://pypi.python.org/pypi/monotonic) library for monotonic time when it is installed.

- `pymongo.collection.Collection.aggregate` now ignores the
`batchSize` argument when running a pipeline with a `$out` stage.

- Always send handshake metadata for new connections.
Issues Resolved ...............

See the PyMongo 3.6.1 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 3.6.0 (2017/08/23)

Version 3.6 adds support for MongoDB 3.6, drops support for CPython 3.3 (PyPy3 is still supported), and drops support for MongoDB versions older than 2.6. If connecting to a MongoDB 2.4 server or older, PyMongo now throws a `pymongo.errors.ConfigurationError`.

Highlights include:

- Support for change streams. See the
`pymongo.collection.Collection.watch` method for details.

- Support for array_filters in
`pymongo.collection.Collection.update_one`, `pymongo.collection.Collection.update_many`, `pymongo.collection.Collection.find_one_and_update`, `pymongo.operations.UpdateOne`, and `pymongo.operations.UpdateMany`.

- New Session API, see `pymongo.mongo_client.MongoClient.start_session`.
- New methods `pymongo.collection.Collection.find_raw_batches` and
`pymongo.collection.Collection.aggregate_raw_batches` for use with external libraries that can parse raw batches of BSON data.

- New methods `pymongo.mongo_client.MongoClient.list_databases` and
`pymongo.mongo_client.MongoClient.list_database_names`.

- New methods `pymongo.database.Database.list_collections` and
`pymongo.database.Database.list_collection_names`.

- Support for mongodb+srv:// URIs. See
`pymongo.mongo_client.MongoClient` for details.

- Index management helpers
(`pymongo.collection.Collection.create_index`, `pymongo.collection.Collection.create_indexes`, `pymongo.collection.Collection.drop_index`, `pymongo.collection.Collection.drop_indexes`, `pymongo.collection.Collection.reindex`) now support maxTimeMS.

- Support for retryable writes and the `retryWrites` URI option.  See
`pymongo.mongo_client.MongoClient` for details.

Deprecations:

- The `useCursor` option for `pymongo.collection.Collection.aggregate`
is deprecated. The option was only necessary when upgrading from MongoDB 2.4 to MongoDB 2.6. MongoDB 2.4 is no longer supported.

- The `pymongo.database.Database.add_user` and
`pymongo.database.Database.remove_user` methods are deprecated. See the method docstrings for alternatives.

Unavoidable breaking changes:

- Starting in MongoDB 3.6, the deprecated methods
`pymongo.database.Database.authenticate` and `pymongo.database.Database.logout` now invalidate all cursors created prior. Instead of using these methods to change credentials, pass credentials for one user to the `pymongo.mongo_client.MongoClient` at construction time, and either grant access to several databases to one user account, or use a distinct client object for each user.

- BSON binary subtype 4 is decoded using RFC-4122 byte order regardless
of the UUID representation. This is a change in behavior for applications that use UUID representation `bson.binary.JAVA_LEGACY` or `bson.binary.CSHARP_LEGACY` to decode BSON binary subtype 4. Other UUID representations, `bson.binary.PYTHON_LEGACY` (the default) and `bson.binary.STANDARD`, and the decoding of BSON binary subtype 3 are unchanged.

Issues Resolved ...............

See the PyMongo 3.6 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 3.5.1 (2017/08/23)

Version 3.5.1 fixes bugs reported since the release of 3.5.0:

- Work around socket.getsockopt issue with NetBSD.
- `pymongo.command_cursor.CommandCursor.close` now closes
the cursor synchronously instead of deferring to a background thread.

- Fix documentation build warnings with Sphinx 1.6.x.
Issues Resolved ...............

See the PyMongo 3.5.1 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 3.5.0 (2017/08/08)

Version 3.5 implements a number of improvements and bug fixes:

Highlights include:

- Username and password can be passed to
`pymongo.mongo_client.MongoClient` as keyword arguments. Before, the only way to pass them was in the URI.

- Increased the performance of using `bson.raw_bson.RawBSONDocument`.
- Increased the performance of
`pymongo.mongo_client.MongoClient.database_names` by using the `nameOnly` option for listDatabases when available.

- Increased the performance of
`pymongo.collection.Collection.bulk_write` by reducing the memory overhead of `pymongo.operations.InsertOne`, `pymongo.operations.DeleteOne`, and `pymongo.operations.DeleteMany`.

- Added the `collation` option to `pymongo.operations.DeleteOne`,
`pymongo.operations.DeleteMany`, `pymongo.operations.ReplaceOne`, `pymongo.operations.UpdateOne`, and `pymongo.operations.UpdateMany`.

- Implemented the `MongoDB Extended JSON
<https://github.com/mongodb/specifications/blob/master/source/extended-json/extended-json.md>`_ specification.

- `bson.decimal128.Decimal128` now works when cdecimal is installed.
- PyMongo is now tested against a wider array of operating systems and CPU
architectures (including s390x, ARM64, and POWER8).

Changes and Deprecations:

- `pymongo.collection.Collection.find` has new options `return_key`,
`show_record_id`, `snapshot`, `hint`, `max_time_ms`, `max_scan`, `min`, `max`, and `comment`. Deprecated the option `modifiers`.

- Deprecated `pymongo.collection.Collection.group`. The group command
was deprecated in MongoDB 3.4 and is expected to be removed in MongoDB 3.6. Applications should use `pymongo.collection.Collection.aggregate` with the `$group` pipeline stage instead.

- Deprecated `pymongo.database.Database.authenticate`. Authenticating
multiple users conflicts with support for logical sessions in MongoDB 3.6. To authenticate as multiple users, create multiple instances of `pymongo.mongo_client.MongoClient`.

- Deprecated `pymongo.database.Database.eval`. The eval command
was deprecated in MongoDB 3.0 and will be removed in a future server version.

- Deprecated `pymongo.database.SystemJS`.
- Deprecated `pymongo.mongo_client.MongoClient.get_default_database`.
Applications should use `pymongo.mongo_client.MongoClient.get_database` without the ``name`` parameter instead.

- Deprecated the MongoClient option `socketKeepAlive``. It now defaults to true
and disabling it is not recommended, see [does TCP keepalive time affect MongoDB Deployments?](https://mongodb.com/docs/manual/faq/diagnostics/#does-tcp-keepalive-time-affect-mongodb-deployments-)

- Deprecated `pymongo.collection.Collection.initialize_ordered_bulk_op`,
`pymongo.collection.Collection.initialize_unordered_bulk_op`, and `pymongo.bulk.BulkOperationBuilder`. Use `pymongo.collection.Collection.bulk_write` instead.

- Deprecated :const:`~bson.json_util.STRICT_JSON_OPTIONS`. Use
:const:`~bson.json_util.RELAXED_JSON_OPTIONS` or :const:`~bson.json_util.CANONICAL_JSON_OPTIONS` instead.

- If a custom `bson.codec_options.CodecOptions` is passed to
`RawBSONDocument`, its `document_class`` must be `RawBSONDocument`.

- `pymongo.collection.Collection.list_indexes` no longer raises
OperationFailure when the collection (or database) does not exist on MongoDB >= 3.0. Instead, it returns an empty `pymongo.command_cursor.CommandCursor` to make the behavior consistent across all MongoDB versions.

- In Python 3, `bson.json_util.loads` now automatically decodes JSON
$binary with a subtype of 0 into `bytes` instead of `bson.binary.Binary`.

- `bson.json_util.loads` now raises `TypeError` or `ValueError`
when parsing JSON type wrappers with values of the wrong type or any extra keys.

- `pymongo.cursor.Cursor.close` and
`pymongo.mongo_client.MongoClient.close` now kill cursors synchronously instead of deferring to a background thread.

- `pymongo.uri_parser.parse_uri` now returns the original value
of the `readPreference` MongoDB URI option instead of the validated read preference mode.

Issues Resolved ...............

See the PyMongo 3.5 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 3.4.0 (2016/11/29)

Version 3.4 implements the new server features introduced in MongoDB 3.4 and a whole lot more:

Highlights include:

- Complete support for MongoDB 3.4:
- Unicode aware string comparison using [Collation](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/crud/configure/#collation).
- Support for the new `bson.decimal128.Decimal128` BSON type.
- A new maxStalenessSeconds read preference option.
- A username is no longer required for the MONGODB-X509 authentication
mechanism when connected to MongoDB >= 3.4.

- `pymongo.collection.Collection.parallel_scan` supports maxTimeMS.
- `pymongo.write_concern.WriteConcern` is automatically
applied by all helpers for commands that write to the database when connected to MongoDB 3.4+. This change affects the following helpers:

- `pymongo.mongo_client.MongoClient.drop_database`
- `pymongo.database.Database.create_collection`
- `pymongo.database.Database.drop_collection`
- `pymongo.collection.Collection.aggregate` (when using $out)
- `pymongo.collection.Collection.create_indexes`
- `pymongo.collection.Collection.create_index`
- `pymongo.collection.Collection.drop_indexes`
- `pymongo.collection.Collection.drop_indexes`
- `pymongo.collection.Collection.drop_index`
- `pymongo.collection.Collection.map_reduce` (when output is not
"inline")

- `pymongo.collection.Collection.reindex`
- `pymongo.collection.Collection.rename`
- Improved support for logging server discovery and monitoring events. See
`pymongo.monitoring` for examples.

- Support for matching iPAddress subjectAltName values for TLS certificate
verification.

- TLS compression is now explicitly disabled when possible.
- The Server Name Indication (SNI) TLS extension is used when possible.
- Finer control over JSON encoding/decoding with
`bson.json_util.JSONOptions`.

- Allow `bson.code.Code` objects to have a scope of `None`,
signifying no scope. Also allow encoding Code objects with an empty scope (i.e. `{}`).

> **Warning:** `None`, as the default scope is `None` instead of `{}`.

> **Note:** (i.e. it sets the close-on-exec flag on socket file descriptors). Support
is limited to a subset of POSIX operating systems (not including Windows) and
the flag usually cannot be set in a single atomic operation. CPython 3.4+
implements PEP 446, creating all file descriptors non-inheritable by
default. Users that require this behavior are encouraged to upgrade to
CPython 3.4+.

Since 3.4rc0, the max staleness option has been renamed from `maxStalenessMS` to `maxStalenessSeconds`, its smallest value has changed from twice `heartbeatFrequencyMS` to 90 seconds, and its default value has changed from `None` or 0 to -1.

Issues Resolved ...............

See the PyMongo 3.4 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 3.3.1 (2016/10/27)

Version 3.3.1 fixes a memory leak when decoding elements inside of a `bson.raw_bson.RawBSONDocument`.

Issues Resolved ...............

See the PyMongo 3.3.1 release notes in Jira for the list of resolved issues in this release.

## Changes in Version 3.3.0 (2016/07/12)

Version 3.3 adds the following major new features:

- C extensions support on big endian systems.
- Kerberos authentication support on Windows using `WinKerberos
<https://pypi.python.org/pypi/winkerberos>`_.

- A new `ssl_clrfile` option to support certificate revocation lists.
- A new `ssl_pem_passphrase` option to support encrypted key files.
- Support for publishing server discovery and monitoring events. See
`pymongo.monitoring` for details.

- New connection pool options `minPoolSize` and `maxIdleTimeMS`.
- New `heartbeatFrequencyMS` option controls the rate at which background
monitoring threads re-check servers. Default is once every 10 seconds.

> **Warning:** It also drops support for python 3.2 (pypy3 continues to be supported).

Issues Resolved ...............

See the PyMongo 3.3 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 3.2.2 (2016/03/15)

Version 3.2.2 fixes a few issues reported since the release of 3.2.1, including a fix for using the `connect` option in the MongoDB URI and support for setting the batch size for a query to 1 when using MongoDB 3.2+.

Issues Resolved ...............

See the PyMongo 3.2.2 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 3.2.1 (2016/02/02)

Version 3.2.1 fixes a few issues reported since the release of 3.2, including running the mapreduce command twice when calling the `pymongo.collection.Collection.inline_map_reduce` method and a `TypeError` being raised when calling `gridfs.GridFSBucket.download_to_stream`. This release also improves error messaging around BSON decoding.

Issues Resolved ...............

See the PyMongo 3.2.1 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 3.2 (2015/12/07)

Version 3.2 implements the new server features introduced in MongoDB 3.2.

Highlights include:

- Full support for MongoDB 3.2 including:
- Support for `pymongo.read_concern.ReadConcern`
- `pymongo.write_concern.WriteConcern` is now applied to
`pymongo.collection.Collection.find_one_and_replace`, `pymongo.collection.Collection.find_one_and_update`, and `pymongo.collection.Collection.find_one_and_delete`.

- Support for the new `bypassDocumentValidation` option in write
helpers.

- Support for reading and writing raw BSON with
`bson.raw_bson.RawBSONDocument`

> **Note:** block until a connection is established or raise
`pymongo.errors.ServerSelectionTimeoutError` if no server is available.
See `pymongo.mongo_client.MongoClient` for details.

Issues Resolved ...............

See the PyMongo 3.2 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 3.1.1 (2015/11/17)

Version 3.1.1 fixes a few issues reported since the release of 3.1, including a regression in error handling for oversize command documents and interrupt handling issues in the C extensions.

Issues Resolved ...............

See the PyMongo 3.1.1 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 3.1 (2015/11/02)

Version 3.1 implements a few new features and fixes bugs reported since the release of 3.0.3.

Highlights include:

- Command monitoring support. See `pymongo.monitoring` for details.
- Configurable error handling for `UnicodeDecodeError`. See the
`unicode_decode_error_handler` option of `bson.codec_options.CodecOptions`.

- Optional automatic timezone conversion when decoding BSON datetime. See the
`tzinfo` option of `bson.codec_options.CodecOptions`.

- An implementation of `gridfs.GridFSBucket` from the new GridFS spec.
- Compliance with the new Connection String spec.
- Reduced idle CPU usage in Python 2.
Changes in internal classes ...........................

The private `PeriodicExecutor` class no longer takes a `condition_class` option, and the private `thread_util.Event` class is removed.

Issues Resolved ...............

See the PyMongo 3.1 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 3.0.3 (2015/06/30)

Version 3.0.3 fixes issues reported since the release of 3.0.2, including a feature breaking bug in the GSSAPI implementation.

Issues Resolved ...............

See the PyMongo 3.0.3 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 3.0.2 (2015/05/12)

Version 3.0.2 fixes issues reported since the release of 3.0.1, most importantly a bug that could route operations to replica set members that are not in primary or secondary state when using `pymongo.read_preferences.PrimaryPreferred` or `pymongo.read_preferences.Nearest`. It is a recommended upgrade for all users of PyMongo 3.0.x.

Issues Resolved ...............

See the PyMongo 3.0.2 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 3.0.1 (2015/04/21)

Version 3.0.1 fixes issues reported since the release of 3.0, most importantly a bug in GridFS.delete that could prevent file chunks from actually being deleted.

Issues Resolved ...............

See the PyMongo 3.0.1 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 3.0 (2015/04/07)

PyMongo 3.0 is a partial rewrite of PyMongo bringing a large number of improvements:

- A unified client class. MongoClient is the one and only client class for
connecting to a standalone mongod, replica set, or sharded cluster. Migrating from a standalone, to a replica set, to a sharded cluster can be accomplished with only a simple URI change.

- MongoClient is much more responsive to configuration changes in your MongoDB
deployment. All connected servers are monitored in a non-blocking manner. Slow to respond or down servers no longer block server discovery, reducing application startup time and time to respond to new or reconfigured servers and replica set failovers.

- A unified CRUD API. All official MongoDB drivers now implement a standard
CRUD API allowing polyglot developers to move from language to language with ease.

- Single source support for Python 2.x and 3.x. PyMongo no longer relies on
2to3 to support Python 3.

- A rewritten pure Python BSON implementation, improving performance
with pypy and cpython deployments without support for C extensions.

- Better support for greenlet based async frameworks including eventlet.
- Immutable client, database, and collection classes, avoiding a host of thread
safety issues in client applications.

PyMongo 3.0 brings a large number of API changes. Be sure to read the changes listed below before upgrading from PyMongo 2.x.

> **Warning:** must use PyMongo with these versions of Python the 2.x branch of PyMongo
will be minimally supported for some time.

SONManipulator changes ......................

The `pymongo.son_manipulator.SONManipulator` API has limitations as a technique for transforming your data. Instead, it is more flexible and straightforward to transform outgoing documents in your own code before passing them to PyMongo, and transform incoming documents after receiving them from PyMongo.

Thus the `pymongo.database.Database.add_son_manipulator` method is deprecated. PyMongo 3's new CRUD API does **not** apply SON manipulators to documents passed to `pymongo.collection.Collection.bulk_write`, `pymongo.collection.Collection.insert_one`, `pymongo.collection.Collection.insert_many`, `pymongo.collection.Collection.update_one`, or `pymongo.collection.Collection.update_many`. SON manipulators are **not** applied to documents returned by the new methods `pymongo.collection.Collection.find_one_and_delete`, `pymongo.collection.Collection.find_one_and_replace`, and `pymongo.collection.Collection.find_one_and_update`.

SSL/TLS changes ...............

When `ssl` is `True` the `ssl_cert_reqs` option now defaults to `ssl.CERT_REQUIRED` if not provided. PyMongo will attempt to load OS provided CA certificates to verify the server, raising `pymongo.errors.ConfigurationError` if it cannot.

Gevent Support ..............

In previous versions, PyMongo supported Gevent in two modes: you could call `gevent.monkey.patch_socket()` and pass `use_greenlets=True` to `pymongo.mongo_client.MongoClient`, or you could simply call `gevent.monkey.patch_all()` and omit the `use_greenlets` argument.

In PyMongo 3.0, the `use_greenlets` option is gone. To use PyMongo with Gevent simply call `gevent.monkey.patch_all()`.

For more information, see [Gevent](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/integrations/#gevent).

`pymongo.mongo_client.MongoClient` changes ..................................................

`pymongo.mongo_client.MongoClient` is now the one and only client class for a standalone server, mongos, or replica set. It includes the functionality that had been split into `MongoReplicaSetClient`: it can connect to a replica set, discover all its members, and monitor the set for stepdowns, elections, and reconfigs. `pymongo.mongo_client.MongoClient` now also supports the full `pymongo.read_preferences.ReadPreference` API.

The obsolete classes `MasterSlaveConnection`, `Connection`, and `ReplicaSetConnection` are removed.

The `pymongo.mongo_client.MongoClient` constructor no longer blocks while connecting to the server or servers, and it no longer raises `pymongo.errors.ConnectionFailure` if they are unavailable, nor `pymongo.errors.ConfigurationError` if the user's credentials are wrong. Instead, the constructor returns immediately and launches the connection process on background threads. The `connect` option is added to control whether these threads are started immediately, or when the client is first used.

Therefore the `alive` method is removed since it no longer provides meaningful information; even if the client is disconnected, it may discover a server in time to fulfill the next operation.

In PyMongo 2.x, `pymongo.mongo_client.MongoClient` accepted a list of standalone MongoDB servers and used the first it could connect to:

```
MongoClient(['host1.com:27017', 'host2.com:27017'])
```

A list of multiple standalones is no longer supported; if multiple servers are listed they must be members of the same replica set, or mongoses in the same sharded cluster.

The behavior for a list of mongoses is changed from "high availability" to "load balancing". Before, the client connected to the lowest-latency mongos in the list, and used it until a network error prompted it to re-evaluate all mongoses' latencies and reconnect to one of them. In PyMongo 3, the client monitors its network latency to all the mongoses continuously, and distributes operations evenly among those with the lowest latency. See [load balancing](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/connect/connection-targets/#replica-sets) for more information.

The client methods `start_request`, `in_request`, and `end_request` are removed, and so is the `auto_start_request` option. Requests were designed to make read-your-writes consistency more likely with the `w=0` write concern. Additionally, a thread in a request used the same member for all secondary reads in a replica set. To ensure read-your-writes consistency in PyMongo 3.0, do not override the default write concern with `w=0`, and do not override the default [read preference](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/crud/configure/#read-and-write-settings) of PRIMARY.

Support for the `slaveOk` (or `slave_okay`), `safe`, and `network_timeout` options has been removed. Use `pymongo.read_preferences.ReadPreference.SECONDARY_PREFERRED` instead of slave_okay. Accept the default write concern, acknowledged writes, instead of setting safe=True. Use socketTimeoutMS in place of network_timeout (note that network_timeout was in seconds, where as socketTimeoutMS is milliseconds).

The `max_pool_size` option has been removed. It is replaced by the `maxPoolSize` MongoDB URI option. `maxPoolSize` is now a supported URI option in PyMongo and can be passed as a keyword argument.

The `copy_database` method is removed, see [Copy and Clone Databases](https://www.mongodb.com/docs/database-tools/mongodump/mongodump-examples/#copy-and-clone-databases) for alternatives.

The `disconnect` method is removed. Use `pymongo.mongo_client.MongoClient.close` instead.

The `get_document_class` method is removed. Use `pymongo.mongo_client.MongoClient.codec_options` instead.

The `get_lasterror_options`, `set_lasterror_options`, and `unset_lasterror_options` methods are removed. Write concern options can be passed to `pymongo.mongo_client.MongoClient` as keyword arguments or MongoDB URI options.

The `pymongo.mongo_client.MongoClient.get_database` method is added for getting a Database instance with its options configured differently than the MongoClient's.

The following read-only attributes have been added:

- `pymongo.mongo_client.MongoClient.codec_options`
The following attributes are now read-only:

- `pymongo.mongo_client.MongoClient.read_preference`
- `pymongo.mongo_client.MongoClient.write_concern`
The following attributes have been removed:

- `pymongo.mongo_client.MongoClient.document_class`
(use `pymongo.mongo_client.MongoClient.codec_options` instead)

- `pymongo.mongo_client.MongoClient.host`
(use `pymongo.mongo_client.MongoClient.address` instead)

- `pymongo.mongo_client.MongoClient.min_wire_version`
- `pymongo.mongo_client.MongoClient.max_wire_version`
- `pymongo.mongo_client.MongoClient.port`
(use `pymongo.mongo_client.MongoClient.address` instead)

- `pymongo.mongo_client.MongoClient.safe`
(use `pymongo.mongo_client.MongoClient.write_concern` instead)

- `pymongo.mongo_client.MongoClient.slave_okay`
(use `pymongo.mongo_client.MongoClient.read_preference` instead)

- `pymongo.mongo_client.MongoClient.tag_sets`
(use `pymongo.mongo_client.MongoClient.read_preference` instead)

- `pymongo.mongo_client.MongoClient.tz_aware`
(use `pymongo.mongo_client.MongoClient.codec_options` instead)

The following attributes have been renamed:

- `pymongo.mongo_client.MongoClient.secondary_acceptable_latency_ms` is
now `pymongo.mongo_client.MongoClient.local_threshold_ms` and is now read-only.

`pymongo.cursor.Cursor` changes .......................................

The `conn_id` property is renamed to `pymongo.cursor.Cursor.address`.

Cursor management changes .........................

`pymongo.cursor_manager.CursorManager` and `pymongo.mongo_client.MongoClient.set_cursor_manager` are no longer deprecated. If you subclass `pymongo.cursor_manager.CursorManager` your implementation of `pymongo.cursor_manager.CursorManager.close` must now take a second parameter, `address`. The `BatchCursorManager` class is removed.

The second parameter to `pymongo.mongo_client.MongoClient.close_cursor is renamed from conn_id` to `address`. `pymongo.mongo_client.MongoClient.kill_cursors` now accepts an `address` parameter.

`pymongo.database.Database` changes ...........................................

The `connection` property is renamed to `pymongo.database.Database.client`.

The following read-only attributes have been added:

- `pymongo.database.Database.codec_options`
The following attributes are now read-only:

- `pymongo.database.Database.read_preference`
- `pymongo.database.Database.write_concern`
Use `pymongo.mongo_client.MongoClient.get_database` for getting a Database instance with its options configured differently than the MongoClient's.

The following attributes have been removed:

- `pymongo.database.Database.safe`
- `pymongo.database.Database.secondary_acceptable_latency_ms`
- `pymongo.database.Database.slave_okay`
- `pymongo.database.Database.tag_sets`
The following methods have been added:

- `pymongo.database.Database.get_collection`
The following methods have been changed:

- `pymongo.database.Database.command`. Support for `as_class`,
`uuid_subtype`, `tag_sets`, and `secondary_acceptable_latency_ms` have been removed. You can instead pass an instance of `bson.codec_options.CodecOptions` as `codec_options` and an instance of a read preference class from `pymongo.read_preferences` as `read_preference`. The `fields` and `compile_re` options are also removed. The `fields` options was undocumented and never really worked. Regular expressions are always decoded to `bson.regex.Regex`.

The following methods have been deprecated:

- `pymongo.database.Database.add_son_manipulator`
The following methods have been removed:

The `get_lasterror_options`, `set_lasterror_options`, and `unset_lasterror_options` methods have been removed. Use `pymongo.write_concern.WriteConcern` with `pymongo.mongo_client.MongoClient.get_database` instead.

`pymongo.collection.Collection` changes ...............................................

The following read-only attributes have been added:

- `pymongo.collection.Collection.codec_options`
The following attributes are now read-only:

- `pymongo.collection.Collection.read_preference`
- `pymongo.collection.Collection.write_concern`
Use `pymongo.database.Database.get_collection` or `pymongo.collection.Collection.with_options` for getting a Collection instance with its options configured differently than the Database's.

The following attributes have been removed:

- `pymongo.collection.Collection.safe`
- `pymongo.collection.Collection.secondary_acceptable_latency_ms`
- `pymongo.collection.Collection.slave_okay`
- `pymongo.collection.Collection.tag_sets`
The following methods have been added:

- `pymongo.collection.Collection.bulk_write`
- `pymongo.collection.Collection.insert_one`
- `pymongo.collection.Collection.insert_many`
- `pymongo.collection.Collection.update_one`
- `pymongo.collection.Collection.update_many`
- `pymongo.collection.Collection.replace_one`
- `pymongo.collection.Collection.delete_one`
- `pymongo.collection.Collection.delete_many`
- `pymongo.collection.Collection.find_one_and_delete`
- `pymongo.collection.Collection.find_one_and_replace`
- `pymongo.collection.Collection.find_one_and_update`
- `pymongo.collection.Collection.with_options`
- `pymongo.collection.Collection.create_indexes`
- `pymongo.collection.Collection.list_indexes`
The following methods have changed:

- `pymongo.collection.Collection.aggregate` now **always** returns an
instance of `pymongo.command_cursor.CommandCursor`. See the documentation for all options.

- `pymongo.collection.Collection.count` now optionally takes a filter
argument, as well as other options supported by the count command.

- `pymongo.collection.Collection.distinct` now optionally takes a filter
argument.

- `pymongo.collection.Collection.create_index` no longer caches
indexes, therefore the `cache_for` parameter has been removed. It also no longer supports the `bucket_size` and `drop_dups` aliases for `bucketSize` and `dropDups`.

The following methods are deprecated:

- `pymongo.collection.Collection.save`
- `pymongo.collection.Collection.insert`
- `pymongo.collection.Collection.update`
- `pymongo.collection.Collection.remove`
- `pymongo.collection.Collection.find_and_modify`
- `pymongo.collection.Collection.ensure_index`
The following methods have been removed:

The `get_lasterror_options`, `set_lasterror_options`, and `unset_lasterror_options` methods have been removed. Use `pymongo.write_concern.WriteConcern` with `pymongo.collection.Collection.with_options` instead.

Changes to `pymongo.collection.Collection.find` and `pymongo.collection.Collection.find_one` ``````````````````````````````````````````````````````````````````````````````````````````````````````````

The following find/find_one options have been renamed:

These renames only affect your code if you passed these as keyword arguments, like find(fields=['fieldname']). If you passed only positional parameters these changes are not significant for your application.

- spec -> filter
- fields -> projection
- partial -> allow_partial_results
The following find/find_one options have been added:

- cursor_type (see `pymongo.cursor.CursorType` for values)
- oplog_replay
- modifiers
The following find/find_one options have been removed:

- network_timeout (use `pymongo.cursor.Cursor.max_time_ms` instead)
- slave_okay (use one of the read preference classes from
`pymongo.read_preferences` and `pymongo.collection.Collection.with_options` instead)

- read_preference (use `pymongo.collection.Collection.with_options`
instead)

- tag_sets (use one of the read preference classes from
`pymongo.read_preferences` and `pymongo.collection.Collection.with_options` instead)

- secondary_acceptable_latency_ms (use the `localThresholdMS` URI option
instead)

- max_scan (use the new `modifiers` option instead)
- snapshot (use the new `modifiers` option instead)
- tailable (use the new `cursor_type` option instead)
- await_data (use the new `cursor_type` option instead)
- exhaust (use the new `cursor_type` option instead)
- as_class (use `pymongo.collection.Collection.with_options` with
`bson.codec_options.CodecOptions` instead)

- compile_re (BSON regular expressions are always decoded to
`bson.regex.Regex`)

The following find/find_one options are deprecated:

- manipulate
The following renames need special handling.

- timeout -> no_cursor_timeout -
The default for `timeout` was True. The default for `no_cursor_timeout` is False. If you were previously passing False for ``t`imeout` you must pass **True** for `no_cursor_timeout`` to keep the previous behavior.

`pymongo.errors` changes ..............................

The exception classes `UnsupportedOption` and `TimeoutError` are deleted.

`gridfs` changes ......................

Since PyMongo 1.6, methods `open` and `close` of `gridfs.GridFS` raised an `UnsupportedAPI` exception, as did the entire `GridFile` class. The unsupported methods, the class, and the exception are all deleted.

`bson` changes ....................

The `compile_re` option is removed from all methods that accepted it in `bson` and `bson.json_util`. Additionally, it is removed from `pymongo.collection.Collection.find`, `pymongo.collection.Collection.find_one`, `pymongo.collection.Collection.aggregate`, `pymongo.database.Database.command`, and so on. PyMongo now always represents BSON regular expressions as `bson.regex.Regex` objects. This prevents errors for incompatible patterns, see PYTHON-500. Use `bson.regex.Regex.try_compile` to attempt to convert from a BSON regular expression to a Python regular expression object.

PyMongo now decodes the int64 BSON type to `bson.int64.Int64`, a trivial wrapper around long (in python 2.x) or int (in python 3.x). This allows BSON int64 to be round tripped without losing type information in python 3. Note that if you store a python long (or a python int larger than 4 bytes) it will be returned from PyMongo as `bson.int64.Int64`.

The `as_class`, `tz_aware`, and `uuid_subtype` options are removed from all BSON encoding and decoding methods. Use `bson.codec_options.CodecOptions` to configure these options. The APIs affected are:

- `bson.decode_all`
- `bson.decode_iter`
- `bson.decode_file_iter`
- `bson.BSON.encode`
- `bson.BSON.decode`
This is a breaking change for any application that uses the BSON API directly and changes any of the named parameter defaults. No changes are required for applications that use the default values for these options. The behavior remains the same.

Issues Resolved ...............

See the PyMongo 3.0 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 2.9.5 (2017/06/30)

Version 2.9.5 works around ssl module deprecations in Python 3.6, and expected future ssl module deprecations. It also fixes bugs found since the release of 2.9.4.

- Use ssl.SSLContext and ssl.PROTOCOL_TLS_CLIENT when available.
- Fixed a C extensions build issue when the interpreter was built with -std=c99
- Fixed various build issues with MinGW32.
- Fixed a write concern bug in `pymongo.database.Database.add_user` and
`pymongo.database.Database.remove_user` when connected to MongoDB 3.2+

- Fixed various test failures related to changes in gevent, MongoDB, and our CI
test environment.

Issues Resolved ...............

See the PyMongo 2.9.5 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 2.9.4 (2016/09/30)

Version 2.9.4 fixes issues reported since the release of 2.9.3.

- Fixed __repr__ for closed instances of `pymongo.mongo_client.MongoClient`.
- Fixed `pymongo.mongo_replica_set_client.MongoReplicaSetClient` handling of
uuidRepresentation.

- Fixed building and testing the documentation with python 3.x.
- New documentation for [TLS](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/security/tls/#configure-transport-layer-security--tls-) and [Atlas](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/connect/connection-targets/#atlas).
Issues Resolved ...............

See the PyMongo 2.9.4 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 2.9.3 (2016/03/15)

Version 2.9.3 fixes a few issues reported since the release of 2.9.2 including thread safety issues in `pymongo.collection.Collection.ensure_index`, `pymongo.collection.Collection.drop_index`, and `pymongo.collection.Collection.drop_indexes`.

Issues Resolved ...............

See the PyMongo 2.9.3 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 2.9.2 (2016/02/16)

Version 2.9.2 restores Python 3.1 support, which was broken in PyMongo 2.8. It improves an error message when decoding BSON as well as fixes a couple other issues including `pymongo.collection.Collection.aggregate` ignoring `pymongo.collection.Collection.codec_options` and `pymongo.database.Database.command` raising a superfluous `DeprecationWarning`.

Issues Resolved ...............

See the PyMongo 2.9.2 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 2.9.1 (2015/11/17)

Version 2.9.1 fixes two interrupt handling issues in the C extensions and adapts a test case for a behavior change in MongoDB 3.2.

Issues Resolved ...............

See the PyMongo 2.9.1 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 2.9 (2015/09/30)

Version 2.9 provides an upgrade path to PyMongo 3.x. Most of the API changes from PyMongo 3.0 have been backported in a backward compatible way, allowing applications to be written against PyMongo >= 2.9, rather then PyMongo 2.x or PyMongo 3.x. See the [PyMongo 3 Migration Guide](https://pymongo.readthedocs.io/en/3.12.1/migrate-to-pymongo3.html) for detailed examples.

> **Note:** that were removed in PyMongo 3.0.
`pymongo.mongo_client.MongoClient`:
 - `pymongo.mongo_client.MongoClient.host`
 - `pymongo.mongo_client.MongoClient.port`
 - `pymongo.mongo_client.MongoClient.use_greenlets`
 - `pymongo.mongo_client.MongoClient.document_class`
 - `pymongo.mongo_client.MongoClient.tz_aware`
 - `pymongo.mongo_client.MongoClient.secondary_acceptable_latency_ms`
 - `pymongo.mongo_client.MongoClient.tag_sets`
 - `pymongo.mongo_client.MongoClient.uuid_subtype`
 - `pymongo.mongo_client.MongoClient.disconnect`
 - `pymongo.mongo_client.MongoClient.alive`
`pymongo.mongo_replica_set_client.MongoReplicaSetClient`:
 - `pymongo.mongo_replica_set_client.MongoReplicaSetClient.use_greenlets`
 - `pymongo.mongo_replica_set_client.MongoReplicaSetClient.document_class`
 - `pymongo.mongo_replica_set_client.MongoReplicaSetClient.tz_aware`
 - `pymongo.mongo_replica_set_client.MongoReplicaSetClient.secondary_acceptable_latency_ms`
 - `pymongo.mongo_replica_set_client.MongoReplicaSetClient.tag_sets`
 - `pymongo.mongo_replica_set_client.MongoReplicaSetClient.uuid_subtype`
 - `pymongo.mongo_replica_set_client.MongoReplicaSetClient.alive`
`pymongo.database.Database`:
 - `pymongo.database.Database.secondary_acceptable_latency_ms`
 - `pymongo.database.Database.tag_sets`
 - `pymongo.database.Database.uuid_subtype`
`pymongo.collection.Collection`:
 - `pymongo.collection.Collection.secondary_acceptable_latency_ms`
 - `pymongo.collection.Collection.tag_sets`
 - `pymongo.collection.Collection.uuid_subtype`

> **Warning:** In previous versions of PyMongo, changing the value of
`pymongo.mongo_client.MongoClient.document_class` changed
the behavior of all existing instances of
`pymongo.collection.Collection`::
 >>> coll = client.test.test
 >>> coll.find_one()
 {u'_id': ObjectId('5579dc7cfba5220cc14d9a18')}
 >>> from bson.son import SON
 >>> client.document_class = SON
 >>> coll.find_one()
 SON([(u'_id', ObjectId('5579dc7cfba5220cc14d9a18'))])
The document_class setting is now configurable at the client,
database, collection, and per-operation level. This required breaking
the existing behavior. To change the document class per operation in a
forward compatible way use
`pymongo.collection.Collection.with_options`::
 >>> coll.find_one()
 {u'_id': ObjectId('5579dc7cfba5220cc14d9a18')}
 >>> from bson.codec_options import CodecOptions
 >>> coll.with_options(CodecOptions(SON)).find_one()
 SON([(u'_id', ObjectId('5579dc7cfba5220cc14d9a18'))])

Issues Resolved ...............

See the PyMongo 2.9 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 2.8.1 (2015/05/11)

Version 2.8.1 fixes a number of issues reported since the release of PyMongo 2.8. It is a recommended upgrade for all users of PyMongo 2.x.

Issues Resolved ...............

See the PyMongo 2.8.1 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 2.8 (2015/01/28)

Version 2.8 is a major release that provides full support for MongoDB 3.0 and fixes a number of bugs.

Special thanks to Don Mitchell, Ximing, Can Zhang, Sergey Azovskov, and Heewa Barfchin for their contributions to this release.

Highlights include:

- Support for the SCRAM-SHA-1 authentication mechanism (new in MongoDB 3.0).
- JSON decoder support for the new $numberLong and $undefined types.
- JSON decoder support for the $date type as an ISO-8601 string.
- Support passing an index name to `pymongo.cursor.Cursor.hint`.
- The `pymongo.cursor.Cursor.count` method will use a hint if one
has been provided through `pymongo.cursor.Cursor.hint`.

- A new socketKeepAlive option for the connection pool.
- New generator based BSON decode functions, `bson.decode_iter`
and `bson.decode_file_iter`.

- Internal changes to support alternative storage engines like wiredtiger.
> **Note:** will be removed in PyMongo 3.0. These include:
- `pymongo.mongo_client.MongoClient.start_request`
- `pymongo.mongo_client.MongoClient.in_request`
- `pymongo.mongo_client.MongoClient.end_request`
- `pymongo.mongo_client.MongoClient.copy_database`
- `pymongo.database.Database.error`
- `pymongo.database.Database.last_status`
- `pymongo.database.Database.previous_error`
- `pymongo.database.Database.reset_error_history`
- `pymongo.master_slave_connection.MasterSlaveConnection`
The JSON format for `bson.timestamp.Timestamp` has changed from
'{"t": <int>, "i": <int>}' to '{"$timestamp": {"t": <int>, "i": <int>}}'.
This new format will be decoded to an instance of
`bson.timestamp.Timestamp`. The old format will continue to be
decoded to a python dict as before. Encoding to the old format is no
longer supported as it was never correct and loses type information.

Issues Resolved ...............

See the PyMongo 2.8 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 2.7.2 (2014/07/29)

Version 2.7.2 includes fixes for upsert reporting in the bulk API for MongoDB versions previous to 2.6, a regression in how son manipulators are applied in `pymongo.collection.Collection.insert`, a few obscure connection pool semaphore leaks, and a few other minor issues. See the list of issues resolved for full details.

Issues Resolved ...............

See the PyMongo 2.7.2 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 2.7.1 (2014/05/23)

Version 2.7.1 fixes a number of issues reported since the release of 2.7, most importantly a fix for creating indexes and manipulating users through mongos versions older than 2.4.0.

Issues Resolved ...............

See the PyMongo 2.7.1 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 2.7 (2014/04/03)

PyMongo 2.7 is a major release with a large number of new features and bug fixes. Highlights include:

- Full support for MongoDB 2.6.
- A new [bulk write operations API](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/crud/bulk-write/#collection-bulk-write-example).
- Support for server side query timeouts using
`pymongo.cursor.Cursor.max_time_ms`.

- Support for writing `pymongo.collection.Collection.aggregate`
output to a collection.

- A new `pymongo.collection.Collection.parallel_scan` helper.
- `pymongo.errors.OperationFailure` and its subclasses now include
a `pymongo.errors.OperationFailure.details` attribute with complete error details from the server.

- A new GridFS `gridfs.GridFS.find` method that returns a
`gridfs.grid_file.GridOutCursor`.

- Greatly improved [support for mod_wsgi](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/integrations/#mod_wsgi) when using
PyMongo's C extensions. Read [Jesse's blog post](https://emptysqua.re/blog/python-c-extensions-and-mod-wsgi/) for details.

- Improved C extension support for ARM little endian.
Breaking changes ................

Version 2.7 drops support for replica sets running MongoDB versions older than 1.6.2.

Issues Resolved ...............

See the PyMongo 2.7 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 2.6.3 (2013/10/11)

Version 2.6.3 fixes issues reported since the release of 2.6.2, most importantly a semaphore leak when a connection to the server fails.

Issues Resolved ...............

See the PyMongo 2.6.3 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 2.6.2 (2013/09/06)

Version 2.6.2 fixes a `TypeError` problem when max_pool_size=None is used in Python 3.

Issues Resolved ...............

See the PyMongo 2.6.2 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 2.6.1 (2013/09/03)

Version 2.6.1 fixes a reference leak in the `pymongo.collection.Collection.insert` method.

Issues Resolved ...............

See the PyMongo 2.6.1 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 2.6 (2013/08/19)

Version 2.6 includes some frequently requested improvements and adds support for some early MongoDB 2.6 features.

Special thanks go to Justin Patrin for his work on the connection pool in this release.

Important new features:

- The `max_pool_size` option for `pymongo.mongo_client.MongoClient`
and `pymongo.mongo_replica_set_client.MongoReplicaSetClient` now actually caps the number of sockets the pool will open concurrently. Once the pool has reaches max_pool_size operations will block waiting for a socket to become available. If `waitQueueTimeoutMS` is set, an operation that blocks waiting for a socket will raise `pymongo.errors.ConnectionFailure` after the timeout. By default `waitQueueTimeoutMS` is not set. See [connection pooling](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/connect/connection-options/connection-pools/#connection-pools) for more information.

- The `pymongo.collection.Collection.insert` method automatically splits
large batches of documents into multiple insert messages based on `pymongo.mongo_client.MongoClient.max_message_size`

- Support for the exhaust cursor flag.
See `pymongo.collection.Collection.find` for details and caveats.

- Support for the PLAIN and MONGODB-X509 authentication mechanisms.
See [the authentication docs](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/security/authentication/#authentication-mechanisms) for more information.

- Support aggregation output as a `pymongo.cursor.Cursor`. See
`pymongo.collection.Collection.aggregate` for details.

> **Warning:** would limit only the idle sockets the pool would hold onto, not the
number of open sockets. The default has also changed, from 10 to 100.
If you pass a value for `max_pool_size` make sure it is large enough for
the expected load. (Sockets are only opened when needed, so there is no cost
to having a `max_pool_size` larger than necessary. Err towards a larger
value.) If your application accepts the default, continue to do so.
See [connection pooling](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/connect/connection-options/connection-pools/#connection-pools) for more information.

Issues Resolved ...............

See the PyMongo 2.6 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 2.5.2 (2013/06/01)

Version 2.5.2 fixes a NULL pointer dereference issue when decoding an invalid `bson.dbref.DBRef`.

Issues Resolved ...............

See the PyMongo 2.5.2 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 2.5.1 (2013/05/13)

Version 2.5.1 is a minor release that fixes issues discovered after the release of 2.5. Most importantly, this release addresses some race conditions in replica set monitoring.

Issues Resolved ...............

See the PyMongo 2.5.1 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 2.5 (2013/03/22)

Version 2.5 includes changes to support new features in MongoDB 2.4.

Important new features:

- Support for [GSSAPI (Kerberos)](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/security/authentication/kerberos/#kerberos--gssapi-).
- Support for SSL certificate validation with hostname matching.
- Support for delegated and role based authentication.
- New GEOSPHERE (2dsphere) and HASHED index constants.
> **Note:**  subclass of `pymongo.errors.PyMongoError` if authentication
 fails due to invalid credentials or configuration issues.

Issues Resolved ...............

See the PyMongo 2.5 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 2.4.2 (2013/01/23)

Version 2.4.2 is a minor release that fixes issues discovered after the release of 2.4.1. Most importantly, PyMongo will no longer select a replica set member for read operations that is not in primary or secondary state.

Issues Resolved ...............

See the PyMongo 2.4.2 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 2.4.1 (2012/12/06)

Version 2.4.1 is a minor release that fixes issues discovered after the release of 2.4. Most importantly, this release fixes a regression using `pymongo.collection.Collection.aggregate`, and possibly other commands, with mongos.

Issues Resolved ...............

See the PyMongo 2.4.1 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 2.4 (2012/11/27)

Version 2.4 includes a few important new features and a large number of bug fixes.

Important new features:

- New `pymongo.mongo_client.MongoClient` and
`pymongo.mongo_replica_set_client.MongoReplicaSetClient` classes - these connection classes do acknowledged write operations (previously referred to as 'safe' writes) by default. `pymongo.connection.Connection` and `pymongo.replica_set_connection.ReplicaSetConnection` are deprecated but still support the old default fire-and-forget behavior.

- A new write concern API implemented as a
`pymongo.collection.Collection.write_concern` attribute on the connection, `pymongo.database.Database`, or `pymongo.collection.Collection` classes.

- `pymongo.mongo_client.MongoClient` (and `pymongo.connection.Connection`)
now support Unix Domain Sockets.

- `pymongo.cursor.Cursor` can be copied with functions from the `copy`
module.

- The `pymongo.database.Database.set_profiling_level` method now supports
a `slow_ms` option.

- The replica set monitor task (used by
`pymongo.mongo_replica_set_client.MongoReplicaSetClient` and `pymongo.replica_set_connection.ReplicaSetConnection`) is a daemon thread once again, meaning you won't have to call `pymongo.mongo_replica_set_client.MongoReplicaSetClient.close` before exiting the python interactive shell.

> **Warning:**  The constructors for `pymongo.mongo_client.MongoClient`,
 `pymongo.mongo_replica_set_client.MongoReplicaSetClient`,
 `pymongo.connection.Connection`, and
 `pymongo.replica_set_connection.ReplicaSetConnection` now raise
 `pymongo.errors.ConnectionFailure` instead of its subclass
 `pymongo.errors.AutoReconnect` if the server is unavailable. Applications
 that expect to catch `pymongo.errors.AutoReconnect` should now catch
 `pymongo.errors.ConnectionFailure` while creating a new connection.

Issues Resolved ...............

See the PyMongo 2.4 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 2.3 (2012/08/29)

Version 2.3 adds support for new features and behavior changes in MongoDB 2.2.

Important New Features:

- Support for expanded read preferences including directing reads to tagged
servers - See [secondary reads](https://www.mongodb.com/docs/manual/core/read-preference/#mongodb-readmode-secondary) for more information.

- Support for mongos failover.
- A new `pymongo.collection.Collection.aggregate` method to support
MongoDB's new [aggregation framework](https://mongodb.com/docs/manual/applications/aggregation/).

- Support for legacy Java and C# byte order when encoding and decoding UUIDs.
- Support for connecting directly to an arbiter.
> **Warning:**  Starting with MongoDB 2.2 the getLastError command requires authentication
 when the server's `authentication features
 <https://www.mongodb.com/docs/manual/core/authentication/>`_ are enabled.
 Changes to PyMongo were required to support this behavior change. Users of
 authentication must upgrade to PyMongo 2.3 (or newer) for "safe" write operations
 to function correctly.

Issues Resolved ...............

See the PyMongo 2.3 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 2.2.1 (2012/07/06)

Version 2.2.1 is a minor release that fixes issues discovered after the release of 2.2. Most importantly, this release fixes an incompatibility with mod_wsgi 2.x that could cause connections to leak. Users of mod_wsgi 2.x are strongly encouraged to upgrade from PyMongo 2.2.

Issues Resolved ...............

See the PyMongo 2.2.1 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 2.2 (2012/04/30)

Version 2.2 adds a few more frequently requested features and fixes a number of bugs.

Special thanks go to Alex Grönholm for his contributions to Python 3 support and maintaining the original pymongo3 port. Christoph Simon, Wouter Bolsterlee, Mike O'Brien, and Chris Tompkinson also contributed to this release.

Important New Features:

- Support for Python 3.
See [Python 3](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/reference/upgrade/#upgrade-pymongo-versions) for more information.

- Support for Gevent -
See [Gevent](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/integrations/#gevent) for more information.

- Improved connection pooling.
See [PYTHON-287](https://jira.mongodb.org/browse/PYTHON-287).

> **Warning:**  A number of methods and method parameters that were deprecated in
 PyMongo 1.9 or older versions have been removed in this release.
 The full list of changes can be found in the following JIRA ticket:
 https://jira.mongodb.org/browse/PYTHON-305
 BSON module aliases from the pymongo package that were deprecated in
 PyMongo 1.9 have also been removed in this release. See the following
 JIRA ticket for details:
 https://jira.mongodb.org/browse/PYTHON-304
 As a result of this cleanup some minor code changes may be required
 to use this release.

Issues Resolved ...............

See the PyMongo 2.2 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 2.1.1 (2012/01/04)

Version 2.1.1 is a minor release that fixes a few issues discovered after the release of 2.1. You can now use `pymongo.replica_set_connection.ReplicaSetConnection` to run inline map reduce commands on secondaries. See `pymongo.collection.Collection.inline_map_reduce` for details.

Special thanks go to Samuel Clay and Ross Lawley for their contributions to this release.

Issues Resolved ...............

See the PyMongo 2.1.1 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 2.1 (2011/12/07)

Version 2.1 adds a few frequently requested features and includes the usual round of bug fixes and improvements.

Special thanks go to Alexey Borzenkov, Dan Crosta, Kostya Rybnikov, Flavio Percoco Premoli, Jonas Haag, and Jesse Davis for their contributions to this release.

Important New Features:

- ReplicaSetConnection -
`pymongo.replica_set_connection.ReplicaSetConnection` can be used to distribute reads to secondaries in a replica set. It supports automatic failover handling and periodically checks the state of the replica set to handle issues like primary stepdown or secondaries being removed for backup operations. Read preferences are defined through `pymongo.read_preferences.ReadPreference`.

- PyMongo supports the new BSON binary subtype 4 for UUIDs. The default
subtype to use can be set through `pymongo.collection.Collection.uuid_subtype` The current default remains `bson.binary.OLD_UUID_SUBTYPE` but will be changed to `bson.binary.UUID_SUBTYPE` in a future release.

- The getLastError option 'w' can be set to a string, allowing for options
like "majority" available in newer version of MongoDB.

- Added support for the MongoDB URI options socketTimeoutMS and connectTimeoutMS.
- Added support for the ContinueOnError insert flag.
- Added basic SSL support.
- Added basic support for Jython.
- Secondaries can be used for `pymongo.cursor.Cursor.count`,
`pymongo.cursor.Cursor.distinct`, `pymongo.collection.Collection.group`, and querying `gridfs.GridFS`.

- Added document_class and tz_aware options to
`pymongo.master_slave_connection.MasterSlaveConnection`

Issues Resolved ...............

See the PyMongo 2.1 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 2.0.1 (2011/08/15)

Version 2.0.1 fixes a regression in `gridfs.grid_file.GridIn` when writing pre-chunked strings. Thanks go to Alexey Borzenkov for reporting the issue and submitting a patch.

Issues Resolved ...............

- [PYTHON-271](https://jira.mongodb.org/browse/PYTHON-271):
Regression in GridFS leads to serious loss of data.

## Changes in Version 2.0 (2011/08/05)

Version 2.0 adds a large number of features and fixes a number of issues.

Special thanks go to James Murty, Abhay Vardhan, David Pisoni, Ryan Smith-Roberts, Andrew Pendleton, Mher Movsisyan, Reed O'Brien, Michael Schurter, Josip Delic and Jonas Haag for their contributions to this release.

Important New Features:

- PyMongo now performs automatic per-socket database authentication. You no
longer have to re-authenticate for each new thread or after a replica set failover. Authentication credentials are cached by the driver until the application calls `pymongo.database.Database.logout`.

- slave_okay can be set independently at the connection, database, collection
or query level. Each level will inherit the slave_okay setting from the previous level and each level can override the previous level's setting.

- safe and getLastError options (e.g. w, wtimeout, etc.) can be set
independently at the connection, database, collection or query level. Each level will inherit settings from the previous level and each level can override the previous level's setting.

- PyMongo now supports the `await_data` and `partial` cursor flags. If the
`await_data` flag is set on a `tailable` cursor the server will block for some extra time waiting for more data to return. The `partial` flag tells a mongos to return partial data for a query if not all shards are available.

- `pymongo.collection.Collection.map_reduce` will accept a `dict` or
instance of `bson.son.SON` as the `out` parameter.

- The URI parser has been moved into its own module and can be used directly
by application code.

- AutoReconnect exception now provides information about the error that
actually occurred instead of a generic failure message.

- A number of new helper methods have been added with options for setting and
unsetting cursor flags, re-indexing a collection, fsync and locking a server, and getting the server's current operations.

API changes:

- If only one host:port pair is specified `pymongo.connection.Connection`
will make a direct connection to only that host. Please note that `slave_okay` must be `True` in order to query from a secondary.

- If more than one host:port pair is specified or the `replicaset` option is
used PyMongo will treat the specified host:port pair(s) as a seed list and connect using replica set behavior.

> **Warning:**  The default subtype for `bson.binary.Binary` has changed
 from :const:`~bson.binary.OLD_BINARY_SUBTYPE` (2) to
 :const:`~bson.binary.BINARY_SUBTYPE` (0).

Issues Resolved ...............

See the PyMongo 2.0 release notes in JIRA for the list of resolved issues in this release.

## Changes in Version 1.11 (2011/05/05)

Version 1.11 adds a few new features and fixes a few more bugs.

New Features:

- Basic IPv6 support: pymongo prefers IPv4 but will try IPv6. You can
also specify an IPv6 address literal in the `host` parameter or a MongoDB URI provided it is enclosed in '[' and ']'.

- max_pool_size option: previously pymongo had a hard coded pool size
of 10 connections. With this change you can specify a different pool size as a parameter to `pymongo.connection.Connection` (max_pool_size=<integer>) or in the MongoDB URI (maxPoolSize=<integer>).

- Find by metadata in GridFS: You can know specify query fields as
keyword parameters for `gridfs.GridFS.get_version` and `gridfs.GridFS.get_last_version`.

- Per-query slave_okay option: slave_okay=True is now a valid keyword
argument for `pymongo.collection.Collection.find` and `pymongo.collection.Collection.find_one`.

API changes:

- `pymongo.database.Database.validate_collection` now returns a
dict instead of a string. This change was required to deal with an API change on the server. This method also now takes the optional `scandata` and `full` parameters. See the documentation for more details.

> **Warning:**            for `pymongo.connection.Connection` have been completely
           removed in this release. They were deprecated in pymongo-1.4 and
           have had no effect since then. Please make sure that your code
           doesn't currently pass these parameters when creating a
           Connection instance.

Issues resolved ...............

- [PYTHON-241](https://jira.mongodb.org/browse/PYTHON-241):
Support setting slaveok at the cursor level.

- [PYTHON-240](https://jira.mongodb.org/browse/PYTHON-240):
Queries can sometimes permanently fail after a replica set fail over.

- [PYTHON-238](https://jira.mongodb.org/browse/PYTHON-238):
error after few million requests

- [PYTHON-237](https://jira.mongodb.org/browse/PYTHON-237):
Basic IPv6 support.

- [PYTHON-236](https://jira.mongodb.org/browse/PYTHON-236):
Restore option to specify pool size in Connection.

- [PYTHON-212](https://jira.mongodb.org/browse/PYTHON-212):
pymongo does not recover after stale config

- [PYTHON-138](https://jira.mongodb.org/browse/PYTHON-138):
Find method for GridFS

## Changes in Version 1.10.1 (2011/04/07)

Version 1.10.1 is primarily a bugfix release. It fixes a regression in version 1.10 that broke pickling of ObjectIds. A number of other bugs have been fixed as well.

There are two behavior changes to be aware of:

- If a read slave raises `pymongo.errors.AutoReconnect`
`pymongo.master_slave_connection.MasterSlaveConnection` will now retry the query on each slave until it is successful or all slaves have raised `pymongo.errors.AutoReconnect`. Any other exception will immediately be raised. The order that the slaves are tried is random. Previously the read would be sent to one randomly chosen slave and `pymongo.errors.AutoReconnect` was immediately raised in case of a connection failure.

- A Python `long` is now always BSON encoded as an int64. Previously the
encoding was based only on the value of the field and a `long` with a value less than `2147483648` or greater than `-2147483649` would always be BSON encoded as an int32.

Issues resolved ...............

- [PYTHON-234](https://jira.mongodb.org/browse/PYTHON-234):
Fix setup.py to raise exception if any when building extensions

- [PYTHON-233](https://jira.mongodb.org/browse/PYTHON-233):
Add information to build and test with extensions on windows

- [PYTHON-232](https://jira.mongodb.org/browse/PYTHON-232):
Traceback when hashing a DBRef instance

- [PYTHON-231](https://jira.mongodb.org/browse/PYTHON-231):
Traceback when pickling a DBRef instance

- [PYTHON-230](https://jira.mongodb.org/browse/PYTHON-230):
Pickled ObjectIds are not compatible between pymongo 1.9 and 1.10

- [PYTHON-228](https://jira.mongodb.org/browse/PYTHON-228):
Cannot pickle bson.ObjectId

- [PYTHON-227](https://jira.mongodb.org/browse/PYTHON-227):
Traceback when calling find() on system.js

- [PYTHON-216](https://jira.mongodb.org/browse/PYTHON-216):
MasterSlaveConnection is missing disconnect() method

- [PYTHON-186](https://jira.mongodb.org/browse/PYTHON-186):
When storing integers, type is selected according to value instead of type

- [PYTHON-173](https://jira.mongodb.org/browse/PYTHON-173):
as_class option is not propagated by Cursor.clone

- [PYTHON-113](https://jira.mongodb.org/browse/PYTHON-113):
Redunducy in MasterSlaveConnection

## Changes in Version 1.10 (2011/03/30)

Version 1.10 includes changes to support new features in MongoDB 1.8.x. Highlights include a modified map/reduce API including an inline map/reduce helper method, a new find_and_modify helper, and the ability to query the server for the maximum BSON document size it supports.

- added `pymongo.collection.Collection.find_and_modify`.
- added `pymongo.collection.Collection.inline_map_reduce`.
- changed `pymongo.collection.Collection.map_reduce`.
> **Warning:** collections for map/reduce results. An output collection name must be
provided and the output will replace any existing output collection with
the same name. `pymongo.collection.Collection.map_reduce` now
requires the `out` parameter.

Issues resolved ...............

- PYTHON-225: `pymongo.objectid.ObjectId` class definition should use __slots__.
- PYTHON-223: Documentation fix.
- PYTHON-220: Documentation fix.
- PYTHON-219: KeyError in `pymongo.collection.Collection.find_and_modify`
- PYTHON-213: Query server for maximum BSON document size.
- PYTHON-208: Fix `pymongo.connection.Connection` __repr__.
- PYTHON-207: Changes to Map/Reduce API.
- PYTHON-205: Accept slaveOk in the URI to match the URI docs.
- PYTHON-203: When slave_okay=True and we only specify one host don't autodetect other set members.
- PYTHON-194: Show size when whining about a document being too large.
- PYTHON-184: Raise `pymongo.errors.DuplicateKeyError` for duplicate keys in capped collections.
- PYTHON-178: Don't segfault when trying to encode a recursive data structure.
- PYTHON-177: Don't segfault when decoding dicts with broken iterators.
- PYTHON-172: Fix a typo.
- PYTHON-170: Add `pymongo.collection.Collection.find_and_modify`.
- PYTHON-169: Support deepcopy of DBRef.
- PYTHON-167: Duplicate of PYTHON-166.
- PYTHON-166: Fixes a concurrency issue.
- PYTHON-158: Add code and err string to `db assertion` messages.
## Changes in Version 1.9 (2010/09/28)

Version 1.9 adds a new package to the PyMongo distribution, `bson`. `bson` contains all of the [BSON](https://bsonspec.org) encoding and decoding logic, and the BSON types that were formerly in the `pymongo` package. The following modules have been renamed:

- `pymongo.bson` -> `bson`
- `pymongo._cbson` -> `bson._cbson` and
`pymongo._cmessage`

- `pymongo.binary` -> `bson.binary`
- `pymongo.code` -> `bson.code`
- `pymongo.dbref` -> `bson.dbref`
- `pymongo.json_util` -> `bson.json_util`
- `pymongo.max_key` -> `bson.max_key`
- `pymongo.min_key` -> `bson.min_key`
- `pymongo.objectid` -> `bson.objectid`
- `pymongo.son` -> `bson.son`
- `pymongo.timestamp` -> `bson.timestamp`
- `pymongo.tz_util` -> `bson.tz_util`
In addition, the following exception classes have been renamed:

- `pymongo.errors.InvalidBSON` ->
`bson.errors.InvalidBSON`

- `pymongo.errors.InvalidStringData` ->
`bson.errors.InvalidStringData`

- `pymongo.errors.InvalidDocument` ->
`bson.errors.InvalidDocument`

- `pymongo.errors.InvalidId` ->
`bson.errors.InvalidId`

The above exceptions now inherit from `bson.errors.BSONError` rather than `pymongo.errors.PyMongoError`.

> **Note:**         created with the old names, so these changes should not break
        existing code. The old names will eventually be deprecated and then
        removed, so users should begin migrating towards the new names now.

> **Warning:** The change to the exception hierarchy mentioned above is
possibly breaking. If your code is catching
`pymongo.errors.PyMongoError`, then the exceptions raised
by `bson` will not be caught, even though they would have been
caught previously. Before upgrading, it is recommended that users
check for any cases like this.

- the C extension now shares buffer.c/h with the Ruby driver
- `bson` no longer raises `pymongo.errors.InvalidName`,
all occurrences have been replaced with `bson.errors.InvalidDocument`.

- renamed `bson._to_dicts` to `bson.decode_all`.
- renamed `bson.BSON.from_dict` to `bson.BSON.encode`
and `bson.BSON.to_dict` to `bson.BSON.decode`.

- added `pymongo.cursor.Cursor.batch_size`.
- allow updating (some) file metadata after a
`gridfs.grid_file.GridIn` instance has been closed.

- performance improvements for reading from GridFS.
- special cased slice with the same start and stop to return an empty
cursor.

- allow writing `unicode` to GridFS if an `encoding`
attribute has been specified for the file.

- added `gridfs.GridFS.get_version`.
- scope variables for `bson.code.Code` can now be specified as
keyword arguments.

- added `gridfs.grid_file.GridOut.readline` to
`gridfs.grid_file.GridOut`.

- make a best effort to transparently auto-reconnect if a
`pymongo.connection.Connection` has been idle for a while.

- added `pymongo.database.SystemJS.list` to
`pymongo.database.SystemJS`.

- added `file_document` argument to `gridfs.grid_file.GridOut`
to allow initializing from an existing file document.

- raise `pymongo.errors.TimeoutError` even if the
`getLastError` command was run manually and not through "safe" mode.

- added `uuid` support to `bson.json_util`.
## Changes in Version 1.8.1 (2010/08/13)

- fixed a typo in the C extension that could cause safe-mode
operations to report a failure (`SystemError`) even when none occurred.

- added a `__ne__` implementation to any class where we define
`__eq__`.

## Changes in Version 1.8 (2010/08/05)

Version 1.8 adds support for connecting to replica sets, specifying per-operation values for `w` and `wtimeout`, and decoding to timezone-aware datetimes.

- fixed a reference leak in the C extension when decoding a
`bson.dbref.DBRef`.

- added support for `w`, `wtimeout`, and `fsync` (and any other
options for `getLastError`) to "safe mode" operations.

- added `pymongo.connection.Connection.nodes` property.
- added a maximum pool size of 10 sockets.
- added support for replica sets.
- DEPRECATED `pymongo.connection.Connection.from_uri` and
`pymongo.connection.Connection.paired`, both are supplanted by extended functionality in `pymongo.connection.Connection`.

- added tz aware support for datetimes in
`bson.objectid.ObjectId`, `bson.timestamp.Timestamp` and `bson.json_util` methods.

- added `pymongo.collection.Collection.drop` helper.
- reuse the socket used for finding the master when a
`pymongo.connection.Connection` is first created.

- added support for `bson.min_key.MinKey`,
`bson.max_key.MaxKey` and `bson.timestamp.Timestamp` to `bson.json_util`.

- added support for decoding datetimes as aware (UTC) - it is highly
recommended to enable this by setting the `tz_aware` parameter to `pymongo.connection.Connection` to `True`.

- added `network_timeout` option for individual calls to
`pymongo.collection.Collection.find` and `pymongo.collection.Collection.find_one`.

- added `gridfs.GridFS.exists` to check if a file exists in
GridFS.

- added support for additional keys in `bson.dbref.DBRef`
instances.

- added `pymongo.errors.OperationFailure.code` attribute to
`pymongo.errors.OperationFailure` exceptions.

- fixed serialization of int and float subclasses in the C extension.
## Changes in Version 1.7 (2010/06/17)

Version 1.7 is a recommended upgrade for all PyMongo users. The full release notes are below, and some more in depth discussion of the highlights is [here](https://dirolf.com/2010/06/17/pymongo-1.7-released.html).

- no longer attempt to build the C extension on big-endian systems.
- added `bson.min_key.MinKey` and
`bson.max_key.MaxKey`.

- use unsigned for `bson.timestamp.Timestamp` in BSON
encoder/decoder.

- support `True` as `"ok"` in command responses, in addition to
`1.0` - necessary for server versions **>= 1.5.X**

- BREAKING change to
`pymongo.collection.Collection.index_information` to add support for querying unique status and other index information.

- added `pymongo.connection.Connection.document_class`, to
specify class for returned documents.

- added `as_class` argument for
`pymongo.collection.Collection.find`, and in the BSON decoder.

- added support for creating `bson.timestamp.Timestamp`
instances using a `datetime.datetime`.

- allow `dropTarget` argument for
`pymongo.collection.Collection.rename`.

- handle aware `datetime.datetime` instances, by converting to
UTC.

- added support for `pymongo.cursor.Cursor.max_scan`.
- raise `gridfs.errors.FileExists` exception when creating a
duplicate GridFS file.

- use [y2038](https://github.com/evalEmpire/y2038/) for time handling in
the C extension - eliminates 2038 problems when extension is installed.

- added `sort` parameter to
`pymongo.collection.Collection.find`

- finalized deprecation of changes from versions **<= 1.4**
- take any non-`dict` as an `"_id"` query for
`pymongo.collection.Collection.find_one` or `pymongo.collection.Collection.remove`

- added ability to pass a `dict` for `fields` argument to
`pymongo.collection.Collection.find` (supports `"$slice"` and field negation)

- simplified code to find master, since paired setups don't always have
a remote

- fixed bug in C encoder for certain invalid types (like
`pymongo.collection.Collection` instances).

- don't transparently map `"filename"` key to `name` attribute
for GridFS.

## Changes in Version 1.6 (2010/04/14)

The biggest change in version 1.6 is a complete re-implementation of `gridfs` with a lot of improvements over the old implementation. There are many details and examples of using the new API in [this blog post](https://dirolf.com/2010/03/29/new-gridfs-implementation-for-pymongo.html). The old API has been removed in this version, so existing code will need to be modified before upgrading to 1.6.

- fixed issue where connection pool was being shared across
`pymongo.connection.Connection` instances.

- more improvements to Python code caching in C extension - should
improve behavior on mod_wsgi.

- added `bson.objectid.ObjectId.from_datetime`.
- complete rewrite of `gridfs` support.
- improvements to the `pymongo.database.Database.command` API.
- fixed `pymongo.collection.Collection.drop_indexes` behavior
on non-existent collections.

- disallow empty bulk inserts.
## Changes in Version 1.5.2 (2010/03/31)

- fixed response handling to ignore unknown response flags in queries.
- handle server versions containing '-pre-'.
## Changes in Version 1.5.1 (2010/03/17)

- added `gridfs.grid_file.GridFile._id` property for
`gridfs.grid_file.GridFile` instances.

- fix for making a `pymongo.connection.Connection` (with
`slave_okay` set) directly to a slave in a replica pair.

- accept kwargs for
`pymongo.collection.Collection.create_index` and `pymongo.collection.Collection.ensure_index` to support all indexing options.

- add `pymongo.GEO2D` and support for geo indexing.
- improvements to Python code caching in C extension - should improve
behavior on mod_wsgi.

## Changes in Version 1.5 (2010/03/10)

- added subtype constants to `bson.binary` module.
- DEPRECATED `options` argument to
`pymongo.collection.Collection` and `pymongo.database.Database.create_collection` in favor of kwargs.

- added `pymongo.has_c` to check for C extension.
- added `pymongo.connection.Connection.copy_database`.
- added `pymongo.cursor.Cursor.alive` to tell when a cursor
might have more data to return (useful for tailable cursors).

- added `bson.timestamp.Timestamp` to better support
dealing with internal MongoDB timestamps.

- added `name` argument for
`pymongo.collection.Collection.create_index` and `pymongo.collection.Collection.ensure_index`.

- fixed connection pooling w/ fork
- `pymongo.connection.Connection.paired` takes all kwargs that
are allowed for `pymongo.connection.Connection`.

- `pymongo.collection.Collection.insert` returns list for bulk
inserts of size one.

- fixed handling of `datetime.datetime` instances in
`bson.json_util`.

- added `pymongo.connection.Connection.from_uri` to support
MongoDB connection uri scheme.

- fixed chunk number calculation when unaligned in `gridfs`.
- `pymongo.database.Database.command` takes a string for simple
commands.

- added `pymongo.database.Database.system_js` helper for
dealing with server-side JS.

- don't wrap queries containing `"$query"` (support manual use of
`"$min"`, etc.).

- added `gridfs.errors.GridFSError` as base class for
`gridfs` exceptions.

## Changes in Version 1.4 (2010/01/17)

Perhaps the most important change in version 1.4 is that we have decided to **no longer support Python 2.3**. The most immediate reason for this is to allow some improvements to connection pooling. This will also allow us to use some new (as in Python 2.4 ;) idioms and will help begin the path towards supporting Python 3.0. If you need to use Python 2.3 you should consider using version 1.3 of this driver, although that will no longer be actively supported.

Other changes:

- move `"_id"` to front only for top-level documents (fixes some
corner cases).

- `pymongo.collection.Collection.update` and
`pymongo.collection.Collection.remove` return the entire response to the lastError command when safe is `True`.

- completed removal of things that were deprecated in version 1.2 or
earlier.

- enforce that collection names do not contain the NULL byte.
- fix to allow using UTF-8 collection names with the C extension.
- added `pymongo.errors.PyMongoError` as base exception class
for all `pymongo.errors`. this changes the exception hierarchy somewhat, and is a BREAKING change if you depend on `pymongo.errors.ConnectionFailure` being a `IOError` or `bson.errors.InvalidBSON` being a `ValueError`, for example.

- added `pymongo.errors.DuplicateKeyError` for calls to
`pymongo.collection.Collection.insert` or `pymongo.collection.Collection.update` with `safe` set to `True`.

- removed `pymongo.thread_util`.
- added `pymongo.database.Database.add_user` and
`pymongo.database.Database.remove_user` helpers.

- fix for `pymongo.database.Database.authenticate` when using
non-UTF-8 names or passwords.

- minor fixes for
`pymongo.master_slave_connection.MasterSlaveConnection`.

- clean up all cases where `pymongo.errors.ConnectionFailure`
is raised.

- simplification of connection pooling - makes driver ~2x faster for
simple benchmarks. see [connection pooling](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/connect/connection-options/connection-pools/#connection-pools) for more information.

- DEPRECATED `pool_size`, `auto_start_request` and `timeout`
parameters to `pymongo.connection.Connection`. DEPRECATED `pymongo.connection.Connection.start_request`.

- use `socket.sendall`.
- removed `bson.son.SON.from_xml` as it was only being used
for some internal testing - also eliminates dependency on `elementtree`.

- implementation of `pymongo.message.update` in C.
- deprecate `pymongo.database.Database._command` in favor of
`pymongo.database.Database.command`.

- send all commands without wrapping as `{"query": ...}`.
- support string as `key` argument to
`pymongo.collection.Collection.group` (keyf) and run all groups as commands.

- support for equality testing for `bson.code.Code`
instances.

- allow the NULL byte in strings and disallow it in key names or regex
patterns

## Changes in Version 1.3 (2009/12/16)

- DEPRECATED running `pymongo.collection.Collection.group` as
`pymongo.database.Database.eval`, also changed default for `pymongo.collection.Collection.group` to running as a command

- remove `pymongo.cursor.Cursor.__len__`, which was deprecated
in 1.1.1 - needed to do this aggressively due to it's presence breaking **Django** template for loops

- DEPRECATED `pymongo.connection.Connection.host`,
`pymongo.connection.Connection.port`, `pymongo.database.Database.connection`, `pymongo.database.Database.name`, `pymongo.collection.Collection.database`, `pymongo.collection.Collection.name` and `pymongo.collection.Collection.full_name` in favor of `pymongo.connection.Connection.host`, `pymongo.connection.Connection.port`, `pymongo.database.Database.connection`, `pymongo.database.Database.name`, `pymongo.collection.Collection.database`, `pymongo.collection.Collection.name` and `pymongo.collection.Collection.full_name`, respectively. The deprecation schedule for this change will probably be faster than usual, as it carries some performance implications.

- added `pymongo.connection.Connection.disconnect`
## Changes in Version 1.2.1 (2009/12/10)

- added `changelog` to docs
- added `setup.py doc --test` to run doctests for tutorial, examples
- moved most examples to Sphinx docs (and remove from examples/
directory)

- raise `bson.errors.InvalidId` instead of
`TypeError` when passing a 24 character string to `bson.objectid.ObjectId` that contains non-hexadecimal characters

- allow `unicode` instances for `bson.objectid.ObjectId` init
## Changes in Version 1.2 (2009/12/09)

- `spec` parameter for `pymongo.collection.Collection.remove` is
now optional to allow for deleting all documents in a `pymongo.collection.Collection`

- always wrap queries with `{query: ...}` even when no special options -
get around some issues with queries on fields named `query`

- enforce 4MB document limit on the client side
- added `pymongo.collection.Collection.map_reduce` helper - see
[Aggregation](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/aggregation/#transform-your-data-with-aggregation)

- added `pymongo.cursor.Cursor.distinct` method on
`pymongo.cursor.Cursor` instances to allow distinct with queries

- fix for `pymongo.cursor.Cursor.__getitem__` after
`pymongo.cursor.Cursor.skip`

- allow any UTF-8 string in `bson.BSON` encoder, not
just ASCII subset

- added `bson.objectid.ObjectId.generation_time`
- removed support for legacy `bson.objectid.ObjectId`
format - pretty sure this was never used, and is just confusing

- DEPRECATED `bson.objectid.ObjectId.url_encode` and
`bson.objectid.ObjectId.url_decode` in favor of `str` and `bson.objectid.ObjectId`, respectively

- allow oplog.$main as a valid collection name
- some minor fixes for installation process
- added support for datetime and regex in `bson.json_util`
## Changes in Version 1.1.2 (2009/11/23)

- improvements to `pymongo.collection.Collection.insert` speed
(using C for insert message creation)

- use random number for request_id
- fix some race conditions with `pymongo.errors.AutoReconnect`
## Changes in Version 1.1.1 (2009/11/14)

- added `multi` parameter for
`pymongo.collection.Collection.update`

- fix unicode regex patterns with C extension
- added `pymongo.collection.Collection.distinct`
- added `database` support for `bson.dbref.DBRef`
- added `bson.json_util` with helpers for encoding / decoding
special types to JSON

- DEPRECATED `pymongo.cursor.Cursor.__len__` in favor of
`pymongo.cursor.Cursor.count` with `with_limit_and_skip` set to `True` due to performance regression

- switch documentation to Sphinx
## Changes in Version 1.1 (2009/10/21)

- added `__hash__` for `bson.dbref.DBRef` and
`bson.objectid.ObjectId`

- bulk `pymongo.collection.Collection.insert` works with any
iterable

- fix `bson.objectid.ObjectId` generation when using
`multiprocessing`

- added `pymongo.cursor.Cursor.collection`
- added `network_timeout` parameter for
`pymongo.connection.Connection`

- DEPRECATED `slave_okay` parameter for individual queries
- fix for `safe` mode when multi-threaded
- added `safe` parameter for `pymongo.collection.Collection.remove`
- added `tailable` parameter for `pymongo.collection.Collection.find`
## Changes in Version 1.0 (2009/09/30)

- fixes for
`pymongo.master_slave_connection.MasterSlaveConnection`

- added `finalize` parameter for `pymongo.collection.Collection.group`
- improvements to `pymongo.collection.Collection.insert` speed
- improvements to `gridfs` speed
- added `pymongo.cursor.Cursor.__getitem__` and
`pymongo.cursor.Cursor.__len__` for `pymongo.cursor.Cursor` instances

## Changes in Version 0.16 (2009/09/16)

- support for encoding/decoding `uuid.UUID` instances
- fix for `pymongo.cursor.Cursor.explain` with limits
## Changes in Version 0.15.2 (2009/09/09)

- documentation changes only
## Changes in Version 0.15.1 (2009/09/02)

- various performance improvements
- API CHANGE no longer need to specify direction for
`pymongo.collection.Collection.create_index` and `pymongo.collection.Collection.ensure_index` when indexing a single key

- support for encoding `tuple` instances as `list`
instances

## Changes in Version 0.15 (2009/08/26)

- fix string representation of `bson.objectid.ObjectId`
instances

- added `timeout` parameter for
`pymongo.collection.Collection.find`

- allow scope for `reduce` function in
`pymongo.collection.Collection.group`

## Changes in Version 0.14.2 (2009/08/24)

- minor bugfixes
## Changes in Version 0.14.1 (2009/08/21)

- `gridfs.grid_file.GridFile.seek` and
`gridfs.grid_file.GridFile.tell` for (read mode) `gridfs.grid_file.GridFile` instances

## Changes in Version 0.14 (2009/08/19)

- support for long in `bson.BSON`
- added `pymongo.collection.Collection.rename`
- added `snapshot` parameter for
`pymongo.collection.Collection.find`

## Changes in Version 0.13 (2009/07/29)

- better
`pymongo.master_slave_connection.MasterSlaveConnection` support

- API CHANGE `pymongo.collection.Collection.insert` and
`pymongo.collection.Collection.save both return inserted id`

- DEPRECATED passing an index name to
`pymongo.cursor.Cursor.hint`

## Changes in Version 0.12 (2009/07/08)

- improved `bson.objectid.ObjectId` generation
- added `pymongo.errors.AutoReconnect` exception for when
reconnection is possible

- make `gridfs` thread-safe
- fix for `gridfs` with non `bson.objectid.ObjectId id`
## Changes in Version 0.11.3 (2009/06/18)

- don't allow NULL bytes in string encoder
- fixes for Python 2.3
## Changes in Version 0.11.2 (2009/06/08)

- PEP 8
- updates for `pymongo.collection.Collection.group`
- VS build
## Changes in Version 0.11.1 (2009/06/04)

- fix for connection pooling under Python 2.5
## Changes in Version 0.11 (2009/06/03)

- better build failure detection
- driver support for selecting fields in sub-documents
- disallow insertion of invalid key names
- added `timeout` parameter for `pymongo.connection.Connection`
## Changes in Version 0.10.3 (2009/05/27)

- fix bug with large `pymongo.cursor.Cursor.limit`
- better exception when modules get reloaded out from underneath the C
extension

- better exception messages when calling a
`pymongo.collection.Collection` or `pymongo.database.Database` instance

## Changes in Version 0.10.2 (2009/05/22)

- support subclasses of `dict` in C encoder
## Changes in Version 0.10.1 (2009/05/18)

- alias `pymongo.connection.Connection` as
`pymongo.Connection`

- raise an exception rather than silently overflowing in encoder
## Changes in Version 0.10 (2009/05/14)

- added `pymongo.collection.Collection.ensure_index`
## Changes in Version 0.9.7 (2009/05/13)

- allow sub-collections of $cmd as valid
`pymongo.collection.Collection` names

- add version as `pymongo.version`
- add `--no_ext` command line option to setup.py
