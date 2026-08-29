---
type: "Framework Learn Page"
framework: "PyMongo"
source_repo: "https://github.com/mongodb/mongo-python-driver"
source_branch: "main"
source_path: "doc/api/pymongo/read_preferences.rst"
source_commit: "5cf3268f82f21e7683e10a21e0c36fa947e640fa"
source_commit_short: "5cf3268"
source_commit_date: "2026-08-28T14:23:00-04:00"
generated_at: "2026-08-29T09:39:25.622523Z"
---
# :mod:`read_preferences` -- Utilities for choosing which member of a replica set to read from.

**automodule:** pymongo.read_preferences
   :synopsis: Utilities for choosing which member of a replica set to read from.

   .. autoclass:: pymongo.read_preferences.Primary

      .. max_staleness, min_wire_version, mongos_mode, and tag_sets don't
         make sense for Primary.

      .. autoattribute:: document
      .. autoattribute:: mode
      .. autoattribute:: name

   .. autoclass:: pymongo.read_preferences.PrimaryPreferred
      :inherited-members:
   .. autoclass:: pymongo.read_preferences.Secondary
      :inherited-members:
   .. autoclass:: pymongo.read_preferences.SecondaryPreferred
      :inherited-members:
   .. autoclass:: pymongo.read_preferences.Nearest
      :inherited-members:

   .. autoclass:: ReadPreference

      .. autoattribute:: PRIMARY
      .. autoattribute:: PRIMARY_PREFERRED
      .. autoattribute:: SECONDARY
      .. autoattribute:: SECONDARY_PREFERRED
      .. autoattribute:: NEAREST