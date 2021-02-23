# https://www.acmicpc.net/problem/12851
from collections import deque
def answer(n, k):
    q = deque()
    min_count = 0
    min_cost = float('inf')
    visited = [False for _ in range(100001)]
    q.append((n, 0))
    while q:
        now, cost = q.popleft()
        visited[now] = True

        if now == k:
            if cost == min_cost:
                min_count += 1
            elif cost < min_cost:
                min_count = 1
                min_cost = cost
            continue

        cost += 1

        if cost > min_cost:
            continue

        if now + 1 < 100001:
            if not visited[now + 1] or min_cost == cost:
                q.append((now + 1, cost))
        if now - 1 >= 0:
            if not visited[now - 1] or min_cost == cost:
                q.append((now - 1, cost))
        if 2 * now < 100001:
            if not visited[now * 2] or min_cost == cost:
                q.append((now * 2, cost))
    return min_cost, min_count

import sys
input = sys.stdin.readline
n, k = map(int, input().split())
print(*answer(n, k))