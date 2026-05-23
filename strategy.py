from abc import ABC, abstractmethod
import asyncio

class ProcessingStrategy(ABC):

    @abstractmethod
    async def process(self, data):
        pass


class FastProcessingStrategy(ProcessingStrategy):

    async def process(self, data):
        await asyncio.sleep(1)
        return f"FAST_PROCESSED_{data}"


class ThoroughProcessingStrategy(ProcessingStrategy):

    async def process(self, data):
        await asyncio.sleep(3)
        return f"THOROUGH_PROCESSED_{data}"