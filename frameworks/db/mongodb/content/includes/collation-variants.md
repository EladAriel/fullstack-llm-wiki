---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/collation-variants.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Some collation locales have variants, which use special language-specific rules. To specify a locale variant, use the following syntax:

```javascript
{ "locale" : "<locale code>@collation=<variant>" }
```

For example, to use the `unihan` variant of the Chinese collation:

```javascript
{ "locale" : "zh@collation=unihan" }
```
