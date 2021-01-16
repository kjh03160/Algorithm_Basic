# https://www.acmicpc.net/problem/7562

from collections import deque
def answer(now_r, now_c, dest_r, dest_c):
    global G, DIRECTION, ans, visited

    visited[now_r][now_c] = True

    q = deque()
    for i in DIRECTION:
        q.append((now_r, now_c, i[0], i[1], 0))

    while q:
        nrow, ncol, drow, dcol, a = q.popleft()
        if nrow == dest_r and ncol == dest_c:
            return a

        row, col = nrow + drow, ncol + dcol

        if row >= len(G) or col >= len(G) or row < 0 or col < 0:
            continue

        if not visited[row][col]:
            a += 1
            visited[row][col] = True
            for i in DIRECTION:
                q.append((row, col, i[0], i[1], a))

import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
DIRECTION = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

t = int(input())
ans = []
for i in range(t):
    x = int(input())
    G = [[0 for _ in range(x)] for _ in range(x)]
    visited = [[False for _ in range(x)] for _ in range(x)]
    now_r, now_c = map(int, input().split())
    dest_r, dest_c = map(int, input().split())
    ans.append(answer(now_r, now_c, dest_r, dest_c))

print(*ans, sep='\n')

