---
type: "Framework Learn Page"
framework: "nextjs"
source_repo: "https://github.com/vercel/next.js/"
source_branch: "canary"
source_path: "docs/01-app/03-api-reference/05-config/01-next-config-js/adapterPath.mdx"
source_commit: "79142d7806ff4194c8d9885b80fa69db5ecf534a"
source_commit_short: "79142d78"
source_commit_date: "2026-06-20T23:40:12Z"
generated_at: "2026-06-21T12:07:17Z"
---

---
title: adapterPath
description: Configure a custom adapter for Next.js to hook into the build process.
---

Next.js provides a built-in adapters API. It allows deployment platforms or build systems to integrate with the Next.js build process.

For a full reference implementation, see the [`nextjs/adapter-vercel`](https://github.com/nextjs/adapter-vercel) adapter.

## Configuration

To use an adapter, specify the path to your adapter module in `adapterPath`:

```js filename="next.config.js"
/** @type {import('next').NextConfig} */
const nextConfig = {
  adapterPath: require.resolve('./my-adapter.js'),
}

module.exports = nextConfig
```

Alternatively `NEXT_ADAPTER_PATH` can be set to enable zero-config usage in deployment platforms.

## Adapters

For full adapter implementation details, use the dedicated Adapters section:

- [Configuration](/docs/app/api-reference/adapters/configuration)
- [Creating an Adapter](/docs/app/api-reference/adapters/creating-an-adapter)
- [API Reference](/docs/app/api-reference/adapters/api-reference)
- [Testing Adapters](/docs/app/api-reference/adapters/testing-adapters)
- [Routing with `@next/routing`](/docs/app/api-reference/adapters/routing-with-next-routing)
- [Implementing PPR in an Adapter](/docs/app/api-reference/adapters/implementing-ppr-in-an-adapter)
- [Runtime Integration](/docs/app/api-reference/adapters/runtime-integration)
- [Invoking Entrypoints](/docs/app/api-reference/adapters/invoking-entrypoints)
- [Output Types](/docs/app/api-reference/adapters/output-types)
- [Routing Information](/docs/app/api-reference/adapters/routing-information)
- [Use Cases](/docs/app/api-reference/adapters/use-cases)

## Creating an Adapter

See [Creating an Adapter](/docs/app/api-reference/adapters/creating-an-adapter).

## API Reference

See [API Reference](/docs/app/api-reference/adapters/api-reference).

## Testing Adapters

See [Testing Adapters](/docs/app/api-reference/adapters/testing-adapters).

## Routing with `@next/routing`

See [Routing with `@next/routing`](/docs/app/api-reference/adapters/routing-with-next-routing).

## Implementing PPR in an Adapter

See [Implementing PPR in an Adapter](/docs/app/api-reference/adapters/implementing-ppr-in-an-adapter).

## Runtime Integration

See [Runtime Integration](/docs/app/api-reference/adapters/runtime-integration).

## Invoking Entrypoints

See [Invoking Entrypoints](/docs/app/api-reference/adapters/invoking-entrypoints).

## Output Types

See [Output Types](/docs/app/api-reference/adapters/output-types).

## Routing Information

See [Routing Information](/docs/app/api-reference/adapters/routing-information).

## Use Cases

See [Use Cases](/docs/app/api-reference/adapters/use-cases).
