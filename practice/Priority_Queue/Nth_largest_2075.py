# https://www.acmicpc.net/problem/2075
import heapq
import sys


input = sys.stdin.readline
n = int(input())
q = []

for _ in range(n):
    x = list(map(int, input().split()))
    for k in range(len(x)):
        if not len(q):
            heapq.heappush(q, x[k])
        if x[k] > q[0]:
            if len(q) >= n:
                heapq.heappop(q)
            heapq.heappush(q, x[k])
print(heapq.heappop(q))