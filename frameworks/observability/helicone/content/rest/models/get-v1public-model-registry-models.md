---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/rest/models/get-v1public-model-registry-models.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.259361Z"
---
# Get V1Public Model Registry Models

---
title: "Get Model Registry"
sidebarTitle: "Get All Available Models"
description: "Returns all models and endpoints supported by the Helicone AI Gateway"
openapi: get /v1/public/model-registry/models
---

This endpoint returns the complete catalog of AI models and provider endpoints that the Helicone AI Gateway can route to. The gateway uses this registry to determine which providers support a requested model and how to intelligently route requests for maximum reliability and cost optimization.

When you request a model through the AI Gateway (like `gpt-4o-mini`), the gateway consults this registry to find all providers offering that model, then applies routing logic to select the best provider based on your configuration, availability, and pricing.