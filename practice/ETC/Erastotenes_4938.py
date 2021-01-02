# https://www.acmicpc.net/problem/4948

import math
def answer(n):
    N = [True for _ in range(2 * n + 1)]
    N[0] = False
    for i in range(2, int(math.sqrt(2 * n)) + 1):
        if N[i]:
            for j in range(i * i, 2 * n + 1, i):
                N[j] = False
    # print(N)
    return N[n + 1:].count(True)

import sys
input = sys.stdin.readline
n = int(input())
while True:
    print(answer(n))
    n = int(input())

    if n == 0:
        break