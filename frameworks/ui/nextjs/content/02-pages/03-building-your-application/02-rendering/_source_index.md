---
type: "Framework Learn Page"
framework: "Next.js"
source_repo: "https://github.com/vercel/next.js/"
source_branch: "canary"
source_path: "docs/02-pages/03-building-your-application/02-rendering/index.mdx"
source_commit: "33a5d542e519fe4e05c8c8c2c2845da9f741699b"
source_commit_short: "33a5d542"
source_commit_date: "2026-08-29T00:04:45-07:00"
generated_at: "2026-08-29T09:40:24.324394Z"
---
# Index

---
title: Rendering
description: Learn the fundamentals of rendering in React and Next.js.
---

By default, Next.js **prerenders** every page. This means that Next.js generates HTML for each page in advance, instead of having it all done by client-side JavaScript. Prerendering can result in better performance and SEO.

Each generated HTML is associated with minimal JavaScript code necessary for that page. When a page is loaded by the browser, its JavaScript code runs and makes the page fully interactive (this process is called [hydration](https://react.dev/reference/react-dom/client/hydrateRoot) in React).

### Prerendering

Next.js has two forms of prerendering: **Static Generation** and **Server-side Rendering**. The difference is in **when** it generates the HTML for a page.

- Static Generation: The HTML is generated at **build time** and will be reused on each request.
- Server-side Rendering: The HTML is generated on **each request**.

Importantly, Next.js lets you choose which prerendering form you'd like to use for each page. You can create a "hybrid" Next.js app by using Static Generation for most pages and using Server-side Rendering for others.

We recommend using Static Generation over Server-side Rendering for performance reasons. Statically generated pages can be cached by CDN with no extra configuration to boost performance. However, in some cases, Server-side Rendering might be the only option.

You can also use client-side data fetching along with Static Generation or Server-side Rendering. That means some parts of a page can be rendered entirely by clientside JavaScript. To learn more, take a look at the [Data Fetching](/docs/pages/building-your-application/data-fetching/client-side) documentation.
