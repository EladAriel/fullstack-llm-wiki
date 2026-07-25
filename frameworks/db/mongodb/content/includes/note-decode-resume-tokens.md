---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/note-decode-resume-tokens.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

MongoDB provides a `"snippet" <snip-overview>`, an extension to :binary:`~bin.mongosh`, that decodes hex-encoded resume tokens.

You can install and run the [resumetoken](https://github.com/mongodb-labs/mongosh-snippets/tree/main/snippets/resumetoken)_ snippet from :binary:`~bin.mongosh`:

```javascript
snippet install resumetoken
decodeResumeToken('<RESUME TOKEN>')
```

You can also run [resumetoken](https://github.com/mongodb-labs/mongosh-snippets/tree/main/snippets/resumetoken)_ from the command line (without using :binary:`~bin.mongosh`) if `npm` is installed on your system:

```javascript
npx mongodb-resumetoken-decoder <RESUME TOKEN>
```

See the following for more details on:

- `resumetoken
<https://github.com/mongodb-labs/mongosh-snippets/tree/main/snippets/resumetoken>`__

- `using snippets <snip-using-snippets>` in :binary:`~bin.mongosh`.
