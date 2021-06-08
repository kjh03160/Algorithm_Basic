# boj.kr/14699

def answer(G, T):
    G.sort(reverse=True)

    DP = [1 for _ in range(n + 1)]

    for height, node in G:
        for adj in T[node]:
            DP[node] = max(DP[node], DP[adj] + 1)
    return DP[1:]

from collections import defaultdict
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
G = list(map(int, input().split()))
G = [(G[i], i + 1) for i in range(len(G))]
T = defaultdict(set)
for _ in range(m):
    a, b = map(int, input().split())
    if G[a - 1][0] < G[b - 1][0]:
        T[a].add(b)
    else:
        T[b].add(a)
print(*answer(G, T), sep='\n')