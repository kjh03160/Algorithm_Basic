# boj.kr/1915

def answer(G):
    DP = [[0 for _ in range(len(G[0]) + 1)] for _ in range(len(G) + 1)]
    size = 0
    for i in range(1, len(G) + 1):
        for j in range(1, len(G[0]) + 1):
            if G[i - 1][j - 1] != 1:
                continue
            DP[i][j] = min(DP[i - 1][j], DP[i][j - 1], DP[i - 1][j - 1]) + 1

            size = max(DP[i][j], size)
    return size ** 2


import sys
input = sys.stdin.readline
n, m = map(int, input().split())
G = [list(map(int, list(input().rstrip()))) for _ in range(n)]
print(answer(G))