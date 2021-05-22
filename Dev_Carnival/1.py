# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


def answer(n, k, L):
    result = []
    eat = [0 for _ in range(len(L))]
    i = k - 1
    while True:
        if eat[i] != -1 and eat[i] <= L[i]:
            eat[i] += 1
        elif eat[i] != -1:
            result.append(i + 1)
            eat[i] = -1
        if len(result) == len(L):
            break
        i = (i + 1) % len(L)
    return result


import sys

input = sys.stdin.readline
n, k = map(int, input().split())
L = list(map(int, input().split()))
print(*answer(n, k, L))
