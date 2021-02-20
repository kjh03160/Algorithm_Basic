# https://www.acmicpc.net/problem/2225

def answer(n, k):
    DP = [[1 for i in range(n + 1)] for _ in range(k + 1)]
    """
    1 -> 1 1 1 1 1..
    2 -> 1 2 3 4 5..
    3 -> 1 3 6 10 15..
    4 -> 1 4 10 20 35..
    """
    for i in range(2, k + 1):
        for j in range(1, n + 1):
            DP[i][j] = (DP[i][j - 1] + DP[i - 1][j]) % 1000000000
    return DP[k][n] % 1000000000


import sys
input = sys.stdin.readline
n, k = map(int, input().split())
print(answer(n, k))