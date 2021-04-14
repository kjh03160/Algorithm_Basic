# 계단 최소 비용 -> 1, 3, 4개 만 가능

def answer(n, K):
    DP = [float('inf') for _ in range(10002)]
    DP[0] = 0
    DP[1] = K[1]
    DP[3] = K[2]
    DP[4] = K[3]
    for i in range(2, n + 1):
        DP[i] = min(DP[i - 1], DP[i - 3], DP[i - 4]) + K[i]
    return DP[n]

import sys
input = sys.stdin.readline
n = int(input().rstrip())
K = [0] + list(map(int, input().split()))
print(answer(n, K))