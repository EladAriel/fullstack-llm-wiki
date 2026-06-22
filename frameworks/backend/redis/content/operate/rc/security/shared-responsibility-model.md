---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rc/security/shared-responsibility-model.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Redis Cloud shared responsibility model
alwaysopen: false
categories:
- docs
- operate
- rc
description: null
linkTitle: Shared responsibility model
weight: 10
---

The security of all Redis Cloud deployments is a shared responsibility. Redis, the public cloud providers (Amazon Web Services [AWS], Google Cloud, and Microsoft Azure), and our customers all help ensure the security of these deployments.

## Redis responsibility

Redis Cloud's offerings are managed by Redis and deployed on AWS, Azure, and Google Cloud infrastructure.

Redis is responsible for the software that runs Redis Cloud. This includes the patching and maintenance of
the operating systems that Redis is deployed on as well as the patching and maintenance of Redis Cloud.

## Cloud provider responsibility

The public cloud provider hosting your Redis Cloud databases is responsible for the physical security of their data centers and
the security of the network, storage, servers, and virtualization that form the core infrastructure of your deployment.

Amazon, Microsoft, and Google public clouds embrace a wide range of security best practices and compliance standards. Compliance information—including audits, attestations, and certifications about resources hosted—can be found on these compliance pages:

* [AWS Compliance](https://aws.amazon.com/compliance/)
* [Google Cloud Compliance](https://cloud.google.com/security/compliance)
* [Azure Compliance](https://azure.microsoft.com/en-us/overview/trusted-cloud/compliance/)

## Customer responsibility

Customers are responsible for the security configurations in their Redis databases and the Redis Cloud console. Customers must understand and implement the Redis Cloud security features and best practices.

Customers are also responsible for the applications built on Redis and the data they store in Redis. Customers determine the cloud provider, region, and availability zone of their deployments.

Customers understand that Redis Cloud Essentials plans are deployed to a multi-tenant infrastructure. Redis Cloud Pro plans are deployed to a single-tenant infrastructure dedicated to one specific customer.

## Continue learning with Redis University

{{< university-links >}}

