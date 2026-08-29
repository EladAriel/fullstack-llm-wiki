---
type: "Framework Learn Page"
framework: "PyMongo"
source_repo: "https://github.com/mongodb/mongo-python-driver"
source_branch: "main"
source_path: "doc/api/bson/binary.rst"
source_commit: "5cf3268f82f21e7683e10a21e0c36fa947e640fa"
source_commit_short: "5cf3268"
source_commit_date: "2026-08-28T14:23:00-04:00"
generated_at: "2026-08-29T09:39:25.618693Z"
---
# :mod:`binary` -- Tools for representing binary data to be stored in MongoDB

**automodule:** bson.binary
   :synopsis: Tools for representing binary data to be stored in MongoDB

   .. autodata:: BINARY_SUBTYPE
   .. autodata:: FUNCTION_SUBTYPE
   .. autodata:: OLD_BINARY_SUBTYPE
   .. autodata:: OLD_UUID_SUBTYPE
   .. autodata:: UUID_SUBTYPE
   .. autodata:: STANDARD
   .. autodata:: PYTHON_LEGACY
   .. autodata:: JAVA_LEGACY
   .. autodata:: CSHARP_LEGACY
   .. autodata:: MD5_SUBTYPE
   .. autodata:: COLUMN_SUBTYPE
   .. autodata:: SENSITIVE_SUBTYPE
   .. autodata:: VECTOR_SUBTYPE
   .. autodata:: USER_DEFINED_SUBTYPE

   .. autoclass:: UuidRepresentation
      :members:

   .. autoclass:: BinaryVectorDtype
      :members:
      :show-inheritance:

   .. autoclass:: BinaryVector
      :members:


   .. autoclass:: Binary(data, subtype=BINARY_SUBTYPE)
      :members:
      :show-inheritance: