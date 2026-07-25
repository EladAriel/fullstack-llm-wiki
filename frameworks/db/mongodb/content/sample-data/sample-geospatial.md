---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/sample-data/sample-geospatial.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=========================

# Sample Geospatial Dataset

The `sample_geospatial` database contains data specifically designed to help familiarize you with :manual:`GeoJSON </reference/geojson/>` data.

.. include:: /includes/search-shared/fact-how-to-load-sample-data.rst

## Collections

This database contains a single collection called `shipwrecks`.

The `sample_geospatial.shipwrecks` collection contains all of the shipwreck data in the dataset. Each document in the collection represents a shipwreck and contains details such as where the wreck took place and the type of wreck that occurred.

### Indexes

The `data` collection contains the following indexes:

### Sample Document

```json
{
  "_id": {
    "$oid": "578f6fa2df35c7fbdbaed8c6"
  },
  "recrd": "",
  "vesslterms": "",
  "feature_type": "Wrecks - Submerged, dangerous",
  "chart": "US,U1,graph,DNC H1409860",
  "latdec": {
    "$numberDouble": "9.3560572"
  },
  "londec": {
    "$numberDouble": "-79.9074173"
  },
  "gp_quality": "",
  "depth": "",
  "sounding_type": "",
  "history": "",
  "quasou": "depth unknown",
  "watlev": "always under water/submerged",
  "coordinates": [
    {
      "$numberDouble": "-79.9074173"
    },
    {
      "$numberDouble": "9.3560572"
    }
  ]
}
```
