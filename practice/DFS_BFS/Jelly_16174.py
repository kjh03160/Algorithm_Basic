# boj.kr/16174

from collections import deque
def answer(G):
    visited = [[False for _ in range(len(G[0]))] for _ in range(len(G))]
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
    direction = [(0, 1), (1, 0)]
    while q:
        row, col = q.popleft()

        if G[row][col] == 0:
            continue

        if row == len(G) - 1 and col == len(G) - 1:
            return 'HaruHaru'

        for r, c in direction:
            drow, dcol = r * G[row][col] + row, c * G[row][col] + col
            if drow >= len(G) or dcol >= len(G):
                continue
            if not visited[drow][dcol]:
                visited[drow][dcol] = True
                q.append((drow, dcol))
    return 'Hing'

import sys
input = sys.stdin.readline
n = int(input())
G = [list(map(int, input().split())) for _ in range(n)]
print(answer(G))