# https://www.acmicpc.net/problem/11052

def answer(n, P):
    DP = [0] + P[:]
    for i in range(2, n + 1):
        for j in range(1, i // 2 + 1):
            DP[i] = max(DP[j] + DP[i - j], DP[i])

    return max(DP)

import sys
input = sys.stdin.readline
n = int(input())
P = list(map(int, input().split()))
print(answer(n, P))