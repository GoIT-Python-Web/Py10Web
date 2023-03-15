import aiohttp
import asyncio
import platform


async def request(url: str):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as resp:
                if resp.status == 200:
                    result = await resp.json()
                    return result
                else:
                    print(f"Error status: {resp.status} for {url}")
        except aiohttp.ClientConnectorError as err:
            print(f'Connection error: {url}', str(err))


async def main():
    result = await request('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5')
    if result:
        exc, = list(filter(lambda el: el["ccy"] == 'USD', result))
        return f"USD Продаж {exc['sale']}, Покупка {exc['buy']}"
    return 'Not found'


if __name__ == '__main__':
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    r = asyncio.run(main())
    print(r)
