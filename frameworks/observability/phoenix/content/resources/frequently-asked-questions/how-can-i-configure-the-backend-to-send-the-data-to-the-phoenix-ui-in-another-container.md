---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/resources/frequently-asked-questions/how-can-i-configure-the-backend-to-send-the-data-to-the-phoenix-ui-in-another-container.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.877460Z"
---
# How Can I Configure The Backend To Send The Data To The Phoenix Ui In Another Container

---
title: "How can I configure the backend to send the data to the phoenix UI in another container?"
description: "_If you are working on an API whose endpoints perform RAG, but would like the phoenix server not to be launched as another thread._"
---


You can do this by configuring the following the [environment](/docs/phoenix/environments) variable PHOENIX\_COLLECTOR\_ENDPOINT to point to the server running in a different process or container.
