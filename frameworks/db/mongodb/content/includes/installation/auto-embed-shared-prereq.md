---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/installation/auto-embed-shared-prereq.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Create endpoint service |api| keys if you want  {+avs+} to automatically generate embeddings for text data in your collection. To learn more, see `Automated Embedding <avs-auto-embeddings>`.

> **Important:** Automated Embedding is in Preview. The feature and corresponding documentation
might change at any time during the Preview period. To learn more, see `Preview
Features <https://www.mongodb.com/docs/preview-features/>`__.

We recommend that you create two keys, one for generating embeddings at index-time and another for generating embeddings at query-time, from two |service| projects. You can create the endpoint service |api| keys from the :dochub:`{+atlas-ui+} </voyage-api-keys>` if you don't already have the keys.

> **Note:** Your provider endpoint for generating embeddings depends on
whether you create the |api| keys from the {+atlas-ui+} or
directly from |voyage|.
