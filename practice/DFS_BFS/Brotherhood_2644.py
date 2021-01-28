# https://www.acmicpc.net/problem/2644

from collections import deque
def answer(G, x, y):
    visited = [False for _ in range(len(G) + 1)]
    q = deque()
    q.append((x, 0))
    visited[x] = True
    while q:
        node, count = q.popleft()

        for brother in G[node]:
            if not visited[brother]:
                if brother == y:
                    return count + 1
                visited[brother] = True
                q.append((brother, count + 1))
    return -1


import sys
input = sys.stdin.readline
n = int(input())
G = {i: [] for i in range(1, n + 1)}
x, y = map(int, input().split())
for _ in range(int(input())):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
print(answer(G, x, y))