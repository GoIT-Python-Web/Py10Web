import asyncio
from time import sleep, time

from faker import Faker

fake = Faker('uk-UA')

# Awaitable -> Coroutine
# Awaitable -> Future -> Task


async def async_get_user_from_db(uuid: int):
    await asyncio.sleep(0.5)
    return {'id': uuid, 'name': fake.name(), 'email': fake.email()}


async def main():
    users = []
    for i in range(1, 4):
        task = asyncio.create_task(async_get_user_from_db(i))
        users.append(task)

    result = await asyncio.gather(*users)
    return result


if __name__ == '__main__':
    start = time()
    r = asyncio.run(main())
    print(r)
    print(time() - start)
    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop)
    # r = loop.run_until_complete(main())
    # print(r)
