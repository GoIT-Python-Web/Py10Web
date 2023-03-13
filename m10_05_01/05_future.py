import asyncio
from asyncio import Future

from faker import Faker


from timing import async_timed

fake = Faker('uk-UA')


async def async_get_user_from_db(uuid: int, future: Future):
    await asyncio.sleep(0.5)
    future.set_result({'id': uuid, 'name': fake.name(), 'email': fake.email()})


def make_request(uuid: int) -> Future:
    future = Future()
    asyncio.create_task(async_get_user_from_db(uuid, future))
    return future


@async_timed()
async def main():
    f1 = make_request(1)
    f2 = make_request(2)
    f3 = make_request(3)
    print(dir(f1))
    print(f1, f2, f3)
    print(f1.done(), f2.done(), f3.done())
    result = await asyncio.gather(f1, f2, f3)
    print(f1.done(), f2.done(), f3.done())
    return result


if __name__ == '__main__':
    r = asyncio.run(main())
    print(r)
