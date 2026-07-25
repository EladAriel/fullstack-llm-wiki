---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-tcp-retries-windows.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
