---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-installation-bind-ip-default-in-config.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

By default, MongoDB launches with :setting:`~net.bindIp` set to `127.0.0.1`, which binds to the localhost network interface. This means that the |executable-name| can only accept connections from clients that are running on the same machine. Remote clients will not be able to connect to the |executable-name|, and the |executable-name| will not be able to initialize a `replica set` unless this value is set to a valid network interface.

This value can be configured either:

- in the MongoDB configuration file with :setting:`~net.bindIp`, or
- via the command-line argument :option:`--bind_ip <mongod --bind_ip>`
.. include:: /includes/warning-bind-ip-security-considerations.rst

For more information on configuring :setting:`~net.bindIp`, see `/core/security-mongodb-configuration`.
