# boj.kr/20955

def find(parents, a):
    if a == parents[a]:
        return a
    parents[a] = find(parents, parents[a])
    return parents[a]


def union(parents, a, b):
    a, b = find(parents, a), find(parents, b)

    if a == b:
        return True
    if a > b:
        parents[a] = b
    else:
        parents[b] = a

    return False

def answer(G):
    parents = [i for i in range(n + 1)]
    cut = 0
    for a, b in G:
        is_cycle = union(parents, a, b)
        if is_cycle:
           cut += 1

    diff = set()
    for i in range(1, n + 1):
        diff.add(find(parents, i))

    return len(diff) + cut - 1

import sys
sys.setrecursionlimit(10 ** 6 + 1)
input = sys.stdin.readline
n, m = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(m)]
print(answer(L))