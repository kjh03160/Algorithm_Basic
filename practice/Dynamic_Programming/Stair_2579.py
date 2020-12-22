# https://www.acmicpc.net/problem/2579

def answer(L):
    DP = [[0, 0] for _ in range(len(L) + 1)]
    DP[1] = (L[0], L[0])

    for i in range(2, len(L) + 1):
        DP[i][0] = max(DP[i - 2]) + L[i - 1]
        DP[i][1] = DP[i - 1][0] + L[i - 1]

    return max(DP[-1])

import sys
input = sys.stdin.readline
n = int(input())
L = []
for _ in range(n):
    L.append(int(input()))
print(answer(L))