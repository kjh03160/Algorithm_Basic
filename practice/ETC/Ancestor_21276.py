# https://www.acmicpc.net/problem/21276
def answer(X, tree):
    while True:
        root = get_top_entries(X)
        if not root:
            break

        for name in root:
            for node in X.keys():
                if name in X[node]:
                    X[node].remove(name)
                    if not X[node]:
                        tree[name].append(node)

            X[name] = [-1]
    return tree


def get_top_entries(X):
    return [name for name in X if not X[name]]


import sys
input = sys.stdin.readline
n = int(input())
names = input().split()
temp = {name: set() for name in names}
tree = {name: [] for name in names}
m = int(input())
for _ in range(m):
    x, y = input().split()
    temp[x].add(y)
root = [name for name in temp if not temp[name]]
result = answer(temp, tree)
print(len(root))
print(*sorted(root))
for name in sorted(temp.keys()):
    print(name, len(result[name]), end=" ")
    print(*sorted(result[name]))
