# https://www.acmicpc.net/problem/2252
from collections import deque
def answer(G, L):
    q = deque()
    for x in range(1, len(L)):
        if L[x] == 0:
            q.append(x)
    result = []
    while q:
        result.append(q.popleft())
        for edge in G[result[-1]]:
            L[edge] -= 1
            if L[edge] == 0:
                q.append(edge)
    return result


import sys
input = sys.stdin.readline
n, m = map(int, input().split())
G = {i: set() for i in range(1, n + 1)}
L = [0 for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    G[a].add(b)
    L[b] += 1
print(*answer(G, L))