# Hippocortex Examples

Integration examples for [Hippocortex](https://hippocortex.dev) — persistent memory for AI agents.

## Examples

### Gateway (Any LLM Provider)

The fastest integration — change one URL, no SDK needed.

| Example | Description |
|---------|-------------|
| [gateway/openai.py](gateway/openai.py) | OpenAI via Gateway |
| [gateway/anthropic.py](gateway/anthropic.py) | Anthropic via Gateway |
| [gateway/groq.py](gateway/groq.py) | Groq via Gateway |
| [gateway/ollama.py](gateway/ollama.py) | Ollama (local) via Gateway |
| [gateway/openai.ts](gateway/openai.ts) | OpenAI via Gateway (TypeScript) |

### SDK Auto-Instrumentation

One import adds memory to all LLM calls.

| Example | Description |
|---------|-------------|
| [sdk/auto-openai.py](sdk/auto-openai.py) | Auto-instrument OpenAI (Python) |
| [sdk/auto-openai.ts](sdk/auto-openai.ts) | Auto-instrument OpenAI (TypeScript) |
| [sdk/manual-client.py](sdk/manual-client.py) | Manual capture + synthesize |
| [sdk/manual-client.ts](sdk/manual-client.ts) | Manual capture + synthesize (TS) |

### Framework Adapters

| Example | Description |
|---------|-------------|
| [adapters/langgraph-agent.py](adapters/langgraph-agent.py) | LangGraph agent with memory |
| [adapters/crewai-crew.py](adapters/crewai-crew.py) | CrewAI crew with memory |
| [adapters/openai-agents.py](adapters/openai-agents.py) | OpenAI Agents SDK with memory |

### OpenClaw

| Example | Description |
|---------|-------------|
| [openclaw/setup.md](openclaw/setup.md) | Plugin setup guide |

## Prerequisites

1. Sign up at [dashboard.hippocortex.dev](https://dashboard.hippocortex.dev) (free)
2. Copy your API key (`hx_live_...`)
3. Set `export HIPPOCORTEX_API_KEY=hx_live_...`

## Links

- [Documentation](https://hippocortex.dev/docs)
- [JavaScript SDK](https://github.com/vmaiops-alt/hippocortex-js)
- [Python SDK](https://github.com/vmaiops-alt/hippocortex-python)

## License

MIT
