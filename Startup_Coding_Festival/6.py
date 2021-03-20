# -*- coding: utf-8 -*-
# UTF-8 encoding when using korea

m, n = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(n)]

DP = [[0 for _ in range(m)] for _ in range(n)]
DP[0][0] = G[0][0]
for i in range(n):
    for j in range(m):
        if 0 <= i - 1 < n and 0 <= j - 1 < m:
            DP[i][j] = max(DP[i - 1][j], DP[i][j - 1]) + G[i][j]
        elif 0 <= i - 1 < n:
            DP[i][j] = DP[i - 1][j] + G[i][j]
        elif 0 <= j - 1 < m:
            DP[i][j] = DP[i][j - 1] + G[i][j]
print(DP[-1][-1])

# import heapq

# q = []
# heapq.heappush(q, (0, 0, -G[0][0]))
# max_cost = 0
# D = [[0, 1], [1, 0]]
# while q:
# 	row, col, cost = heapq.heappop(q)
# 	if row == n - 1 and col == m - 1:
# 		max_cost = max(abs(cost), abs(max_cost))
# 		continue

# 	if max_cost > abs(cost):
# 		continue

# 	for r, c in D:
# 		drow, dcol = r + row, c + col
# 		if 0 <= drow < n and 0 <= dcol < m:
# 			heapq.heappush(q, (drow, dcol, cost - G[drow][dcol]))
# print(max_cost)
