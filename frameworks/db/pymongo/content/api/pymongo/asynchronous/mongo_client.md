---
type: "Framework Learn Page"
framework: "PyMongo"
source_repo: "https://github.com/mongodb/mongo-python-driver"
source_branch: "main"
source_path: "doc/api/pymongo/asynchronous/mongo_client.rst"
source_commit: "5cf3268f82f21e7683e10a21e0c36fa947e640fa"
source_commit_short: "5cf3268"
source_commit_date: "2026-08-28T14:23:00-04:00"
generated_at: "2026-08-29T09:39:25.624442Z"
---
# :mod:`mongo_client` -- Tools for connecting to MongoDB


**automodule:** pymongo.asynchronous.mongo_client
   :synopsis: Tools for connecting to MongoDB

   .. autoclass:: pymongo.asynchronous.mongo_client.AsyncMongoClient(host='localhost', port=27017, document_class=dict, tz_aware=False, connect=True, **kwargs)

      .. automethod:: close

      .. describe:: c[db_name] || c.db_name

         Get the `db_name` :class:`~pymongo.asynchronous.database.AsyncDatabase` on :class:`AsyncMongoClient` `c`.

         Raises :class:`~pymongo.errors.InvalidName` if an invalid database name is used.

      .. autoattribute:: topology_description
      .. autoattribute:: address
      .. autoattribute:: primary
      .. autoattribute:: secondaries
      .. autoattribute:: arbiters
      .. autoattribute:: is_primary
      .. autoattribute:: is_mongos
      .. autoattribute:: nodes
      .. autoattribute:: codec_options
      .. autoattribute:: read_preference
      .. autoattribute:: write_concern
      .. autoattribute:: read_concern
      .. autoattribute:: options
      .. automethod:: start_session
      .. automethod:: list_databases
      .. automethod:: list_database_names
      .. automethod:: drop_database
      .. automethod:: get_default_database
      .. automethod:: get_database
      .. automethod:: server_info
      .. automethod:: watch
      .. automethod:: bulk_write
      .. automethod:: __getitem__
      .. automethod:: __getattr__