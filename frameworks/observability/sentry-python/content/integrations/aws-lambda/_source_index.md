---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/integrations/aws-lambda/index.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.055824Z"
---
# Index

---
title: AWS Lambda
description: "Learn about using Sentry with AWS Lambda."
---

You can instrument your AWS Lambda functions in several different ways:

- **Without touching your code:**
    This method can be instrumented from the Sentry product by those who have access to the AWS infrastructure and doesn't require that you make any direct updates to the code. See the [AWS Lambda guide](/integrations/cloud-monitoring/aws-lambda/).
- **By adding the Sentry Lambda Layer to your function manually:**
    While this is a quick way to add Sentry to your AWS Lambda function, it gives you limited configuration possibilities with environment vars. See <PlatformLink to="/integrations/aws-lambda/manual-layer/">AWS Lambda Layer</PlatformLink>.
- **By manually adding Sentry to your function code:**
    This method requires that you install the Sentry SDK into your AWS Lambda function packages. While it takes more effort to set up, it gives you full control of your setup and manual instrumentation. See <PlatformLink to="/integrations/aws-lambda/manual-instrumentation/">AWS Lambda manual instrumentation</PlatformLink>.
