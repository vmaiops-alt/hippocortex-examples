"""CrewAI crew with Hippocortex memory."""
from hippocortex import Hippocortex
from hippocortex.adapters.crewai import CrewAIAdapter

hx = Hippocortex()
adapter = CrewAIAdapter(hx, session_id="crew-demo")

# Wrap your crew
# enhanced_crew = adapter.wrap(crew)
# result = enhanced_crew.kickoff()
