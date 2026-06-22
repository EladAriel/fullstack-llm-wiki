---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/let-variables-syntax.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Specifies a document with a list of variables. This allows you to improve command readability by separating the variables from the query text.

The document syntax is:

```javascript
{ 
  <variable_name_1>: <expression_1>,
  ...,
  <variable_name_n>: <expression_n>
}
```

The variable is set to the value returned by the expression, and cannot be changed afterwards.

To access the value of a variable in the command, use the double dollar sign prefix (`$$`) together with your variable name in the form `$$<variable_name>`. For example: `$$targetTotal`.
