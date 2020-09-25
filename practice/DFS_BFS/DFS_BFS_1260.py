# https://www.acmicpc.net/problem/1260

from collections import deque

def DFS(v):
    visitied_DFS[v] = True
    DFS_result.append(v)
    for edge in sorted(G[v]):
        if not visitied_DFS[edge]:
            DFS(edge)

def BFS(G, v):
    Q = deque()
    visitied_BFS = [False for _ in range(N + 1)]
    BFS_result.append(v)
    Q.append(v)

    visitied_BFS[v] = True
    while len(Q) > 0:
        x = Q.popleft()
        for edge in sorted(G[x]):
            if not visitied_BFS[edge]:
                visitied_BFS[edge] = True
                BFS_result.append(edge)
                Q.append(edge)

N, E, S = map(int, input().split())
visitied_DFS = [False for _ in range(N + 1)]
DFS_result = []
BFS_result = []
G = [[] for _ in range(N + 1)]
for i in range(E):
    index, value = map(int, input().split())
    G[index].append(value)
    G[value].append(index)
BFS(G, S)
DFS(S)
for i in DFS_result:
    print(i, end=" ")
print()
for i in BFS_result:
    print(i, end=" ")