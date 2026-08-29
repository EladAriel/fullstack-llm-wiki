---
type: "Framework Learn Page"
framework: "Pydantic"
source_repo: "https://github.com/pydantic/pydantic"
source_branch: "main"
source_path: "docs/examples/pydantic_ai.md"
source_commit: "4bc21c0fa28323c0f3e0be93c9ad114b705029c6"
source_commit_short: "4bc21c0"
source_commit_date: "2026-08-29T11:30:40+02:00"
generated_at: "2026-08-29T09:38:50.585271Z"
---
# Pydantic_Ai

[Pydantic AI](https://pydantic.dev/docs/ai/overview/) is a Python agent framework built by the Pydantic team that uses Pydantic validation for [structured output](https://pydantic.dev/docs/ai/core-concepts/output/#structured-output) schema generation and validation.
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

When validation fails (say the model returns a country your validator rejects), Pydantic AI feeds the
validation errors back to the model and asks it to retry. To see this happening in a real application,
instrument it with [Logfire](../integrations/logfire.md), which records
[Pydantic AI](https://pydantic.dev/docs/ai/integrations/logfire/) runs and the validations inside them: each agent run
shows the output the model produced, the errors your validators raised, and the retry that followed.
