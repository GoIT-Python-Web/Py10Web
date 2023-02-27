import pathlib
from queue import Queue
from threading import Thread, Event
import logging


class Writer:
    def __init__(self, filename: str, event_: Event):
        self.filename = filename
        self.files_queue = Queue()
        self.event = event_
        self.file = open(self.filename, 'x', encoding='utf-8')

    def __call__(self, *args, **kwargs):
        while True:
            if self.files_queue.empty():
                if self.event.is_set():
                    break
            else:
                file, content = self.files_queue.get()
                logging.info(f"Writing file {file.name}")
                self.file.write(f"{content}\n")

    def __del__(self):
        self.file.close()


def reader(files_queue: Queue):
    while True:
        if files.empty():
            break

        file = files.get()
        logging.info(f"Read file {file.name}")
        with open(file, 'r', encoding='utf-8') as fd:
            data = []
            for line in fd:
                data.append(line)
            files_queue.put((file, ''.join(data)))


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    event = Event()
    files = Queue()
    list_files = pathlib.Path('.').joinpath('files').glob('*.js')  # **/*.pth
    [files.put(file) for file in list_files]

    writer = Writer('main.js', event)
    if files.empty():
        logging.info('Dir is empty!')
    else:
        tw = Thread(target=writer, name='Writer')
        tw.start()

        threads = []
        for i in range(2):
            tr = Thread(target=reader, args=(writer.files_queue,), name=f'reader#{i}')
            threads.append(tr)
            tr.start()
        [th.join() for th in threads]
        event.set()
