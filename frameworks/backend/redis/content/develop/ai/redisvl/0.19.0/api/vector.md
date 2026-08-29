---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/develop/ai/redisvl/0.19.0/api/vector.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.881526Z"
---
# Vector

---
linkTitle: Vector
title: Vector
url: '/develop/ai/redisvl/0.19.0/api/vector/'
---


The Vector class in RedisVL is a container that encapsulates a numerical vector, it’s datatype, corresponding index field name, and optional importance weight. It is used when constructing multi-vector queries using the MultiVectorQuery class.

## Vector

### `class Vector(*, vector, field_name, dtype='float32', weight=1.0, max_distance=2.0)`

Simple object containing the necessary arguments to perform a multi vector query.

Args:
vector: The vector values as a list of floats or bytes
field_name: The name of the vector field to search
dtype: The data type of the vector (default: "float32")
weight: The weight for this vector in the combined score (default: 1.0)
max_distance: The maximum distance for vector range search (default: 2.0, range: [0.0, 2.0])

Create a new model by parsing and validating input data from keyword arguments.

Raises [ValidationError][pydantic_core.ValidationError] if the input data cannot be
validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

* **Parameters:**
  * **vector** (*list* *[* *float* *]*  *|* *bytes*)
  * **field_name** (*str*)
  * **dtype** (*str*)
  * **weight** (*float*)
  * **max_distance** (*float*)

#### `validate_vector()`

If the vector passed in is an array of float convert it to a byte string.

* **Return type:**
  *Self*

#### `model_config: ClassVar[ConfigDict] = {}`

Configuration for the model, should be a dictionary conforming to [ConfigDict][pydantic.config.ConfigDict].
