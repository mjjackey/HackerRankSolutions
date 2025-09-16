"""
Implement an increasing list,
append(self,val): when appending a value, delete the end item less than the appending item
pop(self,index=-1): delete the end item by default
len(self): output the size when updating the list
"""
class IncreaseList(list):
    def __init__(self, iterable):
        if iterable == None:
            super().__init__()
        else:
            if not self.is_increasing():
                raise ValueError("Initial elements are not non-decreasing!")
            super().__init__(iterable)

    def append(self, item):
        # empty list
        if not self:
            super().append(item)
        else:
            if item < self[-1]:
                super().pop()
            super().append(item)
        # print(f"The length of the list is {len(self)}")

    def pop(self, index = -1):
        super().pop(index)
        # print(f"The length of the list is {len(self)}")

    def len(self):
        return super().__len__()

    def __str__(self):
        return f"IncreaseList: {super().__str__()}, The length of the list : {self.__len__()}"

    def is_increasing(self):
        return all(self[i]<self[i+1] for i in range(self.len()-1))


class MyIncreaseList:
    def __init__(self, items=None):
        self._data = list(items) if items else []
        if not self.is_increasing():
            raise ValueError("Initial elements are not non-decreasing!")

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return f"MyIncreaseList: {self._data}. The length of the list : {self.__len__()}"

    def pop(self,index=-1):
        self._data.pop(index)
        # print(f"The length of the list : {self.__len__()}")

    def append(self, item):
        if len(self)==0:
            self._data.append(item)
        else:
            if item <= self._data[-1]:
                self.pop()
            self._data.append(item)
        # print(f"The length of the list : {len(self)}")

    def is_increasing(self):
        return all(self._data[i] < self._data[i + 1] for i in range(len(self) - 1))

if __name__ == '__main__':
    # lst=[1,2,3]
    lst = IncreaseList([1,2,3])
    print(lst)

    lst.append(5)
    print(lst)

    lst.append(4)
    print(lst)

    print(len(lst))

    lst.pop()
    print(lst)

    lst = MyIncreaseList([1, 2, 3])
    print(lst)

    lst.append(5)
    print(lst)

    lst.append(4)
    print(lst)

    print(len(lst))

    lst.pop()
    print(lst)