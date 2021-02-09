# https://www.acmicpc.net/problem/status/14620

import copy
def answer(G, X):
    result = float('inf')
    for i in range(len(X)):
        if X[i][0] >= result:
            continue
        for j in range(i + 1, len(X)):
            if X[i][0] + X[j][0] >= result:
                continue
            for k in range(j + 1, len(X)):
                c1 = X[i][0]
                c2 = X[j][0]
                c3 = X[k][0]
                if c1 + c2 + c3 >= result:
                    continue
                f1 = (X[i][1], X[i][2])
                f2 = (X[j][1], X[j][2])
                f3 = (X[k][1], X[k][2])

                if upate(copy.deepcopy(G), 1, f1, f2, f3):
                    result = min(result, c1 + c2 + c3)
    return result


def upate(G, k, *args):
    DIRECTION = [(0, 0), (1, 0), (0, 1), (0, -1), (-1, 0)]

    for f in args:
        for r, c in DIRECTION:
            row, col = f[0] + r, f[1] + c
            if G[row][col] == 1:
                return False
            G[row][col] = k
    return True


import sys

input = sys.stdin.readline
n = int(input())
G = []
for _ in range(n):
    G.append(list(map(int, input().split())))

X = []

for i in range(1, n - 1):
    for j in range(1, n - 1):
        v = G[i - 1][j] + G[i][j] + G[i + 1][j] + G[i][j - 1] + G[i][j + 1]
        X.append((v, i, j))


for i in range(n):
    for j in range(n):
        G[i][j] = 0
# X.sort()
# print(X)
print(answer(G, X))
