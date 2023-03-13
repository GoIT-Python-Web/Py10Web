import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def io_bound_op():
    with open(__file__, 'r') as fd:
        return fd.read(14)


def cpu_bound_op(power: int, p: int):
    r = [i ** power for i in range(10 ** p)]
    return sum(r)


async def main():
    loop = asyncio.get_running_loop()

    with ThreadPoolExecutor() as pool:
        f = await loop.run_in_executor(pool, io_bound_op)
        print(f)

    with ProcessPoolExecutor() as pool:
        f = await loop.run_in_executor(pool, cpu_bound_op, 2, 5)
        print(f)

if __name__ == '__main__':
    asyncio.run(main())
