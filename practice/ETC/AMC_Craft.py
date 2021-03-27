from collections import deque
def answer(G, T, W):
    global _T
    q = deque()
    for k in range(len(indg)):
        if not indg[k]:
            q.append(k + 1)

    while q:
        node = q.popleft()
        if node == W:
            return T[node - 1]

        for edge in G[node]:
            indg[edge - 1] -= 1
            T[edge - 1] = max(T[edge - 1], T[node - 1] + _T[edge - 1])
            if not indg[edge - 1]:
                q.append(edge)



import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    T = list(map(int, input().split()))
    _T = [x for x in T]
    G = {i: set() for i in range(1, n + 1)}
    indg = [0 for k in G]
    for _ in range(k):
        a, b = map(int, input().split())
        G[a].add(b)
        indg[b - 1] += 1
    W = int(input())
    print(answer(G, T, W))
