---
type: "Framework Learn Page"
framework: "Next.js"
source_repo: "https://github.com/vercel/next.js/"
source_branch: "canary"
source_path: "docs/01-app/03-api-reference/05-config/01-next-config-js/turbopackRustReactCompiler.mdx"
source_commit: "33a5d542e519fe4e05c8c8c2c2845da9f741699b"
source_commit_short: "33a5d542"
source_commit_date: "2026-08-29T00:04:45-07:00"
generated_at: "2026-08-29T09:40:24.310602Z"
---
# Turbopackrustreactcompiler

---
title: turbopackRustReactCompiler
description: Use the native Rust port of the React Compiler with Turbopack instead of the Babel transform.
version: experimental
---

The `experimental.turbopackRustReactCompiler` option enables the native Rust version of the [React Compiler](/docs/app/api-reference/config/next-config-js/reactCompiler), running it directly inside Turbopack as native code instead of through Node.js as it does with the standard Babel version. This typically results in a noticeable performance improvement.

This option is released as experimental to gather feedback before it becomes the default.

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  // Enable the React Compiler
  reactCompiler: true,
  experimental: {
    // Use the Rust port instead of the Babel transform
    turbopackRustReactCompiler: true,
  },
}

export default nextConfig
```

```js filename="next.config.js" switcher
/** @type {import('next').NextConfig} */
const nextConfig = {
  // Enable the React Compiler
  reactCompiler: true,
  experimental: {
    // Use the Rust port instead of the Babel transform
    turbopackRustReactCompiler: true,
  },
}

module.exports = nextConfig
```

## Good to know

> - This option requires [`reactCompiler`](/docs/app/api-reference/config/next-config-js/reactCompiler) to be enabled. It selects which implementation runs, but does not turn the compiler on by itself.
> - This option is only supported with Turbopack. Using it with webpack will throw an error.
> - When enabled, you do not need to install `babel-plugin-react-compiler`. The Rust compiler runs natively inside Turbopack.

See the [`reactCompiler` option documentation](/docs/app/api-reference/config/next-config-js/reactCompiler) for details on how to use the compiler.

## Version History

| Version   | Changes                                                                                             |
| --------- | --------------------------------------------------------------------------------------------------- |
| `v16.3.0` | Introduced the experimental `turbopackRustReactCompiler` option for the native Rust React Compiler. |
