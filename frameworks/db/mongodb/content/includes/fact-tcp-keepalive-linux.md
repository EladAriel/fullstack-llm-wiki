---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-tcp-keepalive-linux.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

- To view the keepalive setting on Linux, use one of the following
commands:

```bash
  sysctl net.ipv4.tcp_keepalive_time

Or:

.. code-block:: bash

  cat /proc/sys/net/ipv4/tcp_keepalive_time

The value is measured in seconds.

.. note::

  Although the setting name includes ``ipv4``, the
  ``tcp_keepalive_time`` value applies to both IPv4 and IPv6.
```

- To change the `tcp_keepalive_time` value, you can use one of the
following commands, supplying a <value> in seconds:

```bash
  sudo sysctl -w net.ipv4.tcp_keepalive_time=<value>

Or:

.. code-block:: bash

  echo <value> | sudo tee /proc/sys/net/ipv4/tcp_keepalive_time

These operations do not persist across system reboots. To persist
the setting, add the following line to ``/etc/sysctl.conf``,
supplying a *<value>* in seconds, and reboot the machine:

.. code-block:: bash

  net.ipv4.tcp_keepalive_time = <value>

Keepalive values greater than ``300`` seconds,
(5 minutes) will be overridden on :binary:`~bin.mongod` and
:binary:`~bin.mongos` sockets and set to ``300`` seconds.
```
