# acmicpc.net/problem/1890

def answer(G):
    DP = [[0 for _ in range(len(G))] for _ in range(len(G))]
    DP[0][0] = 1
    for i in range(len(DP)):
        for j in range(len(DP)):
            jump = G[i][j]

            if jump == 0:
                continue

            row = i + jump
            if row < len(DP):
                DP[row][j] = DP[i][j] + DP[row][j] if DP[row][j] != 0 else DP[i][j]

            col = j + jump
            if col < len(DP):
                DP[i][col] = DP[i][j] + DP[i][col] if DP[i][col] != 0 else DP[i][j]

    return DP[-1][-1]


import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
n = int(input())
G = [list(map(int, input().split())) for _ in range(n)]
print(answer(G))
