"""Manual client — full control over capture, synthesize, learn, vault."""
import asyncio
from hippocortex import Hippocortex, CaptureEvent

async def main():
    hx = Hippocortex()  # reads HIPPOCORTEX_API_KEY from env

    # 1. Capture events
    await hx.capture(CaptureEvent(
        type="message",
        session_id="demo-session",
        payload={"role": "user", "content": "Deploy the payment service to production"},
    ))

    # 2. Retrieve context for a new query
    context = await hx.synthesize("How do I deploy?")
    print("Context sections:", len(context.sections))
    for section in context.sections:
        print(f"  [{section.type}] {section.content[:100]}...")

    # 3. Trigger knowledge compilation
    result = await hx.learn()
    print(f"Compiled: {result.artifacts.created} artifacts created")

    # 4. Search the vault
    vault_results = await hx.vault_query("API keys")
    print(f"Vault: {len(vault_results.items)} secrets found")

asyncio.run(main())
