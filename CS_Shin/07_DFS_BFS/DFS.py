def DFS(v):
    global current

    visited[v] = 1
    prev[v] = current
    current += 1
    for node in G[v]:
        if visited[node] != 1:
            parent[node] = v
            DFS(node)
    post[v] = current
    current += 1

def DFS_ALL(G): # 그래프에서 끊어진 부분이 있을 때,
    for node in range(1, len(G)):
        if visited[node] != 1:
            DFS(node)
N = 4
visited = [0 for i in range(N + 1)]
parent = [0 for i in range(N + 1)]
prev = [0 for i in range(N + 1)]
post = [0 for i in range(N + 1)]
current = 1
G = [[], [2, 4], [4], [4], []]
DFS_ALL(G)
print(prev[1:])
print(post[1:])