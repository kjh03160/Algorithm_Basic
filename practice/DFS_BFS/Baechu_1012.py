# https://www.acmicpc.net/problem/1012


def dfs(r, c):
    global MAP, M, N
    direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    MAP[r][c] = 0
    for row, col in direction:
        drow = r + row
        dcol = c + col
        if drow < 0 or drow == M or dcol < 0 or dcol == N:
            continue
        if MAP[drow][dcol] == 1:
            MAP[drow][dcol] = 0
            dfs(drow, dcol)
import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    MAP = [[0]*N for _ in range(M)]
    count = 0

    for _ in range(K):
        X, Y = map(int, input().split())
        MAP[X][Y] = 1

    for i in range(M):
        for j in range(N):
            if MAP[i][j] == 1:
                dfs(i, j)
                count += 1
    print(count)