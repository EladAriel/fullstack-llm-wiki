---
type: "Framework Learn Page"
framework: "Next.js"
source_repo: "https://github.com/vercel/next.js/"
source_branch: "canary"
source_path: "docs/01-app/01-getting-started/18-upgrading.mdx"
source_commit: "33a5d542e519fe4e05c8c8c2c2845da9f741699b"
source_commit_short: "33a5d542"
source_commit_date: "2026-08-29T00:04:45-07:00"
generated_at: "2026-08-29T09:40:24.263047Z"
---
# 18 Upgrading

---
title: Upgrading
description: Learn how to upgrade your Next.js application to the latest version or canary.
related:
  title: Version guides
  description: See the version guides for in-depth upgrade instructions.
  links:
    - app/guides/upgrading/version-16
    - app/guides/upgrading/version-15
    - app/guides/upgrading/version-14
---

## Latest version

To update to the latest version of Next.js, you can use the `upgrade` command:

```bash package="pnpm"
pnpm next upgrade
```

```bash package="npm"
npx next upgrade
```

```bash package="yarn"
yarn next upgrade
```

```bash package="bun"
bunx next upgrade
```

Versions before Next.js 16.1.0 do not support the `upgrade` command and need to use a separate package instead:

```bash filename="Terminal"
npx @next/codemod@canary upgrade latest
```

If you prefer to upgrade manually, install the latest Next.js and React versions:

```bash package="pnpm"
pnpm i next@latest react@latest react-dom@latest eslint-config-next@latest
```

```bash package="npm"
npm i next@latest react@latest react-dom@latest eslint-config-next@latest
```

```bash package="yarn"
yarn add next@latest react@latest react-dom@latest eslint-config-next@latest
```

```bash package="bun"
bun add next@latest react@latest react-dom@latest eslint-config-next@latest
```

## Canary version

To update to the latest canary, make sure you're on the latest version of Next.js and everything is working as expected. Then, run the following command:

```bash package="pnpm"
pnpm add next@canary
```

```bash package="npm"
npm i next@canary
```

```bash package="yarn"
yarn add next@canary
```

```bash package="bun"
bun add next@canary
```

### Features available in canary

The following features are currently available in canary:

**Authentication**:

- [`forbidden`](/docs/app/api-reference/functions/forbidden)
- [`unauthorized`](/docs/app/api-reference/functions/unauthorized)
- [`forbidden.js`](/docs/app/api-reference/file-conventions/forbidden)
- [`unauthorized.js`](/docs/app/api-reference/file-conventions/unauthorized)
- [`authInterrupts`](/docs/app/api-reference/config/next-config-js/authInterrupts)
