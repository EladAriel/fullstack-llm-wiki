---
type: "Framework Learn Page"
framework: "nextjs"
source_repo: "https://github.com/vercel/next.js/"
source_branch: "canary"
source_path: "docs/01-app/03-api-reference/05-config/01-next-config-js/typescript.mdx"
source_commit: "79142d7806ff4194c8d9885b80fa69db5ecf534a"
source_commit_short: "79142d78"
source_commit_date: "2026-06-20T23:40:12Z"
generated_at: "2026-06-21T12:07:17Z"
---

---
title: typescript
description: Configure how Next.js handles TypeScript errors during production builds and specify a custom tsconfig file.
---

{/* The content of this doc is shared between the app and pages router. You can use the `<PagesOnly>Content</PagesOnly>` component to add content that is specific to the Pages Router. Any shared content should not be wrapped in a component. */}

Configure TypeScript behavior with the `typescript` option in `next.config.js`:

```js filename="next.config.js"
module.exports = {
  typescript: {
    ignoreBuildErrors: false,
    tsconfigPath: 'tsconfig.json',
  },
}
```

## Options

| Option              | Type      | Default           | Description                                                      |
| ------------------- | --------- | ----------------- | ---------------------------------------------------------------- |
| `ignoreBuildErrors` | `boolean` | `false`           | Allow production builds to complete even with TypeScript errors. |
| `tsconfigPath`      | `string`  | `'tsconfig.json'` | Path to a custom `tsconfig.json` file.                           |

## `ignoreBuildErrors`

Next.js fails your **production build** (`next build`) when TypeScript errors are present in your project.

If you'd like Next.js to dangerously produce production code even when your application has errors, you can disable the built-in type checking step.

Note that this completely skips the TypeScript type checking step. It does not run TypeScript and suppress errors, it bypasses the check entirely.

If disabled, be sure you are running type checks as part of your build or deploy process, otherwise this can be very dangerous.

```js filename="next.config.js"
module.exports = {
  typescript: {
    // !! WARN !!
    // Dangerously allow production builds to successfully complete even if
    // your project has type errors.
    // !! WARN !!
    ignoreBuildErrors: true,
  },
}
```

## `tsconfigPath`

Use a different TypeScript configuration file for builds or tooling:

```js filename="next.config.js"
module.exports = {
  typescript: {
    tsconfigPath: 'tsconfig.build.json',
  },
}
```

See the [TypeScript configuration](/docs/app/api-reference/config/typescript#custom-tsconfig-path) page for more details.
