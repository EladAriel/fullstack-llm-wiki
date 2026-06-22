---
type: "Framework Learn Page"
framework: "nextjs"
source_repo: "https://github.com/vercel/next.js/"
source_branch: "canary"
source_path: "docs/01-app/03-api-reference/05-config/01-next-config-js/pageExtensions.mdx"
source_commit: "79142d7806ff4194c8d9885b80fa69db5ecf534a"
source_commit_short: "79142d78"
source_commit_date: "2026-06-20T23:40:12Z"
generated_at: "2026-06-21T12:07:17Z"
---

---
title: pageExtensions
description: Extend the default page extensions used by Next.js when resolving pages in the Pages Router.
---

{/* The content of this doc is shared between the app and pages router. You can use the `<PagesOnly>Content</PagesOnly>` component to add content that is specific to the Pages Router. Any shared content should not be wrapped in a component. */}

<AppOnly>

By default, Next.js accepts files with the following extensions: `.tsx`, `.ts`, `.jsx`, `.js`. This can be modified to allow other extensions like markdown (`.md`, `.mdx`).

```js filename="next.config.js"
const withMDX = require('@next/mdx')()

/** @type {import('next').NextConfig} */
const nextConfig = {
  pageExtensions: ['js', 'jsx', 'ts', 'tsx', 'md', 'mdx'],
}

module.exports = withMDX(nextConfig)
```

</AppOnly>

<PagesOnly>

You can extend the default Page extensions (`.tsx`, `.ts`, `.jsx`, `.js`) used by Next.js. Inside `next.config.js`, add the `pageExtensions` config:

```js filename="next.config.js"
module.exports = {
  pageExtensions: ['mdx', 'md', 'jsx', 'js', 'tsx', 'ts'],
}
```

Changing these values affects _all_ Next.js pages, including the following:

- [`proxy.js`](/docs/pages/api-reference/file-conventions/proxy)
- [`instrumentation.js`](/docs/pages/guides/instrumentation)
- `pages/_document.js`
- `pages/_app.js`
- `pages/api/`

For example, if you reconfigure `.ts` page extensions to `.page.ts`, you would need to rename pages like `proxy.page.ts`, `instrumentation.page.ts`, `_app.page.ts`.

## Including non-page files in the `pages` directory

You can colocate test files or other files used by components in the `pages` directory. Inside `next.config.js`, add the `pageExtensions` config:

```js filename="next.config.js"
module.exports = {
  pageExtensions: ['page.tsx', 'page.ts', 'page.jsx', 'page.js'],
}
```

Then, rename your pages to have a file extension that includes `.page` (e.g. rename `MyPage.tsx` to `MyPage.page.tsx`). Ensure you rename _all_ Next.js pages, including the files mentioned above.

</PagesOnly>
