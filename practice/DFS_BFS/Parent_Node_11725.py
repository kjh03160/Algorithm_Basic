# https://www.acmicpc.net/problem/11725
from collections import deque
def answer(G):
    new = [0 for _ in range(len(G) + 1)]
    q = deque()
    visited = [False for _ in range(len(G) + 1)]
    q.append((1, 0))
    visited[1] = True
    while q:
        node, parent = q.popleft()
        new[node] = parent
        for i in G[node]:
            if not visited[i]:
                q.append((i, node))
                visited[i] = True
    print(*new[2:], sep='\n')


import sys
input = sys.stdin.readline
n = int(input())
G = {i: [] for i in range(1, n + 1)}
for _ in range(n - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
answer(G)