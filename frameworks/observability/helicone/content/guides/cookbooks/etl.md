---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/guides/cookbooks/etl.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.282409Z"
---
---
title: "ETL / Data Extraction"
sidebarTitle: "ETL / Data Extraction"
description: "Extract, transform, and load data from Helicone into your data warehouse using our CLI tool or REST API."
"twitter:title": "ETL / Data Extraction - Helicone OSS LLM Observability"
---

## Quick Start: Export with CLI

The easiest way to extract your data is using our official npm package:

```bash
# Export to JSONL (recommended for large datasets)
HELICONE_API_KEY="your-api-key" npx @helicone/export --start-date 2024-01-01 --include-body

# Export to CSV for analysis in spreadsheets
HELICONE_API_KEY="your-api-key" npx @helicone/export --format csv --output data.csv --include-body

# Export with property filters (e.g., by environment)
HELICONE_API_KEY="your-api-key" npx @helicone/export --property environment=production --include-body

# Export from EU region
HELICONE_API_KEY="your-eu-api-key" npx @helicone/export --region eu --include-body
```

**Key Features:**
- ✅ Auto-recovery from crashes with checkpoint system
- ✅ Retry logic with exponential backoff
- ✅ Progress tracking with ETA
- ✅ Multiple output formats (JSON, JSONL, CSV)
- ✅ Property and date filtering
- ✅ Region support (US and EU)

See the [export tool documentation](/tools/export) for all available options.

## What Data You Can Extract

Our export tool provides comprehensive access to your LLM data:

- **Request Metadata**: User IDs, session IDs, custom properties
- **Model Information**: Model names, versions, providers
- **Request/Response Bodies**: Full prompts and completions (with `--include-body`)
- **Performance Metrics**: Latency, token counts, cache hits
- **Cost Data**: Per-request costs in USD
- **Feedback**: User ratings and feedback (when available)

## Using the REST API

For custom integrations or programmatic access, use our [REST API](/rest/request/post-v1requestquery-clickhouse):

<Warning>
  **Important:** When filtering by custom properties, you MUST wrap them in a `request_response_rmt` object. See examples below.
</Warning>

**Get all requests:**

```bash
curl --request POST \
  --url https://api.helicone.ai/v1/request/query-clickhouse \
  --header "Content-Type: application/json" \
  --header "authorization: Bearer $HELICONE_API_KEY" \
  --data '{
    "filter": "all",
    "limit": 1000,
    "offset": 0
  }'
```

**Filter by custom property:**

```bash
curl --request POST \
  --url https://api.helicone.ai/v1/request/query-clickhouse \
  --header "Content-Type: application/json" \
  --header "authorization: Bearer $HELICONE_API_KEY" \
  --data '{
    "filter": {
      "request_response_rmt": {
        "properties": {
          "environment": {
            "equals": "production"
          }
        }
      }
    },
    "limit": 1000,
    "offset": 0
  }'
```

**Filter by date range AND property:**

```bash
curl --request POST \
  --url https://api.helicone.ai/v1/request/query-clickhouse \
  --header "Content-Type: application/json" \
  --header "authorization: Bearer $HELICONE_API_KEY" \
  --data '{
    "filter": {
      "left": {
        "request_response_rmt": {
          "request_created_at": {
            "gte": "2024-01-01T00:00:00Z"
          }
        }
      },
      "operator": "and",
      "right": {
        "request_response_rmt": {
          "properties": {
            "appname": {
              "equals": "MyApp"
            }
          }
        }
      }
    },
    "limit": 1000,
    "offset": 0
  }'
```

See the [full API documentation](/rest/request/post-v1requestquery-clickhouse) for more filter options and examples.

## ETL Connectors

We currently provide:
- **CLI tool** for direct export to JSON/JSONL/CSV
- **REST API** for custom integrations

Looking for a specific connector? We're receptive to suggestions! Reach us on [Discord](https://discord.com/invite/zsSTcH2qhG) or submit a [Github issue](https://github.com/Helicone/helicone/issues).
