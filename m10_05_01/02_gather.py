import asyncio
from time import sleep, time

from faker import Faker

fake = Faker('uk-UA')


def sync_get_user_from_db(uuid: int):
    sleep(0.5)
    return {'id': uuid, 'name': fake.name(), 'email': fake.email()}


async def async_get_user_from_db(uuid: int):
    await asyncio.sleep(0.5)
    return {'id': uuid, 'name': fake.name(), 'email': fake.email()}


async def main():
    users = []
    for i in range(1, 4):
        users.append(async_get_user_from_db(i))

    result = await asyncio.gather(*users)

    return result


if __name__ == '__main__':
    start = time()
    for i in range(1, 4):
        user = sync_get_user_from_db(i)
        print(user)
    print(time() - start)

    start = time()
    r = asyncio.run(main())
    print(r)
    print(time() - start)

    data = [1, 2, 4]
    print(data)
    print(*data)  # print(data[0], data[1], data[2])
