---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/degreesToRadians.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=======================================

# $degreesToRadians (expression operator)

## Definition

## Behavior

### `null`, `NaN`, and `+/- Infinity`

If the argument resolves to a value of `null` or refers to a field that is missing, :expression:`$degreesToRadians` returns `null`. If the argument resolves to `NaN`, :expression:`$degreesToRadians` returns `NaN`. If the argument resolves to negative or positive infinity, :expression:`$degreesToRadians` negative or positive infinity respectively.

## Example

The `trigonometry` collection contains a document that contains three angles measured in degrees:

```json
{
  "angle_a" : Decimal128("53.13010235415597870314438744090659"),
  "angle_b" : Decimal128("36.86989764584402129685561255909341"),
  "angle_c" : Decimal128("90")
}
```

The following aggregation operation uses the :expression:`$degreesToRadians` expression to convert each value to its radian equivalent and add them to the input document using the :pipeline:`$addFields` pipeline stage.

```bash
db.trigonometry.aggregate([
  {
    $addFields: {
      "angle_a_rad" : { $degreesToRadians : "$angle_a"},
      "angle_b_rad" : { $degreesToRadians : "$angle_b"},
      "angle_c_rad" : { $degreesToRadians : "$angle_c"}
    }
  }
])
```

The operation returns the following document:

```bash
{
  "_id" : ObjectId("5c50aec71c75c59232b3ede4"),
  "angle_a" : Decimal128("53.13010235415597870314438744090660"),
  "angle_b" : Decimal128("36.86989764584402129685561255909341"),
  "angle_c" : Decimal128("90"),
  "angle_a_rad" : Decimal128("0.9272952180016122324285124629224290"),
  "angle_b_rad" : Decimal128("0.6435011087932843868028092287173227"),
  "angle_c_rad" : Decimal128("1.570796326794896619231321691639752")
}
```

Since `angle_a`, `angle_b`, and `angle_c` are stored as `128-bit decimals <shell-type-decimal>`, the output of :expression:`$degreesToRadians` is a 128-bit decimal.
