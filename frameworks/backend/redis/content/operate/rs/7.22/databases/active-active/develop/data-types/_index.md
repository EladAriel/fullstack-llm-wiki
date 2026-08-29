---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.22/databases/active-active/develop/data-types/_index.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.349985Z"
---
# _Index

---
Title: Data types for Active-Active databases
alwaysopen: false
categories:
- docs
- operate
- rs
- rc
description: Introduction to differences in data types between standalone and Active-Active
  Redis databases.
hideListLinks: false
linktitle: Data types
weight: 90
url: '/operate/rs/7.22/databases/active-active/develop/data-types/'
---


Active-Active databases use conflict-free replicated data types (CRDTs). From a developer perspective, most supported data types work the same for Active-Active and standard Redis databases. However, a few methods also come with specific requirements in Active-Active databases.

Even though they look identical to standard Redis data types, there are specific rules that govern the handling of
conflicting concurrent writes for each data type.

As conflict handling rules differ between data types, some commands have slightly different requirements in Active-Active databases versus standard Redis databases.

See the following articles for more information.

