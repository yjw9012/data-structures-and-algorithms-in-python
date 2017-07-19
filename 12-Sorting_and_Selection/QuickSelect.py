from random import random

def quick_select(S, k):
    if len(S) == 1:
        return S[0]

    pivot = S[0]
    L = [x for x in S if x < pivot]
    E = [x for x in S if x == pivot]
    G = [x for x in S if x > pivot]

    if k <= len(L):
        return quick_select(L, k)
    elif len(L) < k <= len(L) + len(E):
        return pivot
    else:
        return quick_select(G, k - (len(L) + len(E)))


S = [3,10,8,21,1,7]
print(sorted(S))
print(quick_select(S, 2))
