---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/cqa-output.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

|CQA| returns a document containing fields that describe the old configuration, if one exists, and fields describing the new configuration.

- `oldConfiguration`, if it exists, contains fields
describing the old configuration.

- `newConfiguration` contains fields describing the new
configuration.

|CQA| returns a document similar to the following:

```none
{
   ok: 1,
   oldConfiguration: {
     mode: ...,
     samplesPerSecond: ...
   }
   newConfiguration: {
     ...
   }
}
```
