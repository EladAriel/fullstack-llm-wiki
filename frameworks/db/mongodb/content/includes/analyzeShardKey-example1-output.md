---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/analyzeShardKey-example1-output.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
