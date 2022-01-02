import time


ex = [1, 2, 3, ['foo', 'bar', 'duck'], 18, [['nested element', [[['crazy nested element']]]]]]
nested_lists = [[1, 2, 3, 4], ['one', 'two', 'three', 'four'], True]


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
    print('This was generator')


call_generator()


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
            return self.flat.__iter__()  # == iter(self.flat)

    def __next__(self):
        if self.cursor >= self.limit:
            raise StopIteration
        self.item = self.obj[self.cursor]
        self.cursor += 1
        if len(self.obj) == 0:
            return self.obj
        return self.item


mine = MyIterator(ex)
for i in mine:
    print(i)
    time.sleep(0.5)

li = [i for i in MyIterator(ex)]
print(li)





