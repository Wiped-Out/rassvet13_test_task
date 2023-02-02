import asyncio
from functools import wraps


def backoff(
        exceptions: tuple,
        start_sleep_time: int = 0.1,
        factor: int = 2,
        border_sleep_time: int = 10,
):
    def func_wrapper(func):
        @wraps(func)
        async def inner(*args, **kwargs):
            sleeping_time = start_sleep_time
            while sleeping_time <= border_sleep_time:
                sleeping_time *= factor
                if sleeping_time >= border_sleep_time:
                    sleeping_time = border_sleep_time

                try:
                    return await func(*args, **kwargs)
                except exceptions:
                    pass

                await asyncio.sleep(sleeping_time)

        return inner

    return func_wrapper
