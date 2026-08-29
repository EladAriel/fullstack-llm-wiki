---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/storage.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.469060Z"
---
# Storage

**meta:** :description: Explore different storage engines in MongoDB, including options for journaling and handling large files with GridFS.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

The :ref:`storage engine <storage-engines>` is the primary
component of MongoDB responsible for managing data. MongoDB provides a
variety of storage engines, allowing you to choose one most suited to
your application.

The :term:`journal` is a log that helps the database recover in the
event of a hard shutdown. There are several configurable options that
allows the journal to strike a balance between performance and
reliability that works for your particular use case.

:doc:`/core/gridfs` is a versatile storage system that is suited to
handling large files, such as those exceeding the 16 MB document size
limit.

**toctree:** :titlesonly: 
   :hidden: 

   WiredTiger </core/wiredtiger>
   Journaling </core/journaling>