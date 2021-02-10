# https://www.acmicpc.net/problem/1405

def answer(G, P):
    global count
    visited = [[False for _ in range(len(G))] for _ in range(len(G))]
    start_r, start_c = len(G) // 2, len(G) // 2
    dfs(start_r, start_c, P, visited, 1, 0)

    return "%.10f" % (count)


def dfs(row, col, P, visited, perc, end):
    global count
    DIRECTION = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited[row][col] = True
    if end == len(G) // 2:
        count += perc
        return

    for i in range(len(DIRECTION)):
        drow, dcol = row + DIRECTION[i][0], col + DIRECTION[i][1]
        if not visited[drow][dcol]:
            dfs(drow, dcol, P, visited, perc * (P[i] / 100), end + 1)
            visited[drow][dcol] = False


import sys

input = sys.stdin.readline
x = list(map(int, input().split()))
n = x[0]
G = []
for _ in range(n * 2 + 1):
    G.append([0 for i in range(n * 2 + 1)])
perc = x[1:]
count = 0

print(answer(G, perc))
