# boj.kr/21924

def find_parent(parents, a):
    if parents[a] == a:
        return a
    parents[a] = find_parent(parents, parents[a])
    return parents[a]

def union_parent(parents, a, b):
    a = find_parent(parents, a)
    b = find_parent(parents, b)

    if a < b:
        parents[a] = b
    elif a > b:
        parents[b] = a
    else:
        return False
    return True

def answer(L):
    global n
    parents = [i for i in range(n + 1)]
    L.sort(key=lambda x: x[2])
    result = 0
    count = 0
    total = 0
    for i in range(len(L)):
        a, b, cost = L[i]
        if union_parent(parents, a, b):
            result += cost
            count += 1
        total += cost

    return total - result if count == n - 1 else -1

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(m)]
print(answer(L))