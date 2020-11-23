# https://www.acmicpc.net/problem/14852

def answer(n):
    DP = [1, 2, 7] + [0] * (n - 2)
    for i in range(3, n + 1):
        DP[i] = (2 * DP[i - 1] + 4 * DP[i - 2] - DP[i - 4]) % 1000000007

    return DP[n]

import sys
input = sys.stdin.readline

n = int(input())
print(answer(n))