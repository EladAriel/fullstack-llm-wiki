---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/intro-aggregation-operator-expressions.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Expression operators are similar to functions that take arguments. In general, these operators take an array of arguments and have the following form:

```javascript
{ <operator>: [ <argument1>, <argument2> ... ] }
```

If an operator accepts a single argument, you can omit the outer array designating the argument list:

```javascript
{ <operator>: <argument> }
```

To avoid parsing ambiguity if the argument is a literal array, you must wrap the literal array in a :expression:`$literal` expression or keep the outer array that designates the argument list.
