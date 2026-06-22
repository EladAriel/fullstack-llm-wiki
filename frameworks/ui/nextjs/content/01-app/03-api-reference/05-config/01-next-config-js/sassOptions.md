---
type: "Framework Learn Page"
framework: "nextjs"
source_repo: "https://github.com/vercel/next.js/"
source_branch: "canary"
source_path: "docs/01-app/03-api-reference/05-config/01-next-config-js/sassOptions.mdx"
source_commit: "79142d7806ff4194c8d9885b80fa69db5ecf534a"
source_commit_short: "79142d78"
source_commit_date: "2026-06-20T23:40:12Z"
generated_at: "2026-06-21T12:07:17Z"
---

---
title: sassOptions
description: Configure Sass options.
---

`sassOptions` allow you to configure the Sass compiler.

```ts filename="next.config.ts" switcher
import type { NextConfig } from 'next'

const sassOptions = {
  additionalData: `
    $var: red;
  `,
}

const nextConfig: NextConfig = {
  sassOptions: {
    ...sassOptions,
    implementation: 'sass-embedded',
  },
}

export default nextConfig
```

```js filename="next.config.js" switcher
/** @type {import('next').NextConfig} */

const sassOptions = {
  additionalData: `
    $var: red;
  `,
}

const nextConfig = {
  sassOptions: {
    ...sassOptions,
    implementation: 'sass-embedded',
  },
}

module.exports = nextConfig
```

> **Good to know:**
>
> - `sassOptions` are not typed outside of `implementation` because Next.js does not maintain the other possible properties.
> - The `functions` property for defining custom Sass functions is only supported with webpack. When using Turbopack, custom Sass functions are not available because Turbopack's Rust-based architecture cannot directly execute JavaScript functions passed through this option.
