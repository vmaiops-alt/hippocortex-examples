"""OpenAI Agents SDK with Hippocortex memory."""
from hippocortex import Hippocortex
from hippocortex.adapters.openai_agents import OpenAIAgentsAdapter

hx = Hippocortex()
adapter = OpenAIAgentsAdapter(hx, session_id="agents-demo")

# Get context before running
# context = await adapter.get_context("deploy the API service")
# Capture after running
# await adapter.capture_run(run_result)
