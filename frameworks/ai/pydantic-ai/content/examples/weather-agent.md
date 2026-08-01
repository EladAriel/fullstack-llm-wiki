---
type: "Framework Learn Page"
framework: "Pydantic AI"
source_repo: "https://github.com/pydantic/pydantic-ai.git"
source_branch: "main"
source_path: "docs/examples/weather-agent.md"
source_commit: "bf2c7315ecc26d446b872c544bb501a01066b4e2"
source_commit_short: "bf2c731"
source_commit_date: "2026-08-01T09:04:12+00:00"
generated_at: "2026-08-01T12:41:00.856188Z"
---
# Weather Agent

Example of Pydantic AI with multiple tools which the LLM needs to call in turn to answer a question.

Demonstrates:

- [tools](../tools.md)
- [agent dependencies](../dependencies.md)
- [streaming text responses](../output.md#streaming-text)
- Building a [Gradio](https://www.gradio.app/) UI for the agent

In this case the idea is a "weather" agent — the user can ask for the weather in multiple locations,
the agent will use the `get_lat_lng` tool to get the latitude and longitude of the locations, then use
the `get_weather` tool to get the weather for those locations.

## Running the Example

To run this example properly, you might want to add two extra API keys **(Note if either key is missing, the code will fall back to dummy data, so they're not required)**:

- A weather API key from [tomorrow.io](https://www.tomorrow.io/weather-api/) set via `WEATHER_API_KEY`
- A geocoding API key from [geocode.maps.co](https://geocode.maps.co/) set via `GEO_API_KEY`

With [dependencies installed and environment variables set](./setup.md#usage), run:

```bash
python/uv-run -m pydantic_ai_examples.weather_agent
```

## Example Code
```snippet {path="/examples/pydantic_ai_examples/weather_agent.py"}```

## Running the UI

You can build multi-turn chat applications for your agent with [Gradio](https://www.gradio.app/), a framework for building AI web applications entirely in python. Gradio comes with built-in chat components and agent support so the entire UI will be implemented in a single python file!

Here's what the UI looks like for the weather agent:

{{ video('c549d8d8827ded15f326f998e428e6c3', 6) }}


```bash
pip install gradio>=6.7.0
python/uv-run -m pydantic_ai_examples.weather_agent_gradio
```

## UI Code
```snippet {path="/examples/pydantic_ai_examples/weather_agent_gradio.py"}```
