import asyncio
from typing import List, AsyncIterator, Coroutine, Any

from faker import Faker


from timing import async_timed

fake = Faker('uk-UA')


async def async_get_user_from_fake_db(uuid: int):
    await asyncio.sleep(0.5)
    return {'id': uuid, 'name': fake.name(), 'email': fake.email()}


async def get_users(uuids: List[int]) -> AsyncIterator:
    for uuid in uuids:
        yield async_get_user_from_fake_db(uuid)


@async_timed()
async def main(users: AsyncIterator):
    result = []
    async for user in users:
        result.append(user)
    return await asyncio.gather(*result)


if __name__ == '__main__':
    r = asyncio.run(main(get_users([1, 2, 3])))
    print(r)
