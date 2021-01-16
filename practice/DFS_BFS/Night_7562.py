# https://www.acmicpc.net/problem/7562

from collections import deque
def answer(now_r, now_c, dest_r, dest_c):
    global G, DIRECTION, visited

    q = deque()
    q.append((now_r, now_c, 0))
    visited[now_r][now_c] = True
    while q:
        row, col, count = q.popleft()
        if row == dest_r and col == dest_c:
            return count
        for r, c in DIRECTION:
            drow = r + row
            dcol = c + col

            if drow >= len(G) or dcol >= len(G) or drow < 0 or dcol < 0:
                continue
            if not visited[drow][dcol]:
                visited[drow][dcol] = True
                q.append((drow, dcol, count + 1))


import sys
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

