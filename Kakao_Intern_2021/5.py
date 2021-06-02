def solution(k, num, links):
    answer = 0

    L = []
    for i in range(len(links)):
        for node in links[i]:
            if node == -1:
                continue
            L.append((num[node], i, node))
    L.sort()

    parents = [i for i in range(len(num) + 1)]
    print(L)
    result = 0
    n = 0
    G = []
    for edge in L:
        c = edge[0]
        a, b = edge[1], edge[2]
        # 사이클이 발생하지 않을 때
        if not find_parent(parents, a, b):
            result += c
            n += 1
            union_parent(parents, a, b)
        if n == len(num) - k:
            break

    return result

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


k = 3
num = [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1]
links = [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]]

print(solution(k, num, links))