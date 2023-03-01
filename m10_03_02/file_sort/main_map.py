"""
Завдання: Сортування файлів у папці. Скопіювати файли із зазначеної папки і покласти в нову папку з
розширенням цього файлу.
"""

import argparse
from pathlib import Path
from shutil import copyfile
from multiprocessing import Pool, cpu_count

parser = argparse.ArgumentParser(description="Sorting folder")
parser.add_argument("--source", "-s", required=True, help="Source folder")
parser.add_argument("--output", "-o", default="dist", help="Output folder")
args = vars(parser.parse_args())
source = args.get("source")
output = args.get("output")
output_folder = Path(output)  # dist


def read_folder(path: Path) -> list:
    pass


def copy_file(dir: Path) -> None:
    pass


if __name__ == "__main__":
    with Pool(cpu_count()) as pool:
        pool.map(copy_file, read_folder(Path(source)))
        pool.close()
        pool.join()

    print("Finished")
