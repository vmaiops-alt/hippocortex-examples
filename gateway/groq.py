"""Groq via Hippocortex Gateway."""
from openai import OpenAI

client = OpenAI(
    base_url="https://api.hippocortex.dev/v1",
    api_key="hx_live_...",
    default_headers={
        "X-LLM-API-Key": "gsk_...",
        "X-LLM-Base-URL": "https://api.groq.com/openai",
    },
)

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": "What patterns have we seen in errors?"}],
)
print(response.choices[0].message.content)
