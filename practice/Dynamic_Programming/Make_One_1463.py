# https://www.acmicpc.net/problem/1463

def answer(n):
    DP = [10 ** 6 for _ in range(n + 1)]
    DP[0] = 0
    DP[1] = 0
    for i in range(2, n + 1):
        if i % 3 == 0:
            DP[i] = min(DP[i // 3] + 1, DP[i])
        if i % 2 == 0:
            DP[i] = min(DP[i // 2] + 1, DP[i])
        DP[i] = min(DP[i - 1] + 1, DP[i])

    return DP[n]


import sys
input = sys.stdin.readline
n = int(input())
print(answer(n))