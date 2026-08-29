---
type: "Framework Learn Page"
framework: "Next.js"
source_repo: "https://github.com/vercel/next.js/"
source_branch: "canary"
source_path: "docs/01-app/03-api-reference/07-adapters/08-invoking-entrypoints.mdx"
source_commit: "33a5d542e519fe4e05c8c8c2c2845da9f741699b"
source_commit_short: "33a5d542"
source_commit_date: "2026-08-29T00:04:45-07:00"
generated_at: "2026-08-29T09:40:24.295844Z"
---
# 08 Invoking Entrypoints

---
title: Invoking Entrypoints
description: Invoke Node.js and Edge build entrypoints with adapter runtime context.
---

Build output entrypoints use a `handler(..., ctx)` interface, with runtime-specific request/response types.

## Node.js runtime (`runtime: 'nodejs'`)

Node.js entrypoints use the following interface:

```typescript
handler(
  req: IncomingMessage,
  res: ServerResponse,
  ctx: {
    waitUntil?: (promise: Promise<void>) => void
    requestMeta?: RequestMeta
  }
): Promise<void>
```

When invoking Node.js entrypoints directly, adapters can pass helpers directly on `requestMeta` instead of relying on internals. Some of the supported fields are `hostname`,
`revalidate`, and `render404`:

```ts
await handler(req, res, {
  requestMeta: {
    // Relative path from process.cwd() to the Next.js project directory.
    relativeProjectDir: '.',
    // Optional hostname used by route handlers when constructing absolute URLs.
    hostname: '127.0.0.1',
    // Optional internal revalidate function to avoid revalidating over the network
    revalidate: async ({ urlPath, headers, opts }) => {
      // platform-specific revalidate implementation
    },
    // Optional function to render the 404 page for pages router `notFound: true`
    render404: async (req, res, parsedUrl, setHeaders) => {
      // platform-specific 404 rendering implementation
    },
  },
})
```

Relevant files in the Next.js core:

- [`packages/next/src/build/templates/app-page.ts`](https://github.com/vercel/next.js/blob/canary/packages/next/src/build/templates/app-page.ts)
- [`packages/next/src/build/templates/app-route.ts`](https://github.com/vercel/next.js/blob/canary/packages/next/src/build/templates/app-route.ts)
- and [`packages/next/src/build/templates/pages-api.ts`](https://github.com/vercel/next.js/blob/canary/packages/next/src/build/templates/pages-api.ts)

## Edge runtime (`runtime: 'edge'`) (deprecated)

> The Edge Runtime is [deprecated](/docs/messages/edge-runtime-deprecated). New routes should use the Node.js runtime.

Edge entrypoints use the following interface:

```typescript
handler(
  request: Request,
  ctx: {
    waitUntil?: (prom: Promise<void>) => void
    signal?: AbortSignal
    requestMeta?: RequestMeta
  }
): Promise<Response>
```

The shape is aligned around `handler(..., ctx)`, but Node.js and Edge runtimes use different request/response primitives.

For outputs with `runtime: 'edge'`, Next.js also provides `output.edgeRuntime` with the canonical metadata needed to invoke the entrypoint:

```typescript
{
  modulePath: string // Absolute path to the module registered in the edge runtime
  entryKey: string // Canonical key used by the edge entry registry
  handlerExport: string // Export name to invoke, currently 'handler'
}
```

After your edge runtime loads and evaluates the chunks for `modulePath`, use `entryKey` to read the registered entry from the global edge entry registry (`globalThis._ENTRIES`), then invoke `handlerExport` from that entry:

```ts
const entry = await globalThis._ENTRIES[output.edgeRuntime.entryKey]
const handler = entry[output.edgeRuntime.handlerExport]
await handler(request, ctx)
```

Use `edgeRuntime` instead of deriving registry keys or handler names from filenames.

Relevant files in the Next.js core:

- [`packages/next/src/build/templates/edge-ssr.ts`](https://github.com/vercel/next.js/blob/canary/packages/next/src/build/templates/edge-ssr.ts)
- [`packages/next/src/build/templates/edge-app-route.ts`](https://github.com/vercel/next.js/blob/canary/packages/next/src/build/templates/edge-app-route.ts)
- [`packages/next/src/build/templates/pages-edge-api.ts`](https://github.com/vercel/next.js/blob/canary/packages/next/src/build/templates/pages-edge-api.ts)
- and [`packages/next/src/build/templates/middleware.ts`](https://github.com/vercel/next.js/blob/canary/packages/next/src/build/templates/middleware.ts)
