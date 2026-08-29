---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/rest/models/get-v1public-model-registry-models.mdx"
source_commit: "607c855f787d6cc66e83692874bf90f880a08d62"
source_commit_short: "607c855"
source_commit_date: "2026-08-25T19:59:29-04:00"
generated_at: "2026-08-29T09:39:42.299585Z"
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