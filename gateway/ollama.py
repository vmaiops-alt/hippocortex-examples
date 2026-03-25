"""Ollama (local) via Hippocortex Gateway."""
from openai import OpenAI

client = OpenAI(
    base_url="https://api.hippocortex.dev/v1",
    api_key="hx_live_...",
    default_headers={
        "X-LLM-API-Key": "unused",
        "X-LLM-Base-URL": "http://localhost:11434",
    },
)

response = client.chat.completions.create(
    model="llama3.2",
    messages=[{"role": "user", "content": "Review our deployment checklist"}],
)
print(response.choices[0].message.content)
