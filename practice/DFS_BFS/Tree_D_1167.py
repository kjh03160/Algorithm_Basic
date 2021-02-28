# https://www.acmicpc.net/problem/1167


from collections import deque
def answer(G, k):
    global visited
    q = deque()
    q.append((k, 0))
    visited = [False for i in range(len(G) + 1)]
    visited[k] = True
    max_cost = 0
    while q:
        node, cost = q.popleft()

        if max_cost < cost:
            max_cost = cost

        for child in G[node].keys():
            if not visited[child]:
                visited[child] = True
                q.append((child, G[node][child] + cost))

    return max_cost

def dfs(G, index, cost):
    global visited, m, start
    visited[index] = True

    for node in G[index]:
        if not visited[node]:
            dfs(G, node, cost + G[index][node])
            visited[node] = True

    if m < cost:
        m = cost
        start = index

import sys
sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline
n = int(input())
G = {i: {} for i in range(1, n + 1)}
for _ in range(n - 1):
    x = list(map(int, input().split()))
    a = x[0]
    for i in range(1, len(x) - 1, 2):
        b, c = x[i: i + 2]
        G[a][b] = c
        G[b][a] = c

visited = [False for _ in range(len(G) + 1)]
start = 1
m = 0
dfs(G, 1, 0)

m = answer(G, start)
print(m)
