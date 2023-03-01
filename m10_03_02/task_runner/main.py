import pathlib
import sys
from multiprocessing import Process, Queue, Event


class Writer:
    def __init__(self, filename: str, event_: Event):
        self.filename = filename
        self.files_queue = Queue()
        self.event = event_
        self.file = open(self.filename, 'w', encoding='utf-8')

    def __call__(self, *args, **kwargs):
        while True:
            if self.files_queue.empty():
                if self.event.is_set():
                    sys.exit(0)
            else:
                file, content = self.files_queue.get()
                print(f"Writing file {file.name}")
                self.file.write(f"{content}\n")

    def __getstate__(self):
        attributes = {**self.__dict__, 'file': None}
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.file = open(value['filename'], 'w', encoding='utf-8')

    def __del__(self):
        self.file.close()


def reader(work_queue, files):
    while True:
        if files.empty():
            sys.exit(0)

        file = files.get()
        print(f"Read file {file.name}")
        with open(file, 'r', encoding='utf-8') as fd:
            data = []
            for line in fd:
                data.append(line)
            work_queue.put((file, ''.join(data)))


if __name__ == "__main__":

    event = Event()
    files = Queue()

    list_files = pathlib.Path(".").joinpath("files").glob("*.js")
    [files.put(file) for file in list_files]

    writer = Writer('main.js', event)
    if files.empty():
        print('Dir is empty!')
    else:
        pw = Process(target=writer, name='Writer')
        pw.start()

        processes = []
        for i in range(2):
            pr = Process(target=reader, args=(writer.files_queue, files), name=f'reader#{i}')
            processes.append(pr)
            pr.start()
        [pr.join() for pr in processes]
        event.set()
