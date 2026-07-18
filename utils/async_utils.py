
import asyncio
async def run_tasks(*coroutines):
    return await asyncio.gather(*coroutines)
