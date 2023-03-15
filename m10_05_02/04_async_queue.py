import asyncio
from random import randint


async def producer(queue: asyncio.Queue):
    num = randint(1, 100)
    await asyncio.sleep(0.2)
    await queue.put(num)


async def consumer(queue: asyncio.Queue):
    while True:
        num = await queue.get()
        print(num ** 2)
        queue.task_done()


async def main():
    queue = asyncio.Queue()
    consumer_tasks = [asyncio.create_task(consumer(queue)) for _ in range(5)]
    producer_tasks = [asyncio.create_task(producer(queue)) for _ in range(50)]
    await asyncio.gather(*producer_tasks)
    await queue.join()
    [task.cancel() for task in consumer_tasks]


if __name__ == '__main__':
    asyncio.run(main())


