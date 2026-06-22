---
type: "Framework Learn Page"
framework: "nextjs"
source_repo: "https://github.com/vercel/next.js/"
source_branch: "canary"
source_path: "docs/01-app/03-api-reference/03-file-conventions/src-folder.mdx"
source_commit: "79142d7806ff4194c8d9885b80fa69db5ecf534a"
source_commit_short: "79142d78"
source_commit_date: "2026-06-20T23:40:12Z"
generated_at: "2026-06-21T12:07:17Z"
---

---
title: src Folder
nav_title: src
description: Save pages under the `src` folder as an alternative to the root `pages` directory.
related:
  links:
    - app/getting-started/project-structure
---

{/* The content of this doc is shared between the app and pages router. You can use the `<PagesOnly>Content</PagesOnly>` component to add content that is specific to the Pages Router. Any shared content should not be wrapped in a component. */}

As an alternative to having the special Next.js `app` or `pages` directories in the root of your project, Next.js also supports the common pattern of placing application code under the `src` folder.

This separates application code from project configuration files which mostly live in the root of a project, which is preferred by some individuals and teams.

To use the `src` folder, move the `app` Router folder or `pages` Router folder to `src/app` or `src/pages` respectively.

<Image
  alt="An example folder structure with the `src` folder"
  srcLight="/docs/light/project-organization-src-directory.png"
  srcDark="/docs/dark/project-organization-src-directory.png"
  width="1600"
  height="687"
/>

> **Good to know**:
>
> - The `/public` directory should remain in the root of your project.
> - Config files like `package.json`, `next.config.js` and `tsconfig.json` should remain in the root of your project.
> - `.env.*` files should remain in the root of your project.
> - `src/app` or `src/pages` will be ignored if `app` or `pages` are present in the root directory.
> - If you're using `src`, you'll probably also move other application folders such as `/components` or `/lib`.
> - If you're using Proxy, ensure it is placed inside the `src` folder.
> - If you're using Tailwind CSS, you'll need to add the `/src` prefix to the `tailwind.config.js` file in the [content section](https://tailwindcss.com/docs/content-configuration).
> - If you are using TypeScript paths for imports such as `@/*`, you should update the `paths` object in `tsconfig.json` to include `src/`.
