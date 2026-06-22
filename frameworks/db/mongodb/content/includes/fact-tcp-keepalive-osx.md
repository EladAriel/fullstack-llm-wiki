---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-tcp-keepalive-osx.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

- To view the keepalive setting on macOS, issue the following command:
```bash
  sysctl net.inet.tcp.keepidle

The value is measured in milliseconds.

|
```

- To change the `net.inet.tcp.keepidle` value, you can use the
following command, supplying a <value> in milliseconds:

```bash
  sudo sysctl net.inet.tcp.keepidle=<value>

This operation does not persist across system reboots, and must be
set each time your system reboots. See your operating system's
documentation for instructions on setting this value persistently.
Keepalive values greater than or equal to ``600000`` milliseconds
(10 minutes) will be ignored by :binary:`~bin.mongod` and
:binary:`~bin.mongos`.

.. note::

  In macOS 10.15 Catalina, Apple no longer allows for configuration
  of the ``net.inet.tcp.keepidle`` option.
```
