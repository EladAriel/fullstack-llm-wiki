---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/resources/frequently-asked-questions/how-do-i-resolve-phoenix-evals-showing-not_parsable.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.878444Z"
---
# How Do I Resolve Phoenix Evals Showing Not_Parsable

---
title: "How do I resolve Phoenix Evals showing NOT\_PARSABLE?"
description: "`NOT_PARSABLE` errors often occur when LLM responses exceed the `max_tokens` limit or produce incomplete JSON."
---


Here's how to fix it:

<Steps>
<Step>
    Increase `max_tokens`: Update the model configuration as follows:

    ```python
    from phoenix.evals import LLM
    from phoenix.evals import ClassificationEvaluator

    llm = LLM(
        provider="openai",
        model="gpt-4o-2024-08-06",
        api_key=getpass("Enter your OpenAI API key..."),
    )
    # Pass max_tokens and temperature when creating the evaluator
    evaluator = ClassificationEvaluator(
        ...,
        llm=llm,
        temperature=0.2,
        max_tokens=1000,  # Increase token limit
    )
    ```
    </Step>
    <Step>
    Update Phoenix: Use version ≥0.17.4, which removes token limits for OpenAI and increases defaults for other APIs.
    </Step>
    <Step>
    Check Logs: Look for `finish_reason="length"` to confirm token limits caused the issue.
    </Step>
    <Step>
    If the above doesn't work, it's possible the llm-as-a-judge output might not fit into the defined choices for that particular custom Phoenix eval. Double check the prompt output matches the expected choices.
    </Step>
</Steps>
