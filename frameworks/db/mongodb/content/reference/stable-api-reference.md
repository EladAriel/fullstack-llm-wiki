---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/stable-api-reference.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================

# Migrate to a Later API Version

## Compatibility with Future Versions

The only API version that currently exists is `"1"`, but there will be new API versions released in the future. Upgrading your API version provides improved functionality and semantics for your application.

Some API V1 commands and behaviors will be deprecated in future versions of the MongoDB server. Deprecated commands and behaviors are typically not included in the next API version.

### Find Deprecated Commands and Behaviors

To migrate an existing application from API V1 to API V2, you must find and update all of the deprecated commands and behaviors features it uses.

```none
client = MongoClient(
  <connection string>,
  api={"version": "1", "strict": True, "deprecationErrors": True}
)
```

The returns a `APIDeprecationError <api-deprecation-resp>` if your application code tries to use commands and behaviors deprecated in API V1. Once your application tests pass and all deprecation errors have been fixed, you will be ready to test your application with API V2.
