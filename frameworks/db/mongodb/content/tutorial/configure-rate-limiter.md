---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/configure-rate-limiter.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================================================

# Configure the Ingress Connection Establishment Rate Limiter

This procedure describes how to configure rate limiting using the :parameter:`ingressConnectionEstablishmentRateLimiterEnabled` parameter in MongoDB. The rate limiter helps protect your deployment from connection storms that can impact system stability and performance.

## Before You Begin

Before you begin this procedure, ensure you meet the following requirements:

- You have administrative privileges on your MongoDB deployment
- You understand your system's connection load patterns and requirements
- You know your driver's :urioption:`connectTimeoutMS` setting
## Procedure

## Monitoring and Troubleshooting

Monitor the following metrics to ensure you properly configure your rate limiter:

- :serverstatus:`queues.ingressSessionEstablishment`
- :serverstatus:`connections.establishmentRateLimit.rejected`
If you observe increasing numbers of rejected connections, consider:

1. Increasing :parameter:`ingressConnectionEstablishmentRatePerSec` if the cluster appears
to have sufficient CPU resources to handle this load. #. Adjusting :parameter:`ingressConnectionEstablishmentMaxQueueDepth` based on the formula. #. Reviewing driver connection pool settings.
