# https://www.acmicpc.net/problem/12852


def answer(n):
    DP = [[float('inf'), []] for _ in range(n + 1)]
    DP[1] = [0, [1]]
    for i in range(2, n + 1):
        x = i
        if i % 3 == 0 and DP[i][0] > DP[i // 3][0] + 1:
            DP[i][0] = DP[i // 3][0] + 1
            x = i // 3
        if i % 2 == 0 and DP[i][0] > DP[i // 2][0] + 1:
            DP[i][0] = DP[i // 2][0] + 1
            x = i // 2
        if DP[i - 1][0] + 1 < DP[i][0]:
            DP[i][0] = DP[i - 1][0] + 1
            x = i - 1
        DP[i][1].extend([i] + DP[x][1])

    print(DP[-1][0])
    print(*DP[-1][1])

import sys
input = sys.stdin.readline
n = int(input())
answer(n)