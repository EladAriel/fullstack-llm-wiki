---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-tags-field.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

A `tags` document contains user-defined tag field and value pairs for the replica set member.

```javascript
{ "<tag1>": "<string1>", "<tag2>": "<string2>",... }
```

- For read operations, you can specify a tag set in the :ref:`read
preference <replica-set-read-preference-tag-sets>` to direct the operations to replica set member(s) with the specified tag(s).

- For write operations, you can create a customize :doc:`write concern
</reference/write-concern>` using :rsconf:`settings.getLastErrorModes` and :rsconf:`settings.getLastErrorDefaults`.

For more information, see `replica-set-configuration-tag-sets`.
