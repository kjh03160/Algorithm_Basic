# https://www.acmicpc.net/problem/2056
from collections import deque
def answer(G, N, K):
    global result
    q = deque()
    for i in range(1, len(K)):
        if not K[i]:
            q.append((i, N[i]))
    while q:
        node, time = q.popleft()

        for i in G[node]:
            K[i] -= 1
            result[i] = max(result[i], result[node] + N[i])
            if not K[i]:
                q.append((i, result[i]))

import sys
input = sys.stdin.readline
n = int(input())
N = [0]
G = {i: set() for i in range(1, n + 1)}
K = [0 for _ in range(n + 1)]
for x in range(1, n + 1):
    temp = list(map(int, input().split()))
    N.append(temp[0])
    K[x] = temp[1]
    for i in temp[2:]:
        G[i].add(x)
result = [_ for _ in N]
answer(G, N, K)
print(max(result))
