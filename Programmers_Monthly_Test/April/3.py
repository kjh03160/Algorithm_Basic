from collections import deque
def solution(a, edges):
    if sum(a):
        return -1
    count = 0
    G = {i: set() for i in range(len(a))}
    L = [0 for _ in range(len(a))]
    for x, y in edges:
        G[x].add(y)
        G[y].add(x)
        L[x] += 1
        L[y] += 1

    q = deque([i for i in range(len(L)) if L[i] == 1])

    while q:
        i = q.popleft()
        L[i] -= 1
        for node in G[i]:
            if L[node] > 0:
                L[node] -= 1
                if L[node] == 1:
                    q.append(node)
                count += abs(a[i])
                a[node] += a[i]
                a[i] = 0

    return count


print(solution([-5,0,2,1,2], [[0,1],[3,4],[2,3],[0,3]]))















# def solution(a, edges):
#     if sum(a):
#         return -1
#
#     G = {i: set() for i in range(len(a))}
#     for x, y in edges:
#         G[x].add(y)
#         G[y].add(x)
#
#     k = [i for i in range(len(G)) if len(G[i]) == 1]
#     count = 0
#     while k:
#         for i in k:
#             if G[i]:
#                 to = list(G[i])[0]
#                 a[to] += a[i]
#                 count += abs(a[i])
#                 a[i] = 0
#                 G[to].discard(i)
#                 G[i].discard(to)
#         k = [i for i in range(len(G)) if len(G[i]) == 1]
#
#     return count