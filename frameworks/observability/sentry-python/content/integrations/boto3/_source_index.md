---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/integrations/boto3/index.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.061150Z"
---
# Index

---
title: Boto3
description: "Learn about the Boto3 integration and how it adds support for the Boto3 and botocore libraries."
---

The Boto3 integration instruments requests made to Amazon Web Services done with [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) (or the low level [botocore](https://github.com/boto/botocore) library that Boto3 uses under the hood). It creates a span for every request.

## Install

Install `sentry-sdk` from PyPI:

```bash {tabTitle:pip}
pip install "sentry-sdk"
```
```bash {tabTitle:uv}
uv add "sentry-sdk"
```

## Configure

If you have the `boto3` package in your dependencies, the Boto3 integration will be enabled automatically when you initialize the Sentry SDK.

<PlatformContent includePath="getting-started-config" />

## Supported Versions

- botocore: 1.12+
- Python: 3.6+

<Include name="python-use-older-sdk-for-legacy-support.mdx" />
