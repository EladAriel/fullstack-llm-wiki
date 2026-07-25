---
type: "Framework Learn Page"
framework: "LangChain"
source_repo: "https://github.com/langchain-ai/docs"
source_branch: "main"
source_path: "src/oss/langchain/errors/MESSAGE_COERCION_FAILURE.mdx"
source_commit: "2aae1dfc98ee953a9a5185fb6fcdd9efb3f4d878"
source_commit_short: "2aae1dfc"
source_commit_date: "2026-07-25T00:27:23Z"
generated_at: "2026-07-25T11:51:05Z"
---

---
title: MESSAGE_COERCION_FAILURE
---

This error occurs when message objects don't conform to the expected format.

:::python
## Accepted message formats

LangChain modules accept `MessageLikeRepresentation`, which is defined as:

```python
from typing import Union

from langchain_core.prompts.chat import (
    BaseChatPromptTemplate,
    BaseMessage,
    BaseMessagePromptTemplate,
)

MessageLikeRepresentation = Union[
    Union[BaseMessagePromptTemplate, BaseMessage, BaseChatPromptTemplate],
    tuple[
        Union[str, type],
        Union[str, list[dict], list[object]],
    ],
    str,
]
```

These include OpenAI style message objects (`{ role: "user", content: "Hello world!" }`), tuples, and plain strings (which are converted to @[`HumanMessage`] objects).

If a module receives a value outside of one of these formats, you will receive an error:

```python
from langchain_anthropic import ChatAnthropic

uncoercible_message = {"role": "HumanMessage", "random_field": "random value"}

model = ChatAnthropic(model="claude-sonnet-4-6")

model.invoke([uncoercible_message])
```

```text
ValueError: Message dict must contain 'role' and 'content' keys, got {'role': 'HumanMessage', 'random_field': 'random value'}
```
:::
:::js
TODO: Add JS example
:::

## Troubleshooting

To resolve this error:

1. **Ensure proper format**: All inputs to chat models must be an array of LangChain message classes or a supported message-like format
2. Verify no unintended stringification or transformation occurs to your messages
3. Examine the error's stack trace and add logging statements to inspect message objects before they're passed to the model
