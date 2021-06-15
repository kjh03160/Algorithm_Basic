# boj.kr/6497

def find(parents, a):
    if parents[a] == a:
        return a
    parents[a] = find(parents, parents[a])
    return parents[a]

def union(parents, a, b):
    a, b = find(parents, a), find(parents, b)

    if a == b:
        return False
    if a > b:
        parents[b] = a
    else:
        parents[a] = b
    return True

def answer(L, total):
    L.sort()
    parents = [i for i in range(n + 1)]
    count = 0
    m = 0
    for c, a, b in L:
        if union(parents, a, b):
            count += 1
            m += c
            if count == n - 1:
                break
    return total - m


import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    L = []
    total = 0
    for _ in range(m):
        a, b, c = map(int, input().split())
        total += c
        L.append((c, a, b))
    print(answer(L, total))
