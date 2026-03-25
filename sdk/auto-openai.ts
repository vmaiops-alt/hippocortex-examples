// Auto-instrumentation (TypeScript) — one import
import '@hippocortex/sdk/auto'
import OpenAI from 'openai'

const openai = new OpenAI()

const response = await openai.chat.completions.create({
  model: 'gpt-4o',
  messages: [{ role: 'user', content: 'Deploy payments to staging' }],
})
console.log(response.choices[0].message.content)
