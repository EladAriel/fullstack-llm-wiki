---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/guides/cookbooks/github-actions.mdx"
source_commit: "607c855f787d6cc66e83692874bf90f880a08d62"
source_commit_short: "607c855"
source_commit_date: "2026-08-25T19:59:29-04:00"
generated_at: "2026-08-29T09:39:42.330436Z"
---
---
title: "Integrating Helicone with GitHub Actions"
sidebarTitle: "GitHub Actions Integration"
description: "Automate the monitoring and caching of LLM calls in your CI pipelines with Helicone."
"twitter:title": "Integrating Helicone with GitHub Actions - Helicone OSS LLM Observability"
---

<Warning>
<b>IMPORTANT NOTICE</b>

Utilizing Man-In-The-Middle software like this involves significant security and performance risks. Please refer to [tools/mitm-proxy](/tools/mitm-proxy) for detailed information and ensure you fully comprehend the scripts before incorporating this into your CI pipeline.

</Warning>

# Github Actions with Ubuntu/Debian

Maximize the capabilities of Helicone by integrating it into your CI pipelines. This guide provides instructions on how to incorporate Helicone into your Github Actions workflows.

## Setup

Incorporate the following steps into your Github Actions workflow:

1. Add the proxy to your workflow:

```bash
curl -s https://raw.githubusercontent.com/Helicone/helicone/main/mitmproxy.sh | bash -s start
```

2. Set your ENV variables:

```yml
OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
HELICONE_API_KEY: ${{ secrets.HELICONE_API_KEY }}
REQUESTS_CA_BUNDLE: /etc/ssl/certs/ca-certificates.crt
HELICONE_CACHE_ENABLED: "true"
HELICONE_PROPERTY_<KEY>: <VALUE>
```

Variables can also be set within your test. For more information, refer to the [mitm docs](/tools/mitm-proxy).

## Example

```yml
# ...Rest of yml
tests:
  steps:
    - name: Execute OpenAI tests
      run: |
        curl -s https://raw.githubusercontent.com/Helicone/helicone/main/mitmproxy.sh | bash -s start
        # Execute your tests here

      env:
        OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        HELICONE_API_KEY: ${{ secrets.HELICONE_API_KEY }}
        REQUESTS_CA_BUNDLE: /etc/ssl/certs/ca-certificates.crt
        HELICONE_CACHE_ENABLED: "true"
        HELICONE_PROPERTY_<KEY>: <VALUE>
```
