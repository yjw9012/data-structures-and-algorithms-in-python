def DFS(G, u):
    forest = {}
    for v in G.vertices():
        if v not in forest:
            forest[v] = None
            search(G, v, forest)
    return forest

def search(G, u, discovered):

    for e in G.incident_edges(u):
        v = e.opposite(u)
        if v not in discovered:
            discovered[v] = e
            search(G, v, discovered)

def construct_path(u, v, discovered):
    cur = v
    path = []
    while cur is not u:
        path.append(cur)
        cur = discovered[cur].opposite(cur)

    path.append(cur)
    path.reverse()
    return path

def BFS(G, s, discovered):
    q = Queue()
    q.enqueue(s)
    while not q.empty():
        u = q.dequeue()
        for e in G.incident_edges(u):
            v = e.opposite(u)
            if v not in discovered:
                discovered[v] = e
                q.enqueue(v)