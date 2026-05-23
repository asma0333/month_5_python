import asyncio
import time

from functools import lru_cache
from concurrent.futures import ThreadPoolExecutor

from services.strategy import FastProcessingStrategy

class HighPerformanceProcessor:

    def __init__(self):
        self.strategy = FastProcessingStrategy()
        self.executor = ThreadPoolExecutor(max_workers=4)

    @lru_cache(maxsize=100)
    def cached_operation(self, text):

        time.sleep(1)

        return f"CACHED_{text}"

    async def process_item(self, item):

        start = time.time()

        result = await self.strategy.process(item)

        end = time.time()

        return {
            "input": item,
            "result": result,
            "time_taken": round(end-start, 2)
        }

    async def process_concurrently(self, items):

        tasks = [self.process_item(i) for i in items]

        results = await asyncio.gather(*tasks)

        return results