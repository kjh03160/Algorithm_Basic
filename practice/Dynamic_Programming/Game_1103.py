# boj.kr/1103

def answer(G):
    return dfs(G, 0, 0)


def dfs(G, row, col):
    global visited, DP, direction

    if DP[row][col] != 0:
        return DP[row][col]

    DP[row][col] = 1
    visited[row][col] = True
    for r, c, in direction:
        drow, dcol = r * G[row][col] + row, c * G[row][col] + col
        if 0 <= drow < len(G) and 0 <= dcol < len(G[0]) and G[drow][dcol]:
            if visited[drow][dcol]:
                print(-1)
                sys.exit()
            DP[row][col] = max(DP[row][col], dfs(G, drow, dcol) + 1)
    visited[row][col] = False
    return DP[row][col]


import sys
sys.setrecursionlimit(51 * 51)
input = sys.stdin.readline
n, m = map(int, input().split())
G = []
for _ in range(n):
    x = input().rstrip()
    k = []
    for i in x:
        if i.isdigit():
            k.append(int(i))
        else:
            k.append(0)
    G.append(k)

direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
DP = [[0 for _ in range(len(G[0]))] for _ in range(len(G))]
visited = [[False for _ in range(len(G[0]))] for _ in range(len(G))]
print(answer(G))
