"""
Завдання: Сортування файлів у папці. Скопіювати файли із зазначеної папки і покласти в нову папку з розширенням цього
файлу.
"""

import argparse
import asyncio
from time import time

from aiopath import AsyncPath
from aioshutil import copyfile


parser = argparse.ArgumentParser(description='Sorting folder')
parser.add_argument('--source', '-s', required=True, help='Source folder')
parser.add_argument('--output', '-o', default='dist', help='Output folder')
args = vars(parser.parse_args())
source = args.get('source')
output = args.get('output')
output_folder = AsyncPath(output)  # dist


async def read_folder(path: AsyncPath) -> None:
    async for el in path.iterdir():
        if await el.is_dir():
            await read_folder(el)
        else:
            await copy_file(el)


async def copy_file(file: AsyncPath) -> None:
    ext = file.suffix[1:]
    new_path = output_folder / ext
    try:
        await new_path.mkdir(exist_ok=True, parents=True)
        await copyfile(file, new_path / file.name)
    except OSError as error:
        print(error)


if __name__ == '__main__':
    start = time()
    asyncio.run(read_folder(AsyncPath(source)))
    print(f'Completed: {time() - start}')


