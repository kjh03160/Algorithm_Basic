# boj.kr/1516

from collections import deque
def answer(G, starts, T, indg):
    global time
    q = deque(starts)
    while q:
        node = q.popleft()

        for i in G[node]:
            indg[i] -= 1
            time[i] = max(time[i], time[node] + T[i])
            if not indg[i]:
                q.append(i)

import sys
input = sys.stdin.readline
n = int(input())
G = {i: set() for i in range(1, n + 1)}
T = [0]
starts = []
indegrees = [0 for _ in range(n + 1)]
for a in range(1, n + 1):
    i, *b = map(int, input().split())
    for k in b[:-1]:
        indegrees[a] += 1
        G[k].add(a)
    if not b[:-1]:
        starts.append(a)
    T.append(i)
time = [t for t in T]

answer(G, starts, T, indegrees)
print(*time[1:], sep='\n')