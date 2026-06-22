---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-trim-chars-length-limit.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Starting in MongoDB 8.3, the length of the string you provide to `chars` is limited to 4096 characters. If you provide a string longer than 4096 characters, MongoDB returns an error similar to the following:

```none
$trim/$ltrim/$rtrim requires 'chars' to be not greater than 4096 bytes, got 
<length> bytes instead.
```
