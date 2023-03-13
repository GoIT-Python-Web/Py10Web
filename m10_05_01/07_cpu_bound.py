import asyncio
from concurrent.futures import ProcessPoolExecutor

from faker import Faker

fake = Faker('uk-UA')


async def send(email):
    print(f'Hello my friend! {email}')


async def worker():
    while True:
        await asyncio.sleep(1)
        await send(fake.email())


def cpu_bound(counter):
    init = counter
    while counter > 0:
        counter -= 1
    print(f'Completed cpu bound task {init}')
    return init


async def main():
    loop = asyncio.get_running_loop()
    task = loop.create_task(worker())

    with ProcessPoolExecutor(2) as executor:
        futures = [loop.run_in_executor(executor, cpu_bound, num) for num in [60_000_000, 50_000_000, 80_000_000]]
        result = await asyncio.gather(*futures)
        task.cancel()
        return result


if __name__ == '__main__':
    r = asyncio.run(main())
    print(r)
