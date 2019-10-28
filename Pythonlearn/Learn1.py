


ary=list()
ary.append(1) 
ary.append(2) 
ary.remove(1) 
print(len(ary)) #len() :length

# ADT-OOT编程学习

class Bag(object):
    "新的数据类型:Bag"
    def __init__(self,maxsize=10):
        self.maxsize=maxsize
        self._items=list()
    def add(self,item):
        if len(self)>=self.maxsize:
            return Exception('full')
        self._items.append(item)
    def remove(self,item):
        self._items.remove(item)
    def __len__(self):
        return len(self._items)
    def __iter__(self):
        for item in self._items:
            yield item


def test_beg():
    bag=Bag()
    bag.add(1)
    bag.add(2)
    bag.add(3)
    assert len(bag)==3
    bag.remove(3)
    assert len(bag)==2
    for i in bag:
        print(i)

