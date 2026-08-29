---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/iris/langcache/use-langcache.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.317984Z"
---
# Use Langcache

---
alwaysopen: false
categories:
- docs
- operate
- iris
description: null
hideListLinks: true
linktitle: Use LangCache
title: Use the LangCache API on Redis Cloud
weight: 10
aliases:
- /operate/rc/langcache/use-langcache
- /operate/rc/context-engine/langcache/use-langcache/
---

You can use the [LangCache API and SDK]({{< relref "/develop/ai/context-engine/langcache/api-examples" >}}) from your client app to store and retrieve LLM, RAG, or agent responses. 

To access the LangCache API, you need:

- LangCache API base URL
- LangCache service API key
- Cache ID

For LangCache on Redis Cloud, the base URL and cache ID are available in the LangCache service's **Configuration** page in the [**Connectivity** section]({{< relref "/operate/iris/langcache/view-edit-cache#connectivity" >}}).

The LangCache API key is only available immediately after you create the LangCache service. If you lost this value, you will need to [replace the service API key]({{< relref "/operate/iris/langcache/view-edit-cache#replace-service-api-key" >}}) to be able to use the LangCache API.

When you call the API, you need to pass the LangCache API key in the `Authorization` header as a Bearer token and the Cache ID as the `cacheId` path parameter. 

See the [LangCache API and SDK examples]({{< relref "/develop/ai/context-engine/langcache/api-examples" >}}) for more information on how to use the LangCache API.
