---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/disable-transparent-huge-pages.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

================================================================

# Disable Transparent Hugepages (THP) for Self-Managed Deployments

> **Important:** Starting in MongoDB 8.0, MongoDB uses an upgraded version of TCMalloc
that improves performance with Transparent Hugepages enabled. If you are
using MongoDB 8.0 or later, see `enable-thp`.

.. include:: /includes/fact-thp-intro.rst

When running MongoDB 7.0 or earlier on Linux, THP should be disabled for best performance. In earlier versions of MongoDB, database workloads often experience decreased performance with THP enabled because they often use non-contiguous, memory access patterns.

> **Note:** .. include:: /includes/fact-thp-process-level.rst

To ensure that THP is disabled before :binary:`~bin.mongod` starts, create a service file for your operating system that disables THP at boot. The following instructions include examples for both the **systemd** and the **System V init** initialization systems.

Additionally, for :abbr:`RHEL (Red Hat Enterprise Linux)` and CentOS systems that use `ktune` and `tuned` performance profiles, you must create a custom `tuned` profile as well.

## Create a Service File

To create a service file that disables THP, use the built-in initialization system for your operating system. Recent versions of Linux typically use **systemd**, which uses the `systemctl` command. Older versions of Linux use **System V init**, which uses the `service` command. For more information, see the documentation for your operating system.

Use the initialization system for your operating system:

## Using `tuned` and `ktune`

.. include:: /includes/fact-tuned-ktune-profiles.rst

`tuned` and `ktune` are kernel tuning utilities that can affect the Transparent Hugepages setting on your system. If you use `tuned` or `ktune` on your :abbr:`RHEL (Red Hat Enterprise Linux)` or CentOS system while running `mongod`, you must create a custom `tuned` profile to ensure that THP stays disabled.

### Red Hat/CentOS 6

.. include:: /includes/steps/disable-thp-in-tuned-rhel-6.rst

### Red Hat/CentOS 7 and 8

.. include:: /includes/steps/disable-thp-in-tuned-rhel-7.rst
