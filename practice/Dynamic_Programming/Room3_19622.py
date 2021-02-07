# https://www.acmicpc.net/problem/19622

def answer(L):
    DP = [[0, 0] for _ in range(len(L))]

    for i in range(len(L)):
        DP[i][0] = max(DP[i - 1][1], DP[i - 1][0])
        DP[i][1] = DP[i - 1][0] + L[i][2]

    return max(DP[-1])


import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
n = int(input())
L = []
for _ in range(n):
    L.append(list(map(int, input().split())))

print(answer(L))
