import asyncio
from concurrent.futures import ThreadPoolExecutor
from time import time

import requests
from requests.exceptions import InvalidSchema, MissingSchema, InvalidURL

from timing import async_timed

urls = [
    'https://www.google.com.ua/?hl=uk',
    'https://www.python.org/',
    'https://goit.global/ua/',
    'https://duckduckgo.com/',
    'https://github.com/',
    'https://www.codewars.com/',
    'https://www.python.org/qwerty',
    'ws://test.com',
    'test.com.23'
]


def get_preview(url: str) -> (str, str):
    r = requests.get(url)
    return url, r.text[:25]


@async_timed()
async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor(10) as executor:
        futures = [loop.run_in_executor(executor, get_preview, url) for url in urls]
        r = await asyncio.gather(*futures, return_exceptions=True)
        return r


if __name__ == '__main__':
    r = asyncio.run(main())
    print(r)
    for el in r:
        print(isinstance(el, Exception))

    # start = time()
    # results = []
    # for url in urls:
    #     try:
    #         results.append(get_preview(url))
    #     except (InvalidSchema, MissingSchema) as err:
    #         print(err)
    #
    # print(results)
    # print(time() - start)







