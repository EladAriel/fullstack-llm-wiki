---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/sample-data/sample-guides.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=====================

# Sample Guides Dataset

The `sample_guides` database contains data used in :guides:`our guided tutorials <>`.

.. include:: /includes/search-shared/fact-how-to-load-sample-data.rst

## Collections

This database contains a single collection called `planets`.

The `sample_guides.planets` collection contains documents that represent a planet in our Solar System.

Each document includes the following information about the planet:

- Its order from the sun
- Whether it has rings
- The composition of its atmosphere
- Its surface temperature
### Indexes

The `sample_guides.planets` collection contains the following indexes:

### Sample Document

```json
{
  _id: new ObjectId("6220f6b78a733c51b416c80e"),
  name: 'Uranus',
  orderFromSun: 7,
  hasRings: true,
  mainAtmosphere: [ 'H2', 'He', 'CH4' ],
  surfaceTemperatureC: { min: null, max: null, mean: -197.2 }
}
```
