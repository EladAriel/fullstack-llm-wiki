---
type: "Framework Learn Page"
framework: "nextjs"
source_repo: "https://github.com/vercel/next.js/"
source_branch: "canary"
source_path: "docs/01-app/03-api-reference/04-functions/generate-sitemaps.mdx"
source_commit: "79142d7806ff4194c8d9885b80fa69db5ecf534a"
source_commit_short: "79142d78"
source_commit_date: "2026-06-20T23:40:12Z"
generated_at: "2026-06-21T12:07:17Z"
---

---
title: generateSitemaps
nav_title: generateSitemaps
description: Learn how to use the generateSiteMaps function to create multiple sitemaps for your application.
related:
  title: Next Steps
  description: Learn how to create sitemaps for your Next.js application.
  links:
    - app/api-reference/file-conventions/metadata/sitemap
---

You can use the `generateSitemaps` function to generate multiple sitemaps for your application.

## Returns

The `generateSitemaps` returns an array of objects with an `id` property.

## URLs

Your generated sitemaps will be available at `/.../sitemap/[id].xml`. For example, `/product/sitemap/1.xml`.

## Example

For example, to split a sitemap using `generateSitemaps`, return an array of objects with the sitemap `id`. Then, use the `id` to generate the unique sitemaps.

```ts filename="app/product/sitemap.ts" switcher
import type { MetadataRoute } from 'next'
import { BASE_URL } from '@/app/lib/constants'

export async function generateSitemaps() {
  // Fetch the total number of products and calculate the number of sitemaps needed
  return [{ id: 0 }, { id: 1 }, { id: 2 }, { id: 3 }]
}

export default async function sitemap(props: {
  id: Promise<string>
}): Promise<MetadataRoute.Sitemap> {
  const id = await props.id
  // Google's limit is 50,000 URLs per sitemap
  const start = id * 50000
  const end = start + 50000
  const products = await getProducts(
    `SELECT id, date FROM products WHERE id BETWEEN ${start} AND ${end}`
  )
  return products.map((product) => ({
    url: `${BASE_URL}/product/${product.id}`,
    lastModified: product.date,
  }))
}
```

```js filename="app/product/sitemap.js" switcher
import { BASE_URL } from '@/app/lib/constants'

export async function generateSitemaps() {
  // Fetch the total number of products and calculate the number of sitemaps needed
  return [{ id: 0 }, { id: 1 }, { id: 2 }, { id: 3 }]
}

export default async function sitemap(props) {
  const id = await props.id
  // Google's limit is 50,000 URLs per sitemap
  const start = id * 50000
  const end = start + 50000
  const products = await getProducts(
    `SELECT id, date FROM products WHERE id BETWEEN ${start} AND ${end}`
  )
  return products.map((product) => ({
    url: `${BASE_URL}/product/${product.id}`,
    lastModified: product.date,
  }))
}
```

## Version History

| Version   | Changes                                                                                                                                              |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `v16.0.0` | The `id` values returned from `generateSitemaps` are now passed as a promise that resolves to a `string` to the sitemap function.                    |
| `v15.0.0` | `generateSitemaps` now generates consistent URLs between development and production                                                                  |
| `v13.3.2` | `generateSitemaps` introduced. In development, you can view the generated sitemap on `/.../sitemap.xml/[id]`. For example, `/product/sitemap.xml/1`. |
