---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/installation/auto-embed-shared-prereq.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Create endpoint service |api| keys if you want  {+avs+} to automatically generate embeddings for text data in your collection. To learn more, see `Automated Embedding <avs-auto-embeddings>`.

> **Important:** Automated Embedding is in Preview. The feature and corresponding documentation
might change at any time during the Preview period. To learn more, see `Preview
Features <https://www.mongodb.com/docs/preview-features/>`__.

We recommend that you create two keys, one for generating embeddings at index-time and another for generating embeddings at query-time, from two |service| projects. You can create the endpoint service |api| keys from the :dochub:`{+atlas-ui+} </voyage-api-keys>` if you don't already have the keys.

> **Note:** Your provider endpoint for generating embeddings depends on
whether you create the |api| keys from the {+atlas-ui+} or
directly from |voyage|.
