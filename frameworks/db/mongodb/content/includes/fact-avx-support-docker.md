---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-avx-support-docker.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

- MongoDB 5.0+ Docker images require `AVX
<https://en.wikipedia.org/wiki/Advanced_Vector_Extensions>`__ support on your system. If your system does not support AVX, you can use a docker image of MongoDB prior to version 5.0.

> **Warning:**   Versions of MongoDB prior to {+minimum-lts-version+} are EOL'd and
  no longer supported by MongoDB. These versions should be used for
  testing purposes only.
