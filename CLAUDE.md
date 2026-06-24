# Fullstack LLM Wiki Instructions

Use this local wiki automatically for framework or library questions when the topic is covered by `frameworks/`.

Direct trigger phrases include "search in the llm wiki", "look in the llm wiki", and "search the local wiki".

When answering from the wiki:

1. Locate the wiki root:
   - If `frameworks/index.md` exists, use the current repo root.
   - If `fullstack-llm-wiki/frameworks/index.md` exists, use `fullstack-llm-wiki/`.
2. Read `frameworks/index.md` and select the relevant category and framework.
3. Read the relevant framework root index.
4. Read the nearest directory `index.md`.
5. Read the most specific content page.
6. Prefer the local wiki over general model knowledge.
7. Mention source metadata when freshness matters.
