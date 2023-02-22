from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class PrintCommand(Command):
    def __init__(self, message: str):
        self.message = message

    def execute(self):
        print(self.message)


class HelloCommand(PrintCommand):
    def __init__(self):
        super().__init__("Hello")


class ByeCommand(PrintCommand):
    def __init__(self):
        super().__init__("Bye")


if __name__ == '__main__':
    hello = HelloCommand()
    by = ByeCommand()
    hello.execute()
    print('ADKJALkdjadalk')
    by.execute()
    