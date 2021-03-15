# https://www.acmicpc.net/problem/10026

def dfs_1(G, row, col, visited, char):
    DIR = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    stack = []
    visited[row][col] = True
    stack.append((row, col))
    while stack:
        row, col = stack.pop()

        for r, c in DIR:
            drow, dcol = row + r, col + c
            if drow < 0 or dcol < 0 or dcol >= len(G) or drow >= len(G):
                continue
            if not visited[drow][dcol]:
                if G[drow][dcol] != char:
                    continue
                visited[drow][dcol] = True
                stack.append((drow, dcol))

def dfs_2(G, row, col, visited, char):
    DIR = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    stack = []
    stack.append((row, col))
    visited[row][col] = True

    while stack:
        row, col = stack.pop()

        for r, c in DIR:
            drow, dcol = row + r, col + c
            if drow < 0 or dcol < 0 or dcol >= len(G) or drow >= len(G):
                continue
            if not visited[drow][dcol]:
                if char == "R" or char == "G":
                    if G[drow][dcol] == "B":
                        continue
                else:
                    if G[drow][dcol] != char:
                        continue
                visited[drow][dcol] = True
                stack.append((drow, dcol))


def answer(G):
    visited1 = [[False for _ in range(len(G))] for _ in range(len(G))]
    visited2 = [[False for _ in range(len(G))] for _ in range(len(G))]
    ok, no = 0, 0
    for i in range(len(G)):
        for j in range(len(G)):
            if not visited1[i][j]:
                dfs_1(G, i, j, visited1, G[i][j])
                ok += 1
            if not visited2[i][j]:
                dfs_2(G, i, j, visited2, G[i][j])
                no += 1
    return ok, no


import sys
input = sys.stdin.readline
n = int(input())
G = [input() for _ in range(n)]
print(*answer(G))
