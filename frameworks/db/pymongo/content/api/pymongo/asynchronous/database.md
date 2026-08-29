---
type: "Framework Learn Page"
framework: "PyMongo"
source_repo: "https://github.com/mongodb/mongo-python-driver"
source_branch: "main"
source_path: "doc/api/pymongo/asynchronous/database.rst"
source_commit: "5cf3268f82f21e7683e10a21e0c36fa947e640fa"
source_commit_short: "5cf3268"
source_commit_date: "2026-08-28T14:23:00-04:00"
generated_at: "2026-08-29T09:39:25.624634Z"
---
# :mod:`database` -- Database level operations


**automodule:** pymongo.asynchronous.database
   :synopsis: Database level operations

   .. autoclass:: pymongo.asynchronous.database.AsyncDatabase
      :members:

      .. describe:: db[collection_name] || db.collection_name

         Get the `collection_name` :class:`~pymongo.asynchronous.collection.AsyncCollection` of
         :class:`AsyncDatabase` `db`.

         Raises :class:`~pymongo.errors.InvalidName` if an invalid collection
         name is used.

         .. note::  Use dictionary style access if `collection_name` is an
            attribute of the :class:`AsyncDatabase` class eg: db[`collection_name`].

      .. automethod:: __getitem__
      .. automethod:: __getattr__
      .. autoattribute:: codec_options
      .. autoattribute:: read_preference
      .. autoattribute:: write_concern
      .. autoattribute:: read_concern