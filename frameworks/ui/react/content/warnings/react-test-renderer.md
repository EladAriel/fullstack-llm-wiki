---
type: "Framework Learn Page"
framework: "React"
source_repo: "https://github.com/reactjs/react.dev"
source_branch: "main"
source_path: "src/content/warnings/react-test-renderer.md"
source_commit: "7c36f7ac329fe3cf2e11222edce9a535158c2cab"
source_commit_short: "7c36f7a"
source_commit_date: "2026-08-24T10:33:57-07:00"
generated_at: "2026-08-29T09:40:25.474952Z"
---
# React Test Renderer

---
title: react-test-renderer Deprecation Warnings
---

## ReactTestRenderer.create() warning {/*reacttestrenderercreate-warning*/}

react-test-renderer is deprecated. A warning will fire whenever calling ReactTestRenderer.create() or ReactShallowRender.render(). The react-test-renderer package will remain available on NPM but will not be maintained and may break with new React features or changes to React's internals.

The React Team recommends migrating your tests to [@testing-library/react](https://testing-library.com/docs/react-testing-library/intro/) or [@testing-library/react-native](https://callstack.github.io/react-native-testing-library/docs/start/intro) for a modern and well supported testing experience.


## new ShallowRenderer() warning {/*new-shallowrenderer-warning*/}

The react-test-renderer package no longer exports a shallow renderer at `react-test-renderer/shallow`. This was simply a repackaging of a previously extracted separate package: `react-shallow-renderer`. Therefore you can continue using the shallow renderer in the same way by installing it directly. See [Github](https://github.com/enzymejs/react-shallow-renderer) / [NPM](https://www.npmjs.com/package/react-shallow-renderer).
