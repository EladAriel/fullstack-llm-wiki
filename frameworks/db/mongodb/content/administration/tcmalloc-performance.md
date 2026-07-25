---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/administration/tcmalloc-performance.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

===============================================================

# TCMalloc Performance Optimization for a Self-Managed Deployment

.. versionchanged:: 8.0

.. include:: /includes/8.0-tcmalloc-intro.rst

To use the new TCMalloc version:

- Use a `supported operating system <tcmalloc-new-platform-support>`.
- `Enable THP <tcmalloc-new-enable-thp>`.
- `Enable per-CPU caches <tcmalloc-new-per-cpu-caches>`.
## Platform Support

Operating systems that support MongoDB 8.0 also support the updated TCMalloc, **except** for the following:

- RHEL 8 / Oracle 8 on the
`PPC64LE <prod-notes-supported-platforms-PPC64LE>` and `s390x <prod-notes-supported-platforms-s390x>` architectures

- RHEL 9 / CentOS 9 / Oracle 9 on the
`PPC64LE <prod-notes-supported-platforms-PPC64LE>` architecture

These operating systems use the legacy TCMalloc version. If you use these operating systems, `disable THP <disable-thp>`.

Windows uses the legacy TCMalloc version and does not support the updated TCMalloc.

## Enable Transparent Hugepages (THP)

.. include:: /includes/fact-thp-intro.rst

In MongoDB 8.0 and later, ensure that THP is enabled before :binary:`~bin.mongod` starts by creating a service file for your platform's initialization system. If you are using MongoDB 7.0 or earlier, `disable THP <disable-thp>`.

> **Note:** .. include:: /includes/fact-thp-process-level.rst

Additionally, for :abbr:`RHEL (Red Hat Enterprise Linux)` and CentOS systems that use `ktune` and `tuned` performance profiles, you must also create a custom `tuned` profile.

### Create a Service File

To create a service file that enables THP, use the built-in initialization system for your platform. Recent versions of Linux typically use **systemd**, which uses the `systemctl` command. Older versions of Linux tend to use **System V init**, which uses the `service` command. For more information, see the documentation for your operating system.

Use the initialization system for your platform:

### Using `tuned` and `ktune`

.. include:: /includes/fact-tuned-ktune-profiles.rst

`tuned` and `ktune` are kernel tuning utilities that can affect the Transparent Hugepages setting on your system. If you are using `tuned` or `ktune` on your :abbr:`RHEL (Red Hat Enterprise Linux)` or CentOS system while running `mongod`, you must create a custom `tuned` profile to ensure that THP stays enabled.

.. include:: /includes/steps-enable-thp-in-tuned-rhel.rst

## Enable Per-CPU Caches

To verify that TCMalloc is running with per-CPU caches, ensure that:

- :serverstatus:`tcmalloc.usingPerCPUCaches` is `true`.
- :serverstatus:`tcmalloc.tcmalloc.cpu_free` is greater than `0`.
If per-CPU caches aren't enabled, ensure that:

- You disable glibc rseq.
- You're using Linux kernel version 4.18 or later.
### Disable glibc rseq

The new TCMalloc requires [Restartable Sequences (rseq)](https://github.com/google/tcmalloc/blob/master/docs/design.md#restartable-sequences-and-per-cpu-tcmalloc) to implement per-CPU caches. If another application, such as the glibc library, registers an rseq structure before TCMalloc, TCMalloc can't use rseq. Without rseq, TCMalloc uses per-thread caches, which are used by the legacy TCMalloc version.

To enable per-CPU caches, disable glibc’s rseq registration by setting the following environment variable before you start `mongod`:

```sh
 GLIBC_TUNABLES=glibc.pthread.rseq=0
 export GLIBC_TUNABLES
```

### Check Kernel Version

If per-CPU caches are still not enabled after disabling glibc rseq, verify that you're using Linux kernel 4.18 or later:

```sh
uname -r
```

## Learn More

- `8.0-tcmalloc-upgrade`
- [Google's TCMalloc Tuning Guide](https://google.github.io/tcmalloc/tuning.html)
- `tcmalloc serverStatus metrics <server-status-tcmalloc>`
## Contents

- Disable Transparent Hugepages </tutorial/disable-transparent-huge-pages>
