---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/integrations/django/http_errors.mdx"
source_commit: "8557ccbd46b02c43301ef74ff54516736ecf9d69"
source_commit_short: "8557ccb"
source_commit_date: "2026-07-24T13:12:02-04:00"
generated_at: "2026-07-25T19:08:13.523971Z"
---
---
title: Reporting HTTP Errors
sidebar_order: 100
description: "Learn about reporting HTTP errors with Django."
---

If you want to report `404 Not Found` and other errors besides uncaught exceptions (`500 Internal Server Error`) to Sentry, you can write your own Django view for those status codes. For example:

```python
# urls.py
handler404 = 'mysite.views.my_custom_page_not_found_view'

# views.py
import sentry_sdk
from django.http import HttpResponseNotFound

def my_custom_page_not_found_view(*args, **kwargs):
    sentry_sdk.capture_message("Page not found!", level="error")

    # return any response here, e.g.:
    return HttpResponseNotFound("Not found")
```

The error message you send to Sentry will have the usual request data attached.

For details about `capture_message()`, see the [API Documentation](https://getsentry.github.io/sentry-python/api.html#sentry_sdk.api.capture_message).

Refer to [Customizing Error Views](https://docs.djangoproject.com/en/3.0/topics/http/views/#customizing-error-views) from the Django documentation for more information. You can also view our <PlatformLink to="/troubleshooting/">troubleshooting information</PlatformLink>.
