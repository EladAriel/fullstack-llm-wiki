---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/integrations/vectordb/curl.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.208224Z"
---
# Curl

---
title: "Vector DB tracing with cURL"
sidebarTitle: "cURL"
description: "Log any Vector DB interactions to Helicone using cURL."
---

import { strings } from "/snippets/strings.mdx";

## Example

```bash
curl -X POST https://api.worker.helicone.ai/custom/v1/log \
-H "Authorization: Bearer <YOUR_HELICONE_API_KEY>" \
-H "Content-Type: application/json" \
-d '{
  "providerRequest": {
    "url": "custom-model-nopath",
    "json": {
      "_type": "vector_db",
      "operation": "search",
      "text": "sample query text",
      "topK": 3,
      "databaseName": "sample_vector_db"
    },
    "meta": {
      "source": "test_integration",
      "environment": "development"
    }
  },
  "providerResponse": {
    "json": {
      "_type": "vector_db",
      "results": [
        {"id": "doc1", "score": 0.92, "content": "Sample document 1"},
        {"id": "doc2", "score": 0.85, "content": "Sample document 2"},
        {"id": "doc3", "score": 0.78, "content": "Sample document 3"}
      ]
    },
    "status": 200,
    "headers": {
      "content-type": "application/json"
    }
  },
  "timing": {
    "startTime": {
      "seconds": 1625686222,
      "milliseconds": 500
    },
    "endTime": {
      "seconds": 1625686244,
      "milliseconds": 750
    }
  }
}'
```

## Request Structure

### Endpoint

```
POST https://api.worker.helicone.ai/custom/v1/log
```

### Headers

| Name          | Value              |
| ------------- | ------------------ |
| Authorization | Bearer `<YOUR_HELICONE_API_KEY>` |

<div dangerouslySetInnerHTML={{ __html: strings.generateKeyInstructions }} />

### Body

```typescript
export type HeliconeAsyncLogRequest = {
  providerRequest: ProviderRequest;
  providerResponse: ProviderResponse;
  timing: Timing;
};

export type ProviderRequest = {
  url: "custom-model-nopath";
  json: {
    _type: "vector_db";
    operation: "search" | "insert" | "delete" | "update";
    text?: string;
    vector?: number[];
    topK?: number;
    filter?: object;
    databaseName?: string;
    [key: string]: any;
  };
  meta: Record<string, string>;
};

export type ProviderResponse = {
  json: {
    _type?: "vector_db";
    [key: string]: any;
  };
  status: number;
  headers: Record<string, string>;
};

export type Timing = {
  // From Unix epoch in Milliseconds
  startTime: {
    seconds: number;
    milliseconds: number;
  };
  endTime: {
    seconds: number;
    milliseconds: number;
  };
};
```
