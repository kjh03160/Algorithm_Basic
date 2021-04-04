# boj.kr/1325

from collections import deque
def answer(G, index):
    q = deque()
    visited = [False for _ in range(len(G) + 1)]
    q.append(index)
    visited[index] = True
    x = 1
    while q:
        index = q.popleft()
        for i in G[index]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                x += 1
    return x


import sys
input = sys.stdin.readline
n, m = map(int, input().split())
G = {i: set() for i in range(1, n + 1)}
for _ in range(m):
    a, b = map(int, input().split())
    G[b].add(a)

max_len = 0
result = []
for i in G:
    x = answer(G, i)
    if max_len == x:
        result.append(i)
    elif max_len < x:
        result = [i]
        max_len = x
print(*sorted(result))
