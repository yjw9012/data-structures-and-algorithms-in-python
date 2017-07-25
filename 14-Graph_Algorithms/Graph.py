class Graph:

    class Vertex:
        __slots__ = '_data'

        def __init__(self, x):
            self._data = x

        def data(self):
            return self._data

        def __hash__(self):
            return hash(id(self))

    class Edge:
        __slots__ = '_orig', '_dest', '_data'

        def __init__(self, u, v, x):
            self._orig = u
            self._dest = v
            self._data = x

        def endpoints(self):
            return (self._orig, self._dest)

        def opposite(self, v):
            return self._dest if v is self._orig else self._orig

        def data(self):
            return self._data

        def __hash__(self):
            return hash((self._orig, self._dest))

    def __init__(self, directed=False):
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing

    def is_directed(self):
        return self._incoming is not self._outgoing

    def vertex_count(self):
        return len(self._outgoing)

    def vertices(self):
        return self._outgoing.keys()

    def edge_count(self):
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        return total if self.is_directed() else total // 2

    def edges(self):
        result = set()
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())
        return result

    def get_edge(self, u, v):
        return self._outgoing[u].get(v)

    def degree(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

    def incident_edges(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge

    def insert_vertex(self, data=None):
        new_v = self.Vertex(data)
        self._outgoing[new_v] = {}
        if self.is_directed():
            self._incoming[new_v] ={}
        return new_v

    def insert_edge(self, u, v, data=None):
        e = self.Edge(u, v, data)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e