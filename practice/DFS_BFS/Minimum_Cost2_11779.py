# https://www.acmicpc.net/problem/11779
import heapq

def answer(G, start, end):
    q = [(0, start, [start])]
    dist = [[float('inf'), []] for _ in range(len(G) + 1)]
    dist[start][0] = 0
    while q:
        d, v, n = heapq.heappop(q)

        if d > dist[v][0]:
            continue

        for e in G[v].keys():
            if dist[e][0] > d + G[v][e]:
                dist[e] = [d + G[v][e], n + [e]]
                heapq.heappush(q, (dist[e][0], e, n + [e]))
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
x = answer(G, start, end)
print(x[0], len(x[1]), " ".join(map(str, x[1])), sep='\n')