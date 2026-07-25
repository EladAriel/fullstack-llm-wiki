---
type: "Framework Learn Page"
framework: "Material UI"
source_repo: "https://github.com/mui/material-ui.git"
source_branch: "master"
source_path: "docs/data/material/getting-started/supported-platforms/supported-platforms.md"
source_commit: "4d5fe7254baa7e97e38b516f37c7af13128468b7"
source_commit_short: "4d5fe725"
source_commit_date: "2026-07-24T12:25:49+03:00"
generated_at: "2026-07-25T13:39:40.984584Z"
---
# Supported platforms

<p class="description">Learn about the platforms, from modern to old, that are supported by Material UI.</p>

## Browser

Material UI supports the latest, stable releases of all major browsers and platforms.
You don't need to provide any JavaScript polyfill as it manages unsupported browser features internally and in isolation.

<!-- #stable-snapshot -->

| Edge   | Firefox | Chrome | Safari (macOS) | Safari (iOS) |
| :----- | :------ | :----- | :------------- | :----------- |
| >= 121 | >= 121  | >= 117 | >= 17.0        | >= 17.0      |

<!-- #target-branch-reference -->

An extensive list can be found in our [.browserlistrc](https://github.com/mui/material-ui/blob/-/.browserslistrc#L9-L188) (check the `stable` entry).

Because Googlebot uses a web rendering service (WRS) to index the page content, it's critical that Material UI supports it.
[WRS regularly updates the rendering engine it uses](https://developers.google.com/search/blog/2019/05/the-new-evergreen-googlebot).
You can expect Material UI's components to render without major issues.

## Server

<!-- #stable-snapshot -->

Material UI supports [Node.js](https://github.com/nodejs/node) starting with version 14.0 for server-side rendering.
The objective is to support Node.js down to the [last version in maintenance mode](https://github.com/nodejs/Release#release-schedule).

## React

<!-- #react-peer-version -->

Material UI supports the most recent versions of React, starting with ^17.0.0 (the one with event delegation at the React root).
Have a look at the older [versions](https://mui.com/material-ui/getting-started/versions/) for backward compatibility.

## TypeScript

Material UI requires a minimum version of TypeScript 4.9.
This aims to match the policy of [DefinitelyTyped](https://github.com/DefinitelyTyped/DefinitelyTyped), with the support of the versions of TypeScript that are less than two years old.

## webpack

The minimum required version of webpack to bundle applications that use Material UI is v5. webpack <= v4 can't bundle Material UI untranspiled as it uses features such as the [null coalescing operator (`??`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing) and [optional chaining (`?.`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining).
