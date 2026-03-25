"""Anthropic via Hippocortex Gateway."""
from openai import OpenAI

client = OpenAI(
    base_url="https://api.hippocortex.dev/v1",
    api_key="hx_live_...",
    default_headers={
        "X-LLM-API-Key": "sk-ant-...",
        "X-LLM-Base-URL": "https://api.anthropic.com",
    },
)

response = client.chat.completions.create(
    model="claude-sonnet-4-20250514",
    messages=[{"role": "user", "content": "Summarize our last debugging session"}],
)
print(response.choices[0].message.content)
