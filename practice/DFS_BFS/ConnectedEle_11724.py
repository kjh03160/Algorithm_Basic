# https://www.acmicpc.net/problem/11724

def answer(G):
    global n
    count = 0
    visited = [False for _ in range(n + 1)]

    def DFS(i):
        visited[i] = True
        for k in G[i]:
            if not visited[k]:
                DFS(k)

    for i in range(n):
        if not visited[i + 1]:
            DFS(i + 1)
            count += 1
    return count

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int, input().split())
G = {i + 1 : [] for i in range(n)}

for i in range(m):
    x, y = map(int, input().split())
    G[x].append(y)
    G[y].append(x)
print(answer(G))