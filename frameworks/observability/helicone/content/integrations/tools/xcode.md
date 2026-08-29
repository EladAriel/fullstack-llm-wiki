---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/integrations/tools/xcode.mdx"
source_commit: "607c855f787d6cc66e83692874bf90f880a08d62"
source_commit_short: "607c855"
source_commit_date: "2026-08-25T19:59:29-04:00"
generated_at: "2026-08-29T09:39:42.349535Z"
---
# Xcode

---
title: "Xcode Integration (AI Gateway)"
sidebarTitle: "Xcode"
description: "Configure Xcode's Intelligence model provider to route through Helicone's AI Gateway for observability."
---

This guide shows how to add Helicone as a model provider in Xcode so your chats route through the Helicone AI Gateway and show up in your Helicone dashboard.

## Prerequisites

- A Helicone account and API key
- Org/provider keys configured in Helicone (so models can be listed)

## Steps

1) Open Xcode Settings

   - Xcode → Settings…

   <img src="/images/integrations/xcode/xcode-settings.png" alt="Xcode Settings - Intelligence section" />

2) Add Helicone as a model provider

   - Select the Intelligence tab
   - Click "Add a model provider…"

   <img src="/images/integrations/xcode/xcode-add-model.png" alt="Add model provider dialog in Xcode" />

   - Fill the form with:
     - URL: `https://ai-gateway.helicone.ai`
     - API Key: `Bearer <helicone-api-key>`
     - API Key Header: `Authorization`
     - Description: `Helicone` (you can name this however you like)

   <img src="/images/integrations/xcode/xcode-configure-helicone.png" alt="Add model provider dialog in Xcode" />

3) Confirm models are available

   - After saving, Xcode should list available models from Helicone
   - There are many models; use Favorites to pin the ones you use most

   <img src="/images/integrations/xcode/xcode-models-list.png" alt="Models list in Xcode with favorites" />

4) Start chatting and view logs in Helicone

   - Use the chat in Xcode with your selected model
   - Open the Helicone dashboard to see your requests, tokens, and costs

   <img src="/images/integrations/xcode/xcode-chat.png" alt="Chatting in Xcode and viewing requests in Helicone" />

5) Switch chat model

   - In the chat widget, press the dropdown to select a new model.

   <img src="/images/integrations/xcode/xcode-chat-model-select.png" alt="Chatting in Xcode and viewing requests in Helicone" />

## Notes

- URL points to the Helicone AI Gateway. Your Helicone API key is sent via the `Authorization` header.
- If you don’t see models, verify your org/provider keys are set in Helicone and that your key has access.
