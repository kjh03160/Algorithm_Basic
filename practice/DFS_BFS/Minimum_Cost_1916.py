# https://www.acmicpc.net/problem/1916
import heapq

def answer(G, start, end):
    q = [(0, start)]
    dist = [float('inf') for _ in range(len(G) + 1)]
    dist[start] = 0

    while q:
        d, v = heapq.heappop(q)

        if d > dist[v]:
            continue

        for e in G[v].keys():
            if dist[e] > d + G[v][e]:
                dist[e] = d + G[v][e]
                heapq.heappush(q, (dist[e], e))
    return dist[end]


import sys
input = sys.stdin.readline
n = int(input())
G = {i: {} for i in range(1, n + 1)}
m = int(input())
for _ in range(m):
    a, b, c = map(int, input().split())
    G[a][b] = min(G[a].get(b, float('inf')), c)
start, end = map(int, input().split())
print(answer(G, start, end))