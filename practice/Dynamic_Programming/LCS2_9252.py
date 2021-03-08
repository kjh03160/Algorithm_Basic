# https://www.acmicpc.net/problem/9252

def answer(A, B):
    DP = [[[0, ''] for _ in range(len(A) + 1)] for _ in range(len(B) + 1)]

    for i in range(1, len(B) + 1):
        for j in range(1, len(A) + 1):
            if B[i - 1] == A[j - 1]:
                if DP[i][j][0] < DP[i - 1][j - 1][0] + 1:
                    DP[i][j] = [DP[i - 1][j - 1][0] + 1, DP[i - 1][j - 1][1] + A[j - 1]]

            else:
                if DP[i][j - 1][0] > DP[i - 1][j][0]:
                    DP[i][j] = [DP[i][j - 1][0], DP[i][j - 1][1]]
                else:
                    DP[i][j] = [DP[i - 1][j][0], DP[i - 1][j][1]]
                DP[i][j] = max(DP[i][j - 1], DP[i - 1][j])
    print(DP[-1][-1][0])
    print(DP[-1][-1][1]) if DP[-1][-1][0] else None

import sys
input = sys.stdin.readline
A, B = input().rstrip(), input().rstrip()
answer(A, B)