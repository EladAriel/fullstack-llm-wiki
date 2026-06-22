---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/in-use-encryption/cmk-csfle-bash.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

> **Tip:** Use the following command to generate a {+cmk-abbr+}
from a Unix shell or PowerShell:
- Unix/macOS shell:
  .. code-block:: sh
     echo $(head -c 96 /dev/urandom | tr -d '\n')
- PowerShell:
  .. code-block:: none
     $r=[byte[]]::new(96);$g=[System.Security.Cryptography.RandomNumberGenerator]::Create();$g.GetBytes($r);$r
Save the output of the preceding command to a file named `master-key.txt`.
