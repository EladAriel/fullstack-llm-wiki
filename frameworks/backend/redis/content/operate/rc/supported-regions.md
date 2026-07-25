---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rc/supported-regions.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: Supported Cloud providers and regions
alwaysopen: false
categories:
- docs
- operate
- rc
description: null
linktitle: Supported regions
weight: 90
---

Your choice of cloud provider and region may affect latency between your application and your database, and may affect what connectivity options are available for your database.

Redis Cloud supports databases on the following cloud providers:
- [Amazon Web Services (AWS)](#amazon-web-services)
- [Google Cloud](#google-cloud)
- [Microsoft Azure](#microsoft-azure)

## Amazon Web Services

Redis Cloud supports databases in the following Amazon Web Services (AWS) regions.

Redis Cloud Pro databases on AWS support [VPC Peering]({{< relref "/operate/rc/security/vpc-peering#aws-vpc-peering" >}}), [Transit Gateway]({{< relref "/operate/rc/security/aws-transit-gateway" >}}), and [AWS PrivateLink]({{< relref "/operate/rc/security/aws-privatelink" >}}).

{{< rc-supported-regions provider="aws" >}}

## Google Cloud

Redis Cloud supports databases in the following Google Cloud regions.

Redis Cloud Pro databases on Google Cloud support [VPC Peering]({{< relref "/operate/rc/security/vpc-peering#gcp-vpc-peering" >}}) and [Private Service Connect]({{< relref "/operate/rc/security/private-service-connect" >}}).

{{< rc-supported-regions provider="gcp" >}}

## Microsoft Azure

Redis Cloud Essentials is available on the following Microsoft Azure regions:

{{< rc-supported-regions provider="azure" >}}

{{< note >}}
Redis Cloud Pro is available on Azure through [Azure Managed Redis](https://azure.microsoft.com/en-us/products/managed-redis/). See [Azure Managed Redis pricing](https://azure.microsoft.com/en-us/pricing/details/managed-redis/) to view the list of Azure regions that support Azure Managed Redis.
{{< /note >}}


