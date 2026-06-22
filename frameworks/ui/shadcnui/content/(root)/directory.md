---
type: "Framework Learn Page"
framework: "shadcnui"
source_repo: "https://github.com/shadcn-ui/ui"
source_branch: "main"
source_path: "apps/v4/content/docs/(root)/directory.mdx"
source_commit: "5602b81d8344e0d0d7178e3bf57612662cd42957"
source_commit_short: "5602b81d"
source_commit_date: "2026-06-21T15:49:35+04:00"
generated_at: "2026-06-21T12:47:26Z"
---

---
title: Registry Directory
description: Discover community registries for shadcn/ui components and blocks.
---

These registries are built into the CLI with no additional configuration required. To add a component, run: `npx shadcn add @<registry>/<component>`.

<Callout className="bg-muted font-semibold">
  Community registries are maintained by third-party developers. Always review
  code on installation to ensure it meets your security and quality standards.
</Callout>

Don't see a registry? Learn how to [add it here](/docs/registry/registry-index).

<DirectoryList />

## Documentation

You can use the `shadcn` CLI to run your own code registry. Running your own registry allows you to distribute your custom components, hooks, pages, config, rules and other files to any project.

<div className="mt-6 grid gap-4 sm:grid-cols-2">
  <LinkedCard href="/docs/registry/getting-started" className="items-start text-sm md:p-6">
    <div className="font-medium">Getting Started</div>
    <div className="text-muted-foreground">
      Set up and build your own registry
    </div>
  </LinkedCard>

<LinkedCard
  href="/docs/registry/authentication"
  className="items-start text-sm md:p-6"
>
  <div className="font-medium">Authentication</div>
  <div className="text-muted-foreground">
    Secure your registry with authentication
  </div>
</LinkedCard>
<LinkedCard
  href="/docs/registry/namespace"
  className="items-start text-sm md:p-6"
>
  <div className="font-medium">Namespaces</div>
  <div className="text-muted-foreground">
    Configure registries with namespaces
  </div>
</LinkedCard>
<LinkedCard
  href="/docs/registry/registry-index"
  className="items-start text-sm md:p-6"
>
  <div className="font-medium">Add a Registry</div>
  <div className="text-muted-foreground">
    Learn how to add a registry to the directory
  </div>
</LinkedCard>
<LinkedCard
  href="/docs/registry/examples"
  className="items-start text-sm md:p-6"
>
  <div className="font-medium">Examples</div>
  <div className="text-muted-foreground">
    Registry item examples and configurations
  </div>
</LinkedCard>
  <LinkedCard
    href="/docs/registry/registry-json"
    className="items-start text-sm md:p-6"
  >
    <div className="font-medium">Schema</div>
    <div className="text-muted-foreground">
      Schema specification for registry.json
    </div>
  </LinkedCard>
</div>
