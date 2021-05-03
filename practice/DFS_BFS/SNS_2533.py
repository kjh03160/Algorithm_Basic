# boj.kr/2533

def dfs(now):
    visited[now] = True

    DP[now][0] = 1
    DP[now][1] = 0

    for child in G[now]:
        if not visited[child]:
            visited[child] = True
            dfs(child)
            DP[now][0] += min(DP[child])
            DP[now][1] += DP[child][0]


import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
n = int(input())
G = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
visited = [False for _ in range(len(G) + 1)]
DP = [[0, 0] for _ in range(len(G) + 1)]
dfs(1)
print(min(DP[1]))