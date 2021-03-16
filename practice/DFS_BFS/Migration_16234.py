# https://www.acmicpc.net/problem/16234

from collections import deque
def bfs(G, L, R, r_, c_, visited):
    DIR = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    q = deque()
    q.append((r_, c_, G[r_][c_]))
    new = {(r_, c_)}

    visited[r_][c_] = True
    people = 0
    while q:
        row, col, p = q.popleft()
        people += p
        for r, c, in DIR:
            drow, dcol = row + r, c + col
            if drow < 0 or dcol < 0 or drow >= len(G) or dcol >= len(G):
                continue

            if (drow, dcol) not in new and not visited[drow][dcol]:
                if L <= abs(G[drow][dcol] - G[row][col]) <= R:
                    visited[drow][dcol] = True
                    q.append((drow, dcol, G[drow][dcol]))
                    new.add((drow, dcol))

    for r, c in new:
        G[r][c] = people // len(new)

    return len(new) - 1


def answer(G):
    result = 0
    while True:
        visited = [[False for _ in range(n)] for _ in range(n)]
        x = 0
        for i in range(len(G)):
            for j in range(len(G)):
                if not visited[i][j]:
                    x += bfs(G, L, R, i, j, visited)
        if not x:
            break
        result += 1
    return result


import sys
input = sys.stdin.readline
n, L, R = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(n)]
print(answer(G))
