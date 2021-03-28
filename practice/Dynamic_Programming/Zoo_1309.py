# https://www.acmicpc.net/problem/1309

import sys
def answer(n):
    DP = [[0, 0, 0] for _ in range(n + 1)]
    DP[1] = [1, 1, 1]
    for i in range(2, len(DP)):
        DP[i][0] = sum(DP[i - 1]) % 9901
        DP[i][1] = (DP[i - 1][0] + DP[i - 1][2]) % 9901
        DP[i][2] = (DP[i - 1][0] + DP[i - 1][1]) % 9901
    return sum(DP[-1]) % 9901


input = sys.stdin.readline
n = int(input())
print(answer(n))