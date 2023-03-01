"""
Завдання: Сортування файлів у папці. Скопіювати файли із зазначеної папки і покласти в нову папку з
розширенням цього файлу.
"""

import argparse
from pathlib import Path
from shutil import copyfile
from multiprocessing import Process, current_process

parser = argparse.ArgumentParser(description="Sorting folder")
parser.add_argument("--source", "-s", required=True, help="Source folder")
parser.add_argument("--output", "-o", default="dist", help="Output folder")
args = vars(parser.parse_args())
source = args.get("source")
output = args.get("output")
output_folder = Path(output)  # dist


def read_folder(path: Path) -> None:
    pass


def copy_file(file: Path) -> None:
    pass


if __name__ == "__main__":
    pr_rf = Process(target=read_folder, args=(Path(source),))
    pr_rf.start()
    pr_rf.join()
    print("Finished")
