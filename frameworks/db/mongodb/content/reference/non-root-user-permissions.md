---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/non-root-user-permissions.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===================================

# Configure Non-Root User Permissions

To maintain database security, you can limit authorized, non-root users’ privileges, allowing them to perform administrative operations without granting them full root privileges.

This page demonstrates how to allow non-root users to start, stop, and restart `mongod` processes on Linux systems, without allowing them access to all root user privileges. This procedure applies to users belonging to a non-root Linux group, distinct from the group under which the `mongod` process runs.

## Before You Begin

Install `MongoDB Community <install-mdb-community-edition-linux>` or `MongoDB Enterprise <install-mdb-enterprise>`.

## Considerations

> **Important:** The following procedure requires root access for the setup. Incorrect settings
can lead to an unresponsive system, so always test on a development environment
before implementing in production. Ensure you have a current backup of your data.

- We recommend you perform this procedure while setting up a new system. If this
is not possible, perform the procedure during the maintenance window.

- This procedure impacts the settings of only one local system. If you
are using a replica set or a sharded cluster, perform this procedure in a rolling matter. Do not update all of your nodes at once.

- This procedure works with all Linux distributions, but has only been
tested with CentOS 6/7, RHEL 6/7, Ubuntu 18.04, and Amazon Linux 2.

## Procedure

Select the tab for your system provider below.
