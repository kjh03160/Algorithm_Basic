#https://www.acmicpc.net/problem/11279

import heapq

heap = []
import sys

input = sys.stdin.readline
n = int(input())
for i in range(n):
    x = int(input())
    if x == 0:
        if len(heap):
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (-x, x))
