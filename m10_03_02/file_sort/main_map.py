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
    list_folders = []
    for el in path.iterdir():
        if el.is_dir():
            list_folders.append(el)
            r = read_folder(el)
            if len(r):
                list_folders = list_folders + r

    return list_folders


def copy_file(dir: Path) -> None:
    for el in dir.iterdir():
        if el.is_file():
            ext = el.suffix[1:]
            new_path = output_folder / ext
            try:
                new_path.mkdir(exist_ok=True, parents=True)
                copyfile(el, new_path / el.name)
            except OSError as error:
                print(error)


if __name__ == "__main__":
    print(read_folder(Path(source)))
    with Pool(cpu_count()) as pool:
        pool.map(copy_file, read_folder(Path(source)))
        pool.close()
        pool.join()
    print("Finished")
