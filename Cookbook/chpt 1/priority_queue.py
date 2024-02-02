import heapq

class PriorityQueue:
    def __init__(self) -> None:
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name) -> None:
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)
    

if __name__ == '__main__':
    q = PriorityQueue()
    q.push(Item('N'), 1)
    q.push(Item('K'), 2)
    q.push(Item('S'), 5)
    q.push(Item('B'), 9)
    q.push(Item('A'), 13)
    q.push(Item('C'), 11)

    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())