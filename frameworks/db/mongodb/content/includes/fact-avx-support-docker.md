---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-avx-support-docker.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

- MongoDB 5.0+ Docker images require `AVX
<https://en.wikipedia.org/wiki/Advanced_Vector_Extensions>`__ support on your system. If your system does not support AVX, you can use a docker image of MongoDB prior to version 5.0.

> **Warning:**   Versions of MongoDB prior to {+minimum-lts-version+} are EOL'd and
  no longer supported by MongoDB. These versions should be used for
  testing purposes only.
