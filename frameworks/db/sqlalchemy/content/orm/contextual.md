---
type: "Framework Learn Page"
framework: "sqlalchemy"
source_repo: "https://github.com/sqlalchemy/sqlalchemy"
source_branch: "main"
source_path: "doc/build/orm/contextual.rst"
source_commit: "ddf3b6589fd6ccb2affbaea5d4f400a8c1ad02d8"
source_commit_short: "ddf3b658"
source_commit_date: "2026-06-18T14:12:36-04:00"
generated_at: "2026-06-21T07:22:30Z"
---

# Contextual/Thread-local Sessions

Recall from the section `session_faq_whentocreate`, the concept of "session scopes" was introduced, with an emphasis on web applications and the practice of linking the scope of a `.Session` with that of a web request.   Most modern web frameworks include integration tools so that the scope of the `.Session` can be managed automatically, and these tools should be used as they are available.

SQLAlchemy includes its own helper object, which helps with the establishment of user-defined `.Session` scopes.  It is also used by third-party integration systems to help construct their integration schemes.

The object is the `.scoped_session` object, and it represents a **registry** of `.Session` objects.  If you're not familiar with the registry pattern, a good introduction can be found in [Patterns of Enterprise Architecture](https://martinfowler.com/eaaCatalog/registry.html).

> **Warning:**  The `.scoped_session` registry by default uses a Python
 `threading.local()`
 in order to track `_orm.Session` instances.   **This is not
 necessarily compatible with all application servers**, particularly those
 which make use of greenlets or other alternative forms of concurrency
 control, which may lead to race conditions (e.g. randomly occurring
 failures) when used in moderate to high concurrency scenarios.
 Please read `unitofwork_contextual_threadlocal` and
 `session_lifespan` below to more fully understand the implications
 of using `threading.local() to track orm.Session` objects
 and consider more explicit means of scoping when using application servers
 which are not based on traditional threads.

