# boj.kr/1717

def get_parent(parents, a):
    if a == parents[a]:
        return a
    parents[a] = get_parent(parents, parents[a])
    return parents[a]

def is_same_origin(parents, a, b):
    a = get_parent(parents, a)
    b = get_parent(parents, b)
    if a == b:
        return 'YES'
    return "NO"

def union(parents, a, b):
    a = get_parent(parents, a)
    b = get_parent(parents, b)

    if a > b:
        parents[a] = b
    else:
        parents[b] = a


def asnwer(Q):
    global n
    parents = [i for i in range(n + 1)]
    for a, b, c in Q:
        if a == 0:
            union(parents, b, c)
        else:
            print(is_same_origin(parents, b, c))


import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
n, m = map(int, input().split())
Q = [list(map(int, input().split())) for _ in range(m)]
asnwer(Q)