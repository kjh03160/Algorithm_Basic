# https://www.acmicpc.net/problem/1920
import bisect
def answer(L, k):
    index = bisect.bisect(L, k) - 1
    if index >= len(L):
        index = -1
    if L[index] == k:
        return 1
    return 0

import sys
input = sys.stdin.readline
n = int(input())
L = list(map(int, input().split()))
x = int(input())
K = list(map(int, input().split()))

L.sort()

for i in K:
    print(answer(L, i))