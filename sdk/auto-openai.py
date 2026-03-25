"""Auto-instrumentation — one import adds memory to all OpenAI calls."""
import hippocortex.auto  # This is the only change needed
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Deploy payments to staging"}],
)
print(response.choices[0].message.content)
