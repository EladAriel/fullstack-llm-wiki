---
type: "Framework Learn Page"
framework: "FastMCP"
source_repo: "https://github.com/PrefectHQ/fastmcp.git"
source_branch: "main"
source_path: "docs/patterns/contrib.mdx"
source_commit: "44c0907dda78618f882b08de26e31c4428bd74b8"
source_commit_short: "44c0907"
source_commit_date: "2026-07-29T10:22:17-05:00"
generated_at: "2026-07-30T03:45:36.568535Z"
---
# Contrib

---
title: "Contrib Modules"
description: "Community-contributed modules extending FastMCP"
icon: "cubes"
---

import { VersionBadge } from "/snippets/version-badge.mdx"

<VersionBadge version="2.2.1" />

FastMCP includes a `contrib` package that holds community-contributed modules. These modules extend FastMCP's functionality but aren't officially maintained by the core team.

Contrib modules provide additional features, integrations, or patterns that complement the core FastMCP library. They offer a way for the community to share useful extensions while keeping the core library focused and maintainable.

The available modules can be viewed in the [contrib directory](https://github.com/PrefectHQ/fastmcp/tree/main/fastmcp_slim/fastmcp/contrib).

## Usage

To use a contrib module, import it from the `fastmcp.contrib` package:

```python test="skip"
from fastmcp.contrib import my_module
```

## Important Considerations

- **Stability**: Modules in `contrib` may have different testing requirements or stability guarantees compared to the core library.
- **Compatibility**: Changes to core FastMCP might break modules in `contrib` without explicit warnings in the main changelog.
- **Dependencies**: Contrib modules may have additional dependencies not required by the core library. These dependencies are typically documented in the module's README or separate requirements files.

## Contributing

Contrib modules are accepted selectively. Before opening a PR, first open an issue with the problem, intended maintenance model, and why the pattern belongs in-repo instead of a standalone package. If maintainers agree it belongs in `contrib`, prepare the module with:

1. Create a new directory in `fastmcp_slim/fastmcp/contrib/` for your module
2. Add proper tests for your module in `tests/contrib/`
3. Include comprehensive documentation in a README.md file, including usage and examples, as well as any additional dependencies or installation instructions
4. Submit a focused pull request linked to the maintainer-approved issue

The ideal contrib module:
- Solves a specific use case or integration need
- Follows FastMCP coding standards
- Includes thorough documentation and examples
- Has comprehensive tests
- Specifies any additional dependencies
