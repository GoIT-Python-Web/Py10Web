import time
from functools import wraps


def wrong_timelogger(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__}: {end - start}")
        return result
    return wrapper


def timelogger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__}: {end - start}")
        return result
    return wrapper


@timelogger
@timelogger
def long_loop(num: int):
    """
    Long Loop function
    :param num:
    :return: None
    """
    while num > 0:
        num -= 1


if __name__ == '__main__':
    long_loop(100_000)
    print(f"Function name: {long_loop.__name__}")
    print(f"Docstring name: {long_loop.__doc__}")
    print(f"Annotation name: {long_loop.__annotations__}")

    long_loop.__wrapped__.__wrapped__(100_000)
