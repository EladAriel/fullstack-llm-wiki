---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/introduction-write-concern.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

`Write Concern <write-concern>` describes the level of acknowledgment requested from MongoDB for write operations. The level of the write concerns affects how quickly the write operation returns. When write operations have a weak write concern, they return quickly. With stronger write concerns, clients must wait after sending a write operation until MongoDB confirms the write operation at the requested write concern level. With insufficient write concerns, write operations may appear to a client to have succeeded, but may not persist in some cases of server failure.
