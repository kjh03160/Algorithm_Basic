# https://www.acmicpc.net/problem/1149

def answer(L):
    DP = [[0, 0, 0] for _ in range(len(L))]
    DP[0] = L[0][:]
    for i in range(1, len(L)):
        DP[i][0] = min(DP[i - 1][1], DP[i - 1][2]) + L[i][0]
        DP[i][1] = min(DP[i - 1][0], DP[i - 1][2]) + L[i][1]
        DP[i][2] = min(DP[i - 1][1], DP[i - 1][0]) + L[i][2]

    return min(DP[-1])

import sys
input = sys.stdin.readline
n = int(input())
L = []
for _ in range(n):
    L.append(list(map(int, input().split())))

print(answer(L))