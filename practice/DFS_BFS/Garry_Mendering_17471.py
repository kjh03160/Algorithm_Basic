# https://www.acmicpc.net/problem/17471

from collections import deque
from itertools import combinations
def answer(indexes, base, G):
    result = 100 ** 3
    for index in indexes:
        first = index
        second = base.difference(first)
        second_index = list(second)[0]

        first_result = bfs(first[0], G,set(first), cost)
        if first_result == -1:
            continue
        second_result = bfs(second_index, G, second, cost)
        if second_result == -1:
            continue

        result = min(result, abs(first_result - second_result))

    return result if result != 100 ** 3 else -1


def bfs(index, G, cands, cost):
    q = deque()
    q.append((index, cost[index - 1]))
    visited = set()
    visited.add(index)
    p = 0
    while q:
        node, x = q.popleft()
        p += x
        for edge in G[node]:
            if edge not in visited and edge in cands:
                visited.add(edge)
                q.append((edge, cost[edge - 1]))

    if visited == cands:
        return p
    return -1


import sys
input = sys.stdin.readline
n = int(input())
G = {i: [] for i in range(1, n + 1)}
cost = list(map(int, input().split()))
for i in range(1, n + 1):
    G[i].extend(list(map(int, input().split()))[1:])

base = set(G.keys())
indexes= []
for i in range(1, len(G)):
    x = list(combinations(G.keys(), i))
    if len(G) // 2 == i:
        x = x[:len(x) // 2 + 1]
    indexes.extend(x)

print(answer(indexes, base, G))