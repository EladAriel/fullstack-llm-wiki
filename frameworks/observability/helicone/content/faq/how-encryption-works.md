---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/faq/how-encryption-works.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.192206Z"
---
# How Encryption Works

---
title: "How Encryption Works"
sidebarTitle: "Encryption"
description: "Discover how Helicone ensures the security of your API requests through advanced encryption methods and secure handling of API keys."
"twitter:title": "How Encryption Works - Helicone OSS LLM Observability"
---

### What happens to your OpenAI key

When you call a completions request with Helicone's cloud hosted proxy, we get
your OpenAI key to execute the query on your behalf. We also hash your key using
the cryptographically secure SHA-256 hash function and log the hash with your
response.

#### 💡Your OpenAI key is never stored on our servers.\*\*

The first time you login to Helicone's web application, you will enter your
OpenAI key. We hash it in your client using the same hash function above and
persist only the hash in our server.

This allows the web application to match your completion requests with your
account, even though we never know what your key is.

#### 💡 The hash function is irreversible and it is not possible to infer your OpenAI Key from the hash of your keys.

## <br />

### Don't believe us? Check out our open-source code

Helicone is an evolving [open source project](https://github.com/Helicone/valyr)
that is committed to earning the trust of developers. By making our code
publicly available, we provide transparency and allow developers to confirm best
security practices for themselves and suggest improvements where possible.
