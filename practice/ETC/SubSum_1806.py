# https://www.acmicpc.net/problem/1806
def answer(L, s):
    start = 0
    if L[0] >= s:
        return 1
    end = start + 1
    sum_ = L[start] + L[end]
    min_ = float('inf')
    while end < len(L):
        if sum_ >= s:
            min_ = min(min_, end - start + 1)
            sum_ -= L[start]
            start += 1
        else:
            end += 1
            if end == len(L):
                break
            sum_ += L[end]
    return min_ if min_ != float('inf') else 0

import sys
input = sys.stdin.readline
n, s = map(int, input().split())
L = list(map(int, input().split()))
print(answer(L, s))