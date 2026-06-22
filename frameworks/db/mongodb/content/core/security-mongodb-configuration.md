---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/security-mongodb-configuration.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================================

# IP Binding in Self-Managed Deployments

## Overview

MongoDB binaries, :binary:`mongod` and :binary:`mongos`, bind to localhost by default. If the :setting:`net.ipv6` configuration file setting or the `--ipv6` command line option is set for the binary, the binary additionally binds to the localhost IPv6 address.

## Considerations

> **Warning:** Make sure that your :binary:`~bin.mongod` and :binary:`~bin.mongos`
instances are only accessible on trusted networks. If your system
has more than one network interface, bind MongoDB programs to the
private or internal network interface.

If the :setting:`net.ipv6` configuration file setting or the `--ipv6` command line option is set for the binary, the binary additionally binds to the localhost IPv6 address.

.. include:: /includes/fact-bind-to-all-ips.rst

> **Seealso:** - `security-firewalls`
- `configuration-security`
