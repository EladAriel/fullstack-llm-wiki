---
type: "Framework Learn Page"
framework: "nextjs"
source_repo: "https://github.com/vercel/next.js/"
source_branch: "canary"
source_path: "docs/01-app/03-api-reference/05-config/01-next-config-js/supportsImmutableAssets.mdx"
source_commit: "dcf242a17b5d4622bbd9624db531a9d84177619f"
source_commit_short: "dcf242a1"
source_commit_date: "2026-07-25T10:16:19+02:00"
generated_at: "2026-07-25T11:50:53Z"
---

---
title: supportsImmutableAssets
description: Configure support for immutable static assets
---

> **Attention**: This option is primarily intended for [adapter](/docs/app/api-reference/adapters) authors.
> App developers should only set it when troubleshooting adapter-specific issues.
>
> **Enabling this feature when your provider or adapter does not support it can result in broken deployments.**

When skew protection is enabled, static asset requests include a deployment-specific query parameter, for example:

```plain
GET https://foo.com/_next/static/chunks/0d_ks0ow7ur6m.js?dpl=<unique-deployment-id>
```

One downside is that browsers have to download static assets again after each new deployment, even when those assets have not changed.

Immutable static assets allow the `?dpl` query parameter to be omitted for static assets that are guaranteed to be immutable and content-addressed by their filename. This lets browsers cache those assets indefinitely and allows unchanged static assets to be skipped when uploading files during subsequent deployments:

```plain
GET https://foo.com/_next/static/immutable/chunks/0d_ks0ow7ur6m.js
```

You can use this config option to opt out of immutable static assets when your adapter has enabled support for them. If your adapter has not enabled this feature, this option has no effect:

```js filename="next.config.js"
/** @type {import('next').NextConfig} */
const nextConfig = {
  supportsImmutableAssets: false,
}

module.exports = nextConfig
```

See [Supporting immutable static assets](/docs/app/api-reference/adapters/immutable-static-assets) for more information on how to support this feature in an adapter.

## Version History

| Version   | Changes                                    |
| --------- | ------------------------------------------ |
| `v16.3.0` | Added support for immutable static assets. |
