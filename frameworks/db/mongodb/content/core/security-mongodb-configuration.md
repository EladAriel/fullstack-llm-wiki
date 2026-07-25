---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/security-mongodb-configuration.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
