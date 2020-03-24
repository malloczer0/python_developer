from array import array

class customList:
    """
    __new__,
    __init__,
    __len__,
    __contains__,
    __getitem__,
    __setitem__,
    __delitem__,
    __reversed__,
    __iter__,
    __str__, !
    append,
    pop,
    index,
    insert,
    __count__,
    __iadd__,
    remove,
    extend,
    clear
    """

    def __new__(cls, *args, **kwargs):
        print('new')
        return object.__new__(cls)

    def __init__(self, *args):
        print('init')
        if args:
            if type(args[0]) == int:
                self._o = array('i', args)
            elif type(args[0]) == str:
                self._o = array('u', args)
            elif type(args[0]) == float:
                self._o = array('f', args)
        else:
            self._o = None

    def __len__(self):
        if self._o is not None:
            return len(self._o)
        return 0

    def __contains__(self, item):
        if self._o is not None:
            return item in self._o
        return False

    def __getitem__(self, key):
        return self._o[key]

    def __setitem__(self, key, value):
        if key >= len(self._o):
            raise Exception("Index does not exist")
        if type(value) != type(self._o[key]):
            raise Exception("Wrong Type")
        else:
            self._o[key] = value

    def __delitem__(self, key):
        if key >= len(self._o):
            raise Exception("Index does not exist")
        del self._o[key]

    def __reversed__(self):
        if self._o is not None:
            return self._o[::-1]

    def __iter__(self):
        for i in range(self._o.buffer_info()[1]):
            yield self._o[i]


    def append(self, value):
        if self._o is not None:
            if type(value) != type(self._o[0]):
                raise Exception("Wrong Type")
            self._o.fromlist([value])
        else:
            if type(value) == int:
                self._o = array('i', [value])
            elif type(value) == str:
                self._o = array('u', [value])
            elif type(value[0]) == float:
                self._o = array('f', [value])

    def pop(self, key=None):
        if key is None:
            key = len(self._o) - 1
        while key >= len(self._o):
            key -= len(self._o)
        while key < 0:
            key += len(self._o)
        _temp = self._o[key]
        del self._o[key]
        return _temp

    def index(self, value):
        if self._o is None:
            raise Exception("Empty List")
        if type(value) != type(self._o[0]):
            print(type(value), ' ', type(self._o[0]))
            raise Exception("Wrong type")
        for i in range(len(self._o)):
            if self._o[i] == value:
                return i
        raise Exception("Index does not exist")

    def insert(self, key, value):
        self.__setitem__(key, value)

    def __count__(self, item):
        count = 0
        for i in self._arr:
            if i == item:
                count += 1
        return count

    def __iadd__(self, _oth):
        if _oth._o is None:
            return self
        if type(_oth._o[0] == self._o[0]):
            self._o += _oth._o
            return self
        else:
            raise Exception("Wrong Type")

    def remove(self, value):
        if self._o is None:
            raise Exception("No value")
        if type(self._o[0]) != type(value):
            raise Exception("Wrong type")
        for i, x in enumerate(self._o):
            if x == value:
                self.pop(i)
                break
        else:
            raise Exception("No value")

    def extend(self, other):
        return self.__iadd__(other)

    def clear(self):
        self._o = None
        return self


def main():
    l = customList(1, 3, 3, 7, 3, 2, 2, 8)
    print(len(l))
    print(l.__contains__(3))
    l[3] = 1488
    print(l[3])
    del l[0]
    l.append(1)
    l.pop(-7)
    print(l.index(1488))
    l.insert(1, 0)
    for i in l:
        print(i)
    print(reversed(l))
    print(l.index(0))
    l1 = l
    l1.remove(3)
    l.extend(l1)
    l1.clear()



if __name__ == '__main__':
    main()