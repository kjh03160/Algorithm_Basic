# https://www.acmicpc.net/problem/1987
def dfs(G, row, col, alphas, count):
    global result, D

    for r, c, in D:
        drow, dcol = r + row, c + col
        if 0 <= drow < len(G) and 0 <= dcol < len(G[0]):
            asc = ord(G[drow][dcol]) - 65
            if not alphas[asc]:
                alphas[asc] = True
                dfs(G, drow, dcol, alphas, count + 1)
                result = max(result, count + 1)
                alphas[asc] = False

import sys
input = sys.stdin.readline
r, c = map(int, input().split())
G = [input().rstrip() for _ in range(r)]
alpha = [False for _ in range(26)]
start = ord(G[0][0]) - 65
alpha[start] = True
D = [(1, 0), (0, 1), (-1, 0), (0, -1)]
result = 1
dfs(G, 0, 0, alpha, 1)
print(result)

