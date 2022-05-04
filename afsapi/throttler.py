import asyncio
from contextlib import AbstractAsyncContextManager
import time
from typing import Optional, Type, Any
from types import TracebackType


class Throttler:
    """Ensures that a time between executions is taken into account for each wrapped code block,
    which can be configured for every entry."""

    def __init__(self) -> None:
        self._lock = asyncio.Lock()
        self._next_execution_not_before: Optional[float] = None

    class _ThrottleContextManager(AbstractAsyncContextManager[Any]):
        """Ensures that a time between executions is taken into account for each wrapped code block."""

        def __init__(
            self, throttler: "Throttler", time_after_execution_s: float
        ) -> None:
            self.throttler = throttler
            self.time_after_execution_s = time_after_execution_s

        async def __aenter__(self) -> None:
            await self.throttler._lock.acquire()
            if self.throttler._next_execution_not_before is not None:
                additional_wait = (
                    self.throttler._next_execution_not_before - time.monotonic()
                )

                if additional_wait > 0:
                    await asyncio.sleep(additional_wait)

            return None

        async def __aexit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc: Optional[BaseException],
            tb: Optional[TracebackType],
        ) -> None:
            self.throttler._next_execution_not_before = (
                time.monotonic() + self.time_after_execution_s
            )
            self.throttler._lock.release()
            return None

    def throttle(self, throttle_after_call_s: float) -> _ThrottleContextManager:
        return Throttler._ThrottleContextManager(self, throttle_after_call_s)
