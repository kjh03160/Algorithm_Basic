# boj.kr/11473



def lca(a, b, depth, parent):
    # 깊이 맞춰주
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = parent[a]
        else:
            b = parent[b]

    # 같이 위로 올라가면서 같은 조상 찾기
    while a != b:
        a = parent[a]
        b = parent[b]
    return a


def dfs(index, visited, parent, depth):
    global D, G
    visited[index] = True
    D[index] = depth

    for i in G[index]:
        if not visited[i]:
            parent[i] = index
            dfs(i, visited, parent, depth + 1)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)
n = int(input())
G = {i: set() for i in range(1, n + 1)}
D = [0 for _ in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, input().split())
    G[a].add(b)
    G[b].add(a)

visited = [False for _ in range(n + 1)]
parent = [0 for _ in range(n + 1)]
dfs(1, visited, parent, 1)

m = int(input())
for i in range(m):
    a, b = map(int, input().split())
    print(lca(a, b, D, parent))
