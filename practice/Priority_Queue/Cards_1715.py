# https://www.acmicpc.net/problem/1715
import heapq
def answer(K):
    result = 0
    heapq.heapify(K)
    while len(K) >= 2:
        a = heapq.heappop(K)
        b = heapq.heappop(K)
        heapq.heappush(K, a + b)
        result += a + b
    return result


import sys
input = sys.stdin.readline
n = int(input())
K = []
for _ in range(n):
    K.append(int(input()))

print(answer(K))