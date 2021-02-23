# https://www.acmicpc.net/problem/13549
from collections import deque

def answer(n, k):
    q = deque()
    visited = [False for _ in range(100001)]
    q.append((n, 0))
    min_cost = float('inf')
    while q:
        now, cost = q.popleft()
        visited[now] = True
        if now == k:
            min_cost = min(cost, min_cost)
            visited[now] = False
            continue

        if now * 2 < 100001:
            if not visited[now * 2] and now * 2 <= k + 1:
                q.append((now * 2, cost))

        cost += 1

        if now + 1 < 100001:
            if not visited[now + 1]:
                q.append((now + 1, cost))

        if now - 1 >= 0:
            if not visited[now - 1]:
                q.append((now - 1, cost))

    return min_cost

import sys
input = sys.stdin.readline
n, k = map(int, input().split())
print(answer(n, k))