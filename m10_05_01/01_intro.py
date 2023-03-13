import asyncio


async def coro():
    await asyncio.sleep(0)
    return 'Hello world!'


async def main():
    c = coro()
    # print(c)  # coroutine
    # print(dir(c))
    result = await c
    print(f"Result: {result}")
    return result


if __name__ == '__main__':
    r = asyncio.run(main())
    print(f'Result in main process: {r}')
