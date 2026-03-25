// Manual client (TypeScript) — full control
import { Hippocortex } from '@hippocortex/sdk'

const hx = new Hippocortex() // reads HIPPOCORTEX_API_KEY from env

// 1. Capture events
await hx.capture({
  type: 'message',
  sessionId: 'demo-session',
  payload: { role: 'user', content: 'Deploy the payment service' },
})

// 2. Retrieve context
const context = await hx.synthesize('How do I deploy?')
console.log(`Context: ${context.sections.length} sections`)

// 3. Compile knowledge
const result = await hx.learn()
console.log(`Compiled: ${result.artifacts.created} artifacts`)

// 4. Vault
const secrets = await hx.vaultQuery('API keys')
console.log(`Vault: ${secrets.items.length} secrets`)
