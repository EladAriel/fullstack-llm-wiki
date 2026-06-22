---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/analyzeShardKey-example2-output.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

```none
{
  "keyCharacteristics": {
    "numDocsTotal" : 9039,
    "avgDocSizeBytes" : 162,
    "numDocsSampled" : 9039,
    "isUnique" : false,
    "numDistinctValues" : 1495,
    "mostCommonValues" : [
      {
        "value" : {
          "userId" : UUID("aadc3943-9402-4072-aae6-ad551359c596")
        },
        "frequency" : 15
      },
     {
       "value" : {
         "userId" : UUID("681abd2b-7a27-490c-b712-e544346f8d07")
       },
       "frequency" : 14
     },
     {
       "value" : {
         "userId" : UUID("714cb722-aa27-420a-8d63-0d5db962390d")
       },
       "frequency" : 14
     },
     {
       "value" : {
         "userId" : UUID("019a4118-b0d3-41d5-9c0a-764338b7e9d1")
       },
       "frequency" : 14
     },
     {
       "value" : {
         "userId" : UUID("b9c9fbea-3c12-41aa-bc69-eb316047a790")
       },
       "frequency" : 14
     }
   ],
   "monotonicity" : {
     "recordIdCorrelationCoefficient" : -0.0032039729,
     "type" : "not monotonic"
   },
 }
}
```