> **Note:** The `.scoped_session` object is a very popular and useful object
used by many SQLAlchemy applications.  However, it is important to note
that it presents **only one approach** to the issue of `.Session`
management.  If you're new to SQLAlchemy, and especially if the
term "thread-local variable" seems strange to you, we recommend that
if possible you familiarize first with an off-the-shelf integration
system such as [Flask-SQLAlchemy](https://pypi.org/project/Flask-SQLAlchemy/)
or [zope.sqlalchemy](https://pypi.org/project/zope.sqlalchemy).

A `.scoped_session` is constructed by calling it, passing it a **factory** which can create new `.Session` objects.   A factory is just something that produces a new object when called, and in the case of `.Session`, the most common factory is the `.sessionmaker`, introduced earlier in this section.  Below we illustrate this usage:

```
>>> from sqlalchemy.orm import scoped_session
>>> from sqlalchemy.orm import sessionmaker

>>> session_factory = sessionmaker(bind=some_engine)
>>> Session = scoped_session(session_factory)
```

The `.scoped_session` object we've created will now call upon the `.sessionmaker` when we "call" the registry:

```
>>> some_session = Session()
```

Above, `some_session` is an instance of `.Session`, which we can now use to talk to the database.   This same `.Session` is also present within the `.scoped_session` registry we've created.   If we call upon the registry a second time, we get back the **same** `.Session`:

```
>>> some_other_session = Session()
>>> some_session is some_other_session
True
```

This pattern allows disparate sections of the application to call upon a global `.scoped_session`, so that all those areas may share the same session without the need to pass it explicitly.   The `.Session` we've established in our registry will remain, until we explicitly tell our registry to dispose of it, by calling `.scoped_session.remove`:

```
>>> Session.remove()
```

The `.scoped_session.remove` method first calls `.Session.close` on the current `.Session`, which has the effect of releasing any connection/transactional resources owned by the `.Session` first, then discarding the `.Session` itself.  "Releasing" here means that connections are returned to their connection pool and any transactional state is rolled back, ultimately using the `rollback()` method of the underlying DBAPI connection.

At this point, the `.scoped_session` object is "empty", and will create a **new** `.Session` when called again.  As illustrated below, this is not the same `.Session` we had before:

```
>>> new_session = Session()
>>> new_session is some_session
False
```

The above series of steps illustrates the idea of the "registry" pattern in a nutshell.  With that basic idea in hand, we can discuss some of the details of how this pattern proceeds.

## Implicit Method Access

The job of the `.scoped_session` is simple; hold onto a `.Session` for all who ask for it.  As a means of producing more transparent access to this `.Session`, the `.scoped_session` also includes **proxy behavior**, meaning that the registry itself can be treated just like a `.Session` directly; when methods are called on this object, they are **proxied** to the underlying `.Session` being maintained by the registry:

```
Session = scoped_session(some_factory)

# equivalent to:
#
# session = Session()
# print(session.scalars(select(MyClass)).all())
#
print(Session.scalars(select(MyClass)).all())
```

The above code accomplishes the same task as that of acquiring the current `.Session` by calling upon the registry, then using that `.Session`.

## Thread-Local Scope

Users who are familiar with multithreaded programming will note that representing anything as a global variable is usually a bad idea, as it implies that the global object will be accessed by many threads concurrently.   The `.Session` object is entirely designed to be used in a **non-concurrent** fashion, which in terms of multithreading means "only in one thread at a time".   So our above example of `.scoped_session` usage, where the same `.Session` object is maintained across multiple calls, suggests that some process needs to be in place such that multiple calls across many threads don't actually get a handle to the same session.   We call this notion **thread local storage**, which means, a special object is used that will maintain a distinct object per each application thread.   Python provides this via the [threading.local()](https://docs.python.org/library/threading.html#threading.local) construct.  The `.scoped_session` object by default uses this object as storage, so that a single `.Session` is maintained for all who call upon the `.scoped_session` registry, but only within the scope of a single thread.   Callers who call upon the registry in a different thread get a `.Session` instance that is local to that other thread.

Using this technique, the `.scoped_session` provides a quick and relatively simple (if one is familiar with thread-local storage) way of providing a single, global object in an application that is safe to be called upon from multiple threads.

The `.scoped_session.remove` method, as always, removes the current `.Session` associated with the thread, if any.  However, one advantage of the `threading.local()` object is that if the application thread itself ends, the "storage" for that thread is also garbage collected.  So it is in fact "safe" to use thread local scope with an application that spawns and tears down threads, without the need to call `.scoped_session.remove`.  However, the scope of transactions themselves, i.e. ending them via `.Session.commit` or `.Session.rollback`, will usually still be something that must be explicitly arranged for at the appropriate time, unless the application actually ties the lifespan of a thread to the lifespan of a transaction.

## Using Thread-Local Scope with Web Applications

As discussed in the section `session_faq_whentocreate`, a web application is architected around the concept of a **web request**, and integrating such an application with the `.Session` usually implies that the `.Session` will be associated with that request.  As it turns out, most Python web frameworks, with notable exceptions such as the asynchronous frameworks Twisted and Tornado, use threads in a simple way, such that a particular web request is received, processed, and completed within the scope of a single worker thread.  When the request ends, the worker thread is released to a pool of workers where it is available to handle another request.

This simple correspondence of web request and thread means that to associate a `.Session` with a thread implies it is also associated with the web request running within that thread, and vice versa, provided that the `.Session` is created only after the web request begins and torn down just before the web request ends. So it is a common practice to use `.scoped_session` as a quick way to integrate the `.Session` with a web application.  The sequence diagram below illustrates this flow:

```text
 Web Server          Web Framework        SQLAlchemy ORM Code
 --------------      --------------       ------------------------------
 startup        ->   Web framework        # Session registry is established
                     initializes          Session = scoped_session(sessionmaker())

 incoming
 web request    ->   web request     ->   # The registry is *optionally*
                     starts               # called upon explicitly to create
                                          # a Session local to the thread and/or request
                                          Session()

                                          # the Session registry can otherwise
                                          # be used at any time, creating the
                                          # request-local Session() if not present,
                                          # or returning the existing one
                                          Session.execute(select(MyClass)) # ...

                                          Session.add(some_object) # ...

                                          # if data was modified, commit the
                                          # transaction
                                          Session.commit()

                     web request ends  -> # the registry is instructed to
                                          # remove the Session
                                          Session.remove()

                     sends output      <-
 outgoing web    <-
 response
```

Using the above flow, the process of integrating the `.Session` with the web application has exactly two requirements:

1. Create a single `.scoped_session` registry when the web application
first starts, ensuring that this object is accessible by the rest of the application.

2. Ensure that `.scoped_session.remove` is called when the web request ends,
usually by integrating with the web framework's event system to establish an "on request end" event.

As noted earlier, the above pattern is **just one potential way** to integrate a `.Session` with a web framework, one which in particular makes the significant assumption that the **web framework associates web requests with application threads**.  It is however **strongly recommended that the integration tools provided with the web framework itself be used, if available**, instead of `.scoped_session`.

In particular, while using a thread local can be convenient, it is preferable that the `.Session` be associated **directly with the request**, rather than with the current thread.   The next section on custom scopes details a more advanced configuration which can combine the usage of `.scoped_session` with direct request based scope, or any kind of scope.

## Using Custom Created Scopes

The `.scoped_session` object's default behavior of "thread local" scope is only one of many options on how to "scope" a `.Session`.   A custom scope can be defined based on any existing system of getting at "the current thing we are working with".

Suppose a web framework defines a library function `get_current_request()`.  An application built using this framework can call this function at any time, and the result will be some kind of `Request` object that represents the current request being processed. If the `Request` object is hashable, then this function can be easily integrated with `.scoped_session` to associate the `.Session` with the request.  Below we illustrate this in conjunction with a hypothetical event marker provided by the web framework `on_request_end`, which allows code to be invoked whenever a request ends:

```
from my_web_framework import get_current_request, on_request_end
from sqlalchemy.orm import scoped_session, sessionmaker

Session = scoped_session(sessionmaker(bind=some_engine), scopefunc=get_current_request)

@on_request_end
def remove_session(req):
    Session.remove()
```

Above, we instantiate `.scoped_session` in the usual way, except that we pass our request-returning function as the "scopefunc".  This instructs `.scoped_session` to use this function to generate a dictionary key whenever the registry is called upon to return the current `.Session`.   In this case it is particularly important that we ensure a reliable "remove" system is implemented, as this dictionary is not otherwise self-managed.

## Contextual Session API
