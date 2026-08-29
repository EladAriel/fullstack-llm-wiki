---
type: "Framework Learn Page"
framework: "Model Context Protocol"
source_repo: "https://github.com/modelcontextprotocol/modelcontextprotocol"
source_branch: "main"
source_path: "docs/extensions/client-matrix.mdx"
source_commit: "ca4ab3027f7c844cd3039c956438d72e8253f7f5"
source_commit_short: "ca4ab30"
source_commit_date: "2026-08-28T21:24:44-07:00"
generated_at: "2026-08-29T09:38:48.009528Z"
---
# Client Matrix

---
title: Extension Support Matrix
description: Which MCP clients implement which official extensions
---

{/* prettier-ignore-start */}

export const CHECK = () => (
  <span className="flex justify-center">
    <Icon icon="check" iconType="solid" size={18} className="text-green-500" />
  </span>
);

{/* prettier-ignore-end */}

This matrix shows which MCP clients support each [official extension](/extensions/overview). Extensions are always opt-in: a client only uses an extension if both client and server declare support in the `extensions` field of their [capabilities](/extensions/overview#negotiation).

<Note>

This list is maintained by the community. If you notice any inaccuracies or would like to add or update information, please [submit a pull request](https://github.com/modelcontextprotocol/modelcontextprotocol/pulls).

</Note>

## Extension overview

| Extension                                                                             | Identifier                                                 | Description                                                     |
| ------------------------------------------------------------------------------------- | ---------------------------------------------------------- | --------------------------------------------------------------- |
| [MCP Apps](/extensions/apps/overview)                                                 | `io.modelcontextprotocol/ui`                               | Interactive HTML interfaces rendered inline in the conversation |
| [OAuth Client Credentials](/extensions/auth/oauth-client-credentials)                 | `io.modelcontextprotocol/oauth-client-credentials`         | Machine-to-machine auth without interactive user login          |
| [Enterprise-Managed Authorization](/extensions/auth/enterprise-managed-authorization) | `io.modelcontextprotocol/enterprise-managed-authorization` | Centralized access control via enterprise IdP                   |

## Support matrix

| Client                                                                   | [MCP Apps](/extensions/apps/overview) | [OAuth Client Credentials](/extensions/auth/oauth-client-credentials) | [Enterprise Auth](/extensions/auth/enterprise-managed-authorization) |
| ------------------------------------------------------------------------ | :-----------------------------------: | :-------------------------------------------------------------------: | :------------------------------------------------------------------: |
| [Claude (web)](https://claude.ai)                                        |               <CHECK />               |                                                                       |                                                                      |
| [Claude Desktop](https://claude.ai/download)                             |               <CHECK />               |                                                                       |                                                                      |
| [VS Code GitHub Copilot](https://code.visualstudio.com/)                 |               <CHECK />               |                                                                       |                                                                      |
| [Microsoft 365 Copilot](https://www.microsoft.com/microsoft-365-copilot) |               <CHECK />               |                                                                       |                                                                      |
| [Goose](https://block.github.io/goose/)                                  |               <CHECK />               |                                                                       |                                                                      |
| [Postman](https://postman.com)                                           |               <CHECK />               |                                                                       |                                                                      |
| [MCPJam](https://www.mcpjam.com/)                                        |               <CHECK />               |                                                                       |                                                                      |
| [ChatGPT](https://chatgpt.com/)                                          |               <CHECK />               |                                                                       |                                                                      |
| [Cursor](https://cursor.com/)                                            |               <CHECK />               |                                                                       |                                                                      |
| [Archestra.AI](https://www.archestra.ai/)                                |               <CHECK />               |                                                                       |                              <CHECK />                               |
| [PostHog Code](https://posthog.com/code/)                                |               <CHECK />               |                                                                       |                                                                      |

<Note>

Auth extension support (OAuth Client Credentials and Enterprise-Managed Authorization) is tracked separately from the core MCP authorization features (DCR, CIMD). Check each extension's specification and the [ext-auth repository](https://github.com/modelcontextprotocol/ext-auth) for the latest implementation status.

</Note>

## Adding extension support to your client

If you're building an MCP client and want to implement extension support:

1. Review the extension specification (e.g., in the [ext-auth](https://github.com/modelcontextprotocol/ext-auth) or [ext-apps](https://github.com/modelcontextprotocol/ext-apps) repository)
2. Declare support in the `extensions` field of the `io.modelcontextprotocol/clientCapabilities` your client sends in each request's `_meta`, and read the server's `extensions` from its [`server/discover`](/specification/draft/server/discover) response
3. Implement the extension's protocol requirements
4. Submit a pull request to update this matrix

See [Extensions Overview](/extensions/overview#negotiation) for details on the capability negotiation mechanism.
