---
type: "Framework Learn Page"
framework: "shadcnui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/changelog/2026-07-typeset.mdx"
source_commit: "4baadbc6517070ae8f8feb2c97037adc2b305544"
source_commit_short: "4baadbc6"
source_commit_date: "2026-07-23T23:50:36+04:00"
generated_at: "2026-07-25T11:50:48Z"
---

---
title: July 2026 - Introducing shadcn/typeset
description: A complete typography system for HTML, from blog posts to streaming chat. One CSS file you own.
date: 2026-07-10
---

Today we're releasing **shadcn/typeset**: a styling system for HTML and rendered markdown, in one CSS file.

Your app renders the same HTML elements everywhere: headings, paragraphs, lists, tables, and code. You style them for your blog, then your docs, and now chat. Typeset lets you style them once, then tune the rhythm for each context.

```tsx
<div className="typeset">{content}</div>
```

Add one class and everything inside gets styled. Typeset follows the size of its container, uses your theme, and gives you three controls: size, leading, and flow.

You can create as many typesets as you need. Use a tighter rhythm for chat and a roomier one for docs:

```css
.typeset-chat {
  --typeset-leading: 1.6;
  --typeset-flow: 1em;
}

.typeset-docs {
  --typeset-size: 15px;
  --typeset-leading: 1.75;
  --typeset-flow: 1.5em;
}
```

```tsx
<div className="typeset typeset-chat">{message}</div>
<article className="typeset typeset-docs">{page}</article>
```

It's also designed for streaming, so new blocks don't restyle earlier ones. The file lives in your project. There's no package or config layer to work around.

Open the [typeset builder](/typeset) to create yours, or read the [Typeset docs](/docs/typeset) for the full guide.

<div className="flex gap-2">
  <Button asChild size="sm">
    <Link href="/typeset" className="mt-6 no-underline!">
      Build your typeset
    </Link>
  </Button>
  <Button asChild size="sm" variant="outline">
    <Link href="/docs/typeset" className="mt-6 no-underline!">
      Read the docs
    </Link>
  </Button>
</div>
