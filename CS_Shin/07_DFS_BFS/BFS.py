from collections import deque

def BFS(G):
    visited = [False for i in range(len(G) + 1)]
    parent = [-1 for i in range(len(G) + 1)]
    dist = [0 for i in range(len(G) + 1)]

    for node in range(1, len(G)):
        Q.append(node)
        print(node)
        visited[node] = True
        while len(Q) > 0:
            v = Q.popleft()
            for edge in G[v]:
                if not visited[edge]:
                    Q.append(edge)
                    visited[edge] = True
                    parent[edge] = v
                    dist[edge] = dist[v] + 1

N = 4
current = 1
G = [[], [2, 3, 4], [4], [4], []]
Q = deque()
BFS(G)
