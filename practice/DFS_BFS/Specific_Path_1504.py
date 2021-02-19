# https://www.acmicpc.net/problem/1504
import heapq


def answer(G, start):
    q = [(0, start)]
    dist = [float('inf') for _ in range(len(G) + 1)]
    dist[start] = 0
    while q:
        total_cost, node = heapq.heappop(q)

        if dist[node] < total_cost:
            continue

        for v in G[node].keys():
            n_cost = total_cost + G[node][v]
            if n_cost < dist[v]:
                dist[v] = n_cost
                heapq.heappush(q, (n_cost, v))
    return dist


import sys
input = sys.stdin.readline
n, e = map(int, input().split())
G = {i: {} for i in range(1, n + 1)}
for _ in range(e):
    a, b, c = map(int, input().split())
    G[a][b] = c
    G[b][a] = c
V1, V2 = map(int, input().split())


# V1을 구하면 1->v1, v1->v2, v1->n 을 한번에 구할 수 있다!
v1_to = answer(G, V1)
one_to_v1, v_to_v, v1_to_end = v1_to[1], v1_to[V2], v1_to[n]
# V2을 구하면 1->v2, v1->v2, v2->n 을 한번에 구할 수 있다!
v2_to = answer(G, V2)
v2_to_end, one_to_v2 = v2_to[n], v2_to[1]

result = min(one_to_v1 + v2_to_end, one_to_v2 + v1_to_end) + v_to_v
print(result if result != float('inf') else -1)