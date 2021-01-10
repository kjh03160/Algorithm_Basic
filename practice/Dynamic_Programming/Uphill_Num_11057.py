# https://www.acmicpc.net/problem/11057

def answer(n):
    DP = [[0] * 9 for _ in range(n)]
    DP[0] = [1] * 9

    for i in range(1, n):
        for j in range(9):
            DP[i][j] = sum(DP[i - 1][j:])

    return DP

import sys
input = sys.stdin.readline
n = int(input())
result = 0
x = answer(n)
for i in range(n):
    result += sum(x[i])
print((result + 1) % 10007)