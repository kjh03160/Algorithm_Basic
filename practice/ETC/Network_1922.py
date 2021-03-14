# https://www.acmicpc.net/problem/1922

def get_parent(parents, index):
    if parents[index] == index:
        return parents[index]
    return get_parent(parents, parents[index])

def find_parent(parents, a, b):
    a_parent = get_parent(parents, a)
    b_parent = get_parent(parents, b)
    if a_parent == b_parent:
        return True
    return False

def union_parent(parents, a, b):
    a_parent = get_parent(parents, a)
    b_parent = get_parent(parents, b)
    if a_parent < b_parent:
        parents[b_parent] = a_parent
    else:
        parents[a_parent] = b_parent


def answer(n, K):
    result = 0
    parents = [i for i in range(n + 1)]
    for edge in K:
        a, b, c = edge
        if not find_parent(parents, a, b):
            result += c
            union_parent(parents, a, b)
    return result


import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
K = []

for _ in range(m):
    K.append(tuple(map(int, input().split())))
K.sort(key=lambda x: x[2])
print(answer(n, K))