# https://www.acmicpc.net/problem/1043

def get_parent(parents, a):
    if parents[a] == a:
        return a
    return get_parent(parents, parents[a])


def union(parents, a, b):
    a_p, b_p = get_parent(parents, a), get_parent(parents, b)
    if a_p > b_p:
        parents[a_p] = b_p
    elif a_p < b_p:
        parents[b_p] = a_p


def answer(L, M, parents):
    global count
    for i in range(len(M)):
        memebers = M[i]
        flag = True
        for m in memebers:
            p = get_parent(parents, m)
            if p in L:
                flag = False
                break
        if flag:
            count += 1
    return count


import sys
input = sys.stdin.readline
n, m = map(int, input().split())
parents = [i for i in range(n + 1)]
L = list(map(int, input().split()))[1:]
for j in range(1, len(L)):
    union(parents, L[j - 1], L[j])
M = []
for i in range(m):
    x = list(map(int, input().split()))[1:]
    for j in range(1, len(x)):
        union(parents, x[j - 1], x[j])
    M.append(x)
L = set([get_parent(parents, i) for i in L])
count = 0
print(answer(L, M, parents))
