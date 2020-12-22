# https://www.acmicpc.net/problem/10844

def answer(n):
    MOD = 1000000000

    DP = [[0 for _ in range(10)] for _ in range(101)]
    DP[1] = [1 for _ in range(10)]
    DP[1][0] = 0

    for i in range(2, n + 1):
        for j in range(10):
            if j == 0:
                DP[i][j] = DP[i - 1][j + 1] % MOD
            elif j == 9:
                DP[i][j] = DP[i - 1][j - 1] % MOD
            else:
                DP[i][j] = (DP[i - 1][j - 1] + DP[i - 1][j + 1]) % MOD

    return sum(DP[n]) % MOD



import sys
input = sys.stdin.readline
n = int(input())
print(answer(n))