from .MapBase import MapBase
from random import randrange

class HashMapBase(MapBase):

    def __init__(self, capacity=11, p=109345121):
        self._table = [None] * capacity
        self._n = 0
        self._prime = p
        self._scale = 1 + randrange(p-1)
        self._shift = randrange(p)

    def _resize(self):
        print("resize")

    def _hash_func(self, k):
        return (hash(k)*self._scale + self._shift) % self._prime % len(self._table)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        j = self._hash_func(k)
        return self._bucket_getitem(j, k)

    def __setitem__(self, k, v):
        j = self._hash_func(k)
        self._bucket_setitem(j, k, v)
        if self._n > len(self._table):
            self._resize(2 * len(self._table) - 1)

    def __delitem__(self, k):
        j = self._hash_func(k)
        self._bucket_delitem(k)
        self._n -= 1

    def _resize(self, c):
        old = list(self.items())
        self._table = c * [None]
        self._n = 0
        for (k, v) in old:
            self[k] = v