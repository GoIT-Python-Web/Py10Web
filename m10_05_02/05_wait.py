import asyncio
from concurrent.futures import ThreadPoolExecutor
from time import time
from typing import Tuple

import requests


from timing import async_timed

urls = [
    'https://www.google.com.ua/?hl=uk',
    'https://www.python.org/',
    'https://goit.global/ua/',
    'qwerty',
    'https://duckduckgo.com/'
]


def get_preview(url: str) -> Tuple[str, str]:
    r = requests.get(url)
    return url, r.text[:25]


async def main():
    loop = asyncio.get_running_loop()

    with ThreadPoolExecutor(len(urls)) as executor:
        futures = [loop.run_in_executor(executor, get_preview, url) for url in urls]
        done_one, pending = await asyncio.wait(futures, return_when=asyncio.ALL_COMPLETED)
        print('Done: ', done_one)
        print('Pending: ', pending)
        # done_two, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)
        # print('Done: ', done_two)
        # print('Pending: ', pending)
        [el.cancel() for el in pending]
        result = []
        for el in done_one:
            try:
                result.append(await el)
            except Exception as e:
                print(e)
        return result

if __name__ == '__main__':
    r = asyncio.run(main())
    print(r)
