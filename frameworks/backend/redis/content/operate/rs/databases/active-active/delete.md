---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/databases/active-active/delete.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.421067Z"
---
# Delete

---
Title: Delete Active-Active databases
alwaysopen: false
categories:
- docs
- operate
- rs
description: Considerations while deleting Active-Active databases.
linktitle: Delete
weight: 35
---

When you delete an Active-Active database (formerly known as CRDB),
all instances of the Active-Active database are deleted from all participating clusters.

{{% warning %}}
This action is immediate, non-reversible, and has no rollback.
{{% /warning %}}

Because Active-Active databases are made up of instances on multiple participating clusters,
to restore a deleted Active-Active database you must create the database again with all of its instances
and then restore the data to the database from backup.

We recommended that you:

- Back up your data and test the restore on another database before you delete an Active-Active database.
- Consider [flushing the data]({{< relref "/operate/rs/databases/import-export/flush.md" >}}) from the database
    so that you can keep the Active-Active database configuration and restore the data to it if necessary.
