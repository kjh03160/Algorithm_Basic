# boj.kr/2150

from typing import List, Dict

def answer(G, reverse_G):
    visited = [False for _ in range(len(G) + 1)]
    stack = []
    for i in G:
        if not visited[i]:
            dfs(G, i, visited, stack)

    scc = []
    visited = [False for _ in range(len(G) + 1)]
    while stack:
        index = stack.pop()
        nodes = []
        if not visited[index]:
            dfs(reverse_G, index, visited, nodes)
            nodes.sort()
            scc.append(nodes)
    return sorted(scc)

def dfs(G: Dict, index, visited: List, stack: List):
    visited[index] = True

    for i in sorted(G[index], reverse=True):
        if not visited[i]:
            dfs(G, i, visited, stack)
    stack.append(index)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
v, e = map(int, input().split())
G = {i: set() for i in range(1, v + 1)}
reverse_G = {i: set() for i in range(1, v + 1)}
for _ in range(e):
    a, b = map(int, input().split())
    G[a].add(b)
    reverse_G[b].add(a)
result = answer(G, reverse_G)
print(len(result))
for i in result:
    print(*i + [-1])