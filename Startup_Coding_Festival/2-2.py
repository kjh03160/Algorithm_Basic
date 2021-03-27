# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# 부모 찾기
def get_parent(parents, node):
    if parents[node] == node:
        return node
    return get_parent(parents, parents[node])


# 트리에 노드 합치기
def union_parent(parents, a, b):
    a, b = get_parent(parents, a), get_parent(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


# 같은 부모를 가지는가? -> 사이클이 발생하는가?
def find_parent(parents, a, b):
    a = get_parent(parents, a)
    b = get_parent(parents, b)
    if a == b:
        return True
    return False


def answer(costs):
    global G
    costs.sort()
    parents = [i for i in range(len(G) + 1)]
    print(costs)
    result = 0
    for edge in costs:
        c = edge[0]
        a, b = edge[1], edge[2]
        # 사이클이 발생하지 않을 때
        if not find_parent(parents, a, b):
            result += c
            union_parent(parents, a, b)
        print(parents)
    return result


import sys

input = sys.stdin.readline
n = int(input())
G = {}
for _ in range(n):
    a, b, c = input().split()
    if a not in G:
        G[a] = {}
    if b not in G:
        G[b] = {}
    if G[a].get(b):
        G[a][b] = min(G[a][b], int(c))
    else:
        G[a][b] = int(c)

names = {name: i + 1 for i, name in enumerate(G)}
costs = []
for name in G:
    f_idx = names[name]
    for edge in G[name]:
        s_idx = names[edge]
        cost = G[name].get(edge) if G[name].get(edge) else G[edge][name]
        costs.append((cost, f_idx, s_idx))

print(answer(costs))