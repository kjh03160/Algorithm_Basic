# https://www.acmicpc.net/problem/1520

def answer(r, c):
    global count, visited, G, DP
    if r == n - 1 and c == m - 1:
        # count += 1
        return 1
    #print(r, c)
    direction = [(1, 0), (0, 1), (0, -1), (-1, 0)]
    if DP[r][c] == -1:
        DP[r][c] = 0
        for row, col in direction:
            drow = r + row
            dcol = c + col
            #print(drow, dcol)
            if drow >= n or drow < 0 or dcol < 0 or dcol >= m or G[r][c] <= G[drow][dcol]:
                continue

            DP[r][c] += answer(drow, dcol)
    return DP[r][c]
    pass

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
n, m = map(int, input().split())
DP = [[-1 for _ in range(m)] for _ in range(n)]
G = [list(map(int, input().split())) for _ in range(n)]
count = 0
visited = [[False for _ in range(m)] for __ in range(n)]
answer(0, 0)
print(DP[0][0])