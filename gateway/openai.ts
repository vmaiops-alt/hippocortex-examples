// OpenAI via Hippocortex Gateway (TypeScript)
import OpenAI from 'openai'

const client = new OpenAI({
  baseURL: 'https://api.hippocortex.dev/v1',
  apiKey: 'hx_live_...',
  defaultHeaders: {
    'X-LLM-API-Key': 'sk-...',
  },
})

const response = await client.chat.completions.create({
  model: 'gpt-4o',
  messages: [{ role: 'user', content: 'What did we deploy last week?' }],
})
console.log(response.choices[0].message.content)
