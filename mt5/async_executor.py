
import asyncio

class AsyncExecutor:
    async def execute(self, func, *args, **kwargs):
        return await asyncio.to_thread(func, *args, **kwargs)
