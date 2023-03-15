import asyncio
from typing import List, Iterable, Awaitable

from faker import Faker


from timing import async_timed

fake = Faker('uk-UA')


async def async_get_user_from_fake_db(uuid: int):
    await asyncio.sleep(0.5)
    return {'id': uuid, 'name': fake.name(), 'email': fake.email()}


def get_users(uuids: List[int]) -> Iterable[Awaitable]:
    return [async_get_user_from_fake_db(uuid) for uuid in uuids]


@async_timed()
async def main(users: Iterable[Awaitable]):
    return await asyncio.gather(*users)


if __name__ == '__main__':
    r = asyncio.run(main(get_users([1, 2, 3])))
    print(r)
