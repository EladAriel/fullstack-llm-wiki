---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/8.0/references/rest-api/objects/bootstrap/user_defined_module.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.706150Z"
---
# User_Defined_Module

---
Title: user_defined_module object
alwaysopen: false
categories:
- docs
- operate
- rs
description: An object for user-defined module configuration during bootstrap
hideListLinks: true
linkTitle: user_defined_module
weight: $weight
url: '/operate/rs/8.0/references/rest-api/objects/bootstrap/user_defined_module/'
---

A user-defined module configuration object for bootstrap operations.

| Name | Type/Value | Description |
|------|------------|-------------|
| name | string | Module name for presentation and logging purposes (required) |
| location | object | Information on where to download the module from (required)<br />{{<code>}}{
  "location_type": "http | https",
  "url": "string",
  "credentials": {
    "username": "string",
    "password": "string"
  }
}{{</code>}}<br />**location_type**: The type of location, either `http` or `https` (required)<br />**url**: The URL to download the module zip file from (required)<br />**credentials**: Optional credentials for downloads that require basic authentication |

## Module package requirements

The module must be packaged as a `.zip` file containing:

- **module.json**: A metadata file with module information including:
  - `module_name`: The actual module name
  - `version`: Numeric version
  - `semantic_version`: Semantic version string (for example, "1.0.0")
  - `min_redis_version`: Minimum compatible Redis version
  - `commands`: List of commands the module provides
  - `capabilities`: List of module capabilities

- **Module binary**: The compiled `.so` file for the target platform
