---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-default-bind-ip.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

.. include:: /includes/warning-bind-ip-security-considerations.rst

MongoDB binaries, :binary:`~bin.mongod` and :binary:`~bin.mongos`, bind to localhost by default. If the :setting:`net.ipv6` configuration file setting or the `--ipv6` command line option is set for the binary, the binary additionally binds to the localhost IPv6 address.

By default :binary:`~bin.mongod` and :binary:`~bin.mongos` that are bound to localhost only accept connections from clients that are running on the same computer. This binding behavior includes :binary:`~bin.mongosh` and other members of your replica set or sharded cluster. Remote clients cannot connect to binaries that are bound only to localhost.

To override the default binding and bind to other IP addresses, use the :setting:`net.bindIp` configuration file setting or the `--bind_ip` command-line option to specify a list of hostnames or IP addresses.

.. include:: /includes/warning-no-ip-addresses-in-split-horizons.rst

For example, the following :binary:`~bin.mongod` instance binds to both the localhost and the hostname `My-Example-Associated-Hostname`, which is associated with the IP address `198.51.100.1`:

```none
mongod --bind_ip localhost,My-Example-Associated-Hostname
```

In order to connect to this instance, remote clients must specify the hostname  or its associated IP address `198.51.100.1`:

```none
mongosh --host My-Example-Associated-Hostname

mongosh --host 198.51.100.1
```
