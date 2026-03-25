# OpenClaw + Hippocortex Setup

## Option A: Setup Wizard (Recommended)

```bash
npx @hippocortex/setup
```

One command. Installs the plugin, configures your API key, enables the Context Engine, restarts the gateway.

## Option B: Manual

Add to `openclaw.json`:

```json
{
  "plugins": {
    "entries": {
      "hippocortex": {
        "enabled": true,
        "config": {
          "apiKey": "hx_live_...",
          "baseUrl": "https://api.hippocortex.dev",
          "capture": true,
          "retrieval": true,
          "contextEngine": {
            "enabled": true,
            "maxRecentMessages": 50,
            "retrievalBudget": 4000
          }
        }
      }
    }
  }
}
```

Then: `openclaw gateway restart`
