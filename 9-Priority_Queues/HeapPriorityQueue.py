from .PriorityQueueBase import PriorityQueueBase

class HeapPriorityQueue(PriorityQueueBase):

    def __init__(self, contents=()):
        self._data = [self._Item(k, v) for k,v in contents]
        if len(self._data) > 0:
            self._heapify()

    def _heapify(self):
        start = self._parent(len(self) - 1)
        for j in range(start, -1, -1):
            self._down_heap_bubble(j)

    def __len__(self):
        return len(self._data)

    def add(self, k, v):
        self._data.append(PriorityQueueBase._Item(k, v))
        self._up_heap_bubble()

    def _up_heap_bubble(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < parent:
            self._swap(parent, j)
            self._up_heap_bubble(parent)

    def min(self):
        if self.is_empty():
            raise Exception("THIS QUEUE IS EMPTY")
        root = self._data[0]
        return (root._key, root._val)

    def remove_min(self):
        if self.is_empty():
            raise Exception("THIS QUEUE IS EMPTY")
        root = self.min()
        self._down_heap_bubble()
        return root

    def _down_heap_bubble(self, j):
        if self._has_left(j):
            left = self._left(j)
            smaller_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    smaller_child = right

            if self._data[smaller_child] < self._data[j]:
                self._swap(smaller_child, j)
                self._down_heap_bubble(smaller_child)

    def _parent(self, j):
        return (j - 1) // 2

    def _left(self, j):
        return 2 * j + 1

    def _right(self, j):
        return 2 * j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)

    def _has_right(self, j):
        return self._right(j) < len(self._data)

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]








