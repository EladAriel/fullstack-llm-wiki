---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/stable-api.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========

# Stable API

## What is the Stable API, and Should You Use It?

The MongoDB Stable API (previously labeled the Versioned API) lets you upgrade your MongoDB server at will, and ensure that behavior changes between MongoDB versions do not break your application.

MongoDB 5.0 introduces the Stable API for applications communicating with MongoDB server products. The Stable API allows you to specify which version of the MongoDB API your application runs against.

The Stable API provides long-term API stability for applications and supports more frequent releases and automatic server upgrades. This allows your applications to take advantage of rapidly released features without risking backwards-breaking changes.

The default behavior for your driver connection will continue to function as expected, even if you do not explicitly specify an `apiVersion <api-version-desc>`.

The Stable API encompasses the `subset of MongoDB commands <api-v1-command-list>` that applications use to read and write data, create collections and indexes, and perform other common tasks.

> **Note:** Starting in February 2022, the "Versioned API" terminology was
changed to "Stable API". All concepts and features remain the same
with this naming change.

## Backward Compatibility Guarantee

Your application will not experience significant behavior changes resulting from server upgrades. This guarantee holds as long as the new server supports your specified API version.

To guarantee backward compatibility, your application must:

- Declare an API version
- Only use commands and features supported in your specified API version
- Deploy with a supported version of an official driver
## Declare the API Version

----------

|arrow| Use the **Select your language** drop-down menu in the upper-right to set the language of the examples on this page.

----------

To use the Stable API, upgrade to the latest driver and create your application's MongoClient:

`"1"` is currently the only API version available.

By default, clients are non-strict. A non-strict client allows you to run any command, regardless of whether or not it belongs to the Stable API.

## Checking Client API Versions

Use the :dbcommand:`serverStatus` command to check for your application's configured API version. For each application connected to your MongoDB instance, an `appname` appears in the `apiVersions` document.

See `metrics.apiVersions <server-status-apiVersions>` for more information.

```javascript
db.runCommand( { serverStatus: 1 } ).metrics.apiVersions
```

## Create a Strict Client

A strict client rejects all commands outside of the Stable API. Attempts to use commands outside of the Stable API will receive the `APIVersionError <api-vers-resp>` response.

A strict client also ignores `unsupported index types<create-indexes-stable-api>` during `query planning<query-plans-query-optimization>` and execution.

Use the sample code to create a strict client:

## Migrate To Stable API Commands

To migrate your application to use the Stable API, you must:

#. Run your application's test suite with the new MongoClient options. #. Determine which commands and features you're using that are outside of the Stable API. #. Migrate to alternative commands and features in the Stable API.

Once your application uses only commands and features defined in the Stable API, you can redeploy it with the new MongoClient options and be confident that future server upgrades won't negatively impact your application.

## How To Use Commands and Features Outside of the Stable API

To use commands and features outside of the Stable API, you can connect to your deployment with a non-strict client. By default, clients are non-strict.

To create a non-strict client, use the following sample code:

Using this non-strict client allows you to run commands outside of the Stable API. For example, this non-strict client allows you to run the :dbcommand:`createUser` command.

> **Important:** Commands and features outside of the Stable API do not have the same
backward compatibility guarantees as versioned alternatives.

## Stable API Commands

The database commands included in Stable API V1 depend on the MongoDB version you are using. To view the database commands included in the Stable API and the MongoDB version they were introduced, see `stable-api-changelog`.

## Parameters

You can specify the following optional parameters for Stable API in your application's MongoDB driver connection code. Check the MongoDB driver documentation for the driver you use in your application for more information:

.. include:: /includes/stable-api-options.rst

## Behavior

### Parameter Validation

Starting in MongoDB 5.0, API V1 database commands raise an error if passed a parameter not explicitly accepted by the command.

## Stable API Error Responses

This table shows error responses for problematic Stable API requests.

## Contents

- Migrate to Later Version </reference/stable-api-reference>
- Changelog </reference/stable-api-changelog>
