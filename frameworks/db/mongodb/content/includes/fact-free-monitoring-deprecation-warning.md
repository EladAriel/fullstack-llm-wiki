---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-free-monitoring-deprecation-warning.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

> **Warning:** Free monitoring was decommissioned in August 2023.
Beginning in April 2023, you cannot enable free monitoring on MongoDB
Community instances.
The following list shows monitoring options for your deployment:
- **Deploy a MongoDB Atlas dedicated cluster**. :ref:`Migrate your
  data <live-migrate-c2c>` to a :ref:`MongoDB Atlas
  <unified-get-started>` dedicated cluster sized M10 or greater,
  which includes several advanced monitoring and alerting features:
  - `Query Profiler <query-profiler>`
  - `Performance Advisor <performance-advisor>`
  - `Real-Time Performance Panel <real-time-metrics-status-tab>`
- **Deploy a MongoDB Atlas free cluster**. A free Atlas cluster includes
  basic monitoring and alerting capabilities. After you
  :atlas:`create a free cluster
  </tutorial/deploy-free-tier-cluster/>`, use :binary:`mongodump` and
  :binary:`mongorestore` to manually create a backup of your database
  and import your data from your MongoDB Community instance.
- **Use MongoDB Cloud Manager**. The `MongoDB Cloud Manager
  <https://docs.cloudmanager.mongodb.com/>`_ free tier includes basic
  monitoring capabilities.
