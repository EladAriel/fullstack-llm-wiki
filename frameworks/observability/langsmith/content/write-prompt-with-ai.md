---
type: "Framework Learn Page"
framework: "LangSmith"
source_repo: "https://github.com/langchain-ai/docs.git"
source_branch: "main"
source_path: "src/langsmith/write-prompt-with-ai.mdx"
source_commit: "a174f9cf7c91ee5eb14ee2382eb48bfe6e4956e9"
source_commit_short: "a174f9c"
source_commit_date: "2026-08-28T17:04:12-07:00"
generated_at: "2026-08-29T09:39:50.655660Z"
---
# Write Prompt With Ai

---
title: Write your prompt with AI
sidebarTitle: Write your prompt with AI
---

The prompt canvas makes it easy to edit a prompt with the help of an LLM. This allows you to iterate faster on long prompts and also makes it easier to make overarching stylisting or tonal changes to your prompt. You can enter the promp canvas by clicking the glowing wand over any message in your prompt:

![Prompt canvas open](/langsmith/images/prompt-canvas-open.gif)

## Chat sidebar

You can use the chat sidebar to ask questions about your prompt, or to give instructions in natural language to the LLM for how to rewrite your prompt.

![Prompt canvas rewrite](/langsmith/images/prompt-canvas-rewrite.gif)

<Note>
You can also edit the prompt directly - you don't **need** to use the LLM. This is useful if you know what edits you want to make and just want to make them directly
</Note>

## Quick actions

There are quick actions to change the reading level or length of the prompt with a single mouse click:

![Prompt canvas quick actions](/langsmith/images/prompt-canvas-quick-actions.gif)

## Custom quick actions

You can also save your own custom quick actions, for ease of use across all the prompts you are working on in LangSmith:

![Prompt canvas custom quick action](/langsmith/images/prompt-canvas-custom-quick-action.gif)

## Diffing

You can also see the specific differences between each version of your prompt by selecting the diff slider in the top right of the canvas:

![Prompt canvas diff](/langsmith/images/prompt-canvas-diff.gif)

## Saving and using prompts

Lastly, you can save the prompt you have created in the canvas by clicking the "Use this Version" button in the bottom right:

![Prompt canvas save](/langsmith/images/prompt-canvas-save.gif)
