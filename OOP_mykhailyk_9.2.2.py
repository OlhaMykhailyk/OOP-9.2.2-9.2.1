from abc import ABCMeta, abstractmethod
from operator import contains


class FileReader:
    def __init__(self, filename, list_of_observers):
        self.filename = filename
        self.list_of_observers = list_of_observers.copy()

    def add_observer(self, observer):
        self.list_of_observers.append(observer)

    def send(self, line):
        for observer in self.list_of_observers:
            observer.onReceive(line)

    def read(self):
        with open(self.filename, 'r') as f:
            for line in f:
                self.send(line)

class Observer(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def onReceive(self, line):
        pass

class LineWriter(Observer):
    def onReceive(self, line):
        print(line)

class WordCounter(Observer):
    def __init__(self):
        self.counter = 0
        super().__init__()

    def onReceive(self, line):
        self.counter += len(line.split())

class WordSearcher(Observer):
    def __init__(self, word):
        self.word = word
        self.contains = False
        super().__init__()

    def onReceive(self, line):
        self.contains = True if line.find(self.word) >= 0 else self.contains

if __name__ == '__main__':
    f = FileReader("testfile", [])

    for i in range(3):
        f.add_observer(LineWriter())
        f.add_observer(WordCounter())
        f.add_observer(WordSearcher("hello"))

    f.read()

    for observer in f.list_of_observers:
        if isinstance(observer, WordCounter):
            print(observer.counter)
        elif isinstance(observer, WordSearcher):
            print(observer.contains)