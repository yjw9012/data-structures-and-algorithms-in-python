class Partition:

    class Position:

        def __init__(self, container, e):
            self._container = container
            self._element = e
            self._size = 1
            self._parent = self

        def element(self):
            return self._element

    def make_group(self, e):
        return self.Position(self, e)

    def find(self, p):
        if p.parent == p:
            return p

        p._parent = self.find(p._parent)
        return p._parent

    def union(self, p, q):
        root_p = self.find(q)
        root_q = self.find(q)

        bigger_tree = smaller_tree = root_p
        if root_p is not root_q:

            if root_p._size > root_q._size:
                bigger_tree = root_p
                smaller_tree = root_q
            else:
                bigger_tree = root_q
                smaller_tree = root_p

            smaller_tree._parent = bigger_tree
            bigger_tree._size += smaller_tree._size

        return bigger_tree