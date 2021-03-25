# https://www.acmicpc.net/contest/problem/603/4
from itertools import combinations
def answer(G, H):
    for mid in range(len(G)):
        for start in range(len(G)):
            for end in range(len(G)):
                if dist[start][mid] + dist[mid][end] < dist[start][end]:
                    dist[start][end] = dist[start][mid] + dist[mid][end]

    f, s, r = 0, 0, float('inf')
    for x, y in H:
        first = dist[x - 1]
        second = dist[y - 1]
        result = 0
        for i in range(len(first)):
            result += min(first[i], second[i]) * 2
        if result < r:
            f, s, r = x, y, result
    print(f, s, r)


import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dist = [[float('inf') for _ in range(n)] for _ in range(n)]

for i in range(n):
    dist[i][i] = 0

for _ in range(m):
    x, y = map(int, input().split())
    dist[x - 1][y - 1] = 1
    dist[y - 1][x - 1] = 1
hubo = list(combinations([i for i in range(1, n + 1)], 2))
hubo.sort()
answer(dist, hubo)
