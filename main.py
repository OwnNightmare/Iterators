from typing import Any


def my_iter(pack: list):
    for i in pack:
        if type(i) == list:
            for s in i:
                yield s
        else:
            yield i


ex = [1, 2, 3, None, ['foo', 'bar'], 18, ['some nested element']]
for item in (my_iter(ex)):
    print(item)


flatted = [i for i in my_iter(ex)]
print(flatted)
