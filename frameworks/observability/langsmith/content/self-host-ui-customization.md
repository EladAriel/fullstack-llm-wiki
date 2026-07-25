---
type: "Framework Learn Page"
framework: "LangSmith"
source_repo: "https://github.com/langchain-ai/docs.git"
source_branch: "main"
source_path: "src/langsmith/self-host-ui-customization.mdx"
source_commit: "2aae1dfc98ee953a9a5185fb6fcdd9efb3f4d878"
source_commit_short: "2aae1df"
source_commit_date: "2026-07-25T00:27:23+00:00"
generated_at: "2026-07-25T19:08:33.424658Z"
---
# Self Host Ui Customization

---
title: Customize the error support message
sidebarTitle: Customize the UI
description: Customize support contact information in the LangSmith frontend for self-hosted deployments.
---

## Custom error support message

By default, error messages in LangSmith direct users to the [Support Portal](https://support.langchain.com). You can replace this with your own support contact information.

When set, all error and support messages throughout the UI will display your custom text instead of the default LangChain support email.

<Note>
The custom message is rendered as **plain text** only. HTML tags will not be interpreted and will display as literal text.
</Note>

```yaml Helm
config:
  customErrorSupportMessage: "For help, contact your internal IT team at helpdesk@example.com"
```

To revert to the default behavior, remove the setting or set it to an empty string.
