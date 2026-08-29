---
type: "Framework Learn Page"
framework: "PyMongo"
source_repo: "https://github.com/mongodb/mongo-python-driver"
source_branch: "main"
source_path: "doc/api/pymongo/database.rst"
source_commit: "5cf3268f82f21e7683e10a21e0c36fa947e640fa"
source_commit_short: "5cf3268"
source_commit_date: "2026-08-28T14:23:00-04:00"
generated_at: "2026-08-29T09:39:25.620092Z"
---
# :mod:`database` -- Database level operations

**automodule:** pymongo.database
   :synopsis: Database level operations

   .. autodata:: pymongo.auth.MECHANISMS

   .. autoclass:: pymongo.database.Database
      :members:

      .. describe:: db[collection_name] || db.collection_name

         Get the `collection_name` :class:`~pymongo.collection.Collection` of
         :class:`Database` `db`.

         Raises :class:`~pymongo.errors.InvalidName` if an invalid collection
         name is used.

         .. note::  Use dictionary style access if `collection_name` is an
            attribute of the :class:`Database` class eg: db[`collection_name`].

      .. automethod:: __getitem__
      .. automethod:: __getattr__
      .. autoattribute:: codec_options
      .. autoattribute:: read_preference
      .. autoattribute:: write_concern
      .. autoattribute:: read_concern