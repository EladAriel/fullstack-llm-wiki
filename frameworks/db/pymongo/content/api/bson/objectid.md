---
type: "Framework Learn Page"
framework: "PyMongo"
source_repo: "https://github.com/mongodb/mongo-python-driver"
source_branch: "main"
source_path: "doc/api/bson/objectid.rst"
source_commit: "5cf3268f82f21e7683e10a21e0c36fa947e640fa"
source_commit_short: "5cf3268"
source_commit_date: "2026-08-28T14:23:00-04:00"
generated_at: "2026-08-29T09:39:25.618037Z"
---
# :mod:`objectid` -- Tools for working with MongoDB ObjectIds

**automodule:** bson.objectid
   :synopsis: Tools for working with MongoDB ObjectIds

   .. autoclass:: bson.objectid.ObjectId(oid=None)
      :members:

      .. describe:: str(o)

         Get a hex encoded version of :class:`ObjectId` `o`.

         The following property always holds:

         .. testsetup::

           from bson.objectid import ObjectId

         .. doctest::

           >>> o = ObjectId()
           >>> o == ObjectId(str(o))
           True

         This representation is useful for urls or other places where
         ``o.binary`` is inappropriate.