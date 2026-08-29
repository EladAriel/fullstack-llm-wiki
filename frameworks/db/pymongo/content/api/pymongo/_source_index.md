---
type: "Framework Learn Page"
framework: "PyMongo"
source_repo: "https://github.com/mongodb/mongo-python-driver"
source_branch: "main"
source_path: "doc/api/pymongo/index.rst"
source_commit: "5cf3268f82f21e7683e10a21e0c36fa947e640fa"
source_commit_short: "5cf3268"
source_commit_date: "2026-08-28T14:23:00-04:00"
generated_at: "2026-08-29T09:39:25.620611Z"
---
# :mod:`pymongo` -- Python driver for MongoDB

**automodule:** pymongo
   :synopsis: Python driver for MongoDB

   .. autodata:: version
   .. data:: MongoClient

      Alias for :class:`pymongo.mongo_client.MongoClient`.

   .. data:: AsyncMongoClient

      Alias for :class:`pymongo.asynchronous.mongo_client.AsyncMongoClient`.

   .. data:: ReadPreference

      Alias for :class:`pymongo.read_preferences.ReadPreference`.

   .. autofunction:: has_c
   .. data:: MIN_SUPPORTED_WIRE_VERSION

      The minimum wire protocol version PyMongo supports.

   .. data:: MAX_SUPPORTED_WIRE_VERSION

      The maximum wire protocol version PyMongo supports.

   .. autofunction:: timeout

Sub-modules:

**toctree:** :maxdepth: 3

   asynchronous/index
   auth_oidc
   change_stream
   client_options
   client_session
   collation
   collection
   command_cursor
   cursor
   database
   driver_info
   encryption
   encryption_options
   errors
   mongo_client
   monitoring
   operations
   pool
   read_concern
   read_preferences
   results
   server_api
   server_description
   topology_description
   uri_parser
   write_concern
   event_loggers