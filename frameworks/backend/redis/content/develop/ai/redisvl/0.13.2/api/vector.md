---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/develop/ai/redisvl/0.13.2/api/vector.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
linkTitle: Vector
title: Vector
url: '/develop/ai/redisvl/0.13.2/api/vector/'
---


The Vector class in RedisVL is a container that encapsulates a numerical vector, it’s datatype, corresponding index field name, and optional importance weight. It is used when constructing multi-vector queries using the MultiVectorQuery class.

## Vector

### `class Vector(*, vector, field_name, dtype='float32', weight=1.0)`

Simple object containing the necessary arguments to perform a multi vector query.

Create a new model by parsing and validating input data from keyword arguments.

Raises [ValidationError][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

* **Parameters:**
  * **vector** (*List* *[* *float* *]*  *|* *bytes*)
  * **field_name** (*str*)
  * **dtype** (*str*)
  * **weight** (*float*)

#### `validate_vector()`

If the vector passed in is an array of float convert it to a byte string.

* **Return type:**
  *Self*

#### `model_config: ClassVar[ConfigDict] = {}`

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].
