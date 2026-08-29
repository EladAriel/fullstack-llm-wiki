---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/resources/frequently-asked-questions/how-can-i-configure-the-backend-to-send-the-data-to-the-phoenix-ui-in-another-container.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.948889Z"
---
# How Can I Configure The Backend To Send The Data To The Phoenix Ui In Another Container

---
title: "How can I configure the backend to send the data to the phoenix UI in another container?"
description: "_If you are working on an API whose endpoints perform RAG, but would like the phoenix server not to be launched as another thread._"
---


You can do this by configuring the following the [environment](/docs/phoenix/environments) variable PHOENIX\_COLLECTOR\_ENDPOINT to point to the server running in a different process or container.
