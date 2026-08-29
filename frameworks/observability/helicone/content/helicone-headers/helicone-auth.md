---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/helicone-headers/helicone-auth.mdx"
source_commit: "607c855f787d6cc66e83692874bf90f880a08d62"
source_commit_short: "607c855"
source_commit_date: "2026-08-25T19:59:29-04:00"
generated_at: "2026-08-29T09:39:42.265189Z"
---
# Helicone Auth

---
title: "Helicone Auth"
sidebarTitle: "Helicone Auth"
description: "Complete guide to Helicone authentication. Learn about API key types, permissions, regional variations, and alternative authentication methods."
"twitter:title": "Helicone Authentication - Open Source LLM Observability"
---

## Helicone Auth keys

When creating a new Helicone API key you have the ability to enable read and write permissions.

Write keys can be used through Helicone via our proxy, feedback or any other Helicone service when calling a `POST` or using our gateway.

<Frame caption="When creating a key you can choose whether or not you want to enable reads.">
  <img
    src="/images/auth/new_key.png"
    alt="Option to enable read permission when creating a new Helicone API key."
  />
</Frame>

<Note>
  Key's with read permissions will start with `sk-` and keys with write
  permissions will start with `pk-`.
</Note>

## Helicone Keys in the EU

For our EU customers, keys are generated with the prefix `eu-` this allows our edge workers to know which region to route the request to.

## Using `Helicone-Auth` not in the header

Typically to authenticate Helicone you will need to add a header called `Helicone-Auth`. However, in some environments you do not have access to headers, and you only have the ability to change the base URL. In this case, you can actually embed the API key directly into the URL path.

You are now allowed to use a write only key within the URL path to authenticate your requests.

This is done by changing the base URL to `https://gateway.helicone.ai/[HELICONE_API_KEY]/v1/` where `[HELICONE_API_KEY]` is your Helicone API key.

This will work with any of our [supported domains](/getting-started/integration-method/gateway#approved-domains).
