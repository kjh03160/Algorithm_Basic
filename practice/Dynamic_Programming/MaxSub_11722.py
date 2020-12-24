# https://www.acmicpc.net/problem/11722

def answer(L):
    DP = [1 for i in range(len(L))]

    for i in range(len(L)):
        for j in range(i):
            if L[i] < L[j]:
                DP[i] = max(DP[j] + 1, DP[i])
    return max(DP)

import sys

input = sys.stdin.readline
n = int(input())
L = list(map(int, input().split()))

print(answer(L))