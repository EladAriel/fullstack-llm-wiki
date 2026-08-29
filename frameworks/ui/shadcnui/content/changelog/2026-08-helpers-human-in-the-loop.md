---
type: "Framework Learn Page"
framework: "shadcn/ui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/changelog/2026-08-helpers-human-in-the-loop.mdx"
source_commit: "683a5a9b370acdb7785a0529434e6a3b8c7e0441"
source_commit_short: "683a5a9"
source_commit_date: "2026-08-26T10:28:13+04:00"
generated_at: "2026-08-29T09:40:26.958193Z"
---
# 2026 08 Helpers Human In The Loop

---
title: August 2026 - Human in the Loop
description: Mock paused tool calls, approvals, and continuations for the AI SDK with @shadcn/helpers.
date: 2026-08-12
---

**@shadcn/helpers** can now mock human-in-the-loop flows for the AI SDK. A
scripted conversation can pause for real user input, wait for an approval, and
continue with whatever the user decided.

Everything streams through the real
`useChat` lifecycle, so your tool cards, approval prompts, and question flows
behave exactly as they would in production.

```ts showLineNumbers
import { createChat } from "@shadcn/helpers/ai-sdk"

const chat = createChat<ChatMessage>()
  .user("Help me plan the next prototype.")
  .assistant(({ writer }) => {
    writer.text("A couple of questions before I start.")
    writer.tool("askQuestions", { input: { questions } })
  })
  .assistant(({ writer, toolCall }) => {
    writer.text(
      toolCall?.name === "askQuestions" && toolCall.output
        ? `Starting with ${toolCall.output.answers.direction}.`
        : "Starting now."
    )
  })
```

Pass `needsApproval` to pause behind the user's decision. The scripted output
streams after approval, and denial streams automatically.

```ts showLineNumbers
chat
  .assistant(({ writer }) => {
    writer.text("That will archive 3 drafts. I need your approval.")
    writer.tool("archiveDrafts", {
      input: { count: 3 },
      needsApproval: true,
      output: { archived: 3 },
    })
  })
  .assistant(({ writer, toolCall }) => {
    writer.text(
      toolCall?.approved ? "Archived 3 drafts." : "Okay, leaving them in place."
    )
  })
```

<div className="flex flex-wrap gap-2">
  <Button asChild size="sm">
    <Link
      href="/docs/helpers/ai-sdk#human-in-the-loop"
      className="mt-6 no-underline!"
    >
      Read the Docs
    </Link>
  </Button>
</div>
