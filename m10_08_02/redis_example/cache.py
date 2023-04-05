import timeit

import redis
from redis_lru import RedisLRU

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)


def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


@cache
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


@cache
def data_func(l):
    print('Inner call')
    return sum(l)


if __name__ == '__main__':
    # start = timeit.default_timer()
    # r = fib(35)
    # print(f"Duration fib: {timeit.default_timer() - start}, {r}")
    #
    # start = timeit.default_timer()
    # r = fibonacci(135)
    # print(f"Duration fibonacci: {timeit.default_timer() - start}, {r}")
    d = [1, 2, 3]
    r = data_func(d)
    print(r)
    r = data_func(d)
    print(r)
