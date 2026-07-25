---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-trim-chars-length-limit.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in MongoDB 8.3, the length of the string you provide to `chars` is limited to 4096 characters. If you provide a string longer than 4096 characters, MongoDB returns an error similar to the following:

```none
$trim/$ltrim/$rtrim requires 'chars' to be not greater than 4096 bytes, got 
<length> bytes instead.
```
