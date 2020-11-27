# https://www.acmicpc.net/problem/7569
from collections import deque

def answer(G):
    global n, m, h, visited, one
    direction = [(0, 0, 1), (0, 1, 0), (0, -1, 0), (0, 0, -1), (1, 0, 0), (-1, 0, 0)]

    q = deque()
    q.extend(one)
    while q:
        height, row, col = q.popleft()

        visited[height][row][col] = True
        for r, c, h1 in direction:
            drow = r + row
            dcol = c + col
            dheight = h1 + height

            if 0 <= drow < n and 0 <= dcol < m and 0 <= dheight < h and G[dheight][drow][dcol] == 0:
                q.append((dheight, drow, dcol))
                G[dheight][drow][dcol] = G[height][row][col] + 1
    pass

import sys
input = sys.stdin.readline
m, n, h = map(int, input().split())
G = []
one = []
visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]
for h_ in range(h):
    t = []
    for x in range(n):
        temp = list(map(int, input().split()))
        for y in range(m):
            if temp[y] == 1:
                one.append((h_, x, y))
        t.append(temp)
    G.append(t)

result = answer(G)
max_v = 1
for height in range(h):
    flag = False
    for row in range(n):
        for col in range(m):
            if G[height][row][col] == 0:
                max_v = 0
                flag = True
                break
            if G[height][row][col] > max_v:
                max_v = G[height][row][col]
        if flag:
            break
    if flag:
        break
print(max_v - 1)