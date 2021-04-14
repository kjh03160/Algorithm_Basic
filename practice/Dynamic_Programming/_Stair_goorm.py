# 계단 오르기 수

def answer(n):
    DP = [0 for _ in range(n + 1)]
    DP[1] = 1
    DP[3] = 1
    DP[4] = 1
    for i in range(2, len(DP)):
        DP[i] += DP[i - 1] + DP[i - 3] + DP[i - 4]
    return DP[n]

import sys
input = sys.stdin.readline
n = int(input().rstrip())
print(answer(n))