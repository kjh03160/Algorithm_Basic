# boj.kr/20040
def get_parent(parents, a):
    if parents[a] == a:
        return a
    return get_parent(parents, parents[a])

def union_parent(parents, a, b):
    a = get_parent(parents, a)
    b = get_parent(parents, b)

    if a == b:
        return True

    if a > b:
        parents[a] = b
    else:
        parents[b] = a
    return False


def ansewr(L):
    global n

    cycle = False
    parents = [i for i in range(n)]
    count = 0
    for a, b, in L:
        count += 1
        cycle = cycle | union_parent(parents, a, b)
        if cycle:
            return count
    return 0

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
L = []
for _ in range(m):
    L.append(list(map(int, input().split())))
print(ansewr(L))