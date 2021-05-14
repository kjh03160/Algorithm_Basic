# boj.kr/14716

def answer(G):
    visited = [[False for _ in range(len(G[0]))] for _ in range(len(G))]
    count = 0
    for i in range(len(G)):
        for j in range(len(G[0])):
            if not visited[i][j] and G[i][j]:
                dfs(G, i, j, visited)
                count += 1
    return count


def dfs(G, row, col, visited):
    stack = []
    stack.append((row, col))
    while stack:
        row, col = stack.pop()
        visited[row][col] = True

        for r, c, in [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]:
            drow, dcol = row + r, col + c
            if 0 <= drow < len(G) and 0 <= dcol < len(G[0]):
                if not visited[drow][dcol] and G[drow][dcol]:
                    visited[drow][dcol] = True
                    stack.append((drow, dcol))


import sys
input = sys.stdin.readline
m, n = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(m)]
print(answer(G))