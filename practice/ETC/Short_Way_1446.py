# boj.kr/1446

def answer(G):
    global d
    G.sort()
    dist = [_ for _ in range(10001)]
    for i in range(len(dist)):
        if i != 0:
            dist[i] = min(dist[i], dist[i - 1] + 1)

        for start, end, dt in G:
            if start == i and end <= d and dist[end] > dist[start] + dt:
                dist[end] = dist[start] + dt
    return dist[d]

import sys
input = sys.stdin.readline
n, d = map(int, input().split())
G = []
for i in range(n):
    G.append(list(map(int, input().split())))
print(answer(G))