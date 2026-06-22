---
type: "Framework Learn Page"
framework: "nextjs"
source_repo: "https://github.com/vercel/next.js/"
source_branch: "canary"
source_path: "docs/01-app/02-guides/upgrading/version-14.mdx"
source_commit: "79142d7806ff4194c8d9885b80fa69db5ecf534a"
source_commit_short: "79142d78"
source_commit_date: "2026-06-20T23:40:12Z"
generated_at: "2026-06-21T12:07:17Z"
---

---
title: How to upgrade to version 14
nav_title: Version 14
description: Upgrade your Next.js Application from Version 13 to 14.
---

{/* The content of this doc is shared between the app and pages router. You can use the `<PagesOnly>Content</PagesOnly>` component to add content that is specific to the Pages Router. Any shared content should not be wrapped in a component. */}

## Upgrading from 13 to 14

To update to Next.js version 14, run the following command using your preferred package manager:

```bash filename="Terminal"
npm i next@next-14 react@18 react-dom@18 && npm i eslint-config-next@next-14 -D
```

```bash filename="Terminal"
yarn add next@next-14 react@18 react-dom@18 && yarn add eslint-config-next@next-14 -D
```

```bash filename="Terminal"
pnpm i next@next-14 react@18 react-dom@18 && pnpm i eslint-config-next@next-14 -D
```

```bash filename="Terminal"
bun add next@next-14 react@18 react-dom@18 && bun add eslint-config-next@next-14 -D
```

> **Good to know:** If you are using TypeScript, ensure you also upgrade `@types/react` and `@types/react-dom` to their latest versions.

### v14 Summary

- The minimum Node.js version has been bumped from 16.14 to 18.17, since 16.x has reached end-of-life.
- The `next export` command has been removed in favor of `output: 'export'` config. Please see the [docs](https://nextjs.org/docs/app/guides/static-exports) for more information.
- The `next/server` import for `ImageResponse` was renamed to `next/og`. A [codemod is available](/docs/app/guides/upgrading/codemods#next-og-import) to safely and automatically rename your imports.
- The `@next/font` package has been fully removed in favor of the built-in `next/font`. A [codemod is available](/docs/app/guides/upgrading/codemods#built-in-next-font) to safely and automatically rename your imports.
- The WASM target for `next-swc` has been removed.
