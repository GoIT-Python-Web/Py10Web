import pathlib
from multiprocessing import Process, Queue, Event


class Concat:
    pass


def reader(work_queue, files_queue):
    pass


if __name__ == "__main__":

    event_reader = Event()
    files_queue = Queue()

    list_files = pathlib.Path(".").joinpath("files").glob("*.js")
