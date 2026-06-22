---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/time-series/timeseries-operators-java.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Each of the following examples uses a `dowJonesTickerData` collection that contains documents with the following structure:

Calculate Average Price per Month `````````````````````````````````

This example aggregation pipeline performs the following actions:

- Uses :expression:`$dateTrunc` to truncate each document's `date` to the
appropriate month.

- Uses :pipeline:`$group` to group the documents by month and symbol.
- Uses :group:`$avg` to calculate the average price per month.
The pipeline returns a set of documents where each document contains the average closing price per month for a particular stock.

Calculate a Rolling Average Over 30 Days ````````````````````````````````````````

The next example aggregation pipeline performs the following operations:

- Uses :pipeline:`$setWindowFields` to specify a window of 30 days.
- Calculates a rolling average of the closing price over the last 30
days for each stock.

The pipeline returns a set of documents where each document includes a `$averageMonthClosingPrice` field that contains the average of the previous month's closing price for that stock symbol.
