# https://www.acmicpc.net/problem/4386

def get_parent(parent, index):
    if index == parent[index]:
        return index
    return get_parent(parent, parent[index])

def find_parent(parent, a, b):
    a = get_parent(parent, a)
    b = get_parent(parent, b)

    if a == b:
        return True
    return False

def union_(parent, a, b):
    a, b = get_parent(parent, a), get_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


import math
def distance(x1, y1, x2, y2):
    return math.sqrt(((x1 -x2) ** 2) + ((y1 - y2) ** 2))

def answer(P):
    cost = []

    for i in range(len(P)):
        for j in range(i + 1, len(P)):
            cost.append((distance(P[i][0], P[i][1], P[j][0], P[j][1]), i, j))
    parent = [i for i in range(len(P) + 1)]
    cost.sort()
    result = 0
    count = 0
    for i in cost:
        c, p1, p2 = i

        if not find_parent(parent, p1, p2):
            result += c
            count += 1
            union_(parent, p1, p2)
            if count == len(P) - 1:
                return result

    return result


import sys
input = sys.stdin.readline
n = int(input())
P = [tuple(map(float, input().split())) for _ in range(n)]

print("%.2f" % answer(P))