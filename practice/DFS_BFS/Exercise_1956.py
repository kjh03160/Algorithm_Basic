# https://www.acmicpc.net/problem/1956
import heapq

def answer(K):
    for mid in range(n):
        for start in range(n):
            for end in range(n):
                if K[start][end] > K[start][mid] + K[mid][end]:
                    K[start][end] = K[start][mid] + K[mid][end]

    result = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            if K[i][j] != float('inf') and K[j][i] != float('inf'):
                result = min(K[i][j] + K[j][i], result)

    return result if result != float('inf') else -1


def answer2(G, start):
    q = [[0, start]]
    dist = [float('inf') for _ in range(len(G) + 1)]
    while q:
        d, v = heapq.heappop(q)

        if dist[v] < d:
            continue

        if v == start and d:
            return d

        for e in G[v].keys():
            if dist[e] > d + G[v][e]:
                dist[e] = d + G[v][e]
                heapq.heappush(q, (d + G[v][e], e))
    return dist[start]



import sys
input = sys.stdin.readline
n, k = map(int,input().split())
G = {i: {} for i in range(1, n + 1)}
# K = [[float('inf') for _ in range(n)] for _ in range(n)]
for _ in range(k):
    a, b, c = map(int, input().split())
    # K[a - 1][b - 1] = c
    G[a][b] = c
# print(answer(K))
x = min([answer2(G, i) for i in range(1, n + 1)])
print(x if x != float('inf') else -1)