---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/queryStats/toggle-logging.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============================

# Toggle $queryStats Log Output

.. include:: /includes/aggregation/queryStats/logging-intro.rst

Including `$queryStats` output in the logs provides more information on specific `$queryStats` operations, but can negatively impact cluster performance as log updates take more time and resources.

## About this Task

When MongoDB logs `$queryStats` output, the results are redacted and anonymized. `$queryStats` output does not contain literals or field values.

For an example of transformed `$queryStats` output, see `queryStats-example-transformed`.

## Steps

## Examples

The following examples show the differences in log messages when `$queryStats` output is included.

> **Note:** The example log entries are reformatted for readability.

### `$queryStats` Output Omitted (Default Behavior)

```javascript
{
  "t":{"$date":"2023-11-27T20:58:59.212+00:00"},"s":"D1", "c":"QRYSTATS",
  "id":7808300, "ctx":"conn31","msg":"Logging invocation
  $queryStats","attr":{"commandSpec":{"transformIdentifiers":{"algorithm":"hmac-sha-256","hmacKey":"###"}}
}
```

### `$queryStats` Output Included

```javascript
{
  "t":{"$date":"2023-11-27T20:58:59.212+00:00"},"s":"D1", "c":"QRYSTATS",
  "id":7808300, "ctx":"conn31","msg":"Logging invocation
  $queryStats","attr":{"commandSpec":{"transformIdentifiers":{"algorithm":"hmac-sha-256","hmacKey":"###"}}
}

{
  "t":{"$date":"2023-11-27T20:58:59.212+00:00"},"s":"D3", "c":"QRYSTATS",
  "id":7808301, "ctx":"conn31","msg":"Logging all outputs of
  $queryStats","attr":{"thisOutput":"{key: {queryShape: {cmdNs: {db:
  \"hYt+nW/sr1/Zc3YR8nlGWFoesJdvywkw+cR9rMGzXU4=\", coll:
  \"TRx6R3rvstYgX96gNmeOi5E3QVsOqzRbv7A9j3q7OvM=\"}, command: \"find\",
  filter: {Wb/Uu22DzKZ/Os+ZvLgPKFKGZPV4cIMZ3Ybv1HfYih4=: {$lt:
  \"?date\"}}, projection: {r5zQZllsGoqQuQp4Jm0eH2M6RrMqH84KHowcFaiverg=:
  true}, sort: {r5zQZllsGoqQuQp4Jm0eH2M6RrMqH84KHowcFaiverg=: 1}},
  readConcern: {}, collectionType: \"nonExistent\"}, metrics:
  {lastExecutionMicros: 208, execCount: 21, totalExecMicros: {sum: 6079,
  max: 1875, min: 198, sumOfSquares: 4401645}, firstResponseExecMicros:
  {sum: 6079, max: 1875, min: 198, sumOfSquares: 4401645}, docsReturned:
  {sum: 0, max: 0, min: 0, sumOfSquares: 0}, firstSeenTimestamp:
  2023-11-27T19:15:51.317Z, latestSeenTimestamp:
  2023-11-27T20:55:51.309Z}, asOf: 2023-11-27T20:58:59.212Z}"}
}

{
  "t":{"$date":"2023-11-27T20:58:59.213+00:00"},"s":"D3", "c":"QRYSTATS",
  "id":7808301, "ctx":"conn31","msg":"Logging all outputs of
  $queryStats","attr":{"thisOutput":"{key: {queryShape: {cmdNs: {db:
  \"j+Caz+gxt7vl++gmeCAWrvyhDL17WaNrSIDi6Au7VI0=\", coll:
  \"f/LCkK/kVEbt4fk2NNbyDPhxas+kzCLLcVbjeNBbhyg=\"}, let:
  {pUZAyEEImSXcu8deG05tfIf6F/H92YsFnkZXIeRQtgc=: \"?number\"}, command:
  \"aggregate\", pipeline: [{$group: {_id: \"?number\",
  5E6FSc5VxCvIZK0jrqkY3k3aX51jSc73hQwO/8kH0lo=: {$sum: \"?number\"}}}],
  explain: true, allowDiskUse: false}, client: {driver: {name:
  \"nodejs|mongosh\", version: \"5.1.0\"}, os: {type: \"Darwin\", name:
  \"darwin\", architecture: \"arm64\", version: \"22.6.0\"}, platform:
  \"Node.js v16.19.1, LE (unified)\", version: \"5.1.0|1.8.0\",
  application: {name: \"mongosh 1.8.0\"}}, collectionType: \"collection\",
  cursor: {batchSize: \"?number\"}}, metrics: {lastExecutionMicros: 0,
  execCount: 1, totalExecMicros: {sum: 0, max: 0, min: 0, sumOfSquares:
  0}, firstResponseExecMicros: {sum: 0, max: 0, min: 0, sumOfSquares: 0},
  docsReturned: {sum: 0, max: 0, min: 0, sumOfSquares: 0},
  firstSeenTimestamp: 2023-11-27T19:31:36.463Z, latestSeenTimestamp:
  2023-11-27T19:31:36.463Z}, asOf: 2023-11-27T20:58:59.213Z}"}
}

// Additional $queryStats output...
```

## Learn More

- `auditing`
- `audit-message`
- :atlas:`Configure a Custom Auditing Filter </database-auditing/#std-label-auditing-custom-filter>`
