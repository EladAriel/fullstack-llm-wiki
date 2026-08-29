---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rc/cloud-integrations/_index.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.285036Z"
---
# _Index

---
LinkTitle: Marketplace integrations
Title: Manage marketplace integrations
alwaysopen: false
categories:
- docs
- operate
- rc
description: Describes how to integrate Redis Cloud subscriptions into existing cloud
  provider services, whether existing subscriptions or through vendor marketplaces.
hideListLinks: true
weight: 48
---

By default, Redis Cloud subscriptions are hosted in cloud vendor accounts owned and managed by Redis.

To integrate Redis Cloud into an existing cloud vendor account, you can:

- Subscribe to Redis Cloud through [AWS Marketplace]({{< relref "/operate/rc/cloud-integrations/aws-marketplace/" >}}).

- Subscribe to Redis Cloud through [Google Cloud Marketplace]({{< relref "/operate/rc/cloud-integrations/gcp-marketplace/" >}}).

When you subscribe to Redis Cloud through a cloud vendor marketplace, billing is handled through the marketplace.

Redis also offers monthly and annual commitments through cloud vendor marketplaces. [Contact sales](https://redis.io/meeting/) if you're interested in a monthly or annual offer.

## Marketplace billing considerations

Cloud vendor marketplaces provide a convenient way to handle multiple subscription fees.  However, this also means that billing issues impact multiple subscriptions, including Redis Cloud.

When billing details change, you should verify that each service is operating normally and reflects the updated billing details.  Otherwise, you might experience unexpected consequences, such as data loss or subscription removal.

For best results, we recommend:

- [Backing up all data]({{< relref "/operate/rc/databases/back-up-data" >}}) _before_ updating billing details.

- Contacting [support](https://redis.io/support/) or your account team for assistance.