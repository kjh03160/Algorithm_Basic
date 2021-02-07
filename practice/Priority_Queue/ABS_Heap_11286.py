# https://www.acmicpc.net/problem/11286

import sys
input = sys.stdin.readline
n = int(input())

import heapq
q = []

for i in range(n):
    x = int(input())
    if x:
        heapq.heappush(q, (abs(x), x))

    else:
        if q:
            print(heapq.heappop(q)[1])
        else:
            print(0)