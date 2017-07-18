from .HashMapBase import HashMapBase

class ChainHashMap(HashMapBase):

    def _bucket_get_item(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError("Key Error")
        return bucket[k]

    def _bucket_set_item(self, j, k, v):
        bucket = self._table[j]
        if bucket is None:
            self._table[j] = UnsortedTableMap()

        oldsize = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j]) > oldsize:
            self._n += 1

    def _bucket_del_item(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError("Key Error")

        del bucket[k]

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:
                for key in bucket:
                    yield key