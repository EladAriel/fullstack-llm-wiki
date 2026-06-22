---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-backup-snapshots-with-ebs-in-raid10.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

### Snapshots with Amazon EBS in a RAID 10 Configuration

If your deployment depends on Amazon's Elastic Block Storage (EBS) with RAID configured within your instance, it is impossible to get a consistent state across all disks using the platform's snapshot tool. As an alternative, you can do one of the following:

- Set a :dbcommand:`fsync` lock to flush all writes and lock the
cluster against new writes to help reduce the likelihood of an inconsistent state occurring during the backup process.

If you choose this option see `backup-without-journaling`.

- Configure `LVM` to run and hold your MongoDB data files on top of the
RAID within your system.

If you choose this option, perform the LVM backup operation described in `lvm-backup-operation`.
