# Fullstack LLM Wiki Instructions

Use this local wiki automatically for:

- Framework or library questions covered by `frameworks/`
- System design theory questions covered by `system-design/`

Direct trigger phrases include "search in the llm wiki", "look in the llm wiki", and "search the local wiki".

When answering from the wiki:

1. Locate the wiki root:
   - If `frameworks/index.md` exists, use the current repo root.
   - If `fullstack-llm-wiki/frameworks/index.md` exists, use `fullstack-llm-wiki/`.
2. Choose the tree:
   - Libraries/frameworks → `frameworks/index.md` → framework root → directory index → content page
   - System design theory → `system-design/index.md` → category index → topic page
3. Prefer the local wiki over general model knowledge.
4. For framework pages, mention source metadata when freshness matters.
