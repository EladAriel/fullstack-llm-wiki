---
type: "Framework Learn Page"
framework: "FastMCP"
source_repo: "https://github.com/PrefectHQ/fastmcp.git"
source_branch: "main"
source_path: "docs/python-sdk/fastmcp-utilities-logging.mdx"
source_commit: "44c0907dda78618f882b08de26e31c4428bd74b8"
source_commit_short: "44c0907"
source_commit_date: "2026-07-29T10:22:17-05:00"
generated_at: "2026-07-30T03:45:36.539178Z"
---
---
title: logging
sidebarTitle: logging
---

# `fastmcp.utilities.logging`


Logging utilities for FastMCP.

## Functions

### `get_logger` <sup><a href="https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/utilities/logging.py#L14" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
get_logger(name: str) -> logging.Logger
```


Get a logger nested under FastMCP namespace.

**Args:**
- `name`: the name of the logger, which will be prefixed with 'FastMCP.'

**Returns:**
- a configured logger instance


### `configure_logging` <sup><a href="https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/utilities/logging.py#L29" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
configure_logging(level: Literal['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'] | int = 'INFO', logger: logging.Logger | None = None, enable_rich_tracebacks: bool | None = None, **rich_kwargs: Any) -> None
```


Configure logging for FastMCP.

**Args:**
- `logger`: the logger to configure
- `level`: the log level to use
- `rich_kwargs`: the parameters to use for creating RichHandler


### `temporary_log_level` <sup><a href="https://github.com/PrefectHQ/fastmcp/blob/main/fastmcp_slim/fastmcp/utilities/logging.py#L117" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python
temporary_log_level(level: str | None, logger: logging.Logger | None = None, enable_rich_tracebacks: bool | None = None, **rich_kwargs: Any)
```


Context manager to temporarily set log level and restore it afterwards.

**Args:**
- `level`: The temporary log level to set (e.g., "DEBUG", "INFO")
- `logger`: Optional logger to configure (defaults to FastMCP logger)
- `enable_rich_tracebacks`: Whether to enable rich tracebacks
- `**rich_kwargs`: Additional parameters for RichHandler

