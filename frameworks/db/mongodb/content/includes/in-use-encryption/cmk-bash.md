---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/in-use-encryption/cmk-bash.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

> **Tip:** Use the following command to generate a {+cmk-abbr+}
from a Unix shell or PowerShell:
- Unix/macOS shell:
  .. code-block:: sh
     echo $(head -c 96 /dev/urandom | tr -d '\n')
- PowerShell:
  .. code-block:: none
     $r=[byte[]]::new(96);$g=[System.Security.Cryptography.RandomNumberGenerator]::Create();$g.GetBytes($r);$r
Save the output of the preceding command to a file named `customer-master-key.txt`.
