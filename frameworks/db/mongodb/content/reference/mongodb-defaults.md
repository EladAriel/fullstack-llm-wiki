---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/mongodb-defaults.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================================

# Default MongoDB Read Concerns/Write Concerns

However, going forward, this page could be a 1-stop shop for defaults used in MongoDB and as such the file itself is named mongodb-defaults in anticipation of future work.

## Read Concern

.. figure:: /images/read-write-concern-inheritance.bakedsvg.svg

### Default Read Concern

The :red:`default` `read concern <read-concern>` is as follows:

### Specify Read Concern: MongoDB Drivers

### Additional Information

For more information on the available read concerns, see `/reference/read-concern`.

## Write Concern

.. figure:: /images/read-write-concern-inheritance.bakedsvg.svg

### Default Write Concern

.. include:: /includes/5.0-default-wc.rst

### Specify Write Concern: MongoDB Drivers

### Additional Information

For more information on the available write concerns, see `/reference/write-concern`.

## Causal Consistency Guarantees

With `causally consistent client sessions <sessions>`, the client sessions only guarantee causal consistency if:

- the associated read operations use :readconcern:`"majority"` read
concern, and

- the associated write operations use :writeconcern:`"majority"`
write concern.
