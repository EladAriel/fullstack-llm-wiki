---
type: "Framework Learn Page"
framework: "Sentry Python"
source_repo: "https://github.com/getsentry/sentry-docs.git"
source_branch: "master"
source_path: "docs/platforms/python/legacy-sdk/transports.mdx"
source_commit: "8b4e4a23b18ee70f5fdb05bcda48869c10be2f60"
source_commit_short: "8b4e4a2"
source_commit_date: "2026-08-28T22:17:56+00:00"
generated_at: "2026-08-29T09:40:09.039540Z"
---
# Transports

---
draft: true
categories: []
toc: true
title: Transports
noindex: true
tags: []
---

<Alert level="warning" title="Deprecation Warning">

A new Python SDK has superseded this deprecated version. Sentry preserves this documentation for customers using the old client. We recommend using the [updated Python SDK](/platforms/python/) for new projects.

</Alert>

A transport is the mechanism in which Raven sends the HTTP request to the Sentry server. By default, Raven uses a threaded asynchronous transport, but you can easily adjust this by passing your own transport class.

The transport class is passed via the `transport` parameter on `Client`:

```python
from raven import Client

Client('...', transport=TransportClass)
```

Options are passed to transports via the querystring.

All transports should support at least the following options:

`timeout = 1`

The time to wait for a response from the server, in seconds.

`verify_ssl = 1`

If the connection is HTTPS, validate the certificate and hostname.

`ca_certs = [raven]/data/cacert.pem`

A certificate bundle to use when validating SSL connections.

For example, to increase the timeout and to disable SSL verification:

```python
SENTRY_DSN = '___DSN___?timeout=5&verify_ssl=0'
```

## Eventlet

Should only be used within an Eventlet IO loop.

```python
from raven.transport.eventlet import EventletHTTPTransport

Client('...', transport=EventletHTTPTransport)
```

## Gevent

Should only be used within a Gevent IO loop.

```python
from raven.transport.gevent import GeventedHTTPTransport

Client('...', transport=GeventedHTTPTransport)
```

## Requests

Requires the `requests` library. Synchronous.

```python
from raven.transport.requests import RequestsHTTPTransport

Client('...', transport=RequestsHTTPTransport)
```

Alternatively, a threaded client also exists for Requests:

```python
from raven.transport.threaded_requests import ThreadedRequestsHTTPTransport

Client('...', transport=ThreadedRequestsHTTPTransport)
```

## Sync

A synchronous blocking transport.

```python
from raven.transport.http import HTTPTransport

Client('...', transport=HTTPTransport)
```

## Threaded (Default)

Spawns an async worker for processing messages.

```python
from raven.transport.threaded import ThreadedHTTPTransport

Client('...', transport=ThreadedHTTPTransport)
```

## Tornado

Should only be used within a Tornado IO loop.

```python
from raven.transport.tornado import TornadoHTTPTransport

Client('...', transport=TornadoHTTPTransport)
```

## Twisted

Should only be used within a Twisted event loop.

```python
from raven.transport.twisted import TwistedHTTPTransport

Client('...', transport=TwistedHTTPTransport)
```
