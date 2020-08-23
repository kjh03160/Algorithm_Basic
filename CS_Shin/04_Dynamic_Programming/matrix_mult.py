# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import math


def matrix_mult():  # M0 부터 Mn 까지 행렬 곱 최소비용 구하기
    for j in range(1, n):   # Mj 까지의 비용 계산
        for i in range(j - 1, -1, -1):  # i <= j, 아래의 값이 먼저 계산되어야 하기에 역순
            C[i][j] = math.inf  # math module에서 제공하는 매우 큰 정수
            for k in range(i, j):
                # DP[i][j] = min(DP[i][k] + DP[k + 1][j] + P[i] * P[k + 1] * P[j + 1])
                # Mi부터 Mj까지의 비용 = (Mi~Mk의 비용) + (Mk+1 ~ Mj의 비용) + 앞의 두 행렬 곱셈 비용
                cost = C[i][k] + C[k + 1][j] + P[i] * P[k + 1] * P[j + 1]

                if C[i][j] > cost:  # 최소 비용
                    C[i][j] = cost
    return C[0][n - 1]

"""
3
10 100 5 50

6
2 5 3 5 10 2 4
"""
n = int(input())  # n = 행렬 갯수, M_0부터 행렬시작임을 주의!
P = [int(x) for x in input().split()]  # M_i = p_i x p_{i+1}
C = [[0] * n for _ in range(n)]  # 비용을 저장할 2차원 리스트 C 초기화
min_cost = matrix_mult()
print(min_cost)