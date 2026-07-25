---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/list-index-field-limit-behaviors.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

When the index key size limit applies:

- .. include:: /includes/fact-index-key-length-operation-behaviors.rst
:start-after: index-field-limit-ensureIndex :end-before: index-field-limit-reIndex

- .. include:: /includes/fact-index-key-length-operation-behaviors.rst
:start-after: index-field-limit-reIndex :end-before: index-field-limit-insert

- .. include:: /includes/fact-index-key-length-operation-behaviors.rst
:start-after: index-field-limit-insert :end-before: index-field-limit-update

- .. include:: /includes/fact-index-key-length-operation-behaviors.rst
:start-after: index-field-limit-update :end-before: index-field-limit-restore-import

- .. include:: /includes/fact-index-key-length-operation-behaviors.rst
:start-after: index-field-limit-restore-import :end-before: index-field-limit-rs-secondary

- .. include:: /includes/fact-index-key-length-operation-behaviors.rst
:start-after: index-field-limit-rs-secondary :end-before: index-field-limit-chunk-migration

- .. include:: /includes/fact-index-key-length-operation-behaviors.rst
:start-after: index-field-limit-chunk-migration
