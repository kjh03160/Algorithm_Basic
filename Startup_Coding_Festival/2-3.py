import sys, copy

input = sys.stdin.readline




n, q = map(int, input().split())
G = {i: set() for i in range(1, n + 1)}
X = {i: set() for i in range(1, n + 1)}
for _ in range(n - 1):
    a, b = map(int, input().split())
    G[a].add(b)
    X[b].add(a)
tree = {i: set() for i in G}
indegrees = [len(X[i]) for i in range(1, n + 1)]
root = [i for i in range(1, n + 1) if not indegrees[i - 1]][0]

from collections import deque

def answer(G, root, tree):
    q = deque()
    q.append(root)
    while q:
        r = q.popleft()
        print(r)
        for node in G.keys():
            if r in G[node]:
                G[node].remove(r)
                if not G[node]: # r은 node의 상위 물품이다.
                    q.append(node)
                    tree[r].add(node)
    return tree

def dfs(X, index, visited):
    global L
    L[index] = set(list(visited))
    for i in X[index]:
        if i not in visited:
            visited.add(i)
            dfs(X, i, visited)
            visited.remove(i)

tree = answer(X, root, tree)
L = [set() for i in range(len(G) + 1)]
dfs(tree, root, {root})
for _ in range(q):
    is_up, is_down = map(int, input().split())
    if is_up != is_down and is_up in L[is_down]:
        print("yes")
    else:
        print("no")
