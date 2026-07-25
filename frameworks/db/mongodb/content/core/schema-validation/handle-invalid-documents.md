---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/schema-validation/handle-invalid-documents.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
