---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/integrations/anthropic/claude-code.mdx"
source_commit: "607c855f787d6cc66e83692874bf90f880a08d62"
source_commit_short: "607c855"
source_commit_date: "2026-08-25T19:59:29-04:00"
generated_at: "2026-08-29T09:39:42.353595Z"
---
# Claude Code

---
title: "Claude Code"
sidebarTitle: "Claude Code"
description: "Integrate Helicone to log your Claude Code interactions."
"twitter:title": "Claude Code - Helicone OSS LLM Observability"
icon: "plug"
iconType: "solid"
---

import { strings } from "/snippets/strings.mdx";
import LegacyWarning from "/snippets/legacy-provider-warning.mdx";

<LegacyWarning />

Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks.

## {strings.howToIntegrate}

<Steps>
  <Step title={strings.generateKey}>
    <div dangerouslySetInnerHTML={{ __html: strings.generateKeyInstructions }} />
  </Step>

  <Step title={strings.exportBaseUrl("Anthropic")}>
    ```bash
    export ANTHROPIC_BASE_URL=https://anthropic.helicone.ai/<your-helicone-api-key>
    ```
  </Step>

  <Step title={strings.logYourRequest}>
    In your terminal, replace "what is the meaning of life?" with your own prompt.

    ```bash
    claude -p 'what is the meaning of life?'
    ```
  </Step>

  <Step title={strings.verifyInHelicone}>
    <div dangerouslySetInnerHTML={{ __html: strings.verifyInHeliconeDesciption("Claude Code") }} />
  </Step>
</Steps>
