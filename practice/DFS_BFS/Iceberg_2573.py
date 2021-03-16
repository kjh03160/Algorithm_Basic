# https://www.acmicpc.net/problem/2573
def dfs(row, col, count, visited):
    D = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    for r_, c_ in D:
        if G[row + r_][col + c_] == 0:
            count += 1
    stack = [(row, col, count)]
    new = [(row, col, count)]
    while stack:
        r, c, count = stack.pop()

        for row, col in D:
            drow, dcol = r + row, c + col
            if not visited[drow][dcol] and G[drow][dcol]:
                visited[drow][dcol] = True
                count = 0
                for r_, c_ in D:
                    if G[drow + r_][dcol + c_] == 0:
                        count += 1
                stack.append((drow, dcol, count))
                new.append((drow, dcol, count))

    for r, c, count in new:
        G[r][c] -= count
        if G[r][c] < 0:
            G[r][c] = 0
    return True

def answer(G):
    count = 0
    while True:
        visited = [[False for _ in range(len(G[0]))] for _ in range(len(G))]
        x = 0
        f = False
        for i in range(1, len(G) - 1):
            for j in range(1, len(G[0]) - 1):
                if not visited[i][j]:
                    visited[i][j] = True
                    if G[i][j]:
                        if f:
                            return count
                        f = f or dfs(i, j, 0, visited)
                    else:
                        x += 1
        count += 1

        if x == (len(G) - 2) * (len(G[0]) - 2):
            return 0

    return count


import sys

input = sys.stdin.readline
n, m = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(n)]
print(answer(G))
