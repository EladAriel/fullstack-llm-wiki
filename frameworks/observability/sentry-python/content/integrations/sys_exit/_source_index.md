---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/integrations/sys_exit/index.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.062051Z"
---
# Index

---
title: sys.exit
description: Learn how to use Sentry to capture sys.exit calls.
---

The `SysExitIntegration` records `sys.exit` calls by capturing the `SystemExit` exception raised by `sys.exit`.

## Install

```bash {tabTitle:pip}
pip install "sentry-sdk"
```
```bash {tabTitle:uv}
uv add "sentry-sdk"
```

## Configure

The `SysExitIntegration` is disabled by default, and the SDK only captures `SystemExit` exceptions automatically if this integration is manually enabled.

A `sys.exit` call is considered "successful" when the function is passed a value of `0` or `None`. Passing any other value results in an "unsuccessful" exit.

To enable the `SysExitIntegration` and configure it to only capture unsuccessful `sys.exit` calls, use the following:

<SignInNote />

```python
import sentry_sdk
from sentry_sdk.integrations.sys_exit import SysExitIntegration

sentry_sdk.init(
    dsn="___PUBLIC_DSN___",
    # Add data like request headers and IP for users, if applicable;
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
    integrations=[SysExitIntegration()],
)
```

If you wish to capture successful and unsuccessful `sys.exit` calls, use the following, instead:

```python
import sentry_sdk
from sentry_sdk.integrations.sys_exit import SysExitIntegration

sentry_sdk.init(
    dsn="___PUBLIC_DSN___",
    integrations=[SysExitIntegration(capture_successful_exits=True)],
)
```



## Verify

Running the following snippet should result in a `SystemExit` exception being reported to Sentry.

```python
import sys

import sentry_sdk
from sentry_sdk.integrations.sys_exit import SysExitIntegration

sentry_sdk.init(
    dsn="___PUBLIC_DSN___",
    integrations=[SysExitIntegration()],
)

sys.exit(1)
```

If you use `capture_successful_exits=True`, calling `sys.exit(0)` should also report a `SystemExit` exception to Sentry.


<Alert title="Manually-raised SystemExit">

Please note that the `SysExitIntegration` only captures `SystemExit` exceptions which are raised by calling `sys.exit`. If your code raises `SystemExit` without calling `sys.exit`, the exception will not be reported to Sentry.

</Alert>
