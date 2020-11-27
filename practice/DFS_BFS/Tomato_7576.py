# https://www.acmicpc.net/problem/7576

from collections import deque

def answer(G):
    global one, n, m
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    q = deque()
    q.extend(one)
    while q:
        x = q.popleft()
        for r, c in direction:
            drow = r + x[0]
            dcol = c + x[1]
            if 0 <= drow < n and 0 <= dcol < m and G[drow][dcol] == 0:
                q.append((drow, dcol))
                G[drow][dcol] = 1
                dist[drow][dcol] = dist[x[0]][x[1]] + 1
    return dist

import sys
input = sys.stdin.readline
m, n = map(int, input().split())
G = []
one = []
dist = [[0 for _ in range(m)] for _ in range(n)]
k = 0
for i in range(n):
    temp = list(map(int, input().split()))
    for x in range(len(temp)):
        if temp[x] == 1:
            one.append((i, x))
            dist[i][x] = 1
            k += 1
        if temp[x] == -1:
            dist[i][x] = -1
            k += 1
    G.append(temp)

result = answer(G)
if k == n * m:
    print(0)
else:
    f = False
    max = 1
    for row in range(n):
        for col in range(m):

            if result[row][col] > max:
                max = result[row][col]
            if result[row][col] == 0:
                max = 0
                f = True
                break
        if f:
            break
    print(max - 1)
