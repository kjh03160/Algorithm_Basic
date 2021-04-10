# boj.kr/11048

def answer(G):
    DP = [[0 for _ in range(len(G[0]))] for _ in range(len(G))]

    for i in range(len(G)):
        for j in range(len(G[0])):
            if i - 1 >= 0 and j - 1 >= 0:
                DP[i][j] = max(DP[i][j - 1], DP[i - 1][j], DP[i - 1][j - 1]) + G[i][j]
            else:
                DP[i][j] = max(DP[i][j - 1], DP[i - 1][j]) + G[i][j]
    return DP[-1][-1]


import sys
input = sys.stdin.readline
n, m = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(n)]
print(answer(G))