"""OpenAI via Hippocortex Gateway — zero code changes."""
from openai import OpenAI

client = OpenAI(
    base_url="https://api.hippocortex.dev/v1",
    api_key="hx_live_...",  # Your Hippocortex API key
    default_headers={
        "X-LLM-API-Key": "sk-...",  # Your OpenAI key
    },
)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "What did we deploy last week?"}],
)
print(response.choices[0].message.content)
