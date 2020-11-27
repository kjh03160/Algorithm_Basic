# https://www.acmicpc.net/problem/2178

def answer(row, col):
    global n, m, G, visited, count, ans

    visited[row][col] = True
    if row >= n - 1 and col >= m - 1:
        return ans.append(count)
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for r, c in direction:
        drow = row + r
        dcol = col + c
        if drow >= n or drow < 0 or dcol >= m or dcol < 0:
            continue

        if not visited[drow][dcol] and  G[drow][dcol] == '1':
            count += 1
            answer(drow, dcol)
            visited[drow][dcol] = False
            count -= 1

from collections import deque

def answer2(G, visited):
    global n, m
    dist = [[0 for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
    dist[0][0] = 1
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while q:
        row, col = q.popleft()

        for r, c in direction:
            drow = r + row
            dcol = c + col
            if drow >= n or drow < 0 or dcol >= m or dcol < 0:
                continue
            if not visited[drow][dcol] and G[drow][dcol] == '1':
                q.append((drow, dcol))
                dist[drow][dcol] = dist[row][col] + 1
                visited[drow][dcol] = True
    return dist[n - 1][m - 1]



import sys

input = sys.stdin.readline
n, m = map(int, input().split())
G = []
visited = [[False for _ in range(m)] for _ in range(n)]
for _ in range(n):
    G.append(input())
# count = 1
# ans = []
# answer(0, 0)
# print(min(ans))
print(answer2(G, visited))