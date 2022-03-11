import asyncio
from contextlib import AbstractAsyncContextManager
import time
from typing import Optional, Type, Any
from types import TracebackType


class Throttler(AbstractAsyncContextManager[Any]):
    """Ensures that a time between executions is taken into account for each wrapped code block."""

    def __init__(self, time_between_executions_in_s: float) -> None:
        self.time_between_executions_in_s = time_between_executions_in_s

        self._lock = asyncio.Lock()
        self._last_execution_end: Optional[float] = None
        pass

    async def __aenter__(self) -> None:
        await self._lock.acquire()
        if self._last_execution_end is not None:
            time_since_last_execution = time.monotonic() - self._last_execution_end
            if time_since_last_execution < self.time_between_executions_in_s:
                await asyncio.sleep(
                    self.time_between_executions_in_s - time_since_last_execution
                )

        return None

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc: Optional[BaseException],
        tb: Optional[TracebackType],
    ) -> None:
        self._last_execution_end = time.monotonic()
        self._lock.release()
        return None
