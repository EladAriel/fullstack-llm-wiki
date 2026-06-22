---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-tcp-retries-windows.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

On Windows, control TCP Retransmission by adjusting the `TcpMaxDataRetransmissions` parameter.

- To view the `TcpMaxDataRetransmissions` setting on Windows, issue the
following command:

```powershell
  reg query HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters /v TcpMaxDataRetransmissions

By default, the parameter is not set. The system default,
used if the value is absent, is ``5`` retries.
```

- To change the `TcpMaxDataRetransmissions` value, use the following command
in an Administrator :guilabel:`Command Prompt`, where `<value>` is an integer:

```powershell
  reg add HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\ /t REG_DWORD /v TcpMaxDataRetransmission /d <value>
```
