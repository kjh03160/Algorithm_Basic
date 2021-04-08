# boj.kr/14712

def dfs(row, col):
    global n, m, result

    if row == n + 1:
        result += 1
        return

    # 4개가 모이지 않을 때
    if not (G[row][col - 1] == 1 and G[row - 1][col] == 1 and G[row - 1][col - 1] == 1):
        G[row][col] = 1
        # 네모를 둘 때
        if col + 1 == m + 1:
            dfs(row + 1, 1)
        else:
            dfs(row, col + 1)
        G[row][col] = 0

    # 네모를 안 둘때
    if col + 1 == m + 1:
        dfs(row + 1, 1)
    else:
        dfs(row, col + 1)

import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline
n, m = map(int, input().split())
G = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
result = 0
dfs(1, 1)
print(result)