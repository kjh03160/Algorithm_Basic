# https://www.acmicpc.net/problem/11049

def answer(P):
    DP = [[0 for _ in range(len(L))] for _ in range(n)]

    for j in range(1, n):  # Mj 까지의 비용 계산
        for i in range(j - 1, -1, -1):  # i <= j, 아래의 값이 먼저 계산되어야 하기에 역순
            DP[i][j] = 2 ** 32
            for k in range(i, j):
                # DP[i][j] = min(DP[i][k] + DP[k + 1][j] + P[i] * P[k + 1] * P[j + 1])
                # Mi부터 Mj까지의 비용 = (Mi~Mk의 비용) + (Mk+1 ~ Mj의 비용) + 앞의 두 행렬 곱셈 비용
                cost = DP[i][k] + DP[k + 1][j] + P[i][0] * P[k][1] * P[j][1]

                if DP[i][j] > cost:  # 최소 비용
                    DP[i][j] = cost
    return DP[0][n - 1]

import sys
input = sys.stdin.readline
n = int(input())
L = []
for _ in range(n):
    L.append(tuple(map(int, input().split())))

print(answer(L))