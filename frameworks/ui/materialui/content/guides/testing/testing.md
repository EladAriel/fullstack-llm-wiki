---
type: "Framework Learn Page"
framework: "Material UI"
source_repo: "https://github.com/mui/material-ui.git"
source_branch: "master"
source_path: "docs/data/material/guides/testing/testing.md"
source_commit: "4d5fe7254baa7e97e38b516f37c7af13128468b7"
source_commit_short: "4d5fe725"
source_commit_date: "2026-07-24T12:25:49+03:00"
generated_at: "2026-07-25T13:39:40.980764Z"
---
# Testing

<p class="description">Write tests to prevent regressions and write better code.</p>

## Userspace

It's generally recommended to test your application without tying the tests too closely to Material UI.
This is how Material UI components are tested internally.
A library that has a first-class API for this approach is [`@testing-library/react`](https://testing-library.com/docs/react-testing-library/intro/).

For example, when rendering a `TextField` your test should not need to query for the specific Material UI instance of the `TextField` but rather for the `input`, or `[role="textbox"]`.

By not relying on the React component tree you make your test more robust against internal changes in Material UI or, if you need snapshot testing, adding additional wrapper components such as context providers.
We don't recommend snapshot testing though.
["Effective snapshot testing" by Kent C. Dodds](https://kentcdodds.com/blog/effective-snapshot-testing) goes into more details why snapshot testing might be misleading for React component tests.

## Internal

We have **a wide range** of tests for Material UI so we can
iterate with confidence on the components, for instance, the visual regression tests provided by [Argos](https://argos-ci.com) have proven to be really helpful.
To learn more about the internal tests, you can have a look at the [README](https://github.com/mui/material-ui/blob/HEAD/test/README.md).
