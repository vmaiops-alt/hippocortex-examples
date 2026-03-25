"""LangGraph agent with Hippocortex memory."""
from hippocortex import Hippocortex
from hippocortex.adapters.langgraph import LangGraphAdapter

hx = Hippocortex()
adapter = LangGraphAdapter(hx, session_id="langgraph-demo")

# Wrap your compiled graph
# wrapped = adapter.wrap(compiled_graph)
# result = await wrapped.ainvoke({"messages": [...]})
