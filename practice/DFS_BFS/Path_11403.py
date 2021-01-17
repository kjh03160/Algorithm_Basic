# https://www.acmicpc.net/problem/11403

from collections import deque


def answer(i, j):
    global n
    visited = [0 for _ in range(n + 1)]
    q = deque()
    q.extend(G[i])
    while q:
        x = q.popleft()
        if x == j:
            return 1
        for edge in G[x]:
            if not visited[edge]:
                visited[edge] = True
                q.append(edge)


import sys

input = sys.stdin.readline
n = int(input())
G = {i: [] for i in range(1, n + 1)}
for i in range(1, n + 1):
    temp = list(map(int, input().split()))
    G[i] = [x for x in range(1, len(temp) + 1) if temp[x - 1]]

ans = [[0 for _ in range(n)] for _ in range(n)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        result = answer(i, j)
        ans[i - 1][j - 1] = result if result else 0
    print(" ".join(map(str, ans[i - 1])))
