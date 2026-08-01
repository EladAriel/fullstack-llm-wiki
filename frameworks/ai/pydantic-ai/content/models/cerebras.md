---
type: "Framework Learn Page"
framework: "Pydantic AI"
source_repo: "https://github.com/pydantic/pydantic-ai.git"
source_branch: "main"
source_path: "docs/models/cerebras.md"
source_commit: "bf2c7315ecc26d446b872c544bb501a01066b4e2"
source_commit_short: "bf2c731"
source_commit_date: "2026-08-01T09:04:12+00:00"
generated_at: "2026-08-01T12:41:00.858156Z"
---
# Cerebras

## Install

To use `CerebrasModel`, you need to either install `pydantic-ai`, or install `pydantic-ai-slim` with the `cerebras` optional group:

```bash
pip/uv-add "pydantic-ai-slim[cerebras]"
```

## Configuration

To use [Cerebras](https://cerebras.ai/) through their API, go to [cloud.cerebras.ai](https://cloud.cerebras.ai/?utm_source=3pi_pydantic-ai&utm_campaign=partner_doc) and generate an API key.

For a list of available models, see the [Cerebras models documentation](https://inference-docs.cerebras.ai/models).

## Environment variable

Once you have the API key, you can set it as an environment variable:

```bash
export CEREBRAS_API_KEY='your-api-key'
```

You can then use `CerebrasModel` by name:

```python
from pydantic_ai import Agent

agent = Agent('cerebras:llama-3.3-70b')
...
```

Or initialise the model directly with just the model name:

```python
from pydantic_ai import Agent
from pydantic_ai.models.cerebras import CerebrasModel

model = CerebrasModel('llama-3.3-70b')
agent = Agent(model)
...
```

## `provider` argument

You can provide a custom `Provider` via the `provider` argument:

```python
from pydantic_ai import Agent
from pydantic_ai.models.cerebras import CerebrasModel
from pydantic_ai.providers.cerebras import CerebrasProvider

model = CerebrasModel(
    'llama-3.3-70b', provider=CerebrasProvider(api_key='your-api-key')
)
agent = Agent(model)
...
```

You can also customize the `CerebrasProvider` with a custom `httpx.AsyncClient`:

```python
from httpx import AsyncClient

from pydantic_ai import Agent
from pydantic_ai.models.cerebras import CerebrasModel
from pydantic_ai.providers.cerebras import CerebrasProvider

custom_http_client = AsyncClient(timeout=30)
model = CerebrasModel(
    'llama-3.3-70b',
    provider=CerebrasProvider(api_key='your-api-key', http_client=custom_http_client),
)
agent = Agent(model)
...
```
