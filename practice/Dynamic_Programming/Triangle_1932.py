# https://www.acmicpc.net/problem/1932

def answer(L):
    DP = [[0 for _ in range(len(L))] for _ in range(len(L))]
    DP[0][0] = L[0][0]
    for i in range(1, len(L)):
        for j in range(i + 1):
            DP[i][j] = max(DP[i - 1][j], DP[i - 1][j - 1]) + L[i][j]
    return max(DP[-1])

import sys
input = sys.stdin.readline

n = int(input())
L = []
for _ in range(n):
    L.append(list(map(int, input().split())))

print(answer(L))