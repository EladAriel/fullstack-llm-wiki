---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/integrations/aws-lambda/container-image/index.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.064429Z"
---
# Index

---
title: AWS Lambda Container Image
description: "Learn how to set up Sentry with a Container Image."
sidebar_order: 3000
---

<Alert level="warning" title="Deprecation Notice">

The Python AWS Lambda Container Image is deprecated.

Please instrument your AWS Lambda function in one of the following ways instead:

- **Without touching your code:**
    This method can be instrumented from the Sentry product by those who have access to the AWS infrastructure and doesn't require that you make any direct updates to the code. See the [AWS Lambda guide](/integrations/cloud-monitoring/aws-lambda/).
- **By adding the Sentry Lambda Layer to your function manually:**
    While this is a quick way to add Sentry to your AWS Lambda function, it gives you limited configuration possibilities with environment vars. See <PlatformLink to="/integrations/aws-lambda/manual-layer/">AWS Lambda Layer</PlatformLink>.
- **By manually adding Sentry to your function code:**
    This method requires that you install the Sentry SDK into your AWS Lambda function packages. While it takes more effort to set up, it gives you full control of your setup and manual instrumentation. See <PlatformLink to="/integrations/aws-lambda/manual-instrumentation/">AWS Lambda manual instrumentation</PlatformLink>.

</Alert>

As an alternative setup method, you can add Sentry to your [Container Image](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html). To import Sentry's Layer Image, add the following to your Dockerfile:

```docker {tabTitle: Dockerfile}
COPY --from=public.ecr.aws/sentry/sentry-python-serverless-sdk:<VERSION> /opt/ /opt
```

Replace `VERSION` with a specific version number (for example, 6). You can see a complete list of available versions in Sentry's [Amazon ECR repository](https://gallery.ecr.aws/sentry/sentry-python-serverless-sdk).

## Function Configuration

Set your image’s CMD value to the Sentry Handler:

```docker {tabTitle: Dockerfile}
CMD ["sentry_sdk.integrations.init_serverless_sdk.sentry_lambda_handler"]
```

Next, set the following environment variables in AWS:

- Set `SENTRY_INITIAL_HANDLER` to the path of your function handler
- Set `SENTRY_DSN` to your Sentry DSN
- Set `SENTRY_TRACES_SAMPLE_RATE` to your preferred [sampling rate](/platforms/python/sampling/#sampling-transaction-events) for transactions

Alternatively, you can also set the environment variables in your Dockerfile. Values set in AWS override the values in a Dockerfile if both are provided.


```docker {tabTitle: Dockerfile}
ENV SENTRY_INITIAL_HANDLER="<PATH_TO_FUNCTION_HANDLER>"
ENV SENTRY_DSN="___PUBLIC_DSN___"
ENV SENTRY_TRACES_SAMPLE_RATE="1.0"
```
