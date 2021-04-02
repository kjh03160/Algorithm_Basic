# boj.kr/17404

def answer(L):
    min_ = float('inf')
    for i in range(3):
        DP = [[0, 0, 0] for _ in range(len(L))]

        if i == 0:
            DP[0] = (L[0][0], float('inf'), float('inf'))
        elif i == 1:
            DP[0] = (float('inf'), L[0][1], float('inf'))
        else:
            DP[0] = (float('inf'), float('inf'), L[0][2])

        for j in range(1, len(DP)):
            DP[j] = [
                min(DP[j - 1][1], DP[j - 1][2]) + L[j][0],
                min(DP[j - 1][0], DP[j - 1][2]) + L[j][1],
                min(DP[j - 1][1], DP[j - 1][0]) + L[j][2]
            ]
        DP[-1].pop(i)
        min_ = min(min(DP[-1]), min_)
    return min_

import sys
input = sys.stdin.readline
n = int(input())
K = [list(map(int, input().split())) for _ in range(n)]
print(answer(K))

