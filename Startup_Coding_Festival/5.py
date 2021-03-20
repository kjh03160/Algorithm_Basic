# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
m, n = map(int, input().split())
G = []
C = []
for i in range(n):
    x = input()
    for j in range(len(x)):
        if x[j] == "c":
            C.append((i, j))
    G.append(x)

from collections import deque

D = [[1, 0], [0, 1], [0, -1], [-1, 0]]
q = deque()
for i in range(len(C)):
    q.append((C[i][0], C[i][1], 0))
visited = [[False for _ in range(m)] for _ in range(n)]
min_count = float('inf')
while q:
    r, c, count = q.popleft()

    if r == n - 1 and G[r][c] == ".":
        min_count = min(min_count, count)
        continue
    if count > min_count:
        continue

    for row, col in D:
        drow, dcol = r + row, c + col
        if 0 <= drow < n and 0 <= dcol < m:
            if not visited[drow][dcol] and G[drow][dcol] == ".":
                visited[drow][dcol] = True
                if col:
                    q.append((drow, dcol, count + 1))
                else:
                    q.append((drow, dcol, count))
# print(min_count)
print(min_count) if min_count != float('inf') else print(-1)