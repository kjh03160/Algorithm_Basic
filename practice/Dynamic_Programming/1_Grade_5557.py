# boj.kr/5557

def answer(L):
    DP = [[0 for _ in range(21)] for _ in range(len(L) - 1)]
    DP[0][L[0]] = 1
    for i in range(1, len(L) - 1):
        for j in range(21):
            if DP[i - 1][j]:
                plus = j + L[i]
                minus = j - L[i]
                if 0 <= plus <= 20:
                    DP[i][plus] += DP[i - 1][j]
                if 0 <= minus <= 20:
                    DP[i][minus] += DP[i - 1][j]
    return DP[-1][L[-1]]

import sys
input = sys.stdin.readline
n = int(input())
L = list(map(int, input().split()))
print(answer(L))