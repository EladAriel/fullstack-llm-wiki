---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/time-series/migrate-timeseries-sample-collection.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

```javascript
db.weatherdata.insertOne(
   {
      _id: ObjectId("5553a998e4b02cf7151190b8"),
      st: "x+47600-047900",
      ts: ISODate("1984-03-05T13:00:00Z"),
      position: {
         type: "Point",
         coordinates: [ -47.9, 47.6 ]
      },
      elevation: 9999,
      callLetters: "VCSZ",
      qualityControlProcess: "V020",
      dataSource: "4",
      type: "FM-13",
      airTemperature: { value: -3.1, quality: "1" },
      dewPoint: { value: 999.9, quality : "9" },
      pressure: { value: 1015.3, quality: "1" },
      wind: {
         direction: { angle: 999, quality: "9" },
         type: "9",
         speed: { rate: 999.9, quality: "9" }
      },
      visibility: {
         distance: { value: 999999, quality : "9" },
         variability: { value: "N", quality: "9" }
      },
      skyCondition: {
         ceilingHeight: { value: 99999, quality: "9", determination: "9" },
         cavok: "N"
      },
      sections: [ "AG1" ],
      precipitationEstimatedObservation: { 
         discrepancy: "2",
         estimatedWaterDepth: 999 
      }
   }
)
```
