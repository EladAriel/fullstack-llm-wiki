---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-use-aggregation-not-map-reduce.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in MongoDB 5.0, `map-reduce <map-reduce>` is deprecated:

- Instead of `map-reduce <map-reduce>`, you should use an
`aggregation pipeline <aggregation-pipeline>`. Aggregation pipelines provide better performance and usability than map-reduce.

- You can rewrite map-reduce operations using :ref:`aggregation pipeline
stages <aggregation-pipeline-operator-reference>`, such as :pipeline:`$group`, :pipeline:`$merge`, and others.

- For map-reduce operations that require custom functionality, you can
use the :group:`$accumulator` and :expression:`$function` aggregation operators. You can use those operators to define custom aggregation expressions in JavaScript.

For examples of aggregation pipeline alternatives to map-reduce, see:

- `map-reduce-to-agg-pipeline`
- `map-reduce-examples`
