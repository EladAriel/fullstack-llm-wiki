---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/timeseries/timeseries-compression.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=======================

# Time Series Compression

This page describes how MongoDB compresses data in time series collections, and how you can optimize compression.

## Default Compression Algorithm

Time series collections use `zstd` compression, which differs from the global default compression algorithm, `snappy`.

## Column Compression

.. include:: /includes/timeseries-compression-overview.rst

These enhancements further reduce size of data on disk when compressed with `zstd`, and also significantly reduce space used in the WiredTiger cache.

The types of compression introduced are:

- Delta Encoding
- Object compression
- Array compression (starting in MongoDB 6.0)
- Run Length encoding (RLE)
### Delta Encoding (Delta Compression)

Delta Encoding takes advantage of the data in your time series collection having time-series characteristics. Instead of storing absolute values, Delta Encoding assumes that the measurements will not change rapidly between each other. This approach reduces the amount of information required by only storing the difference between measurements.

### Delta of Delta Encoding (Delta of Delta Compression)

With data that increases monotonically, Delta of Delta Encoding can further minimize the size of the number stored by calculating a delta of the delta itself.

### Object and Array Compression

Column compression ensures that if you are using objects and arrays in your documents, you receive the same compression benefits had those embedded fields existed at the root level of your document.

## Learn More

To learn how to optimize compression, see `tsc-best-practice-optimize-compression`.
