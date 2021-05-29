# boj.kr/21772

def backtrack(G, row, col, time, eat):
    global result, t

    if t == time:
        result = max(result, eat)
        return

    for r, c in direction:
        drow, dcol = r + row, c + col
        if 0 <= drow < len(G) and 0 <= dcol < len(G[0]):
            if G[drow][dcol] == "S":
                G[drow][dcol] = "."
                backtrack(G, drow, dcol, time + 1, eat + 1)
                G[drow][dcol] = "S"
            elif G[drow][dcol] == "." or G[drow][dcol] == "G":
                backtrack(G, drow, dcol, time + 1, eat)
    backtrack(G, row, col, time + 1, eat)


import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
n, m, t = map(int, input().split())
G = []
r, c = None, None
for i in range(n):
    x = list(input().rstrip())
    for j in range(len(x)):
        if x[j] == "G":
            r, c = i, j
    G.append(x)
result = 0
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
backtrack(G, r, c, 0, 0)
print(result)
