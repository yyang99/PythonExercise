from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def notify(self, data):
        ...

class Publisher:
    def __init__(self):
        self.observers = []

    def add(self, observer):
        if observer in self.observers:
            print(f"Error add {observer}, the observer already subscribe")
        else:
            self.observers.append(observer)

    def remove(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError as e:
            print(f"Error remove observer {observer}, the observer has not subscribed before")

    def notify(self):
        [o.notify(self) for o in self.observers]


class DataFormater(Publisher):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self._data: int = 0

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_value):
        try:
            self._data = int(new_value)
        except ValueError as e:
            print(f"Error: {e}")
        else:
            self.notify()

    def __str__(self):
        return f"{type(self).__name__}: '{self.name }' now has data == {self._data}"

class HexFormater(Observer):
    def notify(self, publisher):
        print(f"{type(self).__name__}: {publisher.name} now has a HEX value {publisher.data:#x}")

class BinFormater(Observer):
    def notify(self, publisher):
        print(f"{type(self).__name__}: {publisher.name} now has a Bin value {publisher.data:#b}")

if __name__ == '__main__':
    df = DataFormater('test1')
    df.data = 10
    print(df)
    print()
    df.add(HexFormater())
    df.data = 16
    print(df)

    df.add(BinFormater())
    df.data = 17
    print(df)

    df.data = 'hello'