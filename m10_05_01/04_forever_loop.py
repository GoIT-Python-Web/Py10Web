import asyncio
from time import sleep, time

from faker import Faker

fake = Faker('uk-UA')


async def send(email):
    print(f'Hello my friend! {email}')


async def worker():
    while True:
        await asyncio.sleep(1)
        await send(fake.email())


if __name__ == '__main__':
    asyncio.run(worker())
    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop)
    # loop.create_task(worker())
    # loop.run_forever()
