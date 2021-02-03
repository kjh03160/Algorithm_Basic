# https://www.acmicpc.net/problem/17070
def dp(G):
    DP = [[[0 for _ in range(3)] for _ in range(len(G))] for _ in range(len(G))]
    DP[0][1][0] = 1

    for i in range(len(G)):
        for j in range(1, len(G)):
            if G[i][j] == 1:
                continue
            for s in range(3):
                if s == 0:  # 현재 가로 -> 이전에는 대각 or 가로였다
                    if DP[i][j][s] == 0:
                        DP[i][j][s] = DP[i][j - 1][s] + DP[i][j - 1][2]
                    else:
                        DP[i][j][s] += DP[i - 1][j - 1][2] + DP[i][j - 1][0]

                elif s == 1:    # 현재 세로 -> 이전에서 대각 or 세로였다
                    if DP[i][j][s] == 0:
                        DP[i][j][s] = DP[i - 1][j][s] + DP[i - 1][j][2]
                    else:
                        DP[i][j][s] += DP[i - 1][j - 1][2] + DP[i - 1][j][1]

                else:   # 현재 대각 -> 이전에는 가로, 대각, 세로 가능
                    if i - 1 >= 0 and (G[i][j - 1] == 1 or G[i - 1][j]) == 1:
                        continue
                    if DP[i][j][s] == 0:
                        DP[i][j][s] = DP[i - 1][j - 1][1] + DP[i - 1][j - 1][0] + DP[i - 1][j - 1][s]
                    else:
                        DP[i][j][s] += DP[i - 1][j - 1][2] + DP[i][j - 1][0] + DP[i - 1][j][1]
    # print(*DP, sep='\n')
    return sum(DP[-1][-1])


import sys
input = sys.stdin.readline
n = int(input())
G = []
for _ in range(n):
    G.append(list(map(int, input().split())))

print(dp(G))