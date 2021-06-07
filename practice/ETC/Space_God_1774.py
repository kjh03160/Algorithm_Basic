# boj.kr/1774

def find_parent(parents, a):
    if parents[a] == a:
        return a
    parents[a] = find_parent(parents, parents[a])
    return parents[a]


def union_parent(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)

    if a < b:
        parents[a] = b
    elif a > b:
        parents[b] = a
    else:
        return False
    return True


def answer(L):
    L.sort()

    count = 0.0
    for c, a, b in L:
        if union_parent(parents, a, b):
            count += c
    return count


import sys

input = sys.stdin.readline
n, m = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(n)]
X = []
from itertools import combinations

for i in combinations([i for i in range(len(G))], 2):
    a, b = G[i[0]], G[i[1]]
    dist = ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** (1 / 2)
    X.append((dist, i[0] + 1, i[1] + 1))

parents = [i for i in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    a, b = G[x - 1], G[y - 1]
    union_parent(parents, x, y)
print("%.2f" % answer(X))