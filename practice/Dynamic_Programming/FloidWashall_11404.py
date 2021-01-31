# https://www.acmicpc.net/problem/11404


import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
dist = [[float('inf') for _ in range(n)] for _ in range(n)]
for i in range(n):
    dist[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a - 1][b - 1] = min(c, dist[a - 1][b - 1])

for mid in range(n):
    for start in range(n):
        for end in range(n):
            if dist[start][mid] + dist[mid][end] < dist[start][end]:
                dist[start][end] = dist[start][mid] + dist[mid][end]

for i in dist:
    for j in i:
        print(j if j != float('inf') else 0, end=' ')
    print()