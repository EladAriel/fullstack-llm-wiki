---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-tcp-retries-linux.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

On most Linux operating systems, control the TCP retransmission by adjusting the `net.ipv4.tcp_retries2` sysctl setting.

> **Note:** Although the setting name includes `ipv4`, the `tcp_retries2` setting
applies to both IPv4 and IPv6.

- To view the current setting, use the `sysctl` command:
- To change the `tcp_retries2` setting at runtime, use the `sysctl` command:
```bash
  sysctl -w net.ipv4.tcp_retries2=8
```

- To make the change permanent, edit the configuration file:
#. Open `/etc/sysctl.conf` in your preferred text editor:

```bash
     vi /etc/sysctl.conf

#. Configure the ``net.ipv4.tcp_retries2`` setting:

  .. code-block:: conf

     net.ipv4.tcp_retries2 = 8

#. Restart the system. 

Your system now uses the new ``tcp_retries2`` setting.
```
