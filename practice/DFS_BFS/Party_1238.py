# boj.kr/1238

import heapq
def answer(G, x):
    q = []
    dist = [float('inf') for _ in range(len(G) + 1)]
    dist[x] = 0
    heapq.heappush(q, (0, x))
    while q:
        d, index = heapq.heappop(q)

        if dist[index] < d:
            continue

        for node in G[index]:
            if dist[node] > d + G[index][node]:
                dist[node] = d + G[index][node]
                heapq.heappush(q, (d + G[index][node], node))
    return dist[1:]


def answer2(G, x):
    q = []
    dist = [float('inf') for _ in range(len(G) + 1)]
    dist[x] = 0
    heapq.heappush(q, (0, x))
    while q:
        d, index = heapq.heappop(q)

        if dist[index] < d:
            continue

        for node in G:
            if index in G[node]:
                if dist[node] > d + G[node][index]:
                    dist[node] = d + G[node][index]
                    heapq.heappush(q, (d + G[node][index], node))
    return dist[1:]



import sys
input = sys.stdin.readline
n, m, x = map(int, input().split())
G = {i: {} for i in range(1, n + 1)}
for _ in range(m):
    a, b, c = map(int, input().split())
    G[a][b] = c

out = answer(G, x)
in_ = answer2(G, x)
max_ = 0
for i, j in zip(out, in_):
    max_ = max(max_, i + j)
print(max_)