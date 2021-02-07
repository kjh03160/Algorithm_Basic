# https://www.acmicpc.net/problem/1655

import heapq
# https://yabmoons.tistory.com/478
import sys
input = sys.stdin.readline
n = int(input())
min_heap = []
max_heap = []
for i in range(n):
    x = int(input())
    if len(min_heap) == len(max_heap):
        heapq.heappush(max_heap, (-x, x))
    else:
        heapq.heappush(min_heap, (x, x))
    if min_heap and max_heap[0][1] > min_heap[0][1]:
        a = heapq.heappop(min_heap)[1]
        b = heapq.heappop(max_heap)[1]
        heapq.heappush(min_heap, (b, b))
        heapq.heappush(max_heap, (-a, a))

    print(max_heap[0][1])