---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/example-multiple-fill-methods.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

When you use the :pipeline:`$setWindowFields` stage to fill missing values, you can set values for a different field than the field you fill from. As a result, you can use multiple fill methods in a single :pipeline:`$setWindowFields` stage and output the results in distinct fields.

The following pipeline populates missing `price` fields using |linear-interpolation| and the last-observation-carried-forward method:

```javascript
db.stock.aggregate( [
   {
      $setWindowFields:
         {
            sortBy: { time: 1 },
            output:
               {
                  linearFillPrice: { $linearFill: "$price" },
                  locfPrice: { $locf: "$price" }
               }
         }
   }
] )
```

In the example:

- `sortBy: { time: 1 }` sorts the documents by the `time` field in
ascending order, from earliest to latest.

- `output <setWindowFields-output>` specifies:
- `linearFillPrice` as a target field to be filled.
- `{ $linearFill: "$price" }` is the value for the
`linearFillPrice` field. :group:`$linearFill` fills missing `price` values using |linear-interpolation| based on the surrounding `price` values in the sequence.

- `locfPrice` as a target field to be filled.
- `{ $locf: "$price" }` is the value for the `locfPrice` field.
`locf` stands for last observation carried forward. :group:`$locf` fills missing `price` values with the value from the previous document in the sequence.

Example output:

```javascript
[
  {
    _id: ObjectId("620ad555394d47411658b5ef"),
    time: ISODate("2021-03-08T09:00:00.000Z"),
    price: 500,
    linearFillPrice: 500,
    locfPrice: 500
  },
  {
    _id: ObjectId("620ad555394d47411658b5f0"),
    time: ISODate("2021-03-08T10:00:00.000Z"),
    linearFillPrice: 507.5,
    locfPrice: 500
  },
  {
    _id: ObjectId("620ad555394d47411658b5f1"),
    time: ISODate("2021-03-08T11:00:00.000Z"),
    price: 515,
    linearFillPrice: 515,
    locfPrice: 515
  },
  {
    _id: ObjectId("620ad555394d47411658b5f2"),
    time: ISODate("2021-03-08T12:00:00.000Z"),
    linearFillPrice: 505,
    locfPrice: 515
  },
  {
    _id: ObjectId("620ad555394d47411658b5f3"),
    time: ISODate("2021-03-08T13:00:00.000Z"),
    linearFillPrice: 495,
    locfPrice: 515
  },
  {
    _id: ObjectId("620ad555394d47411658b5f4"),
    time: ISODate("2021-03-08T14:00:00.000Z"),
    price: 485,
    linearFillPrice: 485,
    locfPrice: 485
  }
]
```
