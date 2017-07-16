class PriorityQueueBase:

    class _Item:

        def __init__(self, key, val):
            self._key = key
            self._val = val

        def __lt__(self, other):
            return self._key < other._key

    def is_empty(self):
        return len(self) == 0

    