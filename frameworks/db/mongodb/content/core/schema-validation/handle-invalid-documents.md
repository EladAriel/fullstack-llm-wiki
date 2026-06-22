---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/schema-validation/handle-invalid-documents.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================================

# Choose How to Handle Invalid Documents

You can specify how MongoDB handles documents that violate validation rules. When an operation would result in an invalid document, MongoDB can either:

- Reject any insert or update that violates the validation criteria.
This is the default behavior.

- Allow the operation to proceed, but record the violation in the
MongoDB log.

Rejecting invalid documents ensures that your schema stays consistent. However, in certain scenarios you may want to allow invalid documents, such as a data migration containing documents from before a schema was established.

## Context

Your schema's `validationAction` option determines how MongoDB handles invalid documents:

.. note :

```
.. include:: /includes/fact-error-and-log-validation-action-backwards-incompatible.rst
```

## Option 1: Reject Invalid Documents

The following procedure shows how to create a schema validation that rejects invalid documents.

## Option 2: Allow Invalid Documents, but Record Them in the Log

The following procedure shows how to create a schema validation that allows invalid documents, but records invalid documents in the MongoDB log.

## Learn More

- `log-messages-ref`
- `schema-specify-validation-level`
