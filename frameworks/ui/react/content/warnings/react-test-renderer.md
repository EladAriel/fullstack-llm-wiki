---
type: "Framework Learn Page"
framework: "react"
source_repo: "https://github.com/reactjs/react.dev"
source_branch: "main"
source_path: "src/content/warnings/react-test-renderer.md"
source_commit: "8bb31acb86bf68fa33d97dd0f1b834dfa71e2b1a"
source_commit_short: "8bb31acb"
source_commit_date: "2026-06-17T13:38:02-04:00"
generated_at: "2026-06-21T12:23:02Z"
---

---
title: react-test-renderer Deprecation Warnings
---

## ReactTestRenderer.create() warning {/*reacttestrenderercreate-warning*/}

react-test-renderer is deprecated. A warning will fire whenever calling ReactTestRenderer.create() or ReactShallowRender.render(). The react-test-renderer package will remain available on NPM but will not be maintained and may break with new React features or changes to React's internals.

The React Team recommends migrating your tests to [@testing-library/react](https://testing-library.com/docs/react-testing-library/intro/) or [@testing-library/react-native](https://callstack.github.io/react-native-testing-library/docs/start/intro) for a modern and well supported testing experience.


## new ShallowRenderer() warning {/*new-shallowrenderer-warning*/}

The react-test-renderer package no longer exports a shallow renderer at `react-test-renderer/shallow`. This was simply a repackaging of a previously extracted separate package: `react-shallow-renderer`. Therefore you can continue using the shallow renderer in the same way by installing it directly. See [Github](https://github.com/enzymejs/react-shallow-renderer) / [NPM](https://www.npmjs.com/package/react-shallow-renderer).
