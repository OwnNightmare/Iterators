import time


ex = [1, 2, 3, ['foo', 'bar', 'duck'], 18, [['nested element', [[['crazy nested element']]]]]]
nested_lists = [[1, 2, 3, 4], ['one', 'two', 'three', 'four']]


def my_generator(pack: list):
    for elem in pack:
        if isinstance(elem, list):
            for nested_elem in my_generator(elem):
                yield nested_elem
        else:
            yield elem


def call_generator():
    for item in (my_generator(ex)):
        print(item)

    flatted = [i for i in my_generator(ex)]
    print(flatted)
    print('This was generator', '\n')


class MyIterator:

    def __init__(self, obj: list):
        self.obj = obj
        self.flat = []
        self.cursor = 0
        self.limit = len(obj)

    def __iter__(self, data: 'omit or List' = None):
        if data is None:
            for el in self.obj:
                if isinstance(el, list):
                    self.__iter__(el)
                else:
                    self.flat.append(el)
            return self.flat.__iter__()
        else:
            for el in data:
                if isinstance(el, list):
                    self.__iter__(el)
                else:
                    self.flat.append(el)
            return self.flat

    def __next__(self):
        if self.cursor >= len(self.flat):
            raise StopIteration
        self.item = self.flat[self.cursor]
        self.cursor += 1
        return self.item


if __name__ == '__main__':
    call_generator()

    mine = MyIterator(ex)
    for i in mine:
        print(i)

    li = [i for i in MyIterator(ex)]
    print(li, '\n', 'This was Iterator')



