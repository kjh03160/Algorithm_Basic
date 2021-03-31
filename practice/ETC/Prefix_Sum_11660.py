# https://www.acmicpc.net/problem/11660

def answer(G, M):
    for p1, p2 in M:
        x1, y1, x2, y2 = p1 + p2
        min_row, max_row = min(x1, x2), max(x1, x2)
        min_col, max_col = min(y1, y2), max(y1, y2)
        result = 0
        for row in range(min_row, max_row + 1):
            result += G[row][max_col] - G[row][min_col - 1]
        print(result)

    pass


import sys
input = sys.stdin.readline
n, m = map(int, input().split())
G = [[0 for _ in range(n + 1)]]

for _ in range(n):
    x = [0] + list(map(int, input().split()))
    for i in range(1, len(x)):
        x[i] += x[i - 1]
    G.append(x)
M = []
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    M.append(((x1, y1), (x2, y2)))
answer(G, M)