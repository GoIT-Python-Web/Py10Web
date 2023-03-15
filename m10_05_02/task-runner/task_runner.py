import asyncio
from aiofile import async_open
from aiopath import AsyncPath


async def consumer(filename, queue: asyncio.Queue):
    async with async_open(filename, 'w', encoding='utf-8') as afp:
        while True:
            file, content = await queue.get()
            await afp.write(f"{content}\n")
            queue.task_done()


async def producer(file: AsyncPath, queue: asyncio.Queue):
    async with async_open(file, 'r', encoding='utf-8') as afp:
        data = []
        async for line in afp:
            data.append(str(line))
        await queue.put((file, ''.join(data)))


async def main():
    list_files = AsyncPath(".").joinpath("files").glob("*.js")
    print(list_files)
    queue = asyncio.Queue()
    producer_tasks = [asyncio.create_task(producer(file, queue)) async for file in list_files]
    consumer_task = asyncio.create_task(consumer('main.js', queue))
    await asyncio.gather(*producer_tasks)
    await queue.join()
    consumer_task.cancel()


if __name__ == '__main__':
    asyncio.run(main())
