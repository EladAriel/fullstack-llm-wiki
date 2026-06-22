---
type: "Framework Learn Page"
framework: "pydantic"
source_repo: "https://github.com/pydantic/pydantic"
source_branch: "main"
source_path: "docs/examples/pydantic_ai.md"
source_commit: "363728fe0b353db1a1fcb44aac5c38fd96a8cc20"
source_commit_short: "363728fe"
source_commit_date: "2026-06-20T11:20:58+01:00"
generated_at: "2026-06-21T11:37:01Z"
---

[Pydantic AI](https://ai.pydantic.dev/) is a Python agent framework built by the Pydantic team that uses Pydantic validation for [structured output](https://ai.pydantic.dev/output/#structured-output) schema generation and validation.
By specifying an `output_type` on an Agent, you can constrain the LLM to return data that matches your Pydantic model schema.

## LLM Structured Output

```python {test="skip"}
from pydantic_ai import Agent

from pydantic import BaseModel, Field, ValidationInfo, field_validator


class City(BaseModel):
    name: str
    country: str
    population: int = Field(description='Estimated population', gt=0)

    @field_validator('country')
    @classmethod
    def country_must_be_valid(cls, v: str, info: ValidationInfo) -> str:
        valid_countries: list[str] = info.context or []
        if v not in valid_countries:
            raise ValueError(f'Unknown country: {v!r}')
        return v


agent = Agent(
    'openai:gpt-5-mini',
    output_type=list[City],
    # Pydantic validation context (not sent to the model)
    validation_context=['Japan', 'United States', 'Germany'],
)

result = agent.run_sync('List the 3 largest cities in Japan')
print(result.output)
#> [City(name='Tokyo', country='Japan', population=13960000), ...]
```
