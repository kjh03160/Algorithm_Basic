# https://www.acmicpc.net/problem/1753
from heapq import heappush, heappop

def answer(start):
    global G, dist
    q = []
    heappush(q, (0, start))
    dist[start] = 0

    while q:
        w, v = heappop(q)

        if dist[v] < w:
            continue

        for weight, next_v in G[v]:
            next_w = weight + w
            if next_w < dist[next_v]:
                dist[next_v] = next_w
                heappush(q, (next_w, next_v))
    return dist

import sys
input = sys.stdin.readline
v, e = map(int, input().split())
start = int(input())
G = [[] for _ in range(v + 2)]
for _ in range(e):
    u, v_, w = map(int, input().split())
    G[u].append((w, v_))
dist = [9999999999] * (v + 1)

result = answer(start)
for i in result[1:]:
    if i == 9999999999:
        print('INF')
    else:
        print(i)