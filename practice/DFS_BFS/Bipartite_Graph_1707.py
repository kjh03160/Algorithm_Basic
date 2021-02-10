# https://www.acmicpc.net/problem/1707
from collections import deque
def asnwer(G):
    set_list = [set(), set()]
    q = deque()
    visited = [False for _ in range(len(G) + 1)]
    set_index = 0

    for i in range(1, len(G) + 1):
        if not visited[i]:
            q.append((i, set_index))
            visited[i] = True

        while q:
            node, set_index = q.popleft()
            if node in set_list[set_index - 1]:
                return 'No'
            set_list[set_index - 1].add(node)

            for edge in G[node]:
                if edge in set_list[set_index - 1]:
                    return 'NO'
                if not visited[edge]:
                    visited[edge] = True
                    q.append((edge, abs(set_index - 1)))
    return 'YES'


import sys
input = sys.stdin.readline
t = int(input())
for i in range(t):
    v, e = map(int, input().split())
    G = {k: [] for k in range(1, v + 1)}
    for x in range(e):
        p, q = map(int, input().split())
        G[p].append(q)
        G[q].append(p)
    print(asnwer(G))