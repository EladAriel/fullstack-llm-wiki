---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/minMaxScaler.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=====================================================

# $minMaxScaler (Window Function) (expression operator)

## Definition

.. versionadded:: 8.2

Normalizes a numeric expression within a window of values. By default, values can range between zero and one. The smallest value becomes zero, the largest value becomes one, and all other values scale proportionally in between zero and one. You can also specify a custom minimum and maximum value for the normalized output range.

:group:`$minMaxScaler` is only available in the :pipeline:`$setWindowFields` stage.

:group:`$minMaxScaler` window operator has the following syntax:

```none
{ $minMaxScaler: <numeric expression> }
```

The value can be:

- A numeric expression, which is the value that you want to normalize. It
can be a specific numeric field or value calculated from your documents.

- A document in the following format:
```none
  { 
    input: <numeric expression>,
    min: <constant numeric expression>,
    max: <constant numeric expression>
  }

.. list-table:: 
  :header-rows: 1

  * - Field 
    - Description 

  * - ``input``
    - Numeric expression, which contains the value that you want to normalize.

  * - ``min``
    - Minimum value that you want in the output. If omitted, defaults to ``0``.

  * - ``max``
    - Maximum value that you want in the output. If omitted, defaults to ``1``.
```

## Behavior

:group:`$minMaxScaler` uses the following formula to normalize the numeric expression:

```shell
minMaxScaler(x, min, max) = ((x - min(X)) / (max(X) - min(X))) * (max - min) + min 
```

Where:

The :group:`$minMaxScaler` returns an error if the `input` value is any of the following:

- Non-numeric
- Null
- Empty arrays
- Strings
## Examples

Suppose your documents in your collection have a field named `a` with the following values:

```json
{ "_id": 1, "a": 1 } 
{ "_id": 2, "a": 5 }
{ "_id": 3, "a": 13 } 
{ "_id": 4, "a": 21 } 
```

Consider the following pipeline stage and the output:

In the preceding example, the pipeline uses the :group:`$minMaxScaler` to calculate two scaled values:

- `scaled`, which applies the default values, `0` and `1`, to scale.
- `scaledTo100`, which applies a range between `0` and `100` to scale.
The output shows the original value of `a` and the two scaled values. The :group:`$minMaxScaler` uses the following for the documents, where `min(X)` is `1` and `max(X)` is `21` (calculated from the documents), to return the scaled values:

```javascript
scaled = ((1 - 1) / (21 - 1)) * (1 - 0) + 0 = 0
scaledTo100 = ((1 - 1) / (21 - 1)) * (100 - 0) + 0 = 0
```

```javascript
scaled = ((5 - 1) / (21 - 1)) * (1 - 0) + 0 = (4 / 20) * 1 + 0 = 0.2
scaledTo100 = ((5 - 1) / (21 - 1)) * (100 - 0) + 0 = (4 / 20) * 100 + 0 = 20
```

```javascript
scaled = ((13 - 1) / (21 - 1)) * (1 - 0) + 0 = (12 / 20) * 1 + 0 = 0.6
scaledTo100 = ((13 - 1) / (21 - 1)) * (100 - 0) + 0 = (12 / 20) * 100 + 0 = 60
```

```javascript
scaled = ((21 - 1) / (21 - 1)) * (1 - 0) + 0 = (20 / 20) * 1 + 0 = 1
scaledTo100 = ((21 - 1) / (21 - 1)) * (100 - 0) + 0 = (20 / 20) * 100 + 0 = 100
```
