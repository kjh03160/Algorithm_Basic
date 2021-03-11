# https://www.acmicpc.net/problem/1197

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
    global v
    costs.sort()
    parents = [i for i in range(v + 1)]

    result = 0
    for edge in costs:
        c = edge[0]
        a, b = edge[1], edge[2]
        # 사이클이 발생하지 않을 때
        if not find_parent(parents, a, b):
            result += c
            union_parent(parents, a, b)
    return result

    pass


import sys
input = sys.stdin.readline
v, e = map(int, input().split())
costs = []
for _ in range(e):
    a, b, c = map(int, input().split())
    costs.append((c, a, b))
print(answer(costs))