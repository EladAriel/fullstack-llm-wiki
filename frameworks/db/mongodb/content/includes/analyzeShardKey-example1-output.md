---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/analyzeShardKey-example1-output.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

```none
{
   "keyCharacteristics": {
     "numDocsTotal" : 9039,
     "avgDocSizeBytes" : 153,
     "numDocsSampled" : 9039,
     "isUnique" : false,
     "numDistinctValues" : 30,
     "mostCommonValues" : [
         {
           "value" : {
               "lastName" : "Smith"
           },
           "frequency" : 1013
         },
         {
           "value" : {
               "lastName" : "Johnson"
           },
           "frequency" : 984
         },
         {
           "value" : {
               "lastName" : "Jones"
           },
           "frequency" : 962
         },
         {
           "value" : {
               "lastName" : "Brown"
           },
           "frequency" : 925
         },
         {
           "value" : {
               "lastName" : "Davies"
           },
           "frequency" : 852
         }
     ],
     "monotonicity" : {
       "recordIdCorrelationCoefficient" : 0.0771959161,
       "type" : "not monotonic"
   },
 }
}
```
