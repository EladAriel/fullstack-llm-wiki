---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-use-aggregation-not-map-reduce.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
