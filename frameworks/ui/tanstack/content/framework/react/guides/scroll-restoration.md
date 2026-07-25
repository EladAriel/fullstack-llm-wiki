---
type: "Framework Learn Page"
framework: "tanstack"
source_repo: "https://github.com/tanstack/query"
source_branch: "main"
source_path: "docs/framework/react/guides/scroll-restoration.md"
source_commit: "fd50fa14d283c7d6664a796f758498d1ad5bfce7"
source_commit_short: "fd50fa14"
source_commit_date: "2026-07-24T22:22:47+10:00"
generated_at: "2026-07-25T11:50:41Z"
---

---
id: scroll-restoration
title: Scroll Restoration
---

Traditionally, when you navigate to a previously visited page on a web browser, you would find that the page would be scrolled to the exact position where you were before you navigated away from that page. This is called **scroll restoration** and has been in a bit of a regression since web applications have started moving towards client side data fetching. With TanStack Query however, that's no longer the case.

TanStack Query doesn’t implement scroll restoration by itself, but it removes one of the biggest causes of broken restoration in SPA’s: refetch-induced UI resets. By keeping previously fetched data in cache (and optionally using `placeholderData`), navigation back to a page can render instantly with stable layout, making scroll restoration reliable when handled by the router (e.g. React Router’s ScrollRestoration, TanStack Router’s scroll restoration, or a small custom history-based solution).

Out of the box, "scroll restoration" for all queries (including paginated and infinite queries) Just Works™️ in TanStack Query. The reason for this is that query results are cached and able to be retrieved synchronously when a query is rendered. As long as your queries are being cached long enough (the default time is 5 minutes) and have not been garbage collected, scroll restoration will work out of the box all the time.
