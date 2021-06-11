# boj.k/12893

def find_parent(parents, a):
    if parents[a] == a:
        return a
    parents[a] = find_parent(parents, parents[a])
    return parents[a]


def union(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)

    if a == b:
        return False

    if a > b:
        parents[a] = b
    else:
        parents[b] = a

    return True


def answer(G):
    global n

    parents = [i for i in range(n + 1)]
    enemy = [0 for _ in range(n + 1)]
    for a, b in G:
        a = find_parent(parents, a)
        b = find_parent(parents, b)

        # 서로가 적이면서 친구인 관계가 될때 이론 틀림.
        if a == b:
            return 0

        # a의 적 루트
        ae = enemy[a]
        # b의 적 루트
        be = enemy[b]

        # a의 적 루트가 존재하면
        if ae:
            # a의 적은 b의 친구이기에 같은 집합에
            union(parents, ae, b)
        else:
            # 없으면 a의 적의 루트가 b
            enemy[a] = b

        if be:
            union(parents, be, a)
        else:
            enemy[b] = a
    return 1


import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
G = []
for _ in range(m):
    a, b = map(int, input().split())
    G.append((a, b))
print(answer(G))