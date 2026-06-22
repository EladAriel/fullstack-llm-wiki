---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-float-parse-behavior-8.3.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Starting in MongoDB 8.3, the server is able to parse the full range of all representable double precision floating point numbers. This includes subnormal numbers where the most significant digit has leading zeroes and the exponent has the least possible value. For details, see [Subnormal Number](https://en.wikipedia.org/wiki/Subnormal_number).

In earlier versions of MongoDB, the server returns an error when you try to parse these numbers. The following example raises an error in versions earlier than MongoDB 8.3:

```javascript
db.t.insertOne( { v: "7.08263e-317" } )

db.t.aggregate([
  {
    $project: {
      converted: {
        $convert: { input: "$v", to: "double" },
      }
    }
   }
])
```

This example fails with an error similar to the following:

```none
MongoServerError[ConversionFailure]: Executor error during aggregate command on namespace: test.t :: 
caused by :: Failed to parse number '7.08263e-317' in $convert with no onError value: Out of range
```
