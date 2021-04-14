# 계단 최소 비용 -> s1, s2,... sk 개 가능

def answer(n, K, S):
    DP = [float('inf') for _ in range(n + 2)]
    DP[0] = 0
    for i in S:
        if i - 1 < len(K):
            DP[i] = K[i - 1]
    for i in range(2, n + 1):
        for j in S:
            if i - j >= 0:
                DP[i] = min(DP[i - j], DP[i])
        DP[i] += K[i]
    return DP[n] if DP[n] != float('inf') else -1

import sys
input = sys.stdin.readline
n, s = map(int, input().split())
S = list(map(int, input().split()))
K = [0] + list(map(int, input().split()))
print(answer(n, K, S))