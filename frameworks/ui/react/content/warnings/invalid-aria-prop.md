---
type: "Framework Learn Page"
framework: "react"
source_repo: "https://github.com/reactjs/react.dev"
source_branch: "main"
source_path: "src/content/warnings/invalid-aria-prop.md"
source_commit: "8bb31acb86bf68fa33d97dd0f1b834dfa71e2b1a"
source_commit_short: "8bb31acb"
source_commit_date: "2026-06-17T13:38:02-04:00"
generated_at: "2026-06-21T12:23:02Z"
---

---
title: Invalid ARIA Prop Warning
---

This warning will fire if you attempt to render a DOM element with an `aria-*` prop that does not exist in the Web Accessibility Initiative (WAI) Accessible Rich Internet Application (ARIA) [specification](https://www.w3.org/TR/wai-aria-1.1/#states_and_properties).

1. If you feel that you are using a valid prop, check the spelling carefully. `aria-labelledby` and `aria-activedescendant` are often misspelled.

2. If you wrote `aria-role`, you may have meant `role`.

3. Otherwise, if you're on the latest version of React DOM and verified that you're using a valid property name listed in the ARIA specification, please [report a bug](https://github.com/facebook/react/issues/new/choose).
